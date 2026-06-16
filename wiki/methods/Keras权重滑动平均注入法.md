---

type: method
operation_types:
  primary: Construct auxiliary sequence
  secondary: []
title: Keras权重滑动平均注入法
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-04-28-让Keras更酷一些-中间变量-权重滑动和安全生成器.md
source_ids:
  - 6575
method_summary: 通过将移动平均更新算子注入 Keras 模型的 `metrics_updates` 列表中，实现在模型每个训练 Step 自动执行模型权重的指数滑动平均（EMA）计算。
typical_structure: |
  1. 初始化一个空张量列表，形状与目标模型的权重匹配，作为滑动平均的影子权重。
  2. 使用 K.moving_average_update 等函数生成更新算子。
  3. 将生成的更新算子 append 到模型的 metrics_updates 属性列表中。
  4. 训练时框架将隐式地触发 EMA 算子同步执行；训练完成后使用影子权重覆盖模型权重进行推理。
applicability: 在 Keras 框架中训练大模型（特别是 GAN、QANet）时，需要引入权重指数滑动平均以平滑优化轨迹并提升评估指标，且不希望专门自定义重写底层优化器。
tools: 
examples:
  - [[article::6575]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::6575::文章提到“引入了 K.moving_average_update 操作，并且插入到 model.metrics_updates 中...从而完成了滑动平均。”
---





## 适用问题
需要给深度学习模型（如 GAN 或复杂网络）加上指数移动平均（EMA）以平滑训练轨迹、提升模型稳定性与收敛效果，但却因为所使用的框架环境原因而不想针对特定的每个优化器（Adam、SGD 等）去逐个写底层定制代码。

## 核心变换
将一个通常属于**优化器内部核心循环**的参数滑动更新操作，伪装并“注入（Inject）”到模型本身的度量指标更新槽位（`model.metrics_updates`）中，使得该算子与模型的网络训练图深度绑定，实现了**与优化器完全解耦**的滑动平均。

## 典型步骤
1. 定义一个包装类，并在内部根据目标模型的各个权重张量 `model.weights`，分别申请一组同形状、初始为 0 的伴随影子张量。
2. 利用后端提供的指数平滑函数（如 `K.moving_average_update`）构建滑动更新算子。
3. 拦截目标模型的属性，将上述更新算子 `append` 到 `model.metrics_updates` 列表之中。
4. 调用常规的 `fit` 训练模型。在每个 Batch 后，Keras 会自动把度量统计量的更新与梯度下降一起执行。
5. 训练完毕（或评估时），提取影子张量的值覆盖到模型的正常权重之上；若需继续训练则先换回原始权重。

## 直觉
在原版框架设计里，`metrics_updates` 是被设计给准确率、召回率这种统计量在每个 mini-batch 结束后累计其观测状态使用的。既然每次前向和反向传播后，系统无论如何都会强制遍历执行这个列表，那么只需把 EMA “影子张量”的算子也悄悄放进去，每次走一小步，它就会顺风车般跟着一起平滑演化。

## 边界
这种“搭便车”的做法高度依赖 Keras 框架内部将 `metrics_updates` 和损失图一起纳入单次 `session.run` 执行图这一机制。当框架版本变迁或是 Eager Execution 成为主导时，此类“后门注入”方案可能会因为执行管线的变化而失效。另外，在断点续传保存和读取模型权重时，需要额外设计机制去独立保存和加载这些由注入对象持有的影子张量。

## 例子
如果在训练 QANet 或 GAN 时，正常调用 `model.compile`，然后直接调用 `EMAer = ExponentialMovingAverage(model); EMAer.inject()`，接下来就像往常一样 `model.fit`。这不但保留了原本使用的复杂优化器，而且全程不影响原模型。

## 证据
- ev::6575::明确揭示了借道机制的由来：“主要的一点是引入了 `K.moving_average_update` 操作，并且插入到 `model.metrics_updates` 中...使得优化器在进行参数梯度下降后，Keras 引擎顺带执行了影子权重的平滑更新”。
