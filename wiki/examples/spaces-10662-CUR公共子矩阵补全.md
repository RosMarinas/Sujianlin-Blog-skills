---
type: example
title: spaces-10662-CUR公共子矩阵补全
aliases: []
article_id: '10662'
article: '[[低秩近似之路（五）：CUR]]'
section: U的选择
claim: 当 CUR 中间矩阵取公共子矩阵伪逆时，近似可解释为保留选中行列并补全未选块。
notation_mapping:
  M: source M
  C: source C
  R: source R
  U: source U
steps:
- 通过行列交换把选中行列放到分块矩阵的前部。
- 令公共块为 `A`，列骨架为 `[A; C]`，行骨架为 `[A B]`。
- 取中间矩阵 `A^{-1}` 或公共块伪逆。
- 得到右下块近似 `C A^{-1} B`，即用选中行列补全未选块。
used_concepts:
- '[[CUR分解]]'
- '[[伪逆]]'
used_formulas:
- '[[CUR中间矩阵伪逆公式]]'
used_methods:
- '[[将矩阵近似问题化为骨架选择问题]]'
problem_pattern: '[[在误差最优与结构可解释之间选择低秩近似]]'
source_span: ev::10662::U的选择
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-01-12-低秩近似之路-五-CUR.md
source_ids:
- '10662'
status: stable
updated: '2026-06-12'
---

## 问题

源文“U的选择”讨论 CUR 分解中间矩阵 $\boldsymbol{\mathcal{U}}$ 的取法：给定选中的列 $\boldsymbol{\mathcal{C}}$ 和行 $\boldsymbol{\mathcal{R}}$ 后，如何让近似既可计算又有矩阵补全解释。

## 推导

理论最优解是
$$
\boldsymbol{\mathcal{U}}^*=\boldsymbol{\mathcal{C}}^{\dagger}\boldsymbol{M}\boldsymbol{\mathcal{R}}^{\dagger},
$$
而源文重点解释更直观的常用选择
$$
\boldsymbol{\mathcal{U}}=\boldsymbol{M}_{[S_2,S_1]}^{\dagger}.
$$
通过交换行列，把公共子矩阵记作 $\boldsymbol{A}$，原矩阵分块为 $\begin{pmatrix}\boldsymbol{A}&\boldsymbol{B}\\\boldsymbol{C}&\boldsymbol{D}\end{pmatrix}$。若 $\boldsymbol{A}$ 可逆，则 CUR 近似写成
$$
\begin{pmatrix}\boldsymbol{A}\\\boldsymbol{C}\end{pmatrix}\boldsymbol{A}^{-1}\begin{pmatrix}\boldsymbol{A}&\boldsymbol{B}\end{pmatrix}
=\begin{pmatrix}\boldsymbol{A}&\boldsymbol{B}\\\boldsymbol{C}&\boldsymbol{C}\boldsymbol{A}^{-1}\boldsymbol{B}\end{pmatrix}.
$$

## 方法与证据

本例体现“用公共子矩阵伪逆把矩阵近似解释为补全”的方法：选中行列 $\boldsymbol{A},\boldsymbol{B},\boldsymbol{C}$ 被精确保留，未选块 $\boldsymbol{D}$ 由 $\boldsymbol{C}\boldsymbol{A}^{-1}\boldsymbol{B}$ 近似。证据锚点为 `ev::10662::U的选择`。
