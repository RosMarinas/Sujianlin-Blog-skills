---
title: 得分匹配 (Score Matching)
definition: '得分函数定义为对数概率密度的梯度: s(x) = ∇x log p(x)。得分匹配通过学习模型的得分函数来隐式学习数据分布。'
type: concept
status: draft
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# 得分匹配 (Score Matching)

## Definition
得分函数定义为对数概率密度的梯度: s(x) = ∇_x log p(x)。得分匹配通过学习模型的得分函数来隐式学习数据分布。

## Connection to Denoising Autoencoder
最优去噪自编码器: r(x) = x + σ² ∇_x log p̃(x), 其中p̃为加噪分布。
去噪得分匹配: 通过去噪自编码器间接估计得分函数。

## Related Methods
- [[methods/denoising-score-matching]]
- [[sources/spaces-7038-去噪自编码器]]