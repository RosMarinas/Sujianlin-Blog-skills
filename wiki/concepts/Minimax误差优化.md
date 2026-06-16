---
type: concept
title: Minimax误差优化
aliases:
  - Minimax error optimization
  - Chebyshev approximation
definition: 选择参数 $\theta$ 以最小化目标函数与近似函数间的最大绝对误差：$\min_\theta \max_x |f(x) - g(x,\theta)|$，不涉及权重选取，直观且具有强鲁棒性。
standard_notation: $\min_{\theta} \max_{x} |f(x)-g(x,\theta)|$
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-12-29-SquarePlus-可能是运算最简单的ReLU光滑近似.md
source_ids:
  - "7309"
  - "8833"
prerequisites: []
equivalent_forms: []
direct_consequences: []
related_formulas:
  - "formula::GELU双曲正切近似公式"
  - "formula::SquarePlus公式"
related_methods:
  - "method::Minimax误差优化法"
  - "method::局部拟合与全局拟合法"
evidence_spans: []
status: draft
updated: 2026-06-12
---

## 定义

Minimax 误差优化是函数逼近中的一种准则，目标是选择近似函数的参数以最小化在整个定义域上的最大绝对误差。与积分形式的误差（如均方误差）不同，minimax 不涉及权重函数的选取，能够保证在整个定义域上的最坏情况误差最小化。

## 应用

- GELU近似中确定 $\tanh(ax+bx^3)$ 的系数 $b$
- SquarePlus中确定参数 $b$ 以最佳逼近 SoftPlus
- $\Phi(x) \approx \sigma(\lambda x)$ 中确定 $\lambda$
