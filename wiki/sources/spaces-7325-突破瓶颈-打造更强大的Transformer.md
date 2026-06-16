---
type: article_summary
title: 突破瓶颈，打造更强大的Transformer
article_id: "7325"
source_url: https://spaces.ac.cn/archives/7325
date: 2020-04-13
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
series: [Transformer架构与归一化]
topics: [Attention优化]
concepts: [Attention Low Rank Bottleneck, Talking-Heads Attention]
methods: [增大key_size解除注意力低秩瓶颈, Talking-Heads Attention]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
source_ids:
  - "7325"
status: draft
updated: 2026-06-12
---

# 突破瓶颈，打造更强大的Transformer

## 文章核心问题
自注意力机制中是否存在低秩表达瓶颈？如何在不改变模型总体维度（hidden_size）的情况下提升自注意力的表达能力？各个注意力头之间相互孤立的问题如何通过头之间的交互（Talking）来解决？

## 主要结论
- 自注意力机制在 $h$ 较大时，每个头内的投影维度 $d/h$（head_size）过小，导致计算出来的注意力概率矩阵受限于极低的参数量（低秩瓶颈），难以拟合样本数平方大小的联合分布。
- 增大 $Q, K$ 的投影维度（key_size）而不改变 $V$ 的投影维度（head_size），能有效缓解低秩瓶颈，并在参数量相同的情况下取得更好的表现。
- 引入 Talking-Heads Attention，在 softmax 之前和之后，通过参数矩阵对各个头算出来的注意力权重/混合分布进行线性组合（混合分布），能够极大地增强概率拟合能力，从而超越传统的独立多头注意力。

## 推导结构
1. **分析低秩瓶颈**：自注意力计算公式为 $Attention(Q,K,V) = softmax(\frac{QK^{\top}}{\sqrt{d_k}})V$。在常规设计下，每个头将维度降低为 $d/h$，即 $Q, K \in \mathbb{R}^{n \times (d/h)}$。若序列长度为 $n$，则两两注意力得分矩阵包含 $n^2$ 个元素，却由参数量仅为 $2nd/h$ 的低维特征相乘近似，构成低秩瓶颈。
2. **增大 key_size 方案**：将 $Q, K$ 的维度定义为 key_size 并独立调大，而 $V$ 的维度保持为 $head_size = d/h$。这样仅增加了少量参数和内积计算量，但大幅提升了注意力矩阵的秩与拟合空间。
3. **Talking-Heads Attention 方案**：各注意力头的注意力矩阵 $\hat{J}^{(i)} = Q^{(i)}{K^{(i)}}^{\top}$。引入参数矩阵 $\boldsymbol{\lambda}$ 将它们进行加权求和，得到 $\boldsymbol{J} = \boldsymbol{\lambda} \hat{\boldsymbol{J}}$。对 $\boldsymbol{J}$ 做 softmax 归一化后再乘以各头的值矩阵。这种混合分布能够逼近更复杂的概率分布，类似于混合高斯模型（GMM）。

## 关键公式
- 标准 Scaled-Dot Attention: $Attention(Q,K,V) = softmax\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V$
- Talking-Heads 投影叠加: $J^{(i)} = \sum_j \lambda_{ij} \hat{J}^{(j)}$，其中 $\hat{J}^{(j)} = Q^{(j)}{K^{(j)}}^{\top}$
- 混合后注意力矩阵: $P^{(i)} = softmax(J^{(i)})$

## 体现的方法
- 增大key_size解除注意力低秩瓶颈
- Talking-Heads Attention 混合注意力分布

## 所属系列位置
Transformer架构与归一化系列第1篇，开创了对自注意力计算机制本身表达能力缺陷进行优化的探索路线。

## 与其他文章的关系
本篇指出的自注意力低秩瓶颈以及 softmax 之前的混合分布，启发了后续 Synthesizer 对注意力矩阵生成方式的重新评估，也与 FLASH 等单头模型通过其他结构（如GLU）弥补注意力表达能力的思路形成对比。

## 原文证据锚点
- 低秩瓶颈分析：公式 (46) Softmax前的内积逼近限制。
- Talking-Heads公式推导：公式 (86) 到 (94) 的混合变换。
- 实验结论：key_size 固定为 128 效果更优；混合分布能使小 key_size 在多头叠加下表现强劲。
