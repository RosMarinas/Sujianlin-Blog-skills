---
type: proposition
title: "Muon学习率尺度律近似SignSGD"
aliases:
statement: "在原文采用的 Hessian 线性算子假设下，Muon 的最优学习率关于 Batch Size 的形式与 SignSGD 一致。"
assumptions:
  - "二阶近似有效"
  - "原文列出的独立性、缓变性或平均场近似条件成立"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md"
source_ids:
  - "11285"
requires:
  - "[[二阶近似最优学习率公式]]"
proof_route: "计算更新量一阶矩/二阶矩，并代回最优学习率公式。"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
limits:
  - "非凸深度网络中的严格最优性不在本 batch 内提升为稳定结论。"
examples:
evidence_spans:
  - "ev::11285::相同规律"
status: stable
updated: "2026-06-10"
---

# Muon学习率尺度律近似SignSGD

## 命题

在原文采用的 Hessian 线性算子假设下，Muon 的最优学习率关于 Batch Size 的形式与 SignSGD 一致。

## 证明路线

从对应文章的更新量统计量计算出发，代入二阶近似最优学习率公式，读出 Batch Size 依赖。

## 证据

- `ev::11285::相同规律`
