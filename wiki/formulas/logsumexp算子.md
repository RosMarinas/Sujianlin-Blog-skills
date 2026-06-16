---
type: formula
title: logsumexp算子
aliases:
  - LogSumExp
  - Smooth max
latex: \log\left(\sum_{i=1}^n e^{x_i}\right)
symbol_meanings:
  - "$x_i$": 输入向量的第 i 个分量
  - "$n$": 向量维度
standard_notation: "$\text{logsumexp}(x_1, \dots, x_n)$"
conditions: "任意实数输入 $x_i$"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-05-20-函数光滑化杂谈-不可导函数的可导逼近.md
source_ids:
  - "6620"
derived_from: []
implies: []
appears_in:
  - "article::函数光滑化杂谈：不可导函数的可导逼近"
evidence_spans: []
status: draft
updated: 2026-06-12
---
## 概述

（待补充）



## 公式

$$
\max(x_1,x_2,\dots,x_n) \approx \log\left(\sum_{i=1}^n e^{x_i}\right) \triangleq \text{logsumexp}(x_1,\dots,x_n)
$$

更一般的形式含温度参数 $K$：
$$
\max(x_1,x_2,\dots,x_n) \approx \frac{1}{K}\log\left(\sum_{i=1}^n e^{K x_i}\right)
$$
