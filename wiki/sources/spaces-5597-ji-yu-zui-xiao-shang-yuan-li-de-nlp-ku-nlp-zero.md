---
type: article_summary
title: 基于最小熵原理的NLP库：nlp zero
article_id: "5597"
source_url: https://spaces.ac.cn/archives/5597
date: 2018-05-31
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-05-31-基于最小熵原理的NLP库-nlp-zero.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-05-31-基于最小熵原理的NLP库-nlp-zero.md
source_ids:
  - "5597"
status: draft
updated: 2026-06-12
---

## 文章核心问题
介绍基于最小熵原理构建的无监督NLP工具库nlp zero，覆盖分词、词库构建、句模板构建和层次分解。

## 主要结论
通过最小熵原理可以无监督地完成NLP基础任务，nlp zero提供了纯Python实现的开源工具。

## 推导结构
1. 默认分词器使用说明
2. 词库构建流程——统计互信息、构建词库
3. 句模板构建——基于词的统计模式
4. 层次分解——基于前缀树的句子结构解析

## 关键公式
（无核心数学公式，以算法步骤为主）

## 体现的方法
基于互信息的新词发现、基于模板的句子结构分析、最小熵无监督学习

## 所属系列位置
独立文章，属于最小熵原理系列的应用篇

## 与其他文章的关系
与[6920]共享新词发现主题；最小熵原理的代码实现

## 原文证据锚点
Github地址、词库构建示例、句模板构建示例、层次分解示意图