---
type: article_summary
title: 测试函数法推导连续性方程和Fokker-Planck方程
article_id: "9461"
source_url: https://spaces.ac.cn/archives/9461
date: 2023-02-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2023-02-11-测试函数法推导连续性方程和Fokker-Planck方程.md
series: []
topics:
  - 随机过程
  - 偏微分方程
concepts:
  - Fokker-Planck方程
  - 测试函数法
  - 连续性方程
methods:
  - 测试函数法
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-02-11-测试函数法推导连续性方程和Fokker-Planck方程.md
source_ids:
  - "9461"
status: draft
updated: 2026-06-10
---

## 总结

本文系统介绍"测试函数法"——推导ODE连续性方程和SDE Fokker-Planck方程的标准方法。核心技巧是用任意测试函数$\phi(\boldsymbol{x})$的积分等式反推概率密度满足的偏微分方程，配合高维分部积分公式完成严格推导。

## 关键思想

- 测试函数原理：若 $\int f\phi = \int g\phi$ 对任意测试函数成立，则 $f=g$
- 高维分部积分：$\int \boldsymbol{v}\cdot\nabla u\, d\boldsymbol{x} = -\int u\nabla\cdot\boldsymbol{v}\, d\boldsymbol{x}$（无穷远边界项消失）
- ODE演化 $\frac{d\boldsymbol{x}_t}{dt}=\boldsymbol{f}_t$ → 连续性方程 $\partial_t p_t = -\nabla\cdot(p_t\boldsymbol{f}_t)$
- SDE演化 $d\boldsymbol{x}_t = \boldsymbol{f}_t dt + g_t d\boldsymbol{w}$ → Fokker-Planck方程 $\partial_t p_t = -\nabla\cdot(p_t\boldsymbol{f}_t) + \frac{1}{2}g_t^2\nabla^2 p_t$

## 所属系列

[[随机过程]] — [[偏微分方程]] — [[扩散模型理论基础]]
