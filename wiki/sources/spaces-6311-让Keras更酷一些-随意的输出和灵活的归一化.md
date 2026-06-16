---
type: article_summary
title: “让Keras更酷一些！”：随意的输出和灵活的归一化
article_id: "6311"
source_url: https://spaces.ac.cn/archives/6311
date: 2019-01-27
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-01-27-让Keras更酷一些-随意的输出和灵活的归一化.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-01-27-让Keras更酷一些-随意的输出和灵活的归一化.md
source_ids:
  - "6311"
status: draft
updated: 2026-06-11
---

# “让Keras更酷一些！”：随意的输出和灵活的归一化

本文围绕 Keras 中的 loss 定义、metric 监控、权重约束（归一化）以及自带进度条展开探讨。

## 主要内容

1. **可以不要输出**：
   - 传统 Keras 模型要求明确的输出层与 loss 对应。但对复杂模型（如 Seq2Seq、自编码器），可将所有的输入输出通过 `Input` 传入，在 `compile` 前计算任意张量的 loss，然后通过 `model.add_loss(loss)` 将其添加到模型中。
   - `model.compile` 时无需指定 loss，`model.fit` 时的目标值传入 `None` 即可。

2. **更随意的 metric**：
   - 标准 metric 要求是预测值与真实值之间的运算。若要监控中间层输出的某种统计量（如中间层特征的平均模长），可直接修改 `model.metrics_names` 和 `model.metrics_tensors` 列表，在编译后直接 `append` 需要观察的名称和张量。

3. **灵活的权重归一化**：
   - 区分“事后约束”（在优化器更新梯度后截断/映射权重，通过 `kernel_constraint` 等实现）与“事前约束”（在权重输入网络运算前先进行变换，将其视为模型计算图的一部分）。
   - 本文介绍了一种“移花接木”式的事前权重变换方式：拦截 Layer 的 `__call__`，在 `layer.built` 尚未为 `True` 时，手动调用其 `build` 方法建立权重，随后用经过变换的权重（例如除以谱范数进行谱归一化）覆盖原权重属性，最后调用该 layer。
   - 实例：`SpectralNormalization` 包装器。

4. **调用 Keras 自带进度条**：
   - 介绍了如何使用 `keras.utils.Progbar` 来展示进度，并监控具有滑动平均特点的 `values`，指出了可通过 `stateful_metrics` 防止某些特定监控指标被滑动平均更新。
