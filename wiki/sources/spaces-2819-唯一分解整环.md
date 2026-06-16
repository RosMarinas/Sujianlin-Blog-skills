---
type: article_summary
title: 从费马大定理谈起（四）：唯一分解整环
article_id: "2819"
source_url: https://spaces.ac.cn/archives/2819
date: 2014-08-17
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-08-17-从费马大定理谈起-四-唯一分解整环.md
series:
  - [[从费马大定理谈起]]
topics: []
concepts:
  - [[唯一分解整环]]
  - [[欧几里得整环]]
  - [[带余除法]]
  - [[费蜀等式]]
  - [[欧几里得引理]]
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-08-17-从费马大定理谈起-四-唯一分解整环.md
source_ids:
  - "2819"
status: draft
updated: 2026-06-10
---

## 文章核心问题

在高斯整数环 $\mathbb{Z}[i]$ 中建立唯一分解定理（算术基本定理），为 $n=4$ 证明奠定理论基础。

## 主要结论

- 欧几里得整环中成立带余除法，进而可证唯一分解定理。
- 高斯整数环 $\mathbb{Z}[i]$ 是欧几里得整环（因为对任意复数 $\alpha/\beta$ 的实部和虚部四舍五入即可得到带余除法）。
- 带余除法 $\Rightarrow$ 辗转相除法 $\Rightarrow$ 裴蜀等式 $\Rightarrow$ 欧几里得引理 $\Rightarrow$ 唯一分解定理。
- 唯一分解定理在忽略单位数因子的意义下成立。

## 推导结构

1. 定义带余除法：$\alpha = \kappa\beta + \lambda$ 且 $N(\lambda) < N(\beta)$。
2. 证明 $\mathbb{Z}[i]$ 中带余除法成立（利用复数四舍五入）。
3. 由带余除法得辗转相除法，进而得裴蜀等式。
4. 由裴蜀等式证欧几里得引理（素数整除乘积则必整除某一因子）。
5. 用数学归纳法证明唯一分解定理。

## 关键公式

$$
\alpha = \kappa\beta + \lambda,\ N(\lambda) < N(\beta)
$$

$$
\alpha\xi + \beta\eta = d\ (\text{裴蜀等式})
$$

$$
\pi \mid \alpha\beta \Rightarrow \pi \mid \alpha\ \text{或}\ \pi \mid \beta\ (\text{欧几里得引理})
$$

## 体现的方法

- 带余除法构造法。
- 辗转相除法（欧几里得算法）。
- 数学归纳法证明唯一分解性。

## 所属系列位置

系列第四篇，为 $n=4$ 证明提供理论基础。

## 与其他文章的关系

- 建立在第三篇高斯整数的基础上。
- 直接为第五、六篇 $n=4$ 证明中的分解唯一性提供保证。
- 唯一分解性在 $n=3$ 证明中同样需要（艾森斯坦整数环也是欧几里得整环）。
- 第八篇中艾森斯坦整数的唯一分解性通过类比本文学方法证明。

## 原文证据锚点

- 带余除法定义与证明：第 32-55 行
- 裴蜀等式：第 62-67 行
- 欧几里得引理：第 72-84 行
- 唯一分解定理的归纳证明：第 88-93 行
