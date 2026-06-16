---
type: formula
title: EMA等效Batch Size公式
aliases: null
latex: B_{eff}=\frac{1+\beta_1}{1-\beta_1}B
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
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md
source_ids:
- '11301'
derived_from: null
implies: null
appears_in:
- '[[重新思考学习率与Batch Size（四）：EMA]]'
evidence_spans:
- ev::11301::放大批量
- ev::11301::符号动量
status: draft
updated: "2026-06-14"
---

# EMA等效Batch Size公式


## 概述

（待补充）

## 公式

```tex
B_{eff}=\frac{1+\beta_1}{1-\beta_1}B
```

## 作用

EMA等效Batch Size公式 $B_{eff}=\frac{1+\beta_1}{1-\beta_1}B$ 揭示了在神经网络优化器（如带动量的SGD、SignSGDM、Lion甚至Muon）中，梯度的指数滑动平均（EMA）在减小梯度噪声方面的数学本质。通过分析平均场近似下的优化目标并计算EMA后的随机梯度期望与协方差，结果表明：引入动量系数 $\beta_1$ 后，其不仅相当于平滑了梯度轨迹，更是在方差缩减效果上，将原本的 Batch Size $B$ 直接等效放大到了 $\frac{1+\beta_1}{1-\beta_1}$ 倍。这意味着动量以极低的计算成本降低了梯度的随机噪声。然而，这也提示随着动量 $\beta_1$ 的增大，模型将更容易面临“Surge现象”（即随着实际 Batch Size 的增加，最优学习率反而需要减小的反常现象）。

## 证据

- `ev::11301::放大批量`
- `ev::11301::符号动量`
