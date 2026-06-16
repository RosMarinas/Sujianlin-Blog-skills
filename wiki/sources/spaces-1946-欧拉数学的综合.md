---
type: article_summary
title: 费曼积分法(7)：欧拉数学的综合
article_id: "1946"
source_url: https://spaces.ac.cn/archives/1946
date: 2013-03-27
category: 数学研究
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2013-03-27-费曼积分法-7-欧拉数学的综合.md
series:
  - 费曼积分法
concepts:
  - 含参变量积分
  - 微分方程法
methods:
  - 积分符号内取微分法
evidence_spans:
  - ev::1946::二次求导构ODE
  - ev::1946::解微分方程
  - ev::1946::极限顺序问题
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-03-27-费曼积分法-7-欧拉数学的综合.md
source_ids:
  - "1946"
status: draft
updated: 2026-06-10
---

# 费曼积分法(7)：欧拉数学的综合

## 摘要

本文通过求解 $\int_{-\infty}^{+\infty} \cos x/(a^2+x^2)dx$，展示了费曼积分法与微分方程的结合。关键技巧是两次求导构造出二阶线性微分方程 $F''(a)=F(a)$，再利用边界条件 $F(0)=\pi, F(\infty)=0$ 解出 $F(a)=\pi e^{-a}$。

## 公式

### 微分方程构造

设 $F(a)=\int_{-\infty}^{+\infty} \frac{\cos(ax)}{1+x^2}dx$，则：

$$
F''(a)=F(a)-\int_{-\infty}^{+\infty}\cos(ax)dx = F(a)
$$

（其中 $\int_{-\infty}^{+\infty}\cos(ax)dx=0$ 来自文章 1942 的结论）

### 解

$$
F(a)=\pi e^{-a}, \quad \int_{-\infty}^{+\infty} \frac{\cos x}{a^2+x^2}dx = \frac{\pi}{a}e^{-a}
$$
