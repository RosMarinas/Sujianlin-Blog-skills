---
type: formula
title: SquarePlus公式
aliases:
  - SquarePlus
latex: \text{SquarePlus}(x) = \frac{x + \sqrt{x^2 + b}}{2}
symbol_meanings:
  - "$x$": 输入值
  - "$b > 0$": 光滑参数，控制原点处的光滑程度
standard_notation: "$\text{SquarePlus}(x)$"
conditions: "$b > 0$，$x \in \mathbb{R}$"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-12-29-SquarePlus-可能是运算最简单的ReLU光滑近似.md
source_ids:
  - "8833"
derived_from: []
implies:
  - "proposition::SquarePlus凸性与恒大于条件"
appears_in:
  - "article::SquarePlus：可能是运算最简单的ReLU光滑近似"
evidence_spans: []
status: draft
updated: 2026-06-12
---
## 概述

（待补充）



## 公式

$$
\text{SquarePlus}(x) = \frac{x + \sqrt{x^2 + b}}{2}, \quad b > 0
$$

### 导数

$$
\frac{d}{dx}\text{SquarePlus}(x) = \frac{1}{2}\left(1 + \frac{x}{\sqrt{x^2+b}}\right) > 0
$$

$$
\frac{d^2}{dx^2}\text{SquarePlus}(x) = \frac{b}{2(x^2+b)^{3/2}} > 0
$$
