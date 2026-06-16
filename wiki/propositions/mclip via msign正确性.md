---
type: proposition
title: mclip via msign恒等式正确性
aliases:
  - Correctness of mclip through msign identity
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-07-通过msign来计算奇异值裁剪mclip-上.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-23-通过msign来计算奇异值裁剪mclip-下.md
source_ids:
  - "11006"
  - "11059"
related_concepts:
  - "[[矩阵符号函数(msign)]]"
  - "[[奇异值裁剪(mclip)]]"
evidence_spans:
  - ev::11006::msign表示mclip推导
  - ev::11059::mclip通解
  - ev::11059::去嵌套技巧
status: stable
updated: 2026-06-10
---

# mclip via msign恒等式正确性

## 命题陈述

对于任意矩阵 $M \in \mathbb{R}^{n \times m}$，以下恒等式成立：

$$2\text{mclip}(M) = M + \text{msign}(M) + (I - M\text{msign}(M)^\top)\text{msign}(M - \text{msign}(M))$$

更一般地，对任意区间 $[\alpha,\beta]$：

$$\text{mclip}_{[\alpha,\beta]}(M) = \frac{1}{2}[(\alpha+\beta)\text{msign}(M) + (\alpha I - M\text{msign}(M)^\top)\text{msign}(\alpha\text{msign}(M)-M) - (\beta I - M\text{msign}(M)^\top)\text{msign}(\beta\text{msign}(M)-M)]$$

## 证明思路

从标量恒等式 $\min(x,1) = [x+1-(x-1)\text{sign}(x-1)]/2$ 出发，将 $\text{sign}$ 替换为 $\text{msign}$，利用SVD对角化验证矩阵版本的正确性。关键用到 $\text{msign}$ 的正交变换不变性。

## 去嵌套版本

利用 $\text{sign}(x-1) = \text{sign}(x^2-1)$ 可得：

$$2\text{mclip}(M) = M + \text{msign}(M) + (\text{msign}(M)-M)\text{msign}(M^\top M - I)$$

## 奇函数误差抵消版本 ($\alpha=-1,\beta=1$)

$$2\text{mclip}(M) = (\text{msign}(M)+M)\text{msign}(M^\top M + I) + (\text{msign}(M)-M)\text{msign}(M^\top M - I)$$

该版本在bfloat16精度下最优，利用 $\text{msign}(M^\top M + I) \approx I$ 的微小误差与主项误差的抵消。
