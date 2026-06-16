---
type: formula
title: Dirichlet 积分公式
aliases:
- ∫₀^∞ sin x/x dx = π/2
- Dirichlet integral
standard_notation: Dirichlet 积分公式
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2012-06-23-费曼积分法-积分符号内取微分-3.md
- Data/Spaces_ac_cn/markdown/Mathematics/2013-03-24-费曼积分法-5-欧拉数学的传承.md
source_ids:
- '1629'
- '1942'
evidence_spans: []
latex: \int_0^\infty \frac{\sin x}{x}dx = \frac{\pi}{2}
symbol_meanings:
  x: 积分变量
  \pi: 圆周率
  \infty: 无穷大上限
conditions: （待从源文章提取）
appears_in:
- '1629'
- '1942'
---

# Dirichlet 积分公式


## 概述

（待补充）

## 基本公式

$$
\int_0^\infty \frac{\sin x}{x}dx = \frac{\pi}{2}
$$

## 参数化形式

$$
\int_0^\infty e^{-ax}\frac{\sin x}{x}dx = \frac{\pi}{2} - \arctan a
$$

## 推广

对于 $a>0$：

$$
\int_0^\infty \frac{\sin(ax)}{x}dx = \frac{\pi}{2}
$$

$$
\int_0^\infty \cos(ax) dx = 0 \quad (a \neq 0, \text{泛函意义})
$$

## 证明（费曼积分法）

引入参数 $a$ 和因子 $e^{-ax}$：

$$
G(a)=\int_0^\infty e^{-ax}\frac{\sin x}{x}dx
$$

求导得 $G'(a) = -1/(a^2+1)$，积分得 $G(a) = \pi/2 - \arctan a$，取 $a=0$ 即得。