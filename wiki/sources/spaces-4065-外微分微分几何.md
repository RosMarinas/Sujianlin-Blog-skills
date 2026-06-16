---
type: article_summary
title: 【外微分浅谈】6. 微分几何
article_id: "4065"
source_url: https://spaces.ac.cn/archives/4065
date: 2016-11-07
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-11-07-外微分浅谈-6-微分几何.md
series:
  - 外微分浅谈
topics:
  - 微分几何
  - 外微分
concepts:
  - 外微分
  - 正交标架
  - 联络形式
  - 曲率形式
  - 协变导数
  - 黎曼曲率张量
methods:
  - 外微分计算黎曼曲率
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-11-07-外微分浅谈-6-微分几何.md
source_ids:
  - "4065"
status: draft
updated: 2026-06-10
---

## 总结

本文建立外微分与微分几何的系统联系：通过正交标架 $\hat{\boldsymbol{e}}_\mu$ 和余标架 $\omega^\mu$，将黎曼几何的核心对象（联络、曲率）纳入外微分框架。核心方程：
- 标架运动方程 $d\hat{\boldsymbol{e}}_\mu=\hat{\boldsymbol{e}}_\alpha\omega_\mu^\alpha$
- 无挠条件 $d\omega^\mu+\omega_\nu^\mu\land\omega^\nu=0$（来源于 $d^2\boldsymbol{r}=0$）
- 曲率形式 $\mathscr{R}_\nu^\mu=d\omega_\nu^\mu+\omega_\alpha^\mu\land\omega_\nu^\alpha$
- 向量协变导数 $d\boldsymbol{A}=\hat{\boldsymbol{e}}_\mu(d\hat{A}^\mu+\omega_\nu^\mu\hat{A}^\nu)$

## 关键思想

- 两组基：向量基 $\hat{\boldsymbol{e}}_\mu$（对称内积）和余基 $dx^\mu$（反对称外积）的组合是外微分加速微分几何推导的核心
- $d^2\boldsymbol{r}=0$ 导出无挠条件，这是外微分框架下Cartan结构方程的基础
- 曲率形式 $\mathscr{R}_\nu^\mu$ 与黎曼曲率张量的关系：$\mathscr{R}_\nu^\mu=\frac12 R^\mu_{\nu\beta\gamma}\omega^\beta\land\omega^\gamma$
- 标架沿路径的平行移动由路径依赖的 $\exp(\int\omega_\nu^\mu)$ 描述

## 所属系列

[[外微分浅谈]] — [[微分几何]]
