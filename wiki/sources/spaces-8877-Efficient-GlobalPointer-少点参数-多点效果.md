---
type: article_summary
title: Efficient GlobalPointer：少点参数，多点效果
article_id: "8877"
source_url: https://spaces.ac.cn/archives/8877
date: 2022-01-25
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-01-25-Efficient-GlobalPointer-少点参数-多点效果.md
series:
  - [[GlobalPointer与联合抽取]]
topics:
  - [[联合抽取]]
concepts:
  - [[GlobalPointer]]
  - [[Efficient GlobalPointer]]
methods:
  - [[抽取与分类解耦]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-25-Efficient-GlobalPointer-少点参数-多点效果.md
source_ids:
  - "8877"
---

# Efficient GlobalPointer：少点参数，多点效果

本文针对先前提出的用于处理嵌套与非嵌套命名实体识别（NER）的GlobalPointer进行了优化，提出了Efficient GlobalPointer。原始的GlobalPointer由于为每种实体类型都分配了独立的映射变换，导致在实体类别增多时参数规模过于庞大。

Efficient GlobalPointer基于将NER任务解构成“抽取（识别实体片段）”与“分类（确定实体类别）”的设计思路，实现两者投影特征的解耦。模型使所有实体类型共用一套用于“抽取”的注意力投影权重，而通过简单的特征拼接与专属权重向量来实现“分类”。在大幅减少参数量的前提下，Efficient GlobalPointer能够缓解大参数量下更新稀疏及容易过拟合的弊病，在类别数目较多、任务难度较大的CLUENER及CMeEE等数据集上表现出了比CRF和原始GlobalPointer更优的效果。
