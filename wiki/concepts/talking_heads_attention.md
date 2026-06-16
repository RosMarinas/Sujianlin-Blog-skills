---
type: concept
title: Talking-Heads Attention
definition: Talking-Heads Attention（交流头注意力）是Google提出的一种多头注意力变体。它在计算Query和Key的内积后、Softmax之前，以及Softmax之后，引入参数矩阵对各个注意力头的分布进行线性组合，实现多头信息的融合与共享。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
source_ids:
  - "7325"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Talking-Heads Attention

## Definition
Talking-Heads Attention（交流头注意力）是Google提出的一种多头注意力变体。它在计算Query和Key的内积后、Softmax之前，以及Softmax之后，引入参数矩阵对各个注意力头的分布进行线性组合，实现多头信息的融合与共享。

## Explanation
在传统的Multi-Head Attention中，每个头的注意力权重计算是完全独立、互不干扰的。这限制了模型拟合复杂联合概率分布的能力。Talking-Heads Attention引入混合分布的思想（类似于高斯混合模型），通过在Softmax前后乘以参数矩阵 $\boldsymbol{\lambda}$，将不同头的注意力得分矩阵进行加权组合：$\boldsymbol{J} = \boldsymbol{\lambda} \hat{\boldsymbol{J}}$。这样可以利用多个头算出来的低秩分布叠加成拟合能力更强大的概率分布，显著提升了注意力的特征表达能力，在翻译和生成任务上表现优异。
