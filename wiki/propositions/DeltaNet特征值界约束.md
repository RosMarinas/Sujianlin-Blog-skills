---
type: proposition
title: DeltaNet特征值界约束
statement: 在 DeltaNet 的循环迭代中，转移矩阵 I - eta_t * k_t * k_t^T 的全部特征值必须严格落在区间 [-1, 1] 内，以防止状态矩阵累乘过程中的数值爆炸。
assumptions:
  - 转移矩阵为 I - eta_t * k_t * k_t^T
  - 状态矩阵以递归乘法累加计算
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-12-23-为什么DeltaNet要加L2-Normalize.md
source_ids:
  - 11486
proof_route: 秩为 1 的矩阵 k_t * k_t^T 的非零特征值为 ||k_t||^2，其余特征值均为 0。转移矩阵 I - eta_t * k_t * k_t^T 的特征值中，对应于 k_t 方向的特征值为 1 - eta_t ||k_t||^2，其余特征值全为 1。为了在序列累乘中保证稳定性，要求最大模长特征值的绝对值不超过 1，即 -1 <= 1 - eta_t ||k_t||^2 <= 1，两边整理即得特征值界约束。
evidence_spans:
  - ev::11486::基本解释
status: draft
updated: 2026-06-11
---

该命题为 DeltaNet 中对 Key 向量实施 L2 Normalize 以及给学习率限制在 [0, 1] 内提供了最为直接的代数学证明。