---
type: article_summary
title: 重新写了之前的新词发现算法：更快更好的新词发现
article_id: "6920"
source_url: https://spaces.ac.cn/archives/6920
date: 2019-09-09
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-09-09-重新写了之前的新词发现算法-更快更好的新词发现.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-09-重新写了之前的新词发现算法-更快更好的新词发现.md
source_ids:
  - "6920"
status: draft
updated: 2026-06-12
---

## 文章核心问题
重写并优化了之前提出的新词发现（无监督词库构建）算法，利用KenLM和Trie树实现更快更好的新词发现。

## 主要结论
优化后的算法在PKU测试集上达到F1=0.765（使用500万篇文章语料），性能不差于顶会ICLR 2019的结果。

## 推导结构
1. 使用kenlm的count_ngrams统计ngram
2. 使用Trie树加速候选词搜索
3. 互信息过滤与频数过滤
4. 标准评测（基于Bakeoff 2005数据集）

## 关键公式
（以算法流程为主；互信息作为过滤指标）

## 体现的方法
基于ngram统计的无监督新词发现方法、Trie树加速搜索方法、KenLM语言模型工具集成方法

## 所属系列位置
独立文章，属于中文分词/新词发现系列的实践篇

## 与其他文章的关系
与[5597]共享无监督NLP主题；最小熵原理在词发现的应用

## 原文证据锚点
评测结果F1=0.742/0.765、算法步骤、开源地址