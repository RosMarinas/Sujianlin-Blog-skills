---
type: formula
title: 余弦有理分式积分公式
aliases:
- ∫ cos x/(a²+x²) dx = πe^{-a}/a
standard_notation: 余弦有理分式积分公式
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2013-03-27-费曼积分法-7-欧拉数学的综合.md
source_ids:
- '1946'
evidence_spans: []
latex: \int_{-\infty}^{+\infty} \frac{\cos x}{a^2+x^2}dx = \frac{\pi}{a}e^{-a}
symbol_meanings:
  x: 积分变量
  a: 正实数参数
  \pi: 圆周率
  e: 自然常数
conditions: （待从源文章提取）
appears_in:
- '1946'
---

# 余弦有理分式积分公式


## 概述

（待补充）

## 公式

$$
\int_{-\infty}^{+\infty} \frac{\cos x}{a^2+x^2}dx = \frac{\pi}{a}e^{-a}
$$

## 特例

当 $a=1$ 时：

$$
\int_{-\infty}^{+\infty} \frac{\cos x}{1+x^2}dx = \pi e^{-1}
$$

## 证明要点

设 $F(a)=\int_{-\infty}^{+\infty} \frac{\cos(ax)}{1+x^2}dx$，二次求导得 $F''(a) = F(a)$（利用 $\int_{-\infty}^{+\infty}\cos(ax)dx = 0$）。解 $F(a)=C_1 e^a + C_2 e^{-a}$，利用 $F(0)=\pi, F(\infty)=0$ 得 $F(a)=\pi e^{-a}$。由尺度变换得到原公式。