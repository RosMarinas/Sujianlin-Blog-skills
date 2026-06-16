---
type: formula
title: Weiszfeld迭代公式
latex: \boldsymbol{\mu}_{t+1} = \frac{\sum_{i=1}^n \boldsymbol{x}_i / \Vert\boldsymbol{x}_i
  - \boldsymbol{\mu}_t\Vert_2}{\sum_{i=1}^n 1 / \Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2}
symbol_meanings:
  \boldsymbol{\mu}_t: 当前步的几何中位数估计值
  x_i: 高维数据向量
standard_notation: \boldsymbol{\mu}_t, \boldsymbol{x}_i
conditions: \boldsymbol{\mu}_t 不等于任何数据点 x_i
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2026-03-31-中位数-Median-简介.md
source_ids:
- 11693
appears_in:
- - - spaces-11693-中位数-Median-简介
status: draft
updated: '2026-06-14'
---

# Weiszfeld迭代公式


## 概述

（待补充）

## 公式

```tex
\boldsymbol{\mu}_{t+1}
= \frac{\sum_{i=1}^n \boldsymbol{x}_i / \Vert\boldsymbol{x}_i-\boldsymbol{\mu}_t\Vert_2}
{\sum_{i=1}^n 1 / \Vert\boldsymbol{x}_i-\boldsymbol{\mu}_t\Vert_2}
```

Weiszfeld 迭代用于求高维几何中位数。源文先将高维中位向量定义为
$$
\mathop{\text{argmin}}_{\boldsymbol{\mu}}\sum_i\Vert\boldsymbol{x}_i-\boldsymbol{\mu}\Vert_2,
$$
然后从更一般的目标 $\sum_i\Vert\boldsymbol{x}_i-\boldsymbol{\mu}\Vert_2^\alpha$ 出发，令梯度为零，得到一个不动点方程。将 $\boldsymbol{\mu}_t$ 代入右端作为下一步，并取 $\alpha=1$，就得到本页公式。

## 符号与条件

$\boldsymbol{x}_i$ 是高维向量样本，$\boldsymbol{\mu}_t$ 是第 $t$ 步估计。frontmatter 条件要求 $\boldsymbol{\mu}_t$ 不等于任何数据点，原因是分母含 $\Vert\boldsymbol{x}_i-\boldsymbol{\mu}_t\Vert_2$；源文也说明严格的收敛性和唯一性证明较复杂，原文未展开。

## 用途

该公式把没有解析解的几何中位数转成可迭代计算的问题。它保留了中位数优化视角的鲁棒性动机，同时绕开了高维空间没有自然排序的问题。

## 证据

- `source_id: 11693`
- 源文《中位数（Median）简介》“高维空间”“继续推广”段给出几何中位数目标、不动点方程以及 $\alpha=1$ 对应 Weiszfeld 迭代的说明。
