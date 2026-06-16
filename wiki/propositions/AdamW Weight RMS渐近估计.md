---
type: proposition
title: AdamW Weight RMS渐近估计
aliases:
  - Asymptotic Weight RMS for AdamW
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-10-01-AdamW的Weight-RMS的渐近估计-上.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-11-17-AdamW的Weight-RMS的渐近估计-下.md
source_ids:
  - "11307"
  - "11404"
related_concepts:
  - "[[优化动力学视角]]"
  - "[[平均场近似]]"
  - "[[RMS尺度]]"
evidence_spans:
  - ev::11307::快速估计
  - ev::11307::平均场推导
  - ev::11307::结果分析
  - ev::11404::动态版推导
  - ev::11404::微分方程形式
status: stable
updated: 2026-06-10
---

# AdamW Weight RMS渐近估计

## 命题陈述

在平均场近似下，AdamW优化器的权重RMS可由超参解析估计。

常数超参（$\mu=0$）的稳态结果：

$$\|\theta\|_{RMS} \approx \sqrt{\frac{\eta}{2\lambda}}$$

## 推导框架

1. **EMA视角**：$\theta_t = \beta_3\theta_{t-1} + (1-\beta_3)(-u_t/\lambda)$
2. **正交假设**：高维下 $\theta_{t-1} \cdot u_t \approx 0$
3. **平均场**：$\mathbb{E}[u_t^2] \approx \frac{\mathbb{E}[m_t^2]}{\mathbb{E}[v_t]}$
4. **稳态条件**：$\|\theta_t\|_{RMS}^2 = \|\theta_{t-1}\|_{RMS}^2$

## 动态超参

微分方程形式 $d\rho_t/dt \approx -2\lambda_t\eta_t\rho_t + \eta_t^2$ 可处理常见Schedule。

## 收敛条件

无Weight Decay时 $\|\theta_t\|_{RMS}$ 有界 $\iff \sum_{j=1}^\infty \eta_j^2 < \infty$。
