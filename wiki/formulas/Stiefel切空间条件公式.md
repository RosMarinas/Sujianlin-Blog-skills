---

type: formula
title: Stiefel切空间条件公式
aliases: []
latex: "\boldsymbol{W}^{\top}\boldsymbol{\Phi}+\boldsymbol{\Phi}^{\top}\boldsymbol{W}=\b\
  oldsymbol{0}"
symbol_meanings:
  Phi: 可行更新方向
  W: 约束矩阵参数
standard_notation:
  W: 约束矩阵参数
  Phi: 可行更新方向
conditions:
- W^T W=I 的一阶可行方向条件。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-08-08-流形上的最速下降-3-Muon-Stiefel.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-11-03-流形上的最速下降-5-对偶梯度下降.md
source_ids:
- '11221'
- '11388'
derived_from: []
implies: []
appears_in:
- - - 流形上的最速下降：3. Muon + Stiefel
- - - 流形上的最速下降：5. 对偶梯度下降
evidence_spans:
- ev::11221::方程变换
- ev::11388::Stiefel上
status: draft
updated: "2026-06-14"
---

# Stiefel切空间条件公式


## 概述

（待补充）

## 公式

```tex
\boldsymbol{W}^{\top}\boldsymbol{\Phi}+\boldsymbol{\Phi}^{\top}\boldsymbol{W}=\boldsymbol{0}
```

## 条件

- W^T W=I 的一阶可行方向条件。

## 证据

- `ev::11221::方程变换`
- `ev::11388::Stiefel上`