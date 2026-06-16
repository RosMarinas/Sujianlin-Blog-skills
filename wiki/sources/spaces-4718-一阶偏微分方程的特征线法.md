---
type: article_summary
title: 一阶偏微分方程的特征线法
article_id: "4718"
source_url: https://spaces.ac.cn/archives/4718
date: 2017-12-07
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2017-12-07-一阶偏微分方程的特征线法.md
series:
  - "[[偏微分方程]]"
topics:
  - "[[数学分析与级数]]"
concepts:
  - "[[特征线法]]"
  - "[[一阶偏微分方程]]"
  - "[[拟线性方程]]"
methods:
  - "[[特征线法]]"
evidence_spans:
  - "ev::4718::quasilinear_characteristics"
  - "ev::4718::general_characteristics"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-12-07-一阶偏微分方程的特征线法.md
source_ids:
  - "4718"
status: draft
updated: 2026-06-13
---

## 文章核心问题

如何通过特征线法（Method of Characteristics）将一阶偏微分方程的求解转化为常微分方程组的求解？拟线性情形和一般情形的特征线法有何联系和区别？

## 主要结论

1. 拟线性情形：方程 $\boldsymbol{\alpha}(\boldsymbol{x},u)\cdot\partial u/\partial\boldsymbol{x}=\beta(\boldsymbol{x},u)$ 的特征线方程为 $d\boldsymbol{x}/ds=\boldsymbol{\alpha}$，$du/ds=\beta$，构成 $n+1$ 个常微分方程。
2. 一般情形：方程 $F(\boldsymbol{x},u,\boldsymbol{p})=0$ 的特征线方程组扩展为包含 $\boldsymbol{p}$ 的 $2n+1$ 个方程，其中 $\boldsymbol{p}=\partial u/\partial\boldsymbol{x}$。
3. 一般情形在形式上复杂但可退化到拟线性情形：当 $F=\boldsymbol{\alpha}\cdot\boldsymbol{p}-\beta$ 时还原。
4. 特征线法本质是"线动成面"：先解出特征线上的解，再通过初值条件确定积分常数之间的关系，得到解曲面。

## 推导结构

1. 拟线性偏微分方程的特征线法（含实例）
2. 一般一阶偏微分方程的特征线法（含推导和实例）
3. 退化验证和方程组情形

## 关键公式

拟线性情形：$\frac{d\boldsymbol{x}}{ds}=\boldsymbol{\alpha}(\boldsymbol{x},u),\frac{du}{ds}=\beta(\boldsymbol{x},u)$
一般情形：$\frac{d\boldsymbol{x}}{ds}=\frac{\partial F}{\partial\boldsymbol{p}},\frac{d\boldsymbol{p}}{ds}=-\frac{\partial F}{\partial\boldsymbol{x}}-\frac{\partial F}{\partial u}\boldsymbol{p},\frac{du}{ds}=\boldsymbol{p}\cdot\frac{\partial F}{\partial\boldsymbol{p}}$

## 体现的方法

- **特征线法**：将偏微分方程沿特定曲线（特征线）转化为常微分方程组，通过求解ODEs得到PDE的解。

## 所属系列位置

属于《偏微分方程》系列的基础方法文章。

## 与其他文章的关系

无直接关联，属于偏微分方程的独立方法论。
