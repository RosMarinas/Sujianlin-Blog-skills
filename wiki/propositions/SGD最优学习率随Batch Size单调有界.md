---
type: proposition
title: "SGD最优学习率随Batch Size单调有界"
aliases:
statement: "SGD 的二阶近似最优学习率可写为 eta_max/(1+B_noise/B)，随 Batch Size 单调增大但有上界。"
assumptions:
  - "二阶近似有效"
  - "原文列出的独立性、缓变性或平均场近似条件成立"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-01-重新思考学习率与Batch-Size-一-现状.md"
source_ids:
  - "11260"
requires:
  - "[[二阶近似最优学习率公式]]"
proof_route: "计算更新量一阶矩/二阶矩，并代回最优学习率公式。"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
limits:
  - "非凸深度网络中的严格最优性不在本 batch 内提升为稳定结论。"
examples:
evidence_spans:
  - "ev::11260::热身练习"
status: stable
updated: "2026-06-10"
---

# SGD最优学习率随Batch Size单调有界

## 命题

SGD 的二阶近似最优学习率可写为 eta_max/(1+B_noise/B)，随 Batch Size 单调增大但有上界。

## 证明路线

从对应文章的更新量统计量计算出发，代入二阶近似最优学习率公式，读出 Batch Size 依赖。

## 证据

- `ev::11260::热身练习`
