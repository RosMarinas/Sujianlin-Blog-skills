---
type: article_summary
title: 从动力学角度看优化算法（五）：为什么学习率不宜过小？
article_id: "7787"
source_url: https://spaces.ac.cn/archives/7787
date: "2020-10-10"
category: "Big-Data"
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-10-10-从动力学角度看优化算法-五-为什么学习率不宜过小.md
source_html: Data/Spaces_ac_cn/raw/articles/7787/page.html
series:
  - [[从动力学角度看优化算法]]
topics:
  - [[优化动力学]]
concepts:
  - [[优化动力学视角]]
  - [[梯度流]]
formulas:
  - [[梯度流ODE公式]]
methods:
  - [[把优化算法解释为动力系统离散化]]
problem_patterns:
  - [[把优化器经验现象改写为动力系统问题]]
evidence_spans:
  - ev::7787::差分方程到微分方程
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-10-10-从动力学角度看优化算法-五-为什么学习率不宜过小.md
source_ids:
  - "7787"
status: draft
updated: 2026-06-10
---

# 从动力学角度看优化算法（五）：为什么学习率不宜过小？

## 文章核心问题

通过差分方程到微分方程的改写，说明有限学习率带来隐式梯度惩罚。

## 推导位置

本页只记录本轮编译需要的认知对象。原文关键章节包括：降得最快的方向, 藏在学习率中的正则, 差分方程到微分方程, 例行公事的小总结。

## 关键对象

- 系列：[[从动力学角度看优化算法]]
- 主题：[[优化动力学]]
- 方法：[[把优化算法解释为动力系统离散化]]
- 问题模式：[[把优化器经验现象改写为动力系统问题]]

## 原文证据锚点

- `ev::7787::差分方程到微分方程`
