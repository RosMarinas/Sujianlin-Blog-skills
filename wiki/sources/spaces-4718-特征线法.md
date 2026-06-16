---
type: article_summary
title: 一阶偏微分方程的特征线法
article_id: "4718"
source_url: https://spaces.ac.cn/archives/4718
date: 2017-12-07
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2017-12-07-一阶偏微分方程的特征线法.md
series: []
topics:
  - 偏微分方程
concepts:
  - 特征线法
methods:
  - 特征线法
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-12-07-一阶偏微分方程的特征线法.md
source_ids:
  - "4718"
status: draft
updated: 2026-06-10
---

## 总结

本文系统介绍一阶偏微分方程的特征线法（拟线性和一般情形），核心思想是将PDE沿特征线转化为ODE求解。特征线法的本质是先求解解曲线上的常微分方程得到积分常数，再根据初值条件确定常数之间的关系。

## 关键思想

- 拟线性情形：$\boldsymbol{\alpha}\cdot\partial_{\boldsymbol{x}} u = \beta$ 转化 $\frac{d\boldsymbol{x}}{ds}=\boldsymbol{\alpha}, \frac{du}{ds}=\beta$
- 一般情形：$F(\boldsymbol{x},u,\boldsymbol{p})=0$ 需额外引入 $\boldsymbol{p}=\partial u/\partial\boldsymbol{x}$
- 特征线方程：$\frac{d\boldsymbol{x}}{ds}=\frac{\partial F}{\partial\boldsymbol{p}}, \frac{d\boldsymbol{p}}{ds}=-\frac{\partial F}{\partial\boldsymbol{x}}-\frac{\partial F}{\partial u}\boldsymbol{p}, \frac{du}{ds}=\boldsymbol{p}\cdot\frac{\partial F}{\partial\boldsymbol{p}}$
- 方程组情形：仅当偏导数算子一致时特征线法可用

## 所属系列

[[偏微分方程]] — [[数学物理方法]]
