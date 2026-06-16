---
type: article_summary
title: Sinusoidal位置编码追根溯源
article_id: "8231"
source_url: https://spaces.ac.cn/archives/8231
date: 2021-03-08
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-03-08-Transformer升级之路-1-Sinusoidal位置编码追根溯源.md
series: [Transformer升级之路]
topics: [位置编码]
concepts: [Sinusoidal位置编码, 相对位置, 绝对位置, 远程衰减]
methods: [泰勒展开近似, 复数表示位置编码内积, 振荡积分估计衰减]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-03-08-Transformer升级之路-1-Sinusoidal位置编码追根溯源.md
source_ids:
  - "8231"
status: draft
updated: 2026-06-09
---

# Sinusoidal位置编码追根溯源

## 文章核心问题
Transformer为何无法自主识别位置信息？绝对位置编码的内积能否以及如何表达相对位置？Sinusoidal位置编码的远程衰减特性从何而来？

## 主要结论
- 模型对输入的对称性导致了Transformer无法识别位置，需要加入位置编码。
- 绝对位置编码的内积在一定条件下可以表达相对位置。
- Sinusoidal位置编码中的特定周期频率设定使得相对位置的内积具有远程衰减的特性。
- Sinusoidal位置编码的衰减特性来源于高频振荡积分的渐近趋零性。

## 推导结构
作者通过泰勒展开将带有位置编码的模型近似到二阶，分离出表示相对位置信息的交互项。在特定假设下（例如海森矩阵为单位阵），推导并证明了绝对位置编码的内积可以表达相对位置信息，并给出了利用复数进行推导的具体过程。进一步分析了为何Sinusoidal编码具有随着距离增加而衰减的特性（远程衰减），指出这是高频振荡积分的渐近趋零性导致的。最后，探讨了一般情况下的假设合理性，认为如果海森矩阵对角线元素占主导，那么这些良好特性仍然可以近似保留。

## 关键公式
- Sinusoidal位置编码: $PE_{(pos,2i)} = \sin(pos/10000^{2i/d})$, $PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d})$
- 二阶泰勒展开近似: $f(x+p) \approx f(x) + f'(x)p + \frac12 p^{\top}H(x)p$
- 复数形式位置编码内积: $PE(pos_1) \cdot PE(pos_2) = \sum_i \cos(\omega_i (pos_1 - pos_2))$
- 高频振荡积分渐近性质: $\int g(x)e^{i\omega x}dx \to 0$ as $\omega \to \infty$

## 体现的方法
- 泰勒展开近似模型函数
- 复数表示绝对位置编码的内积
- 振荡积分估计相对位置内积的渐近衰减

## 所属系列位置
Transformer升级之路系列第1篇，为整个系列奠定位置编码的理论基础。

## 与其他文章的关系
本文从理论层面分析了Sinusoidal位置编码的数学原理和远程衰减特性，为第2篇提出更优的RoPE提供了理论依据和对比基准。

## 原文证据锚点
- 泰勒展开将位置编码影响近似到二阶
- 复数推导内积表达相对位置
- 振荡积分分析远程衰减特性
