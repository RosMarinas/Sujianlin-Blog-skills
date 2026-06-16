---
type: article_summary
title: 勒贝格(Lebesgue)控制收敛定理
article_id: "3194"
source_url: https://spaces.ac.cn/archives/3194
date: 2015-01-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2015-01-16-勒贝格-Lebesgue-控制收敛定理.md
series:
  - "[[实变函数论]]"
topics:
  - "[[数学分析与级数]]"
concepts:
  - "[[勒贝格控制收敛定理]]"
  - "[[勒贝格积分]]"
methods:
  - "[[算术-几何平均不等式构造控制函数法]]"
evidence_spans:
  - "ev::3194::dominated_convergence_counterexample"
  - "ev::3194::agm_inequality_construction"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2015-01-16-勒贝格-Lebesgue-控制收敛定理.md
source_ids:
  - "3194"
status: draft
updated: 2026-06-13
---

## 文章核心问题

勒贝格控制收敛定理的应用条件和控制函数的构造技巧是什么？过度依赖定理形式而忽略直接计算可能导致什么问题？

## 主要结论

1. 勒贝格控制收敛定理指出如果 $|f_n(x)|\leq F(x)$ 且 $F(x)$ 可积，则可交换极限与积分。
2. 并非所有问题都需要控制收敛定理：如 $\int_0^1\frac{n^2x}{1+n^4x^4}dx$ 可直接积出，且极限与积分不可交换。
3. 对于分母为多项式的典型题型，可以利用算术-几何平均不等式（AM-GM）统一构造控制函数。
4. 控制函数难找的说法很可能源于学艺不精，通过适当拆分分母并应用AM-GM不等式，可以系统性地找到控制函数。

## 推导结构

1. 通过具体例子说明交换极限与积分的陷阱
2. 介绍AM-GM不等式构造控制函数的一般技巧
3. 应用技巧到 $\lim_{n\to\infty}\int_0^1\frac{n^3x}{1+n^4x^2}dx$（找到控制函数 $x^{-1/2}$）

## 关键公式

用AM-GM拆分分母：$1+n^4x^2 = 1+\frac13 n^4 x^2+\frac13 n^4 x^2+\frac13 n^4 x^2 \geq 4\sqrt[4]{\frac{1}{27}}n^3x^{3/2} \geq n^3 x^{3/2}$

## 体现的方法

- **算术-几何平均不等式构造控制函数法**：将分母改写为若干项之和，利用AM-GM不等式放缩为单一幂次项，构造出可积的控制函数。

## 所属系列位置

属于《实变函数论》系列，讨论勒贝格积分理论中的核心定理及其应用技巧。

## 与其他文章的关系

- [[4083 为什么勒贝格积分比黎曼积分强？]]：同为勒贝格积分主题的姊妹篇，4083从更广阔视角对比黎曼与勒贝格积分。
