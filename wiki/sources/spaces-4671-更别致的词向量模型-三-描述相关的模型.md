---
type: article_summary
title: 更别致的词向量模型(三)：描述相关的模型
article_id: "4671"
source_url: https://spaces.ac.cn/archives/4671
date: 2017-11-19
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-三-描述相关的模型.md
source_html: Data/Spaces_ac_cn/raw/articles/4671/page.html
series:
  - "[[更别致的词向量模型]]"
topics:
  - "[[互信息词向量]]"
  - "[[SVD矩阵分解]]"
concepts:
  - "[[互信息词向量]]"
  - "[[词向量几何类比]]"
methods:
  - "[[用互信息内积构造词向量几何]]"
problem_patterns: []
evidence_spans:
  - ev::4671::几何词向量
  - ev::4671::模型形式
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-三-描述相关的模型.md
source_ids:
  - "4671"
status: draft
updated: 2026-06-10
---

# 更别致的词向量模型(三)：描述相关的模型

## 文章核心问题

本文把互信息关系落实为词向量内积模型，使概率相关性变成向量空间几何。

## 主要结论

- 若两个词关系可由互信息表达，就可以用向量内积作为模型形式。
- 词类比来自上下文互信息关系的近似线性组合。

## 推导结构

1. 定义几何词向量目标。
2. 分析类比例子。
3. 写出模型形式。
4. 讨论归一化问题。

## 关键公式

- [[PMI内积词向量公式]]

## 体现的方法

- [[用互信息内积构造词向量几何]]

## 所属系列位置

词向量系列第 3 篇，给出核心模型形式。

## 与其他文章的关系

- bridges: `method::用矩阵分解重写表示学习结构`

## 原文证据锚点

- `ev::4671::几何词向量`
- `ev::4671::模型形式`
