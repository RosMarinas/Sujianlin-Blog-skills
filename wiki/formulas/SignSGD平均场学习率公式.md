---
type: formula
title: SignSGD平均场学习率公式
aliases: null
latex: \eta^* \approx \frac{\sum_i |g_i|}{\beta^{-1}\sum_i H_{i,i}+\beta\sum_{i\ne
  j}H_{i,j}\operatorname{sign}(g_i g_j)},\quad \beta=(1+\mathcal{B}_{simple}/B)^{-1/2}
symbol_meanings:
  eta_star: \eta^*
  noise_scale: \mathcal{B}_{simple}
standard_notation:
  eta_star: \eta^*
  batch_size: B
  noise_scale: \mathcal{B}_{simple}
conditions:
- 二阶损失近似有效
- 更新量统计量可由对应原文假设近似
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md
source_ids:
- '11280'
derived_from: null
implies: null
appears_in:
- '[[重新思考学习率与Batch Size（二）：平均场]]'
evidence_spans:
- ev::11280::反常现象
status: draft
updated: "2026-06-14"
---

# SignSGD平均场学习率公式


## 概述

（待补充）

## 公式

```tex
\eta^* \approx \frac{\sum_i |g_i|}{\beta^{-1}\sum_i H_{i,i}+\beta\sum_{i\ne j}H_{i,j}\operatorname{sign}(g_i g_j)},\quad \beta=(1+\mathcal{B}_{simple}/B)^{-1/2}
```

## 作用

SignSGD 中最优学习率关于标准化 Batch Size 的平均场表达式。

## 证据

- `ev::11280::反常现象`