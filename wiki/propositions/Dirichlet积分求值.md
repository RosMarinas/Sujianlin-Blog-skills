---
type: proposition
title: Dirichlet 积分求值
aliases:
  - ∫₀^∞ sin x/x dx = π/2
status: draft
updated: 2026-06-10
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-06-23-费曼积分法-积分符号内取微分-3.md
source_ids:
  - "1629"
evidence_spans: []
---

# Dirichlet 积分求值

## 命题

$$
\int_0^\infty \frac{\sin x}{x}dx = \frac{\pi}{2}
$$

## 证明（费曼积分法）

设 $G(a)=\int_0^\infty e^{-ax}\frac{\sin x}{x}dx$，则 $G'(a) = -1/(a^2+1)$。积分得 $G(a)=-\arctan a + C$，由 $\lim_{a\to\infty}G(a)=0$ 确定 $C=\pi/2$，代入 $a=0$ 即得。

## 推论

1. $\int_0^\infty \frac{\sin(ax)}{x}dx = \frac{\pi}{2}$（$a>0$）
2. $\int_0^\infty \cos(ax)dx = 0$（$a\neq 0$，泛函意义）
