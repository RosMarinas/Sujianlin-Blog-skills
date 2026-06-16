---
type: article_summary
title: 费曼积分法——积分符号内取微分(3)
article_id: "1629"
source_url: https://spaces.ac.cn/archives/1629
date: 2012-06-23
category: 数学研究
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2012-06-23-费曼积分法-积分符号内取微分-3.md
series:
  - 费曼积分法
concepts:
  - 含参变量积分
methods:
  - 积分符号内取微分法
evidence_spans:
  - ev::1629::例子2
  - ev::1629::例子3
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-06-23-费曼积分法-积分符号内取微分-3.md
source_ids:
  - "1629"
status: draft
updated: 2026-06-10
---

# 费曼积分法——积分符号内取微分(3)

## 摘要

本文通过两个经典例子展示了费曼积分法的应用。例 2 引入了添加 $e^{-ax}$ 因子的技巧求解 $\int_0^\infty \sin x/x\,dx$；例 3 结合微分方程思想求解含参数积分 $\int_0^\infty e^{-x^2-a^2/x^2}dx$。

## 公式

### 例 2：∫₀^∞ sin(x)/x dx

引入参数 $a$:

$$
G(a)=\int_0^\infty e^{-ax}\frac{\sin x}{x}dx
$$

求导后得到 $G'(a) = -1/(a^2+1)$，积分得 $G(a) = -\arctan a + \pi/2$。最终：

$$
\int_0^\infty \frac{\sin x}{x}dx = G(0) = \frac{\pi}{2}
$$

### 例 3：∫₀^∞ exp(-x²-a²/x²) dx

直接对参数 $a$ 求导后通过变量代换 $t=a/x$ 发现 $\frac{du}{da} = -2u$，解得：

$$
u(a)=\int_0^\infty e^{-x^2-\frac{a^2}{x^2}}dx = \frac{\sqrt{\pi}}{2}e^{-2a}
$$
