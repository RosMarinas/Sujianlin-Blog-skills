---
type: concept
title: Kolmogorov定理
definition: 在函数空间的线性子空间中寻找最优逼近的通用充要条件，即对任意方向函数h，在误差最大值集合上，误差符号与h乘积的最大值非负。
standard_notation: "\text{Kolmogorov Characterization}"
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-02-等值振荡定理-最优多项式逼近的充要条件.md
source_ids:
- '10972'
status: draft
updated: '2026-06-13'
---

# Kolmogorov定理

## 定义

Kolmogorov定理是最优 `L_infty` 逼近的通用充要条件。源文设 `S` 是 `C[a,b]` 的线性子空间，`f* in S` 最小化 `||f-g||_infty` 当且仅当对任意方向 `h in S`，误差无穷范数沿 `h` 的方向导数非负。

## 激活场景

它用于从一般线性逼近空间判断最优解，而不局限于多项式。等值振荡定理的证明中，源文先证明 Kolmogorov 条件，再把 `S` 取为不超过 `n` 阶的多项式，从而推出交替最大误差点条件。

## 关键关系

定理中的关键集合是最大误差点 `argmax(|f*(x)-g(x)|)`。方向导数写成在这些点上取 `sign(f*(x)-g(x))h(x)` 的最大值；如果所有方向都不能让这个最大误差一阶下降，则 `f*` 已经是最优逼近。

## 证据

- `Data/Spaces_ac_cn/markdown/Mathematics/2025-06-02-等值振荡定理-最优多项式逼近的充要条件.md`
