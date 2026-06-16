---
type: article_summary
title: 狄拉克函数：级数逼近
article_id: "4187"
source_url: https://spaces.ac.cn/archives/4187
date: 2017-01-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2017-01-11-狄拉克函数-级数逼近.md
series:
  - "[[函数逼近论]]"
topics:
  - "[[数学分析与级数]]"
concepts:
  - "[[狄拉克函数]]"
  - "[[魏尔斯特拉斯定理]]"
  - "[[标准正交基]]"
  - "[[傅里叶级数]]"
  - "[[勒让德多项式]]"
methods:
  - "[[狄拉克核逼近法]]"
evidence_spans:
  - "ev::4187::dirac_weierstrass_poly"
  - "ev::4187::orthonormal_basis_approximation"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-01-11-狄拉克函数-级数逼近.md
source_ids:
  - "4187"
status: draft
updated: 2026-06-13
---

## 文章核心问题

如何通过构造狄拉克函数的不同级数逼近形式，统一地证明魏尔斯特拉斯定理（闭区间上的连续函数可用多项式/三角函数一致逼近），并引出最优逼近的标准正交基方法？

## 主要结论

1. 构造 $\delta_n(x)=\frac{(1-x^2)^n}{I_n}$ 作为 $\delta(x)$ 的逼近，可得 $f(x)=\lim_{n\to\infty}\int f(y)\delta_n(x-y)dy$，这是 $x$ 的 $2n$ 次多项式，证明了多项式逼近定理。
2. 改用 $\delta_n(x)=\frac{\cos^n x}{I_n}$ 可得到三角级数逼近版本。
3. 更一般地，任意满足归一化和尖峰条件的函数列 $\{\delta_n(x)\}$ 都可作为狄拉克函数的逼近。
4. 在标准正交基下，函数逼近系数可由内积直接计算 $\alpha_k=\int f(x)e_k(x)dx$，且增加逼近阶只需追加新项。
5. 幂函数基通过Gram-Schmidt正交化得到勒让德多项式 $P_n(x)$，构成 $[-1,1]$ 上的正交基。

## 推导结构

1. 狄拉克函数的级数逼近构造
2. 魏尔斯特拉斯定理的多项式版本
3. 魏尔斯特拉斯定理的三角级数版本
4. 标准正交基与最优逼近系数
5. 傅里叶级数作为正余弦正交基的特例
6. 勒让德多项式作为幂函数正交基的特例

## 关键公式

$$f(x)=\lim_{n\to\infty}\int_{-1}^1 f(y)\delta_n(x-y)dy,\quad \delta_n(x)=\frac{(1-x^2)^n}{I_n}$$

## 体现的方法

- **狄拉克核逼近法**：将狄拉克函数视为一族函数序列的极限，通过选择不同的核函数构造不同的函数逼近基底。

## 所属系列位置

属于《函数逼近论》系列的方法论核心文章。

## 与其他文章的关系

- [[2555 傅里叶变换：只需要异想天开？]]：共享傅里叶级数主题，2555从级数推广视角，4187从正交基视角。
