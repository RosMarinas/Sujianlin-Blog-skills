---
type: article_summary
title: 从费马大定理谈起（七）：费马平方和定理
article_id: "2886"
source_url: https://spaces.ac.cn/archives/2886
date: 2014-08-23
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-08-23-从费马大定理谈起-七-费马平方和定理.md
series:
  - [[从费马大定理谈起]]
topics: []
concepts:
  - [[费马平方和定理]]
  - [[高斯素数]]
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-08-23-从费马大定理谈起-七-费马平方和定理.md
source_ids:
  - "2886"
status: draft
updated: 2026-06-10
---

## 文章核心问题

在高斯整数环 $\mathbb{Z}[i]$ 中证明费马平方和定理：哪些奇素数可以表示为两个整数的平方和。

## 主要结论

- 奇素数 $p$ 可表示为 $p = a^2 + b^2$ 当且仅当 $p = 4k+1$。
- $4k+1$ 型素数在 $\mathbb{Z}[i]$ 中是合数，$4k+3$ 型素数仍是高斯素数。
- 表示法在忽略顺序和符号的意义下唯一。
- 引理：若 $p = 4k+1$，则存在整数 $x$ 使 $p \mid x^2+1$（可通过威尔逊定理证明）。

## 推导结构

1. 引理：$p=4k+1$ 型素数 $\Rightarrow$ $\exists x$ 使 $p \mid x^2+1$。
2. 在 $\mathbb{Z}[i]$ 中，$p \mid (x+i)(x-i)$。
3. 若 $p$ 是高斯素数则 $p \mid x\pm i$，但 $(x\pm i)/p$ 非高斯整数，矛盾 $\Rightarrow$ $p$ 在 $\mathbb{Z}[i]$ 中可分解。
4. 设 $p = uv$，由范数得 $N(u) = N(v) = p$ $\Rightarrow$ $p = a^2+b^2$。
5. 唯一性证明：利用高斯整数中的因子分解和范数性质。
6. $4k+3$ 型素数不能表示为两个平方和（模 4 分析）。

## 关键公式

$$
p = a^2 + b^2 \iff p = 4k+1 \ (\text{奇素数})
$$

$$
p \mid \left(\frac{p-1}{2}!\right)^2 + 1
$$

$$
p^2 = N(p) = N(u)N(v) \Rightarrow N(u) = N(v) = p
$$

## 体现的方法

- 通过扩展数域（高斯整数）简化数论定理证明。
- 利用范数的积性进行因子分析。
- 威尔逊定理在数论引理证明中的应用。

## 所属系列位置

系列第七篇，在 $n=4$ 证明之后展示高斯整数的应用。

## 与其他文章的关系

- 建立在第三、四篇的高斯整数和唯一分解理论基础上。
- 作为过渡文章，连接 $n=4$ 证明和即将引入的艾森斯坦整数。
- 展示了高斯整数在经典数论问题中的威力（非仅限于费马大定理）。

## 原文证据锚点

- 引理：第 25-28 行
- 主要证明：第 30-47 行
- 威尔逊定理推导：第 56-72 行
