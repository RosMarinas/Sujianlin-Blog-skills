---
type: example
title: spaces-10407-SVD截断证明
aliases: []
article_id: '10407'
article: '[[低秩近似之路（二）：SVD]]'
section: 近似定理
claim: SVD 截断证明通过正交不变性把一般矩阵低秩近似化为非负对角阵截断。
notation_mapping:
  same_as_standard: true
steps:
- 将 `M` 写成 `U Sigma V^T`。
- 用正交不变性把 `||AB-M||_F^2` 转为 `||U^T ABV-Sigma||_F^2`。
- 观察 `U^T ABV` 仍代表任意秩不超过 `r` 的矩阵。
- 对非负对角阵证明保留最大 `r` 个对角元的尾部平方和最小。
used_concepts:
- '[[奇异值分解]]'
used_formulas:
- '[[SVD截断低秩近似公式]]'
used_methods: []
problem_pattern: '[[在误差最优与结构可解释之间选择低秩近似]]'
source_span: ev::10407::近似定理
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-10-01-低秩近似之路-二-SVD.md
source_ids:
- '10407'
status: stable
updated: '2026-06-12'
---

## 问题

源文“近似定理”一节要证明 Eckart-Young-Mirsky 定理中的关键实例：若 $\boldsymbol{M}=\boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^{\top}$，则最优 $r$ 秩近似由截断后的 $\boldsymbol{U}_{[:n,:r]}\boldsymbol{\Sigma}_{[:r,:r]}\boldsymbol{V}_{[:m,:r]}^{\top}$ 给出。

## 推导

前文已经利用 SVD 的正交不变性，把一般矩阵的低秩近似问题化为非负对角阵 $\boldsymbol{\Sigma}$ 的问题。源文随后固定 $\boldsymbol{A}$ 时令 $\boldsymbol{B}$ 取 $\boldsymbol{A}^{\dagger}\boldsymbol{\Sigma}$，把目标改写为
$$
\min_{\boldsymbol{A}}\Vert(\boldsymbol{A}\boldsymbol{A}^{\dagger}-\boldsymbol{I}_n)\boldsymbol{\Sigma}\Vert_F^2.
$$
再对 $\boldsymbol{A}$ 做 SVD，利用 $\boldsymbol{\Sigma}_{\boldsymbol{A}}\boldsymbol{\Sigma}_{\boldsymbol{A}}^{\dagger}$ 是前 $r_{\boldsymbol{A}}$ 项为 1 的对角投影，把问题化成在正交行向量权重 $w_j$ 下最小化 $\sum_j\sigma_j^2w_j$。由于 $0\leq w_j\leq1$ 且总和为 $k\geq n-r$，最小值只能取最小的 $k$ 个奇异值平方之和，最终误差为 $\sum_{j=r+1}^n\sigma_j^2$。

## 方法与证据

本例的方法是“先用正交不变性降到对角阵，再把投影误差转成带约束的权重选择”。证据锚点为 `ev::10407::近似定理`，源文逐步给出伪逆、正交投影、权重和奇异值截断的推导。
