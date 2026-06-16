---
type: example
title: 二次求导构造微分方程求∫ cos x/(a²+x²) dx
aliases:
- ODE构造法
notation_mapping:
  F(a): 含参变量积分
  a: 频率参数
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2013-03-27-费曼积分法-7-欧拉数学的综合.md
source_ids:
- '1946'
evidence_spans: []
article_id: '1946'
article: '[[（待从源文章提取）]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

# 二次求导构造微分方程求∫ cos x/(a²+x²) dx

## 问题

求 $\displaystyle I = \int_{-\infty}^{+\infty} \frac{\cos x}{a^2+x^2}dx$.

## 第一步：参数重新选择

对原参数 $a$ 求导无简化效果。重新参数化：

$$
F(a) = \int_{-\infty}^{+\infty} \frac{\cos(ax)}{1+x^2}dx
$$

原积分满足 $I = \frac{1}{a}F(a)$。

## 第二次求导

第一次求导：

$$
F'(a) = -\int_{-\infty}^{+\infty} \frac{x\sin(ax)}{1+x^2}dx
$$

第二次求导：

$$
F''(a) = \int_{-\infty}^{+\infty} \frac{\cos(ax)}{1+x^2}dx - \int_{-\infty}^{+\infty}\cos(ax)dx = F(a)
$$

其中 $\int_{-\infty}^{+\infty}\cos(ax)dx = 0$ 来自欧拉数学的结论。

## 解微分方程

$$
F''(a) = F(a) \quad\Longrightarrow\quad F(a) = C_1 e^a + C_2 e^{-a}
$$

## 边界条件

- $F(0) = \int_{-\infty}^{+\infty} \frac{1}{1+x^2}dx = \pi$
- $F(\infty) = 0$

得 $C_1 = 0, C_2 = \pi$，故 $F(a) = \pi e^{-a}$。

## 最终结果

$$
\int_{-\infty}^{+\infty} \frac{\cos x}{a^2+x^2}dx = \frac{1}{a}F(a) = \frac{\pi}{a}e^{-a}
$$

## 关键技巧

- 当一次求导不够简单时，尝试两次求导构造 ODE
- 利用前文（1942）的"欧拉数学"结果 $\int\cos(ax)dx = 0$
- 注意 $F'(0) \neq -\pi e^{-a}|_{a=0}$ 的"反常"是因为 $F'(a)$ 在 $a=0$ 处不连续