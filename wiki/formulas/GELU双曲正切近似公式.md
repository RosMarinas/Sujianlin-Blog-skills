---
type: formula
title: GELU双曲正切近似公式
aliases:
  - GELU tanh approximation
  - GELU approximation with tanh
latex: \frac{1}{2}x\left[1 + \tanh\left(\sqrt{\frac{2}{\pi}}\left(x + 0.044715 x^3\right)\right)\right]
symbol_meanings:
  - "$x$": 输入值
standard_notation: "$\text{GELU}(x)$"
conditions: "任意实数 $x$"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
source_ids:
  - "7309"
derived_from: []
implies: []
appears_in:
  - "article::GELU的两个初等函数近似是怎么来的"
evidence_spans: []
status: draft
updated: 2026-06-12
---
## 概述

（待补充）



## 公式

GELU的精确形式：
$$
\text{GELU}(x) = x\Phi(x) = \frac{1}{2}x\left[1 + \text{erf}\left(\frac{x}{\sqrt{2}}\right)\right]
$$

### Tanh近似（全局minimax优化结果）
$$
\text{GELU}(x) \approx \frac{1}{2}x\left[1 + \tanh\left(\sqrt{\frac{2}{\pi}}\left(x + 0.044715 x^3\right)\right)\right]
$$

### Sigmoid近似
$$
\text{GELU}(x) \approx x \sigma(1.702 x)
$$
