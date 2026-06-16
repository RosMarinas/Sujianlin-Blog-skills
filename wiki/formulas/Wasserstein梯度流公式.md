---
title: Wasserstein梯度流公式
type: formula
standard_notation: Wasserstein梯度流公式
tags:
- 梯度流
- Wasserstein
- Fokker-Planck
- 连续性方程
status: draft
updated: '2026-06-14'
source_ids:
- '9660'
sources:
- （待从源文章提取）
latex: \partial_t q_t(\boldsymbol{x}) = \nabla_{\boldsymbol{x}} \cdot \left( q_t(\boldsymbol{x}) \nabla_{\boldsymbol{x}} \frac{\delta F}{\delta q_t(\boldsymbol{x})} \right)
symbol_meanings:
  q_t(\boldsymbol{x}): 时刻 $t$ 的概率密度函数
  F[q]: 自由能泛函
  \frac{\delta F}{\delta q}: 泛函 $F$ 关于概率密度的变分导数
conditions:
- q_t 为随时间演化的光滑概率密度，并满足使分部积分边界项消失的衰减或边界条件。
- 自由能泛函 F[q] 存在可用的一阶变分导数 delta F / delta q。
- 该式按 Wasserstein-2 概率测度空间上的梯度流解释，具体符号以源文的密度演化推导为准。
appears_in:
- '9660'
---
# Wasserstein梯度流公式


## 概述

（待补充）

## Wasserstein梯度流PDE
partial_t q_t(x) = nabla_x . (q_t(x) nabla_x (delta F/delta q_t(x)))

## f-散度的Wasserstein梯度流
partial_t q_t(x) = nabla . (q_t nabla (f(r_t) - r_t f'(r_t))), r_t = p/q_t

## KL散度的Wasserstein梯度流 -> Fokker-Planck方程
partial_t q_t = -nabla . (q_t nabla log p) + nabla^2 q_t
等价SDE: dx = nabla log p(x) dt + sqrt(2) dw