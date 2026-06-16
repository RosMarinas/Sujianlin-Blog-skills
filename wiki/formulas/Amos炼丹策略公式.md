---
title: Amos优化器推导的学习率和权重衰减公式
type: formula
standard_notation: Amos优化器推导的学习率和权重衰减公式
tags:
- Amos
- 学习率
- 权重衰减
- 衰减策略
status: draft
updated: '2026-06-14'
source_ids:
- '9344'
sources:
- （待从源文章提取）
latex: \alpha_t \approx \frac{\alpha_0 \|\boldsymbol{\epsilon}_0\|}{\|\boldsymbol{u}_t\|(2\alpha_0 p_0 t + 1)},\quad \rho_t \approx \frac{\alpha_0^2}{2q(2\alpha_0 p_0 t + 1)}
symbol_meanings:
  \alpha_t: 时刻 $t$ 的学习率
  \rho_t: 时刻 $t$ 的权重衰减系数
  \alpha_0: 初始学习率
  \|\boldsymbol{\epsilon}_0\|: 参数变化尺度估计
  \|\boldsymbol{u}_t\|: 优化器更新向量的范数
  p_0: 收敛速度相关常数
  q: 收敛相关常数
conditions: （待从源文章提取）
appears_in:
- '9344'
---
# Amos优化器推导的学习率和权重衰减公式


## 概述

（待补充）

## 平方反比衰减(固定收敛速度)
alpha_t ~ alpha_0 * ||epsilon_0|| / (||u_t|| * (alpha_0*p*t+1)^2)
rho_t ~ alpha_0^2 / (2*q * (alpha_0*p*t+1)^2)

## 逆时间衰减(递减收敛速度)
alpha_t ~ alpha_0 * ||epsilon_0|| / (||u_t|| * (2*alpha_0*p_0*t+1))
rho_t ~ alpha_0^2 / (2*q * (2*alpha_0*p_0*t+1))

其中||epsilon_0||为参数变化尺度估计，p/q为收敛相关常数。