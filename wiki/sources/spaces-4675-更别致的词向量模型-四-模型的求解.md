---
type: article_summary
title: 更别致的词向量模型(四)：模型的求解
article_id: "4675"
source_url: https://spaces.ac.cn/archives/4675
date: 2017-11-19
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-四-模型的求解.md
source_html: Data/Spaces_ac_cn/raw/articles/4675/page.html
series:
  - "[[更别致的词向量模型]]"
topics:
  - "[[互信息词向量]]"
concepts:
  - "[[点互信息PMI]]"
methods:
  - "[[用互信息内积构造词向量几何]]"
problem_patterns: []
evidence_spans:
  - ev::4675::损失函数
  - ev::4675::互信息估算
  - ev::4675::Adagrad
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-四-模型的求解.md
source_ids:
  - "4675"
status: draft
updated: 2026-06-10
---

# 更别致的词向量模型(四)：模型的求解

## 文章核心问题

本文把互信息内积模型写成平方损失，并用共现频率估计概率，再用 Adagrad 求解。

## 主要结论

- simpler GloVe 的损失直接拟合词向量内积与 PMI 的差。
- 窗口共现、权重和降采样决定 PMI 估计与优化权重。

## 推导结构

1. 定义损失函数。
2. 估计共现概率和边缘概率。
3. 讨论权重/降采样。
4. 写出 Adagrad 更新。

## 关键公式

- [[simpler GloVe损失公式]]

## 体现的方法

- [[用互信息内积构造词向量几何]]

## 所属系列位置

词向量系列第 4 篇，给出训练目标和求解路线。

## 与其他文章的关系

- implements: `method::用互信息内积构造词向量几何`

## 原文证据锚点

- `ev::4675::损失函数`
- `ev::4675::互信息估算`
- `ev::4675::Adagrad`
