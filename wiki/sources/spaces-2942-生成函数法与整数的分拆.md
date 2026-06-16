---
type: article_summary
title: 生成函数法与整数的分拆
article_id: "2942"
source_url: https://spaces.ac.cn/archives/2942
date: 2014-09-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-09-16-生成函数法与整数的分拆.md
series:
  - "[[组合数学与生成函数]]"
topics:
  - "[[数学分析与级数]]"
concepts:
  - "[[生成函数]]"
  - "[[整数分拆]]"
methods:
  - "[[生成函数法]]"
evidence_spans:
  - "ev::2942::ordered_partition_gf"
  - "ev::2942::unordered_partition_gf"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-09-16-生成函数法与整数的分拆.md
source_ids:
  - "2942"
status: draft
updated: 2026-06-13
---

## 文章核心问题

如何利用生成函数（母函数）统一地解决整数分拆问题，包括有序分拆和无序分拆的计数？

## 主要结论

1. 有序分拆（顺序视为不同）的生成函数为 $\left(\frac{1}{1-x}\right)^k$，展开得系数 $\binom{n+k-1}{k-1}$。
2. 无序分拆（顺序视为相同）的生成函数为 $\prod_{r=1}^{k}\left(\frac{1}{1-x^r}\right)$，展开系数依赖于 $n$ 模 $k$ 的结果。
3. 生成函数法的优势在于方法统一、推导规范，虽然具体计算未必简单，但每一步都有据可循。

## 推导结构

1. **有序分拆**：$x+y+z=n$ 对应 $(1+x+x^2+\cdots)^k$，利用泰勒展开求系数。
2. **无序分拆**：$x\leq y\leq z$ 对应 $\prod_{r=1}^k\frac{1}{1-x^r}$，通过变量替换 $y=x+a, z=x+a+b$ 证明。

## 关键公式

有序分拆数：$\alpha(n,k)=\binom{n+k-1}{k-1}$；无序分拆的生成函数：$\sum_{n}\beta(n,k)x^n=\prod_{r=1}^k\frac{1}{1-x^r}$。

## 体现的方法

- **生成函数法**：利用 $x^a\cdot x^b = x^{a+b}$ 的性质将组合计数问题转化为代数级数展开问题。

## 所属系列位置

属于《组合数学与生成函数》系列的基础应用篇。

## 与其他文章的关系

- [[3018 算符的艺术：差分、微分与伯努利数]]：生成函数概念与伯努利数的母函数直接相关。

## 原文证据锚点

- **有序分拆生成函数**：见"有序的分拆"章节。对应 [ev::2942::ordered_partition_gf](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Mathematics/2014-09-16-生成函数法与整数的分拆.md#L31-L43)。
- **无序分拆生成函数**：见"无序的分拆"及"无序的分拆：推导"章节。对应 [ev::2942::unordered_partition_gf](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Mathematics/2014-09-16-生成函数法与整数的分拆.md#L50-L52)。
