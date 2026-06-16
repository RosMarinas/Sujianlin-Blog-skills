---
type: article_summary
title: bert4keras在手，baseline我有：CLUE基准代码
article_id: "8739"
source_url: https://spaces.ac.cn/archives/8739
date: 2021-10-31
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-10-31-bert4keras在手-baseline我有-CLUE基准代码.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-10-31-bert4keras在手-baseline我有-CLUE基准代码.md
source_ids:
  - "8739"
status: draft
updated: 2026-06-12
---

## 文章核心问题
基于bert4keras构建CLUE评测基准的完整baseline代码，覆盖文本分类、匹配、阅读理解、NER等任务。

## 主要结论
baseline代码基本复现甚至超越CLUE官方基准成绩；使用GlobalPointer统一NER和阅读理解表现优异。

## 推导结构
1. 文本分类（IFLYTEK、TNEWS、WSC）
2. 文本匹配（AFQMC、CMNLI、OCNLI、CSL）
3. 阅读理解CMRC2018（GlobalPointer + 滑窗）
4. 单项选择C3（转化为文本匹配）
5. 成语理解CHID（匈牙利算法去重）
6. 实体识别CLUENER（GlobalPointer）
7. 效果对比表格

## 关键公式
（以模型架构说明为主）

## 体现的方法
GlobalPointer统一序列标注方法、滑窗长文本处理方法、匈牙利算法去重后处理方法

## 所属系列位置
独立文章，属于bert4keras应用生态系列

## 与其他文章的关系
基于[6915]的bert4keras框架；GlobalPointer方法在[8373]中有详细介绍

## 原文证据锚点
各任务建模示意图、效果对比表格