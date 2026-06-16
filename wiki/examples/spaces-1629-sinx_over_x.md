---
type: example
title: 指数衰减因子法求 Dirichlet 积分
aliases:
- e^{-ax}因子法
notation_mapping:
  G(a): 含参变量积分
  a: 指数衰减参数
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

# 指数衰减因子法求 Dirichlet 积分

## 问题

求 $\displaystyle I = \int_0^\infty \frac{\sin x}{x}dx$.

## 参数化

添加 $e^{-ax}$ 因子：

$$
G(a) = \int_0^\infty e^{-ax}\frac{\sin x}{x}dx
$$

原积分 $I = G(0)$.

## 求导

$$
G'(a) = \int_0^\infty -e^{-ax}\sin x\,dx = -\frac{1}{a^2+1}
$$

## 还原

$$
G(a) = -\arctan a + C
$$

由 $\lim_{a\to\infty} G(a)=0$ 得 $C = \pi/2$，故：

$$
I = G(0) = \frac{\pi}{2}
$$

## 关键技巧

- 添加 $e^{-ax}$ 因子使得求导后分母 $x$ 被消去
- 利用指数函数积分表求 $\int e^{-ax}\sin x\,dx$
- 参数 $a\to\infty$ 时 $G(a)\to 0$ 确定常数