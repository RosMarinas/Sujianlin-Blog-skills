---
type: article_summary
title: 费曼积分法——积分符号内取微分(4)
article_id: "1637"
source_url: https://spaces.ac.cn/archives/1637
date: 2012-06-26
category: 数学研究
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2012-06-26-费曼积分法-积分符号内取微分-4.md
series:
  - 费曼积分法
concepts:
  - 含参变量积分
  - 泰勒展开余项积分
methods:
  - 积分符号内取微分法
evidence_spans:
  - ev::1637::一般化公式
  - ev::1637::wayne问题
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-06-26-费曼积分法-积分符号内取微分-4.md
source_ids:
  - "1637"
status: draft
updated: 2026-06-10
---

# 费曼积分法——积分符号内取微分(4)

## 摘要

本文给出了费曼积分法的一般化应用：对形如 $F(t)=\int_a^b \frac{f(0)+f'(0)(tx)+\dots+f^{(n)}(0)(tx)^n/n!-f(tx)}{x^{n+1}}dx$ 的泰勒展开余项积分，通过连续 n 次微分将其化为简单形式。利用该公式求解了 wayne 提出的问题。

## 公式

### 一般化公式

$$
F(t)=\int_a^b \frac{P_n(tx)-f(tx)}{x^{n+1}} dx, \quad P_n(u)=\sum_{k=0}^n\frac{f^{(k)}(0)}{k!}u^k
$$

n 次微分得：

$$
\frac{d^n F(t)}{dt^n}=\int_a^b \frac{f^{(n)}(0)-f^{(n)}(tx)}{x} dx
$$

n+1 次微分得：

$$
\frac{d^{n+1} F(t)}{dt^{n+1}}=\int_a^b -f^{(n+1)}(tx) dx
$$

### wayne 问题

对于 $f(x)=\sin x$, $n=2m$：

$$
\int_0^\infty \frac{f(x,2m-1)-\sin x}{x^{2m+1}}dx = \frac{\pi(-1)^{m-1}}{2(2m)!}
$$
