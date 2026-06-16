---
type: article_summary
title: DiVeQ：一种非常简洁的VQ训练方案
article_id: 11328
source_url: https://spaces.ac.cn/archives/11328
date: 2025-10-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-10-08-DiVeQ-一种非常简洁的VQ训练方案.md
topics:
  - [[向量量化]]
concepts:
  - [[DiVeQ]]
propositions:
  - [[DiVeQ等效隐式AuxLoss证明]]
methods:
  - [[DiVeQ无辅助损失量化训练法]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-08-DiVeQ-一种非常简洁的VQ训练方案.md
source_ids:
  - 11328
status: draft
updated: 2026-06-11
---

# DiVeQ：一种非常简洁的VQ训练方案

本文介绍了一种称为 DiVeQ 的离散化向量量化训练方案，它最大的亮点是不再需要传统的两个额外的辅助损失函数（Aux Loss）。

## 核心内容
- **离散梯度设计的痛点**：直通估计器（STE）使得编码器能获得梯度，但编码表无法端到端优化，因而 VQ-VAE 需要引入 $\beta \|q - z\|^2$ 等辅助损失。
- **DiVeQ 重参数化**：将前向计算结果 $z_q$ 重新参数化为 $z_q = z + \|q - z\| \times \text{sg}[\frac{q - z}{\|q - z\|}]$（DiVeQ-detach 形式）。这种设计前向前向仍等于 $q$，但在反向传播时保留了差分向量的模长梯度。
- **隐式辅助损失**：理论推导证明，DiVeQ 在反向传播时引入的梯度项等价于引入了一个自适应权重的辅助损失：$\text{sg}[\mathcal{L}(z_q) - \mathcal{L}(z)] \ln \|q - z\|$。由于当模型开始收敛时，无信息损失的连续表示 $z$ 的损失一定低于离散的 $z_q$，故该项天然为一个拉近 $q$ 和 $z$ 距离的正系数损失。