---

type: concept
title: logsumexp
aliases: []
definition: $\max$ 函数的光滑近似，定义为 $\operatorname{logsumexp}(x_1,\dots,x_n)=\log\sum_{i=1}^n
  e^{x_i}$。
standard_notation: true
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2019-05-20-函数光滑化杂谈-不可导函数的可导逼近.md
source_ids:
- '6620'
prerequisites: []
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods: []
series: []
evidence_spans: []
status: draft
updated: '2026-06-12'
---
# logsumexp

## 定义
Log-Sum-Exp 是一种在数值计算中用于稳定计算多个指数和的对数的技巧，防止直接计算指数时发生数值溢出（overflow）或下溢（underflow）。

## 数学表达
对于目标实数向量 $\boldsymbol{x} = [x_1, x_2, \dots, x_n]$，计算：
$$\text{LSE}(\boldsymbol{x}) = \log \sum_{i=1}^n e^{x_i}$$
当 $x_i$ 很大时直接计算会带来溢出。LSE 技巧通过引入最大值 $c = \max_i x_i$ 进行平移：
$$\text{LSE}(\boldsymbol{x}) = c + \log \sum_{i=1}^n e^{x_i - c}$$
这在 Softmax 损失函数计算和配分函数计算中极为常用。
