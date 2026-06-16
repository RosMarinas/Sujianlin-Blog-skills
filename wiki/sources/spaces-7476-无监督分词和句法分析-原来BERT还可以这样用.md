---
type: article_summary
title: "无监督分词和句法分析！原来BERT还可以这样用"
article_id: "7476"
source_url: https://spaces.ac.cn/archives/7476
date: 2020-06-10
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-06-10-无监督分词和句法分析-原来BERT还可以这样用.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::中文分词]]
  - [[concept::无监督句法分析]]
  - [[concept::MLM预训练]]
methods:
  - [[method::Perturbed Masking]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-10-无监督分词和句法分析-原来BERT还可以这样用.md
source_ids:
  - "7476"
status: draft
updated: 2026-06-10
---

# 无监督分词和句法分析！原来BERT还可以这样用

通过Perturbed Masking技术利用BERT的MLM能力计算token-token相关矩阵：$f(x_i, x_j) = \|H(x \setminus \{x_i\})_i - H(x \setminus \{x_i, x_j\})_i\|_2$。基于相邻token相关度可做无监督中文分词，基于聚类式分块算法可做无监督句法分析，无需任何finetune。
