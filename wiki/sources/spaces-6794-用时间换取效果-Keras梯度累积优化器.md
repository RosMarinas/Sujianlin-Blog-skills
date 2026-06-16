---
type: article_summary
title: 用时间换取效果：Keras梯度累积优化器
article_id: "6794"
source_url: https://spaces.ac.cn/archives/6794
date: 2019-07-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-07-08-用时间换取效果-Keras梯度累积优化器.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-08-用时间换取效果-Keras梯度累积优化器.md
source_ids:
  - "6794"
status: draft
updated: 2026-06-11
---

# 用时间换取效果：Keras梯度累积优化器

本文介绍了在 Keras 中实现梯度累积（Gradient Accumulation）优化器的方法，以在显存有限的情况下模拟大 Batch Size 的训练效果。

## 主要内容

1. **背景需求**：
   - 在 Fine-tune 诸如 BERT 等大型 Transformer 模型时，由于 Attention 的空间和时间复杂度为 $\mathcal{O}(n^2)$，显存极易溢出，导致 Batch Size 只能设得非常小。
   - 小 Batch Size 训练会导致效果变差。如果无法增加显卡，梯度累积是一种可行的权衡方案：通过用时间换空间，模拟出等效于大 Batch Size 的效果。

2. **梯度累积原理**：
   - 传统大 Batch 是一次计算 $N$ 个样本的平均梯度并更新。
   - 梯度累积是：每次计算较小 Batch 的梯度并缓存累加，重复 $k$ 次后，将累计的梯度除以 $k$ 进行参数更新。

3. **Keras 实现修正**：
   - 纠正了之前使用 `K.switch` 控制条件更新的错误实现。在 TF/Keras 中，`K.switch` 并不提供控制执行的选择性，两个分支都会被评估。
   - 正确写法是在**更新量**（梯度）上做文章：每个小 batch 依然更新参数，但通过迭代次数判断，若不满足更新步数，则令当前更新量为 0，仅累积梯度；若满足更新步数，则使用平均后的累积梯度更新，并清空累积变量。
   - 通过 `AccumOptimizer` 封装任意标准 Keras 优化器（如 `Adam`），可无缝应用，避免了重写整个优化器逻辑的麻烦。
   - **局限性**：此方法与 Batch Normalization 冲突，因为 BN 必须基于真实的 Batch 样本计算统计量（均值和方差）。若网络包含 BN，必须使用大显存或多卡。
