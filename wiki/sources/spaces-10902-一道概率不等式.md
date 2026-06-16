---
type: article_summary
title: 一道概率不等式：盯着它到显然成立为止！
article_id: "10902"
source_url: https://spaces.ac.cn/archives/10902
date: 2025-04-30
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-04-30-一道概率不等式-盯着它到显然成立为止.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[概率不等式]]
methods:
  - [[泰勒展开证明不等式法]]
  - [[逆向思维构造级数法]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-04-30-一道概率不等式-盯着它到显然成立为止.md
source_ids:
  - "10902"
status: draft
updated: 2026-06-11
---

## 文章核心问题

求证概率不等式 $\sum_{i=0}^j p^i \leq \sum_{i=0}^j (\log\frac{1}{1-p})^i / i!$，其中 $p\in[0, 1)$。

## 主要结论

不等式成立。两种证明方法：1）泰勒展开硬刚，求导推导出各项系数；2）逆向思维，将求和推到无穷项然后利用指数函数展开。

## 推导结构

1. 初等尝试失败（直接展开幂级数不可行）
2. 泰勒硬刚：定义 $f_j(x)=\sum_{i=0}^j x^i/i!$，通过求导规律证明 $\left.\frac{d^k}{dp^k}f_j(x)\right|_{p=0}=k!$（$k\leq j$时）
3. 逆向思维：将 $\sum_{i=0}^j (\log\frac{1}{1-p})^i/i!$ 写成 $\frac{1}{1-p} - \sum_{i=j+1}^{\infty}(\log\frac{1}{1-p})^i/i!$ 然后展开

## 关键公式

核心不等式：$\sum_{i=0}^j p^i \leq \sum_{i=0}^j \left(\log\frac{1}{1-p}\right)^i/i!$

对数展开：$\log\frac{1}{1-p} = \sum_{i=1}^{\infty} \frac{p^i}{i} = p + \frac{p^2}{2} + \frac{p^3}{3} + \cdots$

## 体现的方法

- 泰勒展开证明不等式法
- 逆向思维构造级数法

## 所属系列位置

独立单篇，不属于系列。

## 与其他文章的关系

涉及概率不等式和级数展开，与logsumexp不等式等相关。

## 原文证据锚点

- 初步尝试：直接展开不可行
- 泰勒硬刚：求导规律推导
- 显然易得：逆向思维构造无穷级数
