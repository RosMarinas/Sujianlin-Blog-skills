---
type: proposition
title: 泰勒展开余项积分的封闭公式
aliases:
  - wayne问题
status: draft
updated: 2026-06-10
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-06-26-费曼积分法-积分符号内取微分-4.md
source_ids:
  - "1637"
evidence_spans: []
---

# 泰勒展开余项积分的封闭公式

## 命题

设 $f(x,2m-1)$ 为 $\sin x$ 在 $0$ 处的 $2m-1$ 阶泰勒展开，则：

$$
\int_0^\infty \frac{f(x,2m-1)-\sin x}{x^{2m+1}}dx = \frac{\pi(-1)^{m-1}}{2(2m)!}
$$

## 证明

利用连续微分法：设 $F(t)$ 为一般泰勒展开余项积分，连续 $2m$ 次微分后化为 $\int_0^\infty \frac{-(-1)^m\sin(tx)}{x}dx = (-1)^{m-1}\pi/2$，再积分 $2m$ 次即得封闭公式。
