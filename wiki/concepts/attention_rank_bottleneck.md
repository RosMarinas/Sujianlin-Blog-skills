---
type: concept
title: Attention Low Rank Bottleneck
definition: Attention低秩瓶颈指的是在自注意力机制中，注意力概率矩阵的秩受到投影特征维度（head_size = d/h）的严格限制，导致模型难以拟合较长序列上复杂的二元分布。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
source_ids:
  - "7325"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Attention Low Rank Bottleneck

## Definition
Attention低秩瓶颈指的是在自注意力机制中，注意力概率矩阵的秩受到投影特征维度（head_size = d/h）的严格限制，导致模型难以拟合较长序列上复杂的二元分布。

## Explanation
在标准的Multi-Head Attention中，Query和Key被投影到较低维度 $d_k = d/h$。如果序列长度为 $n$，注意力概率矩阵共有 $n^2$ 个得分值。然而，它的计算是基于 $Q K^\top$（其中 $Q, K \in \mathbb{R}^{n \times d_k}$），其矩阵的秩最大只有 $d_k$。当 $h$ 较大时，每个头的分量维度 $d_k$ 极小，使得用 $2nd/h$ 的低秩特征去拟合有 $n^2$ 个分量的分布非常困难，限制了注意力的表达能力。通过增加 key_size 或者引入 Talking-Heads 头信息叠加（混合分布）可以有效缓解这一瓶颈。
