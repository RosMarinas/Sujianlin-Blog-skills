---
type: concept
title: W距离
aliases:
- Wasserstein distance
- Earth Mover distance
definition: 基于最优传输理论的距离度量：W_rho[p,q]=(inf_{gamma in Pi[p,q]} iint gamma(x,y)||x-y||^rho
  dxdy)^{1/rho}
standard_notation: W_rho[p,q]
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
source_ids:
- '8512'
evidence_spans: []
series: []
status: deprecated
replaced_by: '[[concept::Wasserstein距离]]'
updated: '2026-06-12'
deprecation_reason: Merged into concept::Wasserstein距离 as part of Pass A node boundary
  repair. Same mathematical object (Wasserstein distance / W-distance) under different
  node names.
---

## 定义

基于最优传输理论的距离度量：W_rho[p,q]=(inf_{gamma in Pi[p,q]} iint gamma(x,y)||x-y||^rho dxdy)^{1/rho}

## 标准符号

W_rho[p,q]