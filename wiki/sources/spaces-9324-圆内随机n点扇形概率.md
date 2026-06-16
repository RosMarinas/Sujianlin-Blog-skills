---
type: article_summary
title: 圆内随机n点在同一个圆心角为θ的扇形的概率
article_id: "9324"
source_url: https://spaces.ac.cn/archives/9324
date: 2022-10-25
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2022-10-25-圆内随机n点在同一个圆心角为θ的扇形的概率.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[顺序统计量]]
  - [[容斥原理]]
methods:
  - [[容斥原理求概率]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2022-10-25-圆内随机n点在同一个圆心角为θ的扇形的概率.md
source_ids:
  - "9324"
status: draft
updated: 2026-06-11
---

## 文章核心问题

圆内均匀分布的n个点，它们位于同一个圆心角为θ的扇形的概率是多少？推广"四鸭共半圆"问题。

## 主要结论

概率为 $P_n(\max(x_1,\ldots,x_n) > x) = \sum_{k=1,1-kx>0}^n (-1)^{k-1} C_n^k (1-kx)^{n-1}$，其中 $x=1-\theta/(2\pi)$。当 $\theta<\pi$ 时简化为 $n(\theta/(2\pi))^{n-1}$。

## 推导结构

1. 等价转换为线段分割的最长段问题
2. 推导联合分布：$p_n(x_1,\ldots,x_n) = (n-1)!$
3. 推导边缘分布：$p_n(x_1,\ldots,x_k) = \frac{(n-1)!}{(n-k-1)!}[1-(x_1+\cdots+x_k)]^{n-k-1}$
4. 容斥原理求最大值的概率

## 关键公式

$P_n(x_1 > c_1,\ldots,x_k > c_k) = [1-(c_1+\cdots+c_k)]^{n-1}$

## 体现的方法

容斥原理求概率、顺序统计量

## 所属系列位置

独立单篇。

## 与其他文章的关系

引用了重参数构建离散分布（9085）和熵的最邻近估计的相关工作。

## 原文证据锚点

- 题目转换：等价于最长线段问题
- 联合分布：$(n-1)!$ 均匀分布
- 边缘分布和容斥原理
- 答案分析
