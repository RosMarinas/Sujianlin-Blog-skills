---
type: proposition
title: SVD截断给出F范数下的最优r秩近似
aliases:
  - Eckart-Young-Mirsky for Frobenius norm
statement: 对矩阵 `M` 的 SVD 截断保留最大的 `r` 个奇异值，可得到 Frobenius 范数下的无约束最优 `r` 秩近似。
assumptions:
  - 使用 Frobenius 范数衡量误差。
  - 近似矩阵只受秩不超过 `r` 的约束。
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-10-01-低秩近似之路-二-SVD.md
source_ids:
  - "10407"
requires:
  - "[[奇异值分解]]"
  - "[[SVD截断低秩近似公式]]"
proof_route: 用 SVD 和正交不变性把一般矩阵问题转化为非负对角阵问题，再证明对角阵保留最大 `r` 个对角元时尾部平方和最小。
methods: []
limits:
  - 该结论是无约束最优；不保证保留原矩阵行列结构。
examples:
  - "[[spaces-10407-SVD截断证明]]"
evidence_spans:
  - ev::10407::低秩近似
  - ev::10407::近似定理
status: stable
updated: 2026-06-09
---

## 证明路线

文章先用 SVD 将 `||AB-M||_F^2` 化为 `||U^T ABV-Sigma||_F^2`，再说明 `U^T ABV` 仍代表任意秩不超过 `r` 的矩阵。因此问题等价于非负对角阵的低秩近似。最后通过权重约束得到尾部奇异值平方和最小。
