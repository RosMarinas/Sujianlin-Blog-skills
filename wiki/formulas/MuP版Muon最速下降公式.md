---

type: formula
title: MuP版Muon最速下降公式
aliases: []
latex: \Delta W=-\eta\sqrt{d_{out}/d_{in}}\,\operatorname{msign}(G),\quad G=\nabla_W\mathcal{L}(W)
symbol_meanings:
  G: 梯度矩阵
  eta: 学习率
  msign: 矩阵符号函数
standard_notation:
  G: 梯度矩阵
  eta: 学习率
  msign: 矩阵符号函数
conditions:
- 在更新稳定性谱范数约束和一阶损失近似下求最速下降。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-02-15-MuP之上-2-线性层与最速下降.md
source_ids:
- '11605'
derived_from: []
implies: []
appears_in:
- '11605'
evidence_spans:
- ev::11605::求解过程
- ev::11605::结果汇总
status: draft
updated: "2026-06-14"
---

# MuP版Muon最速下降公式


## 概述

（待补充）

## 公式

```tex
\Delta W=-\eta\sqrt{d_{out}/d_{in}}\,\operatorname{msign}(G),\quad G=\nabla_W\mathcal{L}(W)
```

## 条件

- 在更新稳定性谱范数约束和一阶损失近似下求最速下降。

## 证据

- `ev::11605::求解过程`
- `ev::11605::结果汇总`