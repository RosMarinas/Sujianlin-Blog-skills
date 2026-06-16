---
type: article_summary
title: 从费马大定理谈起（二）：勾股数
article_id: "2808"
source_url: https://spaces.ac.cn/archives/2808
date: 2014-08-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-08-15-从费马大定理谈起-二-勾股数.md
series:
  - [[从费马大定理谈起]]
topics: []
concepts:
  - [[本原勾股数]]
  - [[互质解]]
methods:
  - [[无穷下降法]](雏形)
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-08-15-从费马大定理谈起-二-勾股数.md
source_ids:
  - "2808"
status: draft
updated: 2026-06-10
---

## 文章核心问题

求解不定方程 $x^2+y^2=z^2$ 的整数解（勾股数），并从中分析证明费马大定理所需的工具。

## 主要结论

- 本原勾股数的通解公式：$a = \pm 2pq,\ b = \pm q^2 \mp p^2,\ c = \pm q^2 \pm p^2$，其中 $p,q$ 互质。
- 有解必有互质解（对所有 $n$ 成立）。
- 关键思想：因式分解 $x^2 = (z-y)(z+y)$ 后利用互质和平方数性质求解。

## 推导结构

1. 假设 $(a,b,c)$ 是互质解。
2. 奇偶分析：$a,b$ 一奇一偶，$c$ 为奇数。
3. 设 $a$ 为偶数，分解 $a^2 = (c-b)(c+b)$。
4. 利用互质和平方数性质，推导出通解公式。

## 关键公式

$$
a^2 = c^2 - b^2 = (c-b)(c+b)
$$

$$
a = \pm 2pq,\ b = \pm q^2 \mp p^2,\ c = \pm q^2 \pm p^2
$$

## 体现的方法

- 奇偶（模2）同余分析。
- 利用唯一分解性质：两个互质数之积为平方数，则每个因子本身为平方数（相差单位数 $\pm 1$）。
- 因式分解转化法：将和平方差转化为乘积形式。

## 所属系列位置

系列第二篇，从 $n=2$ 出发获得基础工具。

## 与其他文章的关系

- 勾股数通解为后续使用高斯整数和艾森斯坦整数求解更高次方程提供了类比模板。
- 本文指出的"因式分解成一次多项式"的需求，为第三篇引入高斯整数做了铺垫。

## 原文证据锚点

- 通解公式推导：第 28-39 行
- 步骤回顾与推广思路：第 41-45 行
