---
type: article_summary
title: MuP之上：4. 坚守参数的稳定性
article_id: "11729"
source_url: https://spaces.ac.cn/archives/11729
date: 2026-04-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2026-04-24-MuP之上-4-坚守参数的稳定性.md
source_html: Data/Spaces_ac_cn/raw/articles/11729/page.html
series:
  - "[[MuP之上]]"
topics:
  - "[[矩阵优化]]"
concepts:
  - "[[谱范数]]"
  - "[[矩阵符号函数]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
problem_patterns: []
evidence_spans:
  - ev::11729::问题背景
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-04-24-MuP之上-4-坚守参数的稳定性.md
source_ids:
  - "11729"
status: draft
updated: 2026-06-10
---

# MuP之上：4. 坚守参数的稳定性

## 文章核心问题

本文讨论如何在训练过程中维持参数稳定性，把 MuP 稳定性指标从初始化推进到训练动态。

## 主要结论

- 线性层的前向稳定性、依赖稳定性和更新稳定性都可用谱范数刻画。
- 参数稳定性可转化为训练过程中约束关键范数的问题。
- 在谱范数下，Post Clip 与 Pre Decay 分别导向奇异值裁剪和谱权重衰减。

## 推导结构

1. 从 MuP 的稳定性指标进入谱范数约束。
2. 抽象出一般参数范数维持框架。
3. 应用到矩阵参数与 Muon。
4. 讨论为什么需要保证而不是只依赖经验安全。

## 关键公式

- [[谱范数定义]]：稳定性指标中的核心矩阵范数。
- [[Muon更新公式]]：矩阵参数更新的背景公式。

## 体现的方法

- [[用稳定性指标约束优化器缩放]]：从稳定性指标推导优化器约束和缩放。

## 所属系列位置

它是 MuP之上第 4 篇，同时连接 MuP、Muon 和矩阵谱约束。

## 与其他文章的关系

- belongs_to: `series::MuP之上`
- belongs_to: `topic::矩阵优化`
- uses: `concept::谱范数`
- motivates: `article::11736`

## 原文证据锚点

- `ev::11729::问题背景`：给出三个稳定性指标及其谱范数形式。
- `ev::11729::文章小结`：总结 Post Clip、Pre Decay、奇异值裁剪和谱权重衰减。
