---
type: article_summary
title: 直接以FID为Loss：从梯度计算到流式训练
article_id: 11738
source_url: https://spaces.ac.cn/archives/11738
date: 2026-05-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2026-05-08-直接以FID为Loss-从梯度计算到流式训练.md
concepts:
  - [[FD Loss]]
formulas:
  - [[FD损失公式]]
  - [[FD损失梯度公式]]
methods:
  - [[FD损失流式训练法]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-05-08-直接以FID为Loss-从梯度计算到流式训练.md
source_ids:
  - 11738
status: draft
updated: 2026-06-11
---

# 直接以FID为Loss：从梯度计算到流式训练

本文探讨了直接将 Fréchet Inception Distance (FID) 作为视觉生成模型微调损失函数的数学求导机理和在大 Batch 统计估计上的工程技巧。

## 核心内容
- **FD 梯度的解析解**：求得 Fréchet Distance 对生成特征协方差矩阵的梯度形式为：$\nabla_{\boldsymbol{\Sigma}_q}\mathcal{W}_2^2 = I - \boldsymbol{\Sigma}_p^{1/2}(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{-1/2}\boldsymbol{\Sigma}_p^{1/2}$。这可以通过 Newton-Schulz 迭代高效计算。
- **Batch Size 困难**：在特征维度高达数千维时，必须基于数万的样本量来做统计估计。若 Batch Size 较小，协方差矩阵不满秩，求逆平方根会发生数值崩溃。
- **流式累积方案**：提出用滑动平均（EMA）在训练中实时缓冲和估计生成特征的均值 $\boldsymbol{\mu}_q$ 和自相关矩 $\boldsymbol{V}_q$，以无感地模拟几万的大 Batch Size，进而进行稳健的特征空间微调。