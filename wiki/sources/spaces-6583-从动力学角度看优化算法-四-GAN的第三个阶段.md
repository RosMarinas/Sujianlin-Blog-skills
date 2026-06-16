---
type: article_summary
title: 从动力学角度看优化算法（四）：GAN的第三个阶段
article_id: "6583"
source_url: https://spaces.ac.cn/archives/6583
date: "2019-05-03"
category: "Big-Data"
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-05-03-从动力学角度看优化算法-四-GAN的第三个阶段.md
source_html: Data/Spaces_ac_cn/raw/articles/6583/page.html
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
  - ev::6583::动力系统
  - ev::6583::缓解策略
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-05-03-从动力学角度看优化算法-四-GAN的第三个阶段.md
source_ids:
  - "6583"
status: draft
updated: 2026-06-10
---

# 从动力学角度看优化算法（四）：GAN的第三个阶段

## 文章核心问题

把 GAN 交替训练写成梯度下降/上升耦合动力系统，并用局部稳定性分析 loss 设计。

## 推导位置

本页只记录本轮编译需要的认知对象。原文关键章节包括：动力系统, Dirac GAN, 常见GAN分析, 缓解策略, 文章小结。

## 关键对象

- 系列：[[从动力学角度看优化算法]]
- 主题：[[优化动力学]]
- 方法：[[把优化算法解释为动力系统离散化]]
- 问题模式：[[把优化器经验现象改写为动力系统问题]]

## 原文证据锚点

- `ev::6583::动力系统`
- `ev::6583::缓解策略`
