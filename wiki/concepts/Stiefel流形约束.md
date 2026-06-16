---
type: concept
title: Stiefel流形约束
aliases: []
definition: 矩阵参数列正交的等式约束，可由 W^T Phi + Phi^T W = 0 描述切空间。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-08-08-流形上的最速下降-3-Muon-Stiefel.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-11-03-流形上的最速下降-5-对偶梯度下降.md
source_ids:
- '11221'
- '11388'
related_methods:
- - - 用切空间投影改写约束最速下降
series:
- - - 流形上的最速下降
evidence_spans:
- ev::11221::方程变换
- ev::11388::Stiefel上
status: draft
updated: '2026-06-12'
---

# Stiefel流形约束

## 定义

矩阵参数列正交的等式约束，可由 W^T Phi + Phi^T W = 0 描述切空间。

## 激活场景

当矩阵参数 $\boldsymbol{W}\in\mathbb{R}^{n\times m}$ 满足 $n>m$ 且 $\boldsymbol{W}^{\top}\boldsymbol{W}=\boldsymbol{I}$ 时，源文称其所在空间为 Stiefel 流形。它出现在给非方阵参数施加列正交约束的优化问题中，例如希望降低 LoRA 参数化冗余或保持类别矩阵的正交结构。

## 关键关系

对更新方向 $\boldsymbol{\Phi}$，一阶近似把更新后仍满足列正交的条件写成
$$
\boldsymbol{W}^{\top}\boldsymbol{\Phi}+\boldsymbol{\Phi}^{\top}\boldsymbol{W}=\boldsymbol{0}.
$$
源文 `11221` 进一步说明 Stiefel 情形比方阵正交更难，因为 $\boldsymbol{W}^{\top}$ 不能直接吸收到 $\mathop{\text{msign}}$ 中；求解需要对称矩阵 $\boldsymbol{X}$，使 $\boldsymbol{\Phi}=\mathop{\text{msign}}(\boldsymbol{G}+\boldsymbol{W}\boldsymbol{X})$ 落在切空间内。

## 证据关系

源文 `11388` 给出对偶梯度下降视角：令 $\boldsymbol{X}$ 与模型参数同步更新，可近似实现 Stiefel 上的 Muon 最速下降。当前页保持 `draft`，因为它只覆盖该系列中的 Muon + Stiefel 用法。

## 证据

- `ev::11221::方程变换`
- `ev::11388::Stiefel上`
