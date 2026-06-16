---
type: article_summary
title: 通向概率分布之路：盘点Softmax及其替代品
article_id: "10145"
source_url: https://spaces.ac.cn/archives/10145
date: 2024-06-14
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-06-14-通向概率分布之路-盘点Softmax及其替代品.md
series:

topics:
  - [[概率分布构建]]
concepts:
  - [[Softmax替代品]]
  - [[Sparsemax]]
methods:

evidence_spans:
  - ev::10145::Softmax性质
  - ev::10145::各种变体对比
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-14-通向概率分布之路-盘点Softmax及其替代品.md
source_ids:
  - "10145"
status: draft
updated: 2026-06-10
---
# 通向概率分布之路：盘点Softmax及其替代品

## 文章核心问题

Softmax有哪些优良性质？有哪些替代方案？各自的优缺点是什么？

## 主要结论

Softmax满足单调性和不变性（加常数不变），是其作为argmax光滑近似的本质。替代方案包括：Margin Softmax（增大类间Margin）、Taylor Softmax（多项式近似、更长尾）、Sparse Softmax（训练时截断Top-k）、Sparsemax（relu(x-λ)自适应稀疏）、Entmax-α（从Softmax到Sparsemax的平滑过渡）和Perturb Max（噪声扰动视角）。

## 推导结构

1. Softmax的定义、性质、梯度、损失函数
2. Softmax变体：Margin、Taylor、Sparse Softmax
3. Perturb Max：Gumbel Max的一般化
4. Sparsemax：定义为relu(x-λ)，可严格为零
5. Entmax-α：从Softmax到Sparsemax的平滑过渡

## 关键公式

Softmax: p_i = e^{x_i}/∑ e^{x_i}
Sparsemax: p_i = relu(x_i - λ(x))
Entmax-α: p_i = relu^{1/β}(βx_i - λ(x)) 其中α=β+1

## 与Transformer升级之路系列的关系

Taylor Softmax可用于线性化Attention

## 原文证据锚点

- ev::10145::Softmax性质 — 单调性和不变性
- ev::10145::各种变体对比 — 各种Softmax替代品的对比
