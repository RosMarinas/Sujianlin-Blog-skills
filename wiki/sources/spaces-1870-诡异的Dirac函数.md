---
type: article_summary
title: 诡异的Dirac函数
article_id: "1870"
source_url: https://spaces.ac.cn/archives/1870
date: 2013-01-14
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2013-01-14-诡异的Dirac函数.md
series: []
topics: ['[[topic::傅里叶分析]]']
concepts: ['[[狄拉克函数]]']
methods: ['[[用测试函数定义与运算广义函数]]']
problem_patterns: []
evidence_spans: ['ev::1870::筛选性质', 'ev::1870::傅里叶表示', 'ev::1870::导数性质']
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-01-14-诡异的Dirac函数.md
source_ids:
  - "1870"
status: draft
updated: 2026-06-11
---

## 文章核心问题
介绍物理与工程中极其重要的 Dirac $\delta(x)$ 函数的物理引入背景、诡异的非普通函数性质、极限逼近表达式、傅里叶积分表示，以及如何在其测试函数积分框架下定义其导数和运算。

## 主要结论
Dirac $\delta$ 函数不是数学上的经典函数，而是一个广义函数（泛函）。其作用只有在它与测试函数进行积分相乘时才得以体现，最核心的物理性质是其“筛选/抽样”性质（$\int f(x)\delta(x)dx = f(0)$）。$\delta$ 函数的导数可通过分部积分法定义，满足 $\int f(x)\delta^{(n)}(x)dx = (-1)^n f^{(n)}(0)$。此外，$\delta$ 函数具有傅里叶积分表示，这是数理方程中极其关键的等价式。

## 推导结构
1. **物理模型引入**：通过长度为 $2l$ 的质量为 $1$ 的均匀直线密度在 $l 	o 0$ 极限下的密度分布引入 $\delta$ 函数，给出经典特征值 $\infty$ 和 0 的定义及其全空间积分为 $1$。
2. **定义筛选性质**：说明 $\delta(x)$ 作用于函数 $f(x)$ 积分为 $f(0)$ 的筛选作用。
3. **极限表达与傅里叶变换**：给出正态分布与柯西分布的极限表示，并导出基于傅里叶变换的核心公式 $\delta(x) = 
rac{1}{2\pi}\int_{-\infty}^{\infty} e^{i\omega x} d\omega$。
4. **导数定义与推导**：应用分部积分性质定义 $\delta'(x)$，通过消除边界项，将导数算子转移到测试函数 $f(x)$ 上，得出 $\int f(x)\delta'(x)dx = -f'(0)$ 并推广至 $n$ 阶。

## 关键公式
- 狄拉克函数筛选律: $\int_{-\infty}^{+\infty} f(x)\delta(x)dx = f(0)$
- 傅里叶积分形式: $\delta(x) = 
rac{1}{2\pi} \int_{-\infty}^{\infty} e^{i\omega x}d\omega$
- 导数的积分性质: $\int_{-\infty}^{+\infty} f(x)\delta^{(n)}(x)dx = (-1)^n f^{(n)}(0)$

## 体现的方法
- `[[用测试函数定义与运算广义函数]]`：通过将广义函数与测试函数的内积（积分）作为定义和演算基础，通过分部积分定义广义函数导数的方法。

## 所属系列位置
无。广义函数专题讨论。

## 与其他文章的关系
- 傅里叶积分表示与 `[[wiki/sources/spaces-1683-复分析学习1-揭示微分与积分的联系.md]]` 在傅里叶展开的思想上相关联。
- 后续在偏微分方程中的应用对应 Green 函数法。

## 原文证据锚点
- `ev::1870::筛选性质`：第5段关于 $\int f(x)\delta(x)dx=f(0)$ 的阐述。
- `ev::1870::傅里叶表示`：第7段关于傅里叶变换导出的积分表达式（公式第4行）。
- `ev::1870::导数性质`：第8段应用分部积分法计算出 $\int f(x)\delta'(x)dx = -f'(0)$ 及其 $n$ 阶推广。
