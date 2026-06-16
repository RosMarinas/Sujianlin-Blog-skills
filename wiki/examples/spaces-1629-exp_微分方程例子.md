---
type: example
title: 微分方程法求 ∫₀^∞ exp(-x²-a²/x²) dx
aliases:
- ODE参数化方法
notation_mapping:
  u(a): 含参变量积分
  a: 参数
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2012-06-23-费曼积分法-积分符号内取微分-3.md
source_ids:
- '1629'
evidence_spans: []
article_id: '1629'
article: '[[（待从源文章提取）]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

# 微分方程法求 ∫₀^∞ exp(-x²-a²/x²) dx

## 问题

已知 $\int_0^\infty e^{-x^2}dx = \sqrt{\pi}/2$，求：

$$
u(a) = \int_0^\infty e^{-x^2-\frac{a^2}{x^2}}dx
$$

## 求导

直接对参数 $a$ 求导：

$$
\frac{du}{da} = \int_0^\infty e^{-x^2-\frac{a^2}{x^2}} \cdot \left(-\frac{2a}{x^2}\right) dx = 2\int_0^\infty e^{-x^2-\frac{a^2}{x^2}} d\left(\frac{a}{x}\right)
$$

## 变量代换

令 $t = a/x$，则：

$$
\int_0^\infty e^{-x^2-\frac{a^2}{x^2}} d\left(\frac{a}{x}\right) = -\int_0^\infty e^{-t^2-\frac{a^2}{t^2}} dt = -u(a)
$$

## 微分方程

$$
\frac{du}{da} = -2u
$$

解得 $u(a) = C e^{-2a}$。

## 确定常数

由 $u(0) = \int_0^\infty e^{-x^2}dx = \sqrt{\pi}/2$ 得 $C = \sqrt{\pi}/2$，故：

$$
u(a) = \frac{\sqrt{\pi}}{2}e^{-2a}
$$

## 关键技巧

- 求导后通过变量代换发现 $\frac{du}{da} = -2u$，无需显式积分
- 利用积分与变量符号无关的性质：$\int e^{-t^2-a^2/t^2}dt = u(a)$
- 结合已知的高斯积分结果确定常数