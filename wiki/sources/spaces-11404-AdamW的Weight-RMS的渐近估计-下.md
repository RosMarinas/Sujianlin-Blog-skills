---
type: article_summary
title: AdamW的Weight RMS的渐近估计（下）
article_id: "11404"
source_url: https://spaces.ac.cn/archives/11404
date: 2025-11-17
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-11-17-AdamW的Weight-RMS的渐近估计-下.md
series: []
topics:
  - "[[优化器分析]]"
concepts:
  - "[[优化动力学视角]]"
  - "[[平均场近似]]"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
problem_patterns: []
evidence_spans:
  - ev::11404::动态版推导
  - ev::11404::无WeightDecay条件
  - ev::11404::微分方程形式
  - ev::11404::平均场近似
  - ev::11404::常见Schedule计算
  - ev::11404::模拟验证
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-11-17-AdamW的Weight-RMS的渐近估计-下.md
source_ids:
  - "11404"
status: draft
updated: 2026-06-10
---

# AdamW的Weight RMS的渐近估计（下）

## 文章核心问题

将上篇的结论从固定学习率和固定Weight Decay推广到动态变化的情形（如Cosine Decay、WSD等常见Schedule），使得结论更为通用。

## 主要结论

- 动态版Weight RMS表达式：$\|\theta_t\|_{RMS}^2 \approx e^{-2\kappa_t}\|\theta_0\|_{RMS}^2 + e^{-2\kappa_t} z_t^2 \frac{\|\mu\|^2/\|\sigma\|^2 + \sum \bar{\beta}_1^2}{\|\mu\|^2/\|\sigma\|^2 + 1}$。
- $\mu=0$ 时简化为 $\|\theta_t\|_{RMS}^2 \approx e^{-2\kappa_t}\|\theta_0\|_{RMS}^2 + e^{-2\kappa_t} \sum e^{2\kappa_j}\eta_j^2$。
- 可导出微分方程形式 $d\rho_t/dt \approx -2\lambda_t\eta_t\rho_t + \eta_t^2$。
- 微分方程稳态解 $\rho_\infty \approx \eta_\infty / (2\lambda_\infty)$：若学习率Decay到0，权重RMS会坍缩到0。
- 给出了线性Decay、Cosine Decay、WSD三种常见Schedule下 $\kappa_t, \nu_t$ 的解析积分结果。
- 无Weight Decay时 $\|\theta_t\|_{RMS}$ 不发散的充要条件是 $\sum \eta_j^2 < \infty$。

## 推导结构

1. 从动态AdamW更新规则出发，用指数形式近似 $1-\eta_t\lambda_t \approx e^{-\eta_t\lambda_t}$。
2. 引入 $\kappa_t = \sum \eta_i\lambda_i$ 进行加权展开。
3. 用平均场近似表达动态版Weight RMS。
4. 给出无Weight Decay情况下的收敛充要条件并证明。
5. 简化为微分方程形式，获得更易计算的解析结果。
6. 用平均场近似进一步简化，得到积分形式的闭合表达式。
7. 计算三种常见Schedule下的 $\kappa_t, \nu_t$。
8. 数值模拟验证。

## 关键公式

- 动态版简化($\mu=0$): $\|\theta_t\|_{RMS}^2 \approx e^{-2\kappa_t}\|\theta_0\|_{RMS}^2 + e^{-2\kappa_t} \sum_{j=1}^t e^{2\kappa_j} \eta_j^2$, $\kappa_t = \sum_{i=1}^t \lambda_i\eta_i$
- 微分方程: $d\rho_t/dt \approx -2\lambda_t\eta_t\rho_t + \eta_t^2$, $\rho_t = \|\theta_t\|_{RMS}^2$
- 稳态: $\lim_{t\to\infty} \rho_t \approx \lim_{t\to\infty} \eta_t/(2\lambda_t)$
- 无WD收敛条件: $\sum_{j=1}^\infty \eta_j^2 < \infty \iff$ Weight RMS有界
- 积分近似: $\|\theta_t\|_{RMS}^2 \approx e^{-2\kappa_t}\|\theta_0\|_{RMS}^2 + e^{-2\kappa_t} \int_0^t e^{2\kappa_s} \eta_s^2 ds$
- 平均场闭合: $\|\theta_t\|_{RMS}^2 \approx e^{-2\kappa_t}\|\theta_0\|_{RMS}^2 + (1-e^{-2\kappa_t})\nu_t/(2\kappa_t)$, $\nu_t = \int \eta_s^2 ds$
- Cosine Decay: $\kappa = \lambda(\eta_{\min}+\eta_{\max})t/2, \nu = (3\eta_{\min}^2+2\eta_{\min}\eta_{\max}+3\eta_{\max}^2)t/8$

## 体现的方法

- **用平均场近似替代复杂期望计算**：将动态系统下的随机权重期望用累积指数加权近似。
- **微分方程转化**：将离散求和近似为积分，得到便于分析的ODE形式。
- **积分近似**：将复杂级数求和用积分替换，获得常见Schedule下解析结果。

## 所属系列位置

独立文章，AdamW Weight RMS估计的下篇。与"重新思考学习率与Batch Size"系列方法相通。

## 与其他文章的关系

- 上篇(11307) 给出固定超参版本，本文推广到动态版本。
- 与 为什么Adam的Update RMS是0.2%(11267) 的方法一致。
- MuP之上(11729) 讨论参数稳定性约束，可从本文预测参数自然演化的RMS。
- 微分方程稳态分析提示：为避免权重坍缩，学习率不应Decay到0，或设置 $\lambda_t \propto \eta_t$。

## 原文证据锚点

- ev::11404::动态版推导: 第20-48行，从动态更新规则到加权展开和平均场近似。
- ev::11404::无WeightDecay条件: 第104-128行，$\sum \eta_j^2 < \infty$ 的充要条件证明。
- ev::11404::微分方程形式: 第154-168行，微分方程推导和稳态分析。
- ev::11404::平均场近似: 第172-189行，平均场闭合形式推导。
- ev::11404::常见Schedule计算: 第193-228行，线性、Cosine、WSD的解析积分。
- ev::11404::模拟验证: 第232-264行，数值模拟代码和验证结果。
