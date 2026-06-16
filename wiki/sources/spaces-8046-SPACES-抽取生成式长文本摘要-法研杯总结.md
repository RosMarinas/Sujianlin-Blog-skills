---
type: article_summary
title: "SPACES：'抽取-生成'式长文本摘要（法研杯总结）"
article_id: "8046"
source_url: https://spaces.ac.cn/archives/8046
date: 2021-01-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-01-01-SPACES-抽取-生成-式长文本摘要-法研杯总结.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::文本摘要]]
  - [[concept::Copy机制]]
  - [[concept::Sparse Softmax]]
methods:
  - [[method::SPACES摘要模型]]
  - [[method::BIO Copy机制]]
  - [[method::Sparse Softmax]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-01-01-SPACES-抽取-生成-式长文本摘要-法研杯总结.md
source_ids:
  - "8046"
status: draft
updated: 2026-06-10
---

# SPACES："抽取-生成"式长文本摘要（法研杯总结）

SPACES是"先抽取后生成"的长文本摘要模型，包含Sparse Softmax、预训练语言模型、生成式、BIO Copy机制、抽取式和Special Words六大技术点。抽取模型使用DGCNN进行句子级序列标注，生成模型使用UniLM+NEZHA+BIO Copy。BIO Copy通过额外B/I/O标签预测实现连续片段复制，Sparse Softmax只保留top-k logits防止过学习。
