---
type: concept
definition: Standard Attention can be theoretically viewed as a Linear Attention with
  infinite dimensions. While practical Linear Attention implementations project queries
  and keys to a finite (often small) lower-dimensional space $m$, Standard Attention
  maps them to an infinite dimensional space.
title: Infinite Dimensional Linear Attention
aliases: []
sources:
- （待从源文章提取）
source_ids:
- （待从源文章提取）
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
---

# Infinite Dimensional Linear Attention (无限维的线性Attention)

## Overview
Standard Attention can be theoretically viewed as a Linear Attention with infinite dimensions. While practical Linear Attention implementations project queries and keys to a finite (often small) lower-dimensional space $m$, Standard Attention maps them to an infinite dimensional space.

## Mathematical Formulation
The conversion aims to find mappings $\phi$ and $\varphi$ such that:
$$
\phi(\boldsymbol{q})\cdot \varphi(\boldsymbol{k})\approx e^{\boldsymbol{q}\cdot \boldsymbol{k}}
$$

### Approaches:
1. **Random Projection (Performer)**: Uses expectations over Gaussian distributions to approximate the exponential.
2. **Taylor Expansion**: Expanding $e^{\boldsymbol{q}\cdot \boldsymbol{k}} = \sum_{m=0}^{\infty} \frac{(\boldsymbol{q}\cdot \boldsymbol{k})^m}{m!}$ and recognizing that $(\boldsymbol{q}\cdot \boldsymbol{k})^m$ can be seen as the inner product of the $m$-th tensor product (outer product) of $\boldsymbol{q}$ and $\boldsymbol{k}$. This leads to a polynomial kernel of dimension $O(d^n)$.
3. **Natural Exponential Definition**: Using $\lim_{n\to\infty} \left(1+\frac{\boldsymbol{q}\cdot \boldsymbol{k}}{n}\right)^n$, resulting in an inner product of the $n$-th tensor power of modified vectors.

## Implications for the Low-Rank Problem
Linear Attention commonly suffers from a low-rank bottleneck. Because it maps tokens to vectors of size $d$, the resulting attention matrix has rank at most $d$. Standard Attention, being equivalent to an infinite-dimensional linear attention, does not suffer from this bottleneck, which theoretically explains why its performance is often superior.