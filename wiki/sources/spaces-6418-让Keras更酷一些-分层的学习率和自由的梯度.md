---
type: article_summary
title: “让Keras更酷一些！”：分层的学习率和自由的梯度
article_id: "6418"
source_url: https://spaces.ac.cn/archives/6418
date: 2019-03-10
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-03-10-让Keras更酷一些-分层的学习率和自由的梯度.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-03-10-让Keras更酷一些-分层的学习率and自由的梯度.md
source_ids:
  - "6418"
status: draft
updated: 2026-06-11
---

# “让Keras更酷一些！”：分层的学习率和自由的梯度

本文探讨了在 Keras 中实现分层设置学习率（Layer-wise Learning Rate）与自由操作梯度的技巧，均无需完全重写优化器。

## 主要内容

1. **分层的学习率**：
   - **参数变换下的优化原理**：通过引入参数尺度缩放 $\boldsymbol{\theta} = \lambda \boldsymbol{\phi}$。根据链式法则进行推导可知：
     - 在 **SGD**（包括带动量）优化器中，对 $\boldsymbol{\phi}$ 进行优化等价于将 $\boldsymbol{\theta}$ 的学习率缩放为 $\lambda^2 \alpha$。
     - 在 **Adam/RMSprop** 等自适应学习率优化器中，因为分母中的二阶矩滑动平均项会抵消一个 $\lambda$ 的尺度，对 $\boldsymbol{\phi}$ 优化等价于将 $\boldsymbol{\theta}$ 的学习率缩放为 $\lambda \alpha$。
   - **实现方法**：利用层包装器 `SetLearningRate`。在层构建（`build`）后，将初始化权重除以 $\lambda$（或 $\sqrt{\lambda}$），然后在前向计算前用 $\lambda \cdot \text{weight}$（或 $\sqrt{\lambda} \cdot \text{weight}$）覆盖它。这种方法能够无缝配合现有的任何优化器，但不可逆，且需小心预训练权重的加载方式。

2. **自由的梯度操作**：
   - **Keras 优化器的 `get_gradients` 方法**：Keras 优化器在 `get_updates` 之前，通过 `get_gradients(self, loss, params)` 统一计算梯度。
   - **动态覆盖（Monkey Patching）**：利用 Python “处处皆对象”的特点，直接通过将一个自定义的梯度计算函数赋值给已有优化器实例 of `get_gradients` 属性（例如 `adam_opt.get_gradients = our_get_gradients`），即可在模型编译（`compile`）时生效，从而能够实现如 L1 裁剪、特定层梯度操纵或梯度冻结等高度自由的操作。
