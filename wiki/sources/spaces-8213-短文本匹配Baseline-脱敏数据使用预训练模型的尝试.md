---
type: article_summary
title: "短文本匹配Baseline：脱敏数据使用预训练模型的尝试"
article_id: "8213"
source_url: https://spaces.ac.cn/archives/8213
date: 2021-03-05
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::文本匹配]]
  - [[concept::MLM预训练]]
methods:
  - [[method::PET范式]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
source_ids:
  - "8213"
status: draft
updated: 2026-06-10
---

# 短文本匹配Baseline：脱敏数据使用预训练模型的尝试

本文提出在脱敏数据（每个字被映射为数字ID）中使用预训练模型的方案：通过字频对齐初始化Embedding层，使用MLM模型同时完成句子对分类（[CLS]处预测[YES]/[NO]）和MLM预训练任务，将分类、预训练和半监督学习统一在单一MLM框架中。
