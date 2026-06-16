---
type: example
title: spaces-11196-超球面切空间投影
aliases: []
article_id: '11196'
article:
- - 流形上的最速下降：1. SGD + 超球面
section: 几何意义
claim: 球面约束下的最快下降方向是梯度到切空间的投影。
notation_mapping:
  w: boldsymbol{w}
  g: boldsymbol{g}
  phi: boldsymbol{varphi}
steps:
- 从最速下降约束公式出发
- 把球面保持约束一阶化
- 得到方向与参数正交
- 将梯度投影到切空间并归一化
used_concepts:
- - - 流形最速下降
- - - 切空间投影
used_formulas:
- - - 最速下降约束公式
- - - 球面切空间投影公式
used_methods:
- - - 用切空间投影改写约束最速下降
problem_pattern:
- - 把约束优化器更新转化为切空间或对偶变量问题
source_span: ev::11196::几何意义
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-08-01-流形上的最速下降-1-SGD-超球面.md
source_ids:
- '11196'
status: stable
updated: '2026-06-12'
---

# spaces-11196-超球面切空间投影

## 问题

源文在“超球面上”和“几何意义”两节讨论参数 $\boldsymbol{w}$ 被约束在单位球面时，最速下降方向应如何从普通梯度修正而来。

## 推导

目标写成
$$
\max_{\boldsymbol{\varphi}}\langle\boldsymbol{g},\boldsymbol{\varphi}\rangle
\quad\text{s.t.}\quad
\Vert\boldsymbol{\varphi}\Vert_2=1,\quad
\Vert\boldsymbol{w}-\eta\boldsymbol{\varphi}\Vert_2=1,\quad
\Vert\boldsymbol{w}\Vert_2=1.
$$
在 $\eta$ 足够小时，一阶近似给出
$$
1=\Vert\boldsymbol{w}-\eta\boldsymbol{\varphi}\Vert_2^2
\approx1-2\eta\langle\boldsymbol{w},\boldsymbol{\varphi}\rangle,
$$
因此方向必须满足 $\langle\boldsymbol{w},\boldsymbol{\varphi}\rangle=0$。引入待定系数后解得
$$
\boldsymbol{\varphi}=
\frac{\boldsymbol{g}-\langle\boldsymbol{g},\boldsymbol{w}\rangle\boldsymbol{w}}
{\Vert\boldsymbol{g}-\langle\boldsymbol{g},\boldsymbol{w}\rangle\boldsymbol{w}\Vert_2}.
$$

## 方法与证据

本例体现“把球面约束一阶化为切空间正交约束，再投影梯度”的方法。证据锚点为 `ev::11196::几何意义`，源文明确把 $\boldsymbol{g}-\langle\boldsymbol{g},\boldsymbol{w}\rangle\boldsymbol{w}$ 解释为梯度到切空间的投影。
