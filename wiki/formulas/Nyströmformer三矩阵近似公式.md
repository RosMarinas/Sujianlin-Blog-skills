---
type: formula
title: Nyströmformer三矩阵近似公式
aliases:
- Nyström attention approximation
source_ids:
- '8180'
evidence_spans:
- ev::8180::三矩阵近似
- ev::8180::伪逆近似
standard_notation:
  A: attention matrix
  Q: query matrix
  K: key matrix
  tilde_Q: query landmark matrix
  tilde_K: key landmark matrix
  dagger: Moore-Penrose pseudoinverse
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
latex: A\approx softmax(Q\tilde K^\top)\,softmax(\tilde Q\tilde K^\top)^\dagger\,softmax(\tilde
  QK^\top).
symbol_meanings:
  A: attention matrix
  K: key matrix
  Q: query matrix
  dagger: Moore-Penrose pseudoinverse
  tilde_K: key landmark matrix
  tilde_Q: query landmark matrix
conditions: （待从源文章提取）
appears_in:
- '8180'
---

# Nyströmformer三矩阵近似公式

## 概述

$$A\approx softmax(Q\tilde K^\top)\,softmax(\tilde Q\tilde K^\top)^\dagger\,softmax(\tilde QK^\top).$$

Nyströmformer提出了一种三矩阵近似公式，用于将标准自注意力（Self-Attention）从 $\mathcal{O}(n^2)$ 的复杂度降低至 $\mathcal{O}(n)$。通过采用类似于 Nyström 方法的思想，它利用自适应平均池化（Segment-Means）等操作，从原始的 Query 矩阵 $Q$ 和 Key 矩阵 $K$ 中提取出小维度的“Landmark”特征矩阵 $\tilde Q, \tilde K \in \mathbb{R}^{m\times d}$。标准注意力矩阵从而被分解为三个较小规模 softmax 矩阵的连乘。其中间项采用了 Moore-Penrose 伪逆（$\dagger$），在实际计算中通过 Chebyshev 型的迭代算法（pINV）来求得近似解，避免了精确求逆带来的高计算成本与反向传播的梯度问题。该重构使得我们可以利用矩阵乘法结合律先计算后两个规模较小的矩阵，极大降低了长序列下的时间和空间复杂度，同时实验证明其在预训练任务（如 MLM）中能维持与标准注意力相媲美的性能。
