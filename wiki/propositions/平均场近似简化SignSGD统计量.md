---
type: proposition
title: "平均场近似简化SignSGD统计量"
aliases:
statement: "平均场近似可把 SignSGD 的复杂分布积分压缩为由梯度均值和方差构成的显式 Batch Size 依赖。"
assumptions:
  - "二阶近似有效"
  - "原文列出的独立性、缓变性或平均场近似条件成立"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md"
source_ids:
  - "11280"
requires:
  - "[[二阶近似最优学习率公式]]"
proof_route: "计算更新量一阶矩/二阶矩，并代回最优学习率公式。"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
limits:
  - "非凸深度网络中的严格最优性不在本 batch 内提升为稳定结论。"
examples:
evidence_spans:
  - "ev::11280::方法大意"
  - "ev::11280::计算过程"
status: stable
updated: "2026-06-10"
---

# 平均场近似简化SignSGD统计量

## 命题

平均场近似可把 SignSGD 的复杂分布积分压缩为由梯度均值和方差构成的显式 Batch Size 依赖。

## 证明路线

从对应文章的更新量统计量计算出发，代入二阶近似最优学习率公式，读出 Batch Size 依赖。

## 证据

- `ev::11280::方法大意`
- `ev::11280::计算过程`
