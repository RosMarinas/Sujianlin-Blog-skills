---
type: formula
title: CUR中间矩阵伪逆公式
aliases:
- CUR U pseudoinverse formula
latex: \mathcal{U}^*=\mathcal{C}^\dagger M\mathcal{R}^\dagger;\quad \mathcal{U}=M_{[S_2,S_1]}^\dagger
symbol_meanings:
  C: 选中的原矩阵列
  M: 原矩阵
  R: 选中的原矩阵行
  S_1: 列索引集合
  S_2: 行索引集合
  U: CUR 中间矩阵
standard_notation:
  M: 原矩阵
  C: 选中的原矩阵列
  R: 选中的原矩阵行
  U: CUR 中间矩阵
  S_1: 列索引集合
  S_2: 行索引集合
conditions:
- '`C` 和 `R` 已经选定。'
- 第一式是 Frobenius 范数下的最优中间矩阵；第二式是常用直观选择。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-01-12-低秩近似之路-五-CUR.md
source_ids:
- '10662'
derived_from:
- '[[伪逆]]'
implies: '[]'
appears_in:
- '[[低秩近似之路（五）：CUR]]'
evidence_spans:
- ev::10662::U的选择
status: draft
updated: "2026-06-14"
---
## 概述

（待补充）



## 说明

CUR分解旨在为原始矩阵 $\boldsymbol{M}\in\mathbb{R}^{n\times m}$ 寻找一个结构清晰的低秩近似。相比于SVD分解中复杂的左右正交矩阵和简单的对角中间矩阵，CUR分解的特点在于直接复用原始矩阵的列集 $\boldsymbol{\mathcal{C}} = \boldsymbol{M}_{[:,S_1]}$ 与行集 $\boldsymbol{\mathcal{R}} = \boldsymbol{M}_{[S_2,:]}$ 作为左右矩阵（其中 $S_1, S_2$ 分别为大小为 $r$ 的列与行索引集合）。这种构造方式保留了矩阵原始元素的物理意义，带来了更优的可解释性与更低的储存成本，但同时也意味着中间矩阵 $\boldsymbol{\mathcal{U}}\in\mathbb{R}^{r\times r}$ 结构上要比SVD的奇异值对角阵更为复杂。

该公式明确了在逼近目标 $\mathop{\text{argmin}}_{S_1,S_2,\boldsymbol{\mathcal{U}}}\Vert \boldsymbol{\mathcal{C}}\boldsymbol{\mathcal{U}}\boldsymbol{\mathcal{R}} - \boldsymbol{M}\Vert_F^2$ 下，参数求解过程中的连续优化部分与离散选择部分的解耦关系。一旦行与列（即 $\boldsymbol{\mathcal{C}}$ 和 $\boldsymbol{\mathcal{R}}$）选定，中间矩阵 $\boldsymbol{\mathcal{U}}$ 就不再需要迭代求解，而是可以通过 Moore-Penrose 伪逆直接给出使得 Frobenius 范数误差最小的解析最优解：$\boldsymbol{\mathcal{U}}^* = \boldsymbol{\mathcal{C}}^{\dagger}\boldsymbol{M}\boldsymbol{\mathcal{R}}^{\dagger}$。同时，在应用中为了计算的简便性，还存在另一种直观的构造方式，即直接选取原矩阵行列交集子矩阵的伪逆，表示为 $\boldsymbol{\mathcal{U}} = \boldsymbol{M}_{[S_2,S_1]}^{\dagger}$。正因为中间矩阵具有如此确定的解析形式，CUR分解的主要技术挑战和复杂度便完全集中于：如何设计高效的算法去寻找那两组最优的离散行列索引 $S_1$ 和 $S_2$。
