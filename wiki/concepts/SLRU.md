---
type: concept
title: SLRU
aliases:
  - Simpler Linear Recurrent Unit
  - 简化线性循环单元
definition: |
  简化线性循环单元（Simpler Linear Recurrent Unit）是LRU模型的实数域简化变体。它摒弃了LRU中用于拟合一般复特征值的复数投影矩阵和复数特征对角矩阵，纯粹保留实数的指数衰减系数来进行序列状态的线性循环计算。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
source_ids:
  - 9554
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# SLRU

## Definition
简化线性循环单元（Simpler Linear Recurrent Unit）是LRU模型的实数域简化变体。它摒弃了LRU中用于拟合一般复特征值的复数投影矩阵和复数特征对角矩阵，纯粹保留实数的指数衰减系数来进行序列状态的线性循环计算。

## Details
SLRU 是对 LRU 的一种极简化探索。在复数域中进行计算虽然在理论上等价于一般矩阵的对角化，但会带来额外的复数运算开销并使得模型难以直接套用常规的实数层（如 Dense 层）。
SLRU 假设状态转移系数 $\lambda$ 均为实数（即相位 $\theta = 0$），将公式退化为实数标量循环。
尽管 SLRU 的实现和直觉更加简单，但其在语言模型任务上的实验效果显著差于包含复特征值的 LRU，这表明在复数域中引入相位的旋转变换和复投影对线性RNN保留完整的序列拟合能力具有不可替代的价值。