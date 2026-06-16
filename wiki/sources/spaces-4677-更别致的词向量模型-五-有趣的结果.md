---
type: article_summary
title: 更别致的词向量模型(五)：有趣的结果
article_id: "4677"
source_url: https://spaces.ac.cn/archives/4677
date: 2017-11-19
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-五-有趣的结果.md
source_html: Data/Spaces_ac_cn/raw/articles/4677/page.html
series:
  - "[[更别致的词向量模型]]"
topics:
  - "[[互信息词向量]]"
concepts:
  - "[[词向量模长ICF解释]]"
  - "[[词向量上下文相关性]]"
methods:
  - "[[用互信息内积构造词向量几何]]"
problem_patterns: []
evidence_spans:
  - ev::4677::模长的含义
  - ev::4677::相关词排序
  - ev::4677::关键词提取
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-五-有趣的结果.md
source_ids:
  - "4677"
status: draft
updated: 2026-06-10
---

# 更别致的词向量模型(五)：有趣的结果

## 文章核心问题

本文解释模型训练出的向量性质：模长近似词重要性，内积/余弦可用于相关词、关键词和句向量。

## 主要结论

- 在模型假设下词向量模长平方近似 -log P(w)，因此高频虚词模长更小。
- 用内积或归一化内积可以把统计相关性转成几何检索。

## 推导结构

1. 分析模长含义。
2. 展示类比和相关词排序。
3. 重新定义相似度。
4. 给出关键词、句子相似和句向量应用。

## 关键公式

- [[词向量模长ICF公式]]
- [[词上下文相关系数公式]]

## 体现的方法

- [[用互信息内积构造词向量几何]]

## 所属系列位置

词向量系列第 5 篇，解释模型结果和应用。

## 与其他文章的关系

- uses: `formula::PMI内积词向量公式`

## 原文证据锚点

- `ev::4677::模长的含义`
- `ev::4677::相关词排序`
- `ev::4677::关键词提取`
