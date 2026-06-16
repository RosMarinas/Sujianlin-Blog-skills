---
type: article_summary
title: 【外微分浅谈】5. 几何意义
article_id: "4062"
source_url: https://spaces.ac.cn/archives/4062
date: 2016-11-06
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-11-06-外微分浅谈-5-几何意义.md
series:
  - 外微分浅谈
topics:
  - 微分几何
  - 外微分
concepts:
  - 外微分
  - 外积
  - 斯托克斯公式
  - 微分形式
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-11-06-外微分浅谈-5-几何意义.md
source_ids:
  - "4062"
status: draft
updated: 2026-06-10
---

## 总结

本文探讨外微分的几何意义：外积对应于向量的有向面积/体积投影，外微分算子 $d$ 对应于沿闭合路径"绕一圈"的变化量。统一微积分基本定理 $\int_{\partial D}\omega=\int_D d\omega$（广义斯托克斯公式）将牛顿-莱布尼茨、格林、高斯、斯托克斯公式统一为微分形式的边界积分等于外微分的区域积分。

## 关键思想

- 外积 $\alpha_\mu dx^\mu\land\beta_\nu dx^\nu = \frac12(\alpha_\mu\beta_\nu-\beta_\mu\alpha_\nu)dx^\mu\land dx^\nu$ 的系数正是 $\det(\alpha_\mu,\beta_\nu)$
- $n$ 个1形式外积等同于雅可比行列式：$df^1\land\dots\land df^n = \det(\partial f^\mu/\partial x^\nu)dx^1\land\dots\land dx^n$
- 外微分 $d$ 的"绕圈子"解释：从1形式到2形式对应于沿无穷小闭合路径的变化量
- 广义斯托克斯公式 $\int_{\partial D}\omega=\int_D d\omega$ 是微分形式框架下的微积分基本定理

## 所属系列

[[外微分浅谈]] — [[微分几何]] — [[微分形式]]
