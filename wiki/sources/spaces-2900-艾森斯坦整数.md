---
type: article_summary
title: 从费马大定理谈起（八）：艾森斯坦整数
article_id: "2900"
source_url: https://spaces.ac.cn/archives/2900
date: 2014-08-30
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-08-30-从费马大定理谈起-八-艾森斯坦整数.md
series:
  - [[从费马大定理谈起]]
topics: []
concepts:
  - [[艾森斯坦整数]]
  - [[范数(数论)]]
  - [[艾森斯坦素数]]
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-08-30-从费马大定理谈起-八-艾森斯坦整数.md
source_ids:
  - "2900"
status: draft
updated: 2026-06-10
---

## 文章核心问题

引入艾森斯坦整数环 $\mathbb{Z}[\omega]$ 的概念和性质，为证明费马大定理 $n=3$ 做准备。其中 $\omega$ 是三次单位根（$\omega^2+\omega+1=0$）。

## 主要结论

- 艾森斯坦整数环 $\mathbb{Z}[\omega] = \{a+b\omega \mid a,b\in\mathbb{Z},\ \omega^2+\omega+1=0\}$ 构成整数环（三次分圆整数环）。
- 范数定义：$N(a+b\omega) = (a+b\omega)(a+b\omega^2) = a^2 - ab + b^2$，满足积性。
- 单位数（可逆元）：$\pm 1,\ \pm\omega,\ \pm\omega^2$，共 6 个。
- $\mathbb{Z}[\omega]$ 是欧几里得整环（从而满足唯一分解定理）。
- 模 $1-\omega$ 分析在艾森斯坦整数环中相当于奇偶分析。

## 推导结构

1. 定义艾森斯坦整数和运算规则。
2. 定义共轭和范数。
3. 单位数与素数定义。
4. 证明 $\mathbb{Z}[\omega]$ 是欧几里得整环。
5. 建立模 $1-\omega$ 同余分析的三条性质。

## 关键公式

$$
\mathbb{Z}[\omega] = \{a+b\omega \mid a,b\in\mathbb{Z}\},\ \omega^2+\omega+1=0
$$

$$
N(a+b\omega) = (a+b\omega)(a+b\omega^2) = a^2 - ab + b^2
$$

$$
(a+b\omega)(c+d\omega) = (ac-bd) + (bc+ad-bd)\omega
$$

$$
1-\omega \mid a+b\omega \iff 3 \mid a+b
$$

$$
1-\omega \nmid a+b\omega \Rightarrow (a+b\omega)^3 \equiv \pm 1 \pmod{9}
$$

## 体现的方法

- 扩展数域方法（扩展到三次分圆整数环）。
- 模 $1-\omega$ 同余分析。

## 所属系列位置

系列第八篇，引入 $n=3$ 证明所需的核心工具。

## 与其他文章的关系

- 与第三篇高斯整数平行对应（分别对应四次和三次分圆整数）。
- 为第九篇 $n=3$ 证明提供基础工具。
- 唯一分解性的证明方法与第四篇高斯整数情况完全类似。

## 原文证据锚点

- 艾森斯坦整数定义和运算：第 22-30 行
- 范数定义：第 33-36 行
- 单位数：第 38 行
- 唯一分解定理证明（欧几里得整环）：第 44-48 行
- 模 $1-\omega$ 分析：第 52-54 行
