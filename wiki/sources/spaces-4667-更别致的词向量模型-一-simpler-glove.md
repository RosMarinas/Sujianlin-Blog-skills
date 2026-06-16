---
type: article_summary
title: 更别致的词向量模型(一)：simpler glove
article_id: "4667"
source_url: https://spaces.ac.cn/archives/4667
date: 2017-11-19
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-一-simpler-glove.md
source_html: Data/Spaces_ac_cn/raw/articles/4667/page.html
series:
  - "[[更别致的词向量模型]]"
topics:
  - "[[互信息词向量]]"
  - "[[SVD矩阵分解]]"
concepts:
  - "[[互信息词向量]]"
  - "[[点互信息PMI]]"
methods:
  - "[[用互信息内积构造词向量几何]]"
problem_patterns: []
evidence_spans:
  - ev::4667::模型缘起
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-一-simpler-glove.md
source_ids:
  - "4667"
status: draft
updated: 2026-06-10
---

# 更别致的词向量模型(一)：simpler glove

## 文章核心问题

本文提出 simpler GloVe 的起点：希望用更少参数、更清晰的统计意义来构造词向量。

## 主要结论

- 词向量可以不依赖中心词/上下文两套参数和可训练偏置，而转向一个更对称的内积模型。
- 系列的目标是用词共现和互信息解释词向量几何。

## 推导结构

1. 指出 GloVe 的复杂性。
2. 提出更简洁的词向量建模方向。
3. 为后续互信息推导铺垫。

## 关键公式

- [[PMI内积词向量公式]]

## 体现的方法

- [[用互信息内积构造词向量几何]]

## 所属系列位置

词向量系列第 1 篇，提出 simpler GloVe 问题意识。

## 与其他文章的关系

- motivates: `article::4669`

## 原文证据锚点

- `ev::4667::模型缘起`
