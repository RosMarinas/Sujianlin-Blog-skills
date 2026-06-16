---
type: article_summary
title: 狄拉克函数：级数逼近
article_id: "4187"
source_url: https://spaces.ac.cn/archives/4187
date: 2017-01-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2017-01-11-狄拉克函数-级数逼近.md
series: []
topics:
  - 函数逼近论
  - 傅里叶分析
concepts:
  - 狄拉克函数
  - 魏尔斯特拉斯定理
  - 标准正交基
  - 傅里叶级数
  - 勒让德多项式
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-01-11-狄拉克函数-级数逼近.md
source_ids:
  - "4187"
status: draft
updated: 2026-06-10
---

## 总结

本文从狄拉克函数的极限构造出发，以统一视角推导魏尔斯特拉斯逼近定理：连续函数可以用多项式（或三角级数）一致逼近。进而在标准正交基框架下导出傅里叶级数（$\sin,\cos$基）和勒让德多项式展开（幂函数基施密特正交化）。

## 关键思想

- 构造 $\delta_n(x)\to\delta(x)$ 的极限函数列是逼近的通用框架
- 多项式逼近：$\delta_n(x)=(1-x^2)^n/I_n$ → 多项式逼近
- 三角级数逼近：$\delta_n(x)=\cos^n x/I_n$ → 正余弦级数逼近
- 标准正交基使逼近系数增量式计算：$f(x)=\sum\alpha_k e_k(x), \alpha_k=\int f(x)e_k(x)dx$
- 傅里叶级数是正余弦正交基下的最优$L^2$逼近
- 勒让德多项式是 $[-1,1]$ 上幂函数基施密特正交化结果
- 实指数也可逼近，但因非周期发散性质不如傅里叶级数实用

## 所属系列

[[傅里叶分析]] — [[函数逼近论]]
