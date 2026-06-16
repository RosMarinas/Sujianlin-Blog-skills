---
type: article_summary
title: 跟风玩玩目前最大的中文GPT2模型（bert4keras）
article_id: "7912"
source_url: https://spaces.ac.cn/archives/7912
date: 2020-11-20
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-11-20-跟风玩玩目前最大的中文GPT2模型-bert4keras.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-11-20-跟风玩玩目前最大的中文GPT2模型-bert4keras.md
source_ids:
  - "7912"
status: draft
updated: 2026-06-12
---

## 文章核心问题
将清华与智源发布的26亿参数中文GPT2模型CPM-LM适配到bert4keras框架，并测试其Few Shot效果。

## 主要结论
CPM-LM具备较强的Few Shot能力，在常识推理、翻译、三元组抽取等任务上表现不错；适配过程的主要坑在于tokenizer设计。

## 推导结构
1. CPM-LM模型介绍（26亿参数，单向语言模型）
2. Tokenizer问题分析（sentencepiece的特殊处理）
3. 适配bert4keras的过程
4. Few Shot应用演示

## 关键公式
（无核心数学公式）

## 体现的方法
大语言模型适配集成方法、Few Shot文本续写方法、sentencepiece定制分词方法

## 所属系列位置
独立文章，属于大型预训练模型应用系列

## 与其他文章的关系
基于[6915]的bert4keras框架；与[7718]共享GPT/LM应用主题

## 原文证据锚点
Few Shot演示代码输出、模型链接、适配说明