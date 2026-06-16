---
type: article_summary
title: '你的语言模型有没有"无法预测的词"？'
article_id: "9046"
source_url: https://spaces.ac.cn/archives/9046
date: 2022-04-20
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-04-20-你的语言模型有没有-无法预测的词.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::语言模型]]
  - [[concept::Softmax分类器]]
concepts:
  - [[concept::Unargmaxable Class]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-20-你的语言模型有没有-无法预测的词.md
source_ids:
  - "9046"
status: draft
updated: 2026-06-10
---

# 你的语言模型有没有"无法预测的词"？

本文研究分类模型中"无法预测的类别"（unargmaxable class）现象。当类别数远大于向量维度时，某些类别可能永远不是概率最大者。通过Minimax定理和Frank-Wolfe算法可判别此类类别。实践中由于维度灾难效应和Normalization技术，语言模型很少出现此问题。
