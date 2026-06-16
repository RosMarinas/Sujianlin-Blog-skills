---

type: formula
title: SimSiam快慢动力学公式
aliases: []
latex: \frac{d\varphi}{dt}=-\frac{\partial\mathcal{L}}{\partial\varphi},\quad \frac{d\theta}{dt}=-\frac{\partial\mathcal{L}}{\partial\theta}
symbol_meanings:
  L: SimSiam 目标
  phi: predictor 参数
  theta: encoder 参数
standard_notation:
  phi: predictor 参数
  theta: encoder 参数
  L: SimSiam 目标
conditions:
- 用于比较 predictor 快变量与 encoder 慢变量的局部动力学。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-12-11-从动力学角度看优化算法-六-为什么SimSiam不退化.md
source_ids:
- '7980'
derived_from: []
implies: []
appears_in:
- - - 从动力学角度看优化算法（六）：为什么SimSiam不退化？
evidence_spans:
- ev::7980::不退化的动力学
status: draft
updated: "2026-06-14"
---

# SimSiam快慢动力学公式


## 概述

（待补充）

## 公式

```tex
\frac{d\varphi}{dt}=-\frac{\partial\mathcal{L}}{\partial\varphi},\quad \frac{d\theta}{dt}=-\frac{\partial\mathcal{L}}{\partial\theta}
```

## 条件

- 用于比较 predictor 快变量与 encoder 慢变量的局部动力学。

## 证据

- `ev::7980::不退化的动力学`