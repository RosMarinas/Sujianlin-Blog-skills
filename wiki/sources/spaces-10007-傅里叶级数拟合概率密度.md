---
type: article_summary
title: 用傅里叶级数拟合一维概率密度函数
article_id: "10007"
source_url: https://spaces.ac.cn/archives/10007
date: 2024-03-07
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-03-07-用傅里叶级数拟合一维概率密度函数.md
series: []
topics:
  - 傅里叶分析
  - 概率密度估计
concepts:
  - 傅里叶级数
  - 概率密度估计
  - Toeplitz矩阵正定性
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-03-07-用傅里叶级数拟合一维概率密度函数.md
source_ids:
  - "10007"
status: draft
updated: 2026-06-10
---

## 总结

本文介绍FBDM（Fourier Basis Density Model），用截断傅里叶级数拟合任意一维概率密度函数。核心贡献是通过自相关构造保证傅里叶系数的Toeplitz矩阵正定性，从而确保概率密度函数非负，并实现归一化。将复杂非负约束转化为可优化的复数系数构造，相比GMM和DFP在KL散度和峰值拟合上有更优表现。

## 关键思想

- 将概率密度函数表示为截断傅里叶级数 $f_{\theta}(x) = \sum_{n=-N}^{N} c_n e^{i\pi n x}$
- 非负约束通过Herglotz定理简化：构造Toeplitz矩阵正定等价于概率密度非负
- 自相关构造法：$c_n = \sum_{k=0}^{N-n} a_k a_{k+n}^*$ 保证正定性
- 归一化因子简单为 $2c_0$
- 正弦级数正则项 $\gamma\sum n^2 |c_n|^2$ 防止过拟合

## 与其他文章关联

- [[spaces-8718-狄拉克函数光滑近似]]: 核密度估计基于Dirac delta光滑近似，FBDM对比核密度估计讨论
- [[spaces-4187-狄拉克函数级数逼近]]: 两者都讨论函数逼近基底

## 所属系列

[[傅里叶分析]] — [[概率密度估计]] — [[函数逼近论]]
