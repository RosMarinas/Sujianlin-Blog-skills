---
type: article_summary
title: 基于Bert的NL2SQL模型：一个简明的Baseline
article_id: "6771"
source_url: https://spaces.ac.cn/archives/6771
date: 2019-06-29
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-06-29-基于Bert的NL2SQL模型-一个简明的Baseline.md
series: []
topics:
  - [[联合抽取]]
concepts:
  - [[NL2SQL]]
methods:
  - [[基于BERT的NL2SQL联合编码]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-06-29-基于Bert的NL2SQL模型-一个简明的Baseline.md
source_ids:
  - "6771"
---

# 基于Bert的NL2SQL模型：一个简明的Baseline

本文提供了一个面向自然语言转SQL语句（NL2SQL）任务的简明Baseline模型。由于NL2SQL任务输入包括自然语言问句以及对应的数据表结构（包含多个列名），模型通过将自然语言问题与所有表头字段拼接后输入BERT进行实时联合编码。

在BERT编码出的特征之上，模型将NL2SQL任务解构为四个分类子任务：通过问题句向量预测WHERE子句的连接符，通过表头向量预测该表头对应列是否被SELECT以及其对应的聚合函数，通过字符序列标注预测条件值和运算符，以及通过计算条件值字向量与表头向量的相似度来映射对应的条件列。
