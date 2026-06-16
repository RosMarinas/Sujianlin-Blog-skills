---
type: article_summary
title: 从动力学角度看优化算法（六）：为什么SimSiam不退化？
article_id: "7980"
source_url: https://spaces.ac.cn/archives/7980
date: "2020-12-11"
category: "Big-Data"
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-12-11-从动力学角度看优化算法-六-为什么SimSiam不退化.md
source_html: Data/Spaces_ac_cn/raw/articles/7980/page.html
series:
  - [[从动力学角度看优化算法]]
topics:
  - [[优化动力学]]
concepts:
  - [[优化动力学视角]]
  - [[梯度流]]
  - [[优化快慢动力学]]
formulas:
  - [[梯度流ODE公式]]
methods:
  - [[把优化算法解释为动力系统离散化]]
problem_patterns:
  - [[把优化器经验现象改写为动力系统问题]]
evidence_spans:
  - ev::7980::不退化的动力学
  - ev::7980::看近似展开
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-12-11-从动力学角度看优化算法-六-为什么SimSiam不退化.md
source_ids:
  - "7980"
status: draft
updated: 2026-06-10
---

# 从动力学角度看优化算法（六）：为什么SimSiam不退化？

## 文章核心问题

用快慢动力学解释 predictor 与 stop_gradient 如何阻止表征坍缩。

## 推导位置

本页只记录本轮编译需要的认知对象。原文关键章节包括：SimSiam, 动力学分析, 不退化的动力学, 看近似展开, 总文末小结。

## 关键对象

- 系列：[[从动力学角度看优化算法]]
- 主题：[[优化动力学]]
- 方法：[[把优化算法解释为动力系统离散化]]
- 问题模式：[[把优化器经验现象改写为动力系统问题]]

## 原文证据锚点

- `ev::7980::不退化的动力学`
- `ev::7980::看近似展开`
