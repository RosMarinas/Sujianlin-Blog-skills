---
type: article_summary
title: "P-tuning：自动构建模版，释放语言模型潜能"
article_id: "8295"
source_url: https://spaces.ac.cn/archives/8295
date: 2021-04-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-04-03-P-tuning-自动构建模版-释放语言模型潜能.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::Prompt Tuning]]
  - [[concept::语言模型]]
methods:
  - [[method::P-tuning]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-03-P-tuning-自动构建模版-释放语言模型潜能.md
source_ids:
  - "8295"
status: draft
updated: 2026-06-10
---

# P-tuning：自动构建模版，释放语言模型潜能

P-tuning放弃"模版必须由自然语言构成"的要求，将模版构建转化为连续参数优化问题。使用[unused*] token作为模版，通过梯度下降优化其Embedding。在小样本场景固定模型仅优化模版参数，大数据场景放开全量微调。配合P-tuning可使GPT在SuperGLUE上超越同等级BERT。
