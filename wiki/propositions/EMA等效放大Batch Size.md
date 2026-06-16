---
type: proposition
title: "EMA等效放大Batch Size"
aliases:
statement: "在梯度和协方差缓变、时间步趋于稳定的条件下，动量 EMA 约等于把 Batch Size 放大到 (1+beta_1)/(1-beta_1) 倍。"
assumptions:
  - "二阶近似有效"
  - "原文列出的独立性、缓变性或平均场近似条件成立"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md"
source_ids:
  - "11301"
requires:
  - "[[二阶近似最优学习率公式]]"
proof_route: "计算更新量一阶矩/二阶矩，并代回最优学习率公式。"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
limits:
  - "非凸深度网络中的严格最优性不在本 batch 内提升为稳定结论。"
examples:
evidence_spans:
  - "ev::11301::放大批量"
status: stable
updated: "2026-06-10"
---

# EMA等效放大Batch Size

## 命题

在梯度和协方差缓变、时间步趋于稳定的条件下，动量 EMA 约等于把 Batch Size 放大到 (1+beta_1)/(1-beta_1) 倍。

## 证明路线

从对应文章的更新量统计量计算出发，代入二阶近似最优学习率公式，读出 Batch Size 依赖。

## 证据

- `ev::11301::放大批量`
