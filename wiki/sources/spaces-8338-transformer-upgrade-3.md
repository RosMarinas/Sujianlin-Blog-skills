---
type: article_summary
title: "Transformer升级之路：3、从Performer到线性Attention"
article_id: "8338"
source_url: https://spaces.ac.cn/archives/8338
date: 2021-04-22
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-04-22-Transformer升级之路-3-从Performer到线性Attention.md
series: [Transformer升级之路]
topics: [线性Attention, Performer]
concepts: [Linear Attention, Performer, Attention Low Rank Bottleneck, Attention Sparsity]
methods: [线性Attention激活函数优化]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-22-Transformer升级之路-3-从Performer到线性Attention.md
source_ids:
  - "8338"
status: draft
updated: 2026-06-09
---

# Transformer升级之路：3、从Performer到线性Attention

## 文章核心问题
线性Attention的理想激活函数是什么？线性Attention在实际应用中面临哪些瓶颈？如何弥补这些缺陷？

## 主要结论
- 证明了通过随机特征映射，理想激活函数是 $e^x$，可以近似标准Attention的指数形式并保持线性复杂度。
- 标准Attention矩阵因为指数函数运算有"升秩"的潜力，保留更多有效信息；线性Attention直接是两个低维矩阵相乘，秩不超过 $m$，需要设 $m > d$。
- 指数函数使得标准Attention更容易集中注意力（稀疏性）；线性Attention比较稠密，效果接近平均池化。稀疏化有助于提升秩。
- 线性Attention需要增加key的维度（key_size），或者结合局部截断、下三角掩码等方式引入稀疏性并提高秩。

## 推导结构
从Performer模型出发，分析其随机特征映射方法，推导线性Attention的理想激活函数应为指数函数 $e^x$。然后分析线性Attention在实际应用中的两个主要瓶颈：低秩问题（Low Rank）和缺乏稀疏性（Sparsity），并探讨弥补方案。

## 关键公式
- 标准Attention: $\text{Attention}(Q,K,V) = \text{softmax}(QK^{\top})V$
- 线性Attention: $\text{Attention}(Q,K,V) = \phi(Q)(\phi(K)^{\top}V)$
- Performer随机特征映射: $\phi(x) = \frac{1}{\sqrt{m}} \exp(\omega^{\top} x - \|x\|^2/2)$
- 理想激活函数: $e^x$

## 体现的方法
- 线性Attention激活函数优化
- 随机特征映射近似标准Attention

## 所属系列位置
Transformer升级之路系列第3篇，从位置编码转向Attention机制本身，讨论线性Attention的理论与实践。

## 与其他文章的关系
本文为系列引入了一个新的维度——Attention计算效率。与第2篇提出的RoPE相结合，可以实现高效的线性Attention + 相对位置编码方案，是后续第5篇（无限维线性Attention）和第6篇（RoPE在线性Attention中的完备性分析）的基础。

## 原文证据锚点
- Performer随机特征映射证明理想激活函数为 $e^x$
- 标准Attention的"升秩"效应分析
- 线性Attention的低秩瓶颈和稀疏性缺失分析
