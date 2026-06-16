---
type: concept
title: MesaNet
aliases:
- Mesa-optimization Attention
- 解析解线性回归Attention
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
- '10017'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
definition: MesaNet利用线性回归的解析解来构建序列模型。它维护G_t = ∑v_j k_j^T和H_t = ∑k_j k_j^T两个状态量，通过解析解S_t
  = G_t H_t^{-1}来计算输出。
---

# MesaNet

## Definition

MesaNet利用线性回归的解析解来构建序列模型。它维护G_t = ∑v_j k_j^T和H_t = ∑k_j k_j^T两个状态量，通过解析解S_t = G_t H_t^{-1}来计算输出。

## Key Formulas

o_t = G_t (H_t + Lambda_t)^{-1} q_t
G_t = gamma_t G_{t-1} + v_t k_t^T
H_t = gamma_t H_{t-1} + k_t k_t^T

## 优缺点

优点：理论上通常优于DeltaNet，因为是解析解
缺点：H_t + Lambda_t不是三角阵，求逆更复杂（需共轭梯度法）；K=V时退化为单位阵；灵活性不如DeltaNet