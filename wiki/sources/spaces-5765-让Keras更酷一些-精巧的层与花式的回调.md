---
type: article_summary
title: “让Keras更酷一些！”：精巧的层与花式的回调
article_id: "5765"
source_url: https://spaces.ac.cn/archives/5765
date: 2018-08-06
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-08-06-让Keras更酷一些-精巧的层与花式的回调.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-08-06-让Keras更酷一些-精巧的层与花式的回调.md
source_ids:
  - "5765"
status: draft
updated: 2026-06-11
---

# “让Keras更酷一些！”：精巧的层与花式的回调

本文介绍了在 Keras 中进行高阶定制化开发的方法，主要围绕自定义层（Custom Layers）和自定义回调函数（Custom Callbacks）展开。

## 主要内容

1. **层的自定义**：
   - **Lambda 层**：最简便的自定义层方式，适用于无训练参数的操作，可通过 `K.in_train_phase` 区分训练与测试阶段。
   - **自定义 Layer 子类**：重写 `__init__`, `build`, `call`, `compute_output_shape`，用于需要增加可训练参数的情况。
   - **多输出层**：通过返回张量列表并显式指定 `compute_output_shape` 对应的 shape 列表来实现多输出层（例如切片分流）。
   - **层与 Loss 的结合**：以 Center Loss 为例，通过在自定义层中定义 `.loss(y_true, y_pred)` 函数，并在 `model.compile` 中直接调用该方法，实现了将层内权重与 loss 深度绑定的写法。

2. **花式回调器**：
   - **保存最优模型**：针对 BLEU 等无法用张量计算的指标，通过编写自定义 `Callback` 类在 `on_epoch_end` 计算并保存最优权重。
   - **修改超参数**：使用 `K.variable` 包装正则化权重，通过自定义回调在特定 epoch 使用 `K.set_value` 动态调整它。
   - **Warmup 学习率调度**：重写 `on_batch_begin`，在前几个 epoch 线性调整学习率，实现更加平滑的模型初始化。
