---
type: article_summary
title: 低秩近似之路（二）：SVD
article_id: "10407"
source_url: https://spaces.ac.cn/archives/10407
date: 2024-10-01
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-10-01-低秩近似之路-二-SVD.md
source_html: null
series:
  - "[[低秩近似之路]]"
topics:
  - "[[低秩近似]]"
concepts:
  - "[[奇异值分解]]"
  - "[[伪逆]]"
methods:
  - "[[将矩阵近似问题化为骨架选择问题]]"
problem_patterns:
  - "[[在误差最优与结构可解释之间选择低秩近似]]"
evidence_spans:
  - ev::10407::结论初探
  - ev::10407::低秩近似
  - ev::10407::近似定理
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-10-01-低秩近似之路-二-SVD.md
source_ids:
  - "10407"
status: draft
updated: 2026-06-09
---

## 文章核心问题

当 `A` 与 `B` 都不给定时，怎样求矩阵 `M` 的最优 `r` 秩近似。

## 主要结论

SVD 将任意实矩阵分解为两个正交矩阵和一个非负对角矩阵，利用正交变换不改变范数，可以把低秩近似问题化为非负对角阵的截断问题。Eckart-Young-Mirsky 定理说明保留最大的 `r` 个奇异值给出最优 `r` 秩近似。

## 推导结构

文章先给出 SVD 形式和几何图景，再展示 SVD 在伪逆、矩阵范数和低秩近似中的作用。随后用谱定理证明 SVD 的存在和构造方式，最后把低秩近似误差归约为尾部奇异值平方和。

## 关键公式

- `M=U Sigma V^T`
- `A^\dagger=V Sigma^\dagger U^T`
- `M_r=U_{[:,:r]} Sigma_{[:r,:r]} V_{[:,:r]}^T`
- `||M-M_r||_F^2=sum_{j>r} sigma_j^2`

## 体现的方法

核心方法是用正交不变性把一般矩阵问题转化为对角矩阵问题。这是后续判断结构化近似“比 SVD 更可解释但不再无约束最优”的参照基线。

## 所属系列位置

这是 [[低秩近似之路]] 的第二篇，给出无约束低秩近似的理论最优基准。

## 与其他文章的关系

- 承接 [[低秩近似之路（一）：伪逆]]，用 SVD 给出伪逆通解。
- 为 [[低秩近似之路（三）：CR]]、[[低秩近似之路（四）：ID]] 和 [[低秩近似之路（五）：CUR]] 提供误差最优但结构不直观的对照。

## 原文证据锚点

- `结论初探`：给出 SVD 基本形式与奇异值。
- `低秩近似`：说明 SVD 将一般低秩问题转化为对角阵问题。
- `近似定理`：给出 Eckart-Young-Mirsky 定理及尾部奇异值误差。
