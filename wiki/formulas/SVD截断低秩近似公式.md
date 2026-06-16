---

type: formula
title: SVD截断低秩近似公式
aliases:
- truncated SVD formula
latex: M_r=U_{[:,:r]}\Sigma_{[:r,:r]}V_{[:,:r]}^T,\quad \|M-M_r\|_F^2=\sum_{j>r}\sigma_j^2
symbol_meanings:
  \boldsymbol{\Sigma}: 非负对角矩阵且对角线元素（奇异值）默认从大到小排列（即 $\sigma_1\geq \sigma_2\geq \cdots \geq 0$）
  \boldsymbol{\Sigma}_{[:r,:r]}: 可重构出原矩阵的最佳低秩近似矩阵 $M_r$
standard_notation:
  convention: Use the symbols exactly as defined in `latex`; meanings are listed in
    `symbol_meanings`.
conditions:
- Frobenius 范数下的无约束 `r` 秩近似。
- 奇异值按非增顺序排列。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-10-01-低秩近似之路-二-SVD.md
source_ids:
- '10407'
derived_from:
- '[[奇异值分解]]'
implies:
- '[[SVD截断给出F范数下的最优r秩近似]]'
appears_in:
- '[[低秩近似之路（二）：SVD]]'
evidence_spans:
- ev::10407::近似定理
status: draft
updated: "2026-06-14"
---
## 概述

（待补充）



## 说明

该公式给出了给定矩阵 $\boldsymbol{M} \in \mathbb{R}^{n \times m}$ 在无约束条件下的最优 $r$ 秩近似（即求解最优化问题 $\mathop{\text{argmin}}_{\boldsymbol{A},\boldsymbol{B}}\Vert \boldsymbol{A}\boldsymbol{B} - \boldsymbol{M}\Vert_F^2$，其中 $\boldsymbol{A}\in\mathbb{R}^{n\times r}, \boldsymbol{B}\in\mathbb{R}^{r\times m}, r < \min(n,m)$）。这是本批所有结构化低秩近似算法的误差最优理论基准。

根据奇异值分解（SVD）定理，任何矩阵皆可分解为 $\boldsymbol{M} = \boldsymbol{U}\boldsymbol{\Sigma} \boldsymbol{V}^{\top}$，其中 $\boldsymbol{U}\in\mathbb{R}^{n\times n}$ 与 $\boldsymbol{V}\in\mathbb{R}^{m\times m}$ 均为正交矩阵，$\boldsymbol{\Sigma}$ 为非负对角矩阵且对角线元素（奇异值）默认从大到小排列（即 $\sigma_1\geq \sigma_2\geq \cdots \geq 0$）。

在数值计算中，通过截断操作保留 $\boldsymbol{U}$ 和 $\boldsymbol{V}$ 的前 $r$ 列（即 $\boldsymbol{U}_{[:,:r]}$ 和 $\boldsymbol{V}_{[:,:r]}$），以及 $\boldsymbol{\Sigma}$ 的前 $r \times r$ 子矩阵 $\boldsymbol{\Sigma}_{[:r,:r]}$，即可重构出原矩阵的最佳低秩近似矩阵 $M_r$。此时，原矩阵与近似矩阵之间的重构误差（Frobenius 范数平方）严格等于所有被舍弃的较小奇异值的平方和，即 $\|M-M_r\|_F^2=\sum_{j>r}\sigma_j^2$。

CR、ID、CUR 等其他低秩近似分解算法的价值不在于超越或替代 SVD 的这个无约束最优结论，而在于它们能够保留原始矩阵中的实际行或列，从而显著增加分解模型的结构性和可解释性。
