---
type: article_summary
title: 从费马大定理谈起（五）：n=4
article_id: "2831"
source_url: https://spaces.ac.cn/archives/2831
date: 2014-08-19
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-08-19-从费马大定理谈起-五-n-4.md
series:
  - [[从费马大定理谈起]]
topics: []
concepts:
  - [[无穷下降法]]
  - [[高斯整数]]
methods:
  - [[无穷下降法]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-08-19-从费马大定理谈起-五-n-4.md
source_ids:
  - "2831"
status: draft
updated: 2026-06-10
---

## 文章核心问题

使用高斯整数和无穷下降法证明费马大定理在 $n=4$ 时成立。

## 主要结论

- 不定方程 $x^4+y^4=z^2$ 在 $\mathbb{Z}[i]$ 中没有全非 0 的解（这比 $x^4+y^4=z^4$ 更强）。
- 证明的关键：模 $1+i$ 分析 + 无穷下降法 + 高斯整数中的唯一分解。
- 需要证明加强命题 $x^4+y^4=z^2$ 而非原命题，这是无穷下降法的特性。

## 推导结构

1. **Step One**: 证明若 $(x,y,z)$ 是解则 $\xi \mid xyz$（模 $1+i$ 分析）。
2. **Step Two**: $\xi$ 只能整除 $x$ 或 $y$ 中的一个（不能整除 $z$）。
3. **Step Three**: 列出模条件。
4. **Step Four**（核心步骤）：设 $(x,y,z)$ 为 $N(x)$ 最小的解，分解 $x^4 = (z-y^2)(z+y^2)$，利用唯一分解得 $z-y^2 = \varepsilon_1 \kappa^4,\ z+y^2 = \varepsilon_2 \iota^4$。
5. **Step Five**: 对单位数 $\varepsilon_1,\varepsilon_2$ 的 4 种情况进行枚举，每种都导出矛盾。

## 关键公式

$$
x^4 = (z-y^2)(z+y^2)
$$

$$
\eta^4 = \mu\nu
$$

$$
-i y^2 = \varepsilon_1 \kappa^4 - \varepsilon_2 \iota^4
$$

## 体现的方法

- 高斯整数中的模 $1+i$ 同余分析（相当于奇偶分析）。
- 无穷下降法：假设最小范数解存在，构造范数更小的解导出矛盾。
- 因式分解 + 唯一分解 + 单位数枚举。

## 所属系列位置

系列第五篇，应用前文工具完成 $n=4$ 证明。

## 与其他文章的关系

- 依赖第三、四篇的高斯整数理论和唯一分解定理。
- 第六篇是本文证明的另一种形式（直接证 $\varepsilon x^4+y^4=z^4$）。
- 与第九篇 $n=3$ 证明结构类似。

## 原文证据锚点

- 核心分解步骤：第 64-83 行
- 单位数枚举与矛盾导出：第 87-121 行
- 为何要证 $x^4+y^4=z^2$ 而非 $x^4+y^4=z^4$：第 22-23 行
