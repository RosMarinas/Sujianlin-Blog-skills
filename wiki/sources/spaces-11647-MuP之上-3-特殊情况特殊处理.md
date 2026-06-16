---
type: article_summary
title: MuP之上：3. 特殊情况特殊处理
article_id: "11647"
source_url: https://spaces.ac.cn/archives/11647
date: 2026-03-02
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2026-03-02-MuP之上-3-特殊情况特殊处理.md
source_html: Data/Spaces_ac_cn/raw/articles/11647/page.html
series:
  - "[[MuP之上]]"
topics:
  - "[[矩阵优化]]"
  - "[[MuP稳定性与矩阵优化]]"
concepts:
  - "[[Embedding输出头稳定性]]"
  - "[[MuP稳定性三条件]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
problem_patterns: []
evidence_spans:
  - ev::11647::嵌入之层
  - ev::11647::输出之头
  - ev::11647::重要不等式
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-03-02-MuP之上-3-特殊情况特殊处理.md
source_ids:
  - "11647"
status: draft
updated: 2026-06-10
---

# MuP之上：3. 特殊情况特殊处理

## 文章核心问题

本文处理 Embedding、输出头、哈达玛积、偏置和注意力缩放等特殊模块，展示稳定性指标需要按模块结构特殊化。

## 主要结论

- Embedding 和输出头不能直接套用普通线性层，需要按输入域、损失项和输出尺度分别分析。
- 注意力缩放、偏置和乘积模块都可以纳入稳定性指标框架，但需要保留各自结构约束。

## 推导结构

1. 回顾线性层结论。
2. 分析 Embedding 输入域导致的尺度差异。
3. 处理输出头和交叉熵损失负责的尺度。
4. 扩展到哈达玛积、线性偏置和注意力缩放。

## 关键公式

- [[Embedding输出头稳定性公式]]

## 体现的方法

- [[用稳定性指标约束优化器缩放]]

## 所属系列位置

MuP之上第 3 篇，把稳定性框架从线性层扩展到特殊模块。

## 与其他文章的关系

- extends: `article::11605`
- precedes: `article::11729`

## 原文证据锚点

- `ev::11647::嵌入之层`
- `ev::11647::输出之头`
- `ev::11647::重要不等式`
