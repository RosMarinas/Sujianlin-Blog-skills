---
type: formula
title: LRU循环方程
aliases:
  - LRU Recurrent Equation
latex: x_t = \lambda x_{t-1} + \gamma u_t
symbol_meanings:
  x_t: 在 t 时刻的复隐藏状态向量（对角化空间分量）
  u_t: 在 t 时刻的输入特征投影向量
  \lambda: 复数转移特征值系数（模长 r，相位角 theta）
  \gamma: 实数对齐缩放系数
standard_notation:
  x_t: hidden_state
  u_t: input_projection
  lambda: complex_eigenvalue
  gamma: scaling_factor
conditions: 所有计算均在复数域中进行以确保对角化不会丢失一般实矩阵的拟合能力，且模长满足 $r < 1$。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
source_ids:
  - 9554
appears_in:
  - [spaces-9554-Google新作试图“复活”RNN-RNN能否再次辉煌](wiki/sources/spaces-9554-Google新作试图“复活”RNN-RNN能否再次辉煌.md)
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# LRU循环方程


## 概述

（待补充）

## Latex
$$x_t = \lambda x_{t-1} + \gamma u_t$$

## Symbol Meanings
- $x_t$: 在 t 时刻的复隐藏状态向量（对角化空间分量）
- $u_t$: 在 t 时刻的输入特征投影向量
- $\lambda$: 复数转移特征值系数（模长 r，相位角 theta）
- $\gamma$: 实数对齐缩放系数

## Conditions
所有计算均在复数域中进行以确保对角化不会丢失一般实矩阵的拟合能力，且模长满足 $r < 1$。