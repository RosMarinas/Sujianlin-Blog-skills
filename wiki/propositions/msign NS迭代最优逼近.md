---
type: proposition
title: msign NS迭代最优多项式逼近
aliases:
  - Optimal polynomial approximation for msign NS iteration
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-05-msign算子的Newton-Schulz迭代-下.md
source_ids:
  - "10996"
related_concepts:
  - "[[矩阵符号函数(msign)]]"
  - "[[Newton-Schulz迭代]]"
  - "[[等值振荡定理]]"
evidence_spans:
  - ev::10996::贪心即最优
  - ev::10996::等值振荡定理
  - ev::10996::贪心最优性证明
status: stable
updated: 2026-06-10
---

# msign NS迭代最优多项式逼近

## 命题陈述

给定区间 $[l,u] \subset [0,1]$，寻找 $T$ 步奇多项式复合函数 $f = f_T \circ \dots \circ f_1$ 逼近常数函数 1 的问题：

$$\argmin_f \max_{x\in[l,u]} |f(x) - 1|$$

其贪心解（逐步求解单步最优）即为全局最优解。

## 证明思路

数学归纳法。假设 $T-1$ 步全局最优解的值域为 $[l_T, u_T]$，对任意 $T-1$ 步解的值域 $[a,b]$，有 $a/b \le l_T/u_T$。由此可证第 $T$ 步的最优误差在 $[l_T, u_T]$ 上取得，且任何非贪心路径都无法超越贪心解。

## 单步最优解

3阶奇多项式情况有解析解：

$$x_1 = \sqrt{\frac{l^2+lu+u^2}{3}},\quad k = -\frac{6}{l^2u+lu^2+2x_1^3}$$

5阶及更高阶可通过简化Remez算法迭代求解。

## 有限精度修正

- 安全因子: $f_t^*(x/1.01)$ 防止bfloat16精度下奇异值溢出
- Recenter: $\gamma f_t^*(x)$ 满足 $\gamma f_t^*(l_t) + \gamma f_t^*(u_t) = 2$
- 区间限制: 用 $\lambda \in (0,1)$ 将优化区间限制为 $[\max(l_t, \lambda u_t), u_t]$
