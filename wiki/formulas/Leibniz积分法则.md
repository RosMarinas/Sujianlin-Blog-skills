---
type: formula
title: Leibniz 积分法则
aliases:
- Leibniz integral rule
- Differentiation under the integral sign
standard_notation: Leibniz 积分法则
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2012-06-12-费曼积分法-积分符号内取微分-2.md
source_ids:
- '1619'
evidence_spans: []
latex: G(a)=\int_{m(a)}^{n(a)} f(x,a)dx
symbol_meanings:
  G(a): 含参变量 $a$ 的积分值
  a: 参变量
  m(a): 积分下限（可为 $a$ 的函数）
  n(a): 积分上限（可为 $a$ 的函数）
  f(x,a): 被积函数，同时依赖于积分变量 $x$ 和参数 $a$
  x: 积分变量
conditions: （待从源文章提取）
appears_in:
- '1619'
---

# Leibniz 积分法则


## 概述

（待补充）

## 一般形式（变限积分）

$$
G(a)=\int_{m(a)}^{n(a)} f(x,a)dx
$$

$$
G'(a)=\int_{m(a)}^{n(a)} \frac{\partial f(x,a)}{\partial a} dx + f(n(a),a)\cdot n'(a)-f(m(a),a)\cdot m'(a)
$$

## 常数限形式

若 $m,n$ 为常数：

$$
\frac{d}{da}\int_{m}^{n} f(x,a)dx = \int_{m}^{n} \frac{\partial f(x,a)}{\partial a} dx
$$

## 说明

这是费曼积分法的基础公式。关键性质是求导与积分可交换顺序（在满足连续性条件的前提下）。