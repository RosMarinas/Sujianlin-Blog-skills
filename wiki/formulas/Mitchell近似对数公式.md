---
type: formula
title: Mitchell近似对数公式
aliases:
  - Mitchell log approximation
  - Mitchell binary logarithm
latex: \log_2 p \approx n + x
symbol_meanings:
  - "$p$": 待求对数的非负实数
  - "$n$": p 的二进制表示中整数部分的位数减1
  - "$x$": $\sum_{i=-m}^{n-1} z_i 2^{i-n}$，即小数部分的数值
standard_notation: "$\text{MitchellLog}_2(p)$"
conditions: "二进制表示 $p = 2^n(1+x)$，其中 $x \in [0,1)$"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-12-14-Mitchell近似-乘法变为加法-误差不超过1-9.md
source_ids:
  - "7991"
derived_from: []
implies:
  - "proposition::Mitchell近似误差上界"
appears_in:
  - "article::Mitchell近似：乘法变为加法，误差不超过1/9"
evidence_spans: []
status: draft
updated: 2026-06-12
---
## 概述

（待补充）



## 公式

利用近似 $\log_2(1+x) \approx x$（$x \in [0,1)$）：

$$
\log_2 p = \log_2[2^n(1+x)] = n + \log_2(1+x) \approx n + x
$$

对应的指数近似：
$$
2^{n+x} \approx 2^n(1+x)
$$

## 误差分析

- 当 $x_1 + x_2 < 1$：近似比例为 $(1+x_1+x_2)/(1+x_1+x_2+x_1x_2)$
- 当 $x_1 + x_2 \geq 1$：近似比例为 $2(x_1+x_2)/(1+x_1+x_2+x_1x_2)$
- 最大相对误差：$1/9$（在 $x_1=x_2=0.5$ 时达到）
