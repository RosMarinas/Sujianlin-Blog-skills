---
type: article_summary
title: 从动力学角度看优化算法（一）：从SGD到动量加速
article_id: "5655"
source_url: https://spaces.ac.cn/archives/5655
date: "2018-06-27"
category: "Mathematics"
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
source_html: Data/Spaces_ac_cn/raw/articles/5655/page.html
series:
  - [[从动力学角度看优化算法]]
topics:
  - [[优化动力学]]
concepts:
  - [[优化动力学视角]]
  - [[梯度流]]
  - [[SGD-SDE近似]]
formulas:
  - [[梯度流ODE公式]]
methods:
  - [[把优化算法解释为动力系统离散化]]
problem_patterns:
  - [[把优化器经验现象改写为动力系统问题]]
evidence_spans:
  - ev::5655::GD与ODE
  - ev::5655::从SGD到SDE
  - ev::5655::动量加速
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
source_ids:
  - "5655"
status: draft
updated: 2026-06-10
---

# 从动力学角度看优化算法（一）：从SGD到动量加速

## 文章核心问题

把 GD/SGD 写成 ODE/SDE 数值求解，并解释动量为二阶动力系统。

## 推导位置

本页只记录本轮编译需要的认知对象。原文关键章节包括：梯度下降, GD与ODE, 从SGD到SDE, 动量加速, Kramers方程。

## 关键对象

- 系列：[[从动力学角度看优化算法]]
- 主题：[[优化动力学]]
- 方法：[[把优化算法解释为动力系统离散化]]
- 问题模式：[[把优化器经验现象改写为动力系统问题]]

## 原文证据锚点

- `ev::5655::GD与ODE`
- `ev::5655::从SGD到SDE`
- `ev::5655::动量加速`
