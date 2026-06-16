---
type: article_summary
title: 从熵、最大熵原理到最大熵模型（三）
article_id: "3567"
source_url: https://spaces.ac.cn/archives/3567
date: 2015-12-20
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2015-12-20-熵-不起-从熵-最大熵原理到最大熵模型-三.md
series:
  - [[熵不起]]
topics:
  - [[信息论基础]]
concepts:
  - [[最大熵模型]]
methods:

evidence_spans:
  - ev::3567::最大熵模型定义
  - ev::3567::特征函数
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2015-12-20-熵-不起-从熵-最大熵原理到最大熵模型-三.md
source_ids:
  - "3567"
status: draft
updated: 2026-06-10
---

# “熵”不起：从熵、最大熵原理到最大熵模型（三）

## 文章核心问题

如何将最大熵原理应用于有监督分类问题，构建最大熵模型（MaxEnt Model）？

## 主要结论

最大熵模型通过特征函数定义约束，用最大熵原理求解条件分布 p(y|x)。结果为指数形式 p(y|x)=exp(-∑ λ_i χ_i(x,y))/Z(x)。模型理论优美但求解困难，在深度学习时代应用受限。

## 推导结构

1. 分类问题的概率视角：求 p(Y|X)
2. 特征函数定义约束
3. 最大化条件熵得到指数形式解
4. 模型的应用与局限性分析

## 关键公式

p(y|x)=exp(-∑_i λ_i χ_i(x,y))/Z(x) — 最大熵模型的条件分布

## 体现的方法

最大熵模型作为有监督分类方法

## 所属系列位置

系列第三篇，结束篇，将最大熵原理应用于有监督分类。

## 原文证据锚点

- ev::3567::最大熵模型定义 — 最大熵模型的构建方法
- ev::3567::特征函数 — 特征函数定义与约束条件
