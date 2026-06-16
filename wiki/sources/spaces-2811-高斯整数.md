---
type: article_summary
title: 从费马大定理谈起（三）：高斯整数
article_id: "2811"
source_url: https://spaces.ac.cn/archives/2811
date: 2014-08-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-08-16-从费马大定理谈起-三-高斯整数.md
series:
  - [[从费马大定理谈起]]
topics: []
concepts:
  - [[高斯整数]]
  - [[范数(数论)]]
  - [[单位数]]
  - [[高斯素数]]
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-08-16-从费马大定理谈起-三-高斯整数.md
source_ids:
  - "2811"
status: draft
updated: 2026-06-10
---

## 文章核心问题

引入高斯整数环 $\mathbb{Z}[i]$ 的概念和相关代数结构，为证明费马大定理 $n=4$ 做准备。

## 主要结论

- 高斯整数 $\mathbb{Z}[i] = \{a+bi \mid a,b\in\mathbb{Z},\ i^2=-1\}$ 构成整数环。
- 范数定义：$N(a+bi) = (a+bi)(a-bi) = a^2+b^2$，满足积性 $N(\xi\eta)=N(\xi)N(\eta)$。
- 单位数（可逆元）：范数为 1 的元素，即 $\pm 1, \pm i$，共 4 个。
- 高斯素数：不能分解为两个非单位数高斯整数之积的元素。
- 模 $1+i$ 分析在高斯整数环中相当于实整数中的奇偶分析。

## 推导结构

1. 介绍环和域的基本概念。
2. 定义高斯整数、范数、单位数。
3. 定义整除、最大公约数、互质、高斯素数。
4. 建立模 $1+i$ 分析的四条关键性质。

## 关键公式

$$
\mathbb{Z}[i] = \{a+bi \mid a,b\in\mathbb{Z},\ i^2=-1\}
$$

$$
N(a+bi) = a^2+b^2
$$

$$
1+i \mid a+bi \iff 2 \mid a+b
$$

$$
1+i \nmid a+bi \Rightarrow (a+bi)^2 \equiv \pm 1 \pmod{4}
$$

$$
1+i \nmid a+bi \Rightarrow (a+bi)^4 \equiv 1 \pmod{8}
$$

## 体现的方法

- 扩展数域方法：将整数概念从 $\mathbb{Z}$ 扩展到 $\mathbb{Z}[i]$。
- 模 $1+i$ 同余分析（高斯整数中的"奇偶分析"）。

## 所属系列位置

系列第三篇，引入 $n=4$ 证明所需的核心工具。

## 与其他文章的关系

- 为第五、六篇 $n=4$ 证明提供基础工具。
- 模 $1+i$ 分析在 $n=4$ 证明中扮演核心角色。
- 与第八篇艾森斯坦整数对应（分别对应四次和三次分圆整数）。

## 原文证据锚点

- 高斯整数定义：第 33-36 行
- 范数定义：第 39-42 行
- 单位数：第 44 行
- 模 $1+i$ 分析性质：第 56-68 行
