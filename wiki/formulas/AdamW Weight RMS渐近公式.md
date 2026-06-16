---

type: formula
title: AdamW Weight RMS渐近公式
aliases:
- Weight RMS asymptotic for AdamW
standard_notation:
  theta_t: model weight vector at step t
  eta_t: learning rate at step t
  lambda_t: weight decay coefficient at step t
  rho_t: squared RMS norm of weights
  kappa_t: accumulated decay integral
  nu_t: accumulated squared learning-rate integral
  beta_1: first-moment momentum coefficient
  beta_3: AdamW decay multiplier
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-10-01-AdamW的Weight-RMS的渐近估计-上.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-11-17-AdamW的Weight-RMS的渐近估计-下.md
source_ids:
- '11307'
- '11404'
related_concepts:
- '[[优化动力学视角]]'
- '[[平均场近似]]'
- '[[RMS尺度]]'
related_propositions:
- '[[AdamW Weight RMS渐近估计]]'
evidence_spans:
- ev::11307::快速估计
- ev::11307::平均场推导
- ev::11307::结果分析
- ev::11404::动态版推导
- ev::11404::微分方程形式
status: draft
updated: "2026-06-14"
latex: \|\theta\|_{RMS} \approx \sqrt{\frac{\eta}{2\lambda}}
symbol_meanings:
  \|\theta\|_{RMS}: 权重向量的 RMS 范数
  \eta: 学习率
  \lambda: 权重衰减系数
  \theta: 模型权重向量
conditions: （待从源文章提取）
appears_in:
- '11307'
- '11404'
---

# AdamW Weight RMS渐近公式


## 概述

（待补充）

## 固定超参稳态 ($\mu=0, t\to\infty$)

$$\|\theta\|_{RMS} \approx \sqrt{\frac{\eta}{2\lambda}}$$

## EMA视角

$$\theta_t = \beta_3\theta_{t-1} + (1-\beta_3)(-u_t/\lambda),\quad \beta_3 = 1-\eta\lambda$$

## 动态版 ($\mu=0$)

$$\|\theta_t\|_{RMS}^2 \approx e^{-2\kappa_t}\|\theta_0\|_{RMS}^2 + e^{-2\kappa_t} \sum_{j=1}^t e^{2\kappa_j} \eta_j^2$$
其中 $\kappa_t = \sum_{i=1}^t \lambda_i \eta_i$

## 微分方程形式

$$\frac{d\rho_t}{dt} \approx -2\lambda_t\eta_t\rho_t + \eta_t^2, \quad \rho_t = \|\theta_t\|_{RMS}^2$$

稳态: $\rho_\infty \approx \eta_\infty / (2\lambda_\infty)$

## 平均场闭合形式

$$\|\theta_t\|_{RMS}^2 \approx e^{-2\kappa_t}\|\theta_0\|_{RMS}^2 + (1-e^{-2\kappa_t}) \frac{\nu_t}{2\kappa_t}, \quad \nu_t = \int_0^t \eta_s^2 ds$$

## SignSGDMW稳态

$$\|\theta\|_{RMS} \approx \sqrt{\frac{\eta}{2\lambda} \frac{1+\beta_1}{1-\beta_1}}$$