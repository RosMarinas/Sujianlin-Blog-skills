---
type: article_summary
title: 费曼积分法(5)：欧拉数学的传承
article_id: "1942"
source_url: https://spaces.ac.cn/archives/1942
date: 2013-03-24
category: 数学研究
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2013-03-24-费曼积分法-5-欧拉数学的传承.md
series:
  - 费曼积分法
concepts:
  - 欧拉数学
  - 含参变量积分
  - 高速振荡三角函数积分
methods:
  - 积分符号内取微分法
evidence_spans:
  - ev::1942::复数扩展
  - ev::1942::sin_ax_over_x
  - ev::1942::cos_ax_integral
  - ev::1942::高速振荡积分
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-03-24-费曼积分法-5-欧拉数学的传承.md
source_ids:
  - "1942"
status: draft
updated: 2026-06-10
---

# 费曼积分法(5)：欧拉数学的传承

## 摘要

本文从复数角度重新审视 $\int_0^\infty \sin x/x\,dx$，引入欧拉数学的不严谨但极具创造性的方法。推导出 $\int_0^\infty \sin(ax)/x\,dx = \pi/2$（$a>0$）和 $\int_0^\infty \cos(ax)dx = 0$（$a\neq 0$）等泛函结果。讨论了高速振荡三角函数积分 $\lim_{\omega\to\infty}\int_a^b f(x)\cos(\omega x)dx = 0$，并提及这与费曼路径积分思想的联系。

## 公式

### 复数扩展

从 $\int_0^\infty \frac{e^{ix}}{x}dx$ 引入 $e^{-ax}$ 因子：

$$
F(a)=\int_0^\infty e^{-ax}\frac{e^{ix}}{x}dx, \quad F'(a)=-\int_0^\infty e^{(-a+i)x}dx=\frac{1}{-a+i}
$$

通过分离实部和虚部得到：

$$
\int_0^\infty \frac{\sin x}{x}dx = \frac{\pi}{2}
$$

### 推广结果

对于 $a>0$：

$$
\int_0^\infty \frac{\sin(ax)}{x}dx = \frac{\pi}{2}, \quad \int_0^\infty \cos(ax)dx = 0
$$

### 高速振荡积分（Riemann-Lebesgue 引理的思想）

$$
\lim_{\omega\to\infty} \int_a^b f(x)\cos(\omega x)dx = 0
$$
