---
type: article_summary
title: "搜狐文本匹配：基于条件LayerNorm的多任务baseline"
article_id: "8337"
source_url: https://spaces.ac.cn/archives/8337
date: 2021-04-16
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-04-16-搜狐文本匹配-基于条件LayerNorm的多任务baseline.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::文本匹配]]
  - [[concept::条件LayerNorm]]
methods:
  - [[method::条件LayerNorm多任务学习]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-16-搜狐文本匹配-基于条件LayerNorm的多任务baseline.md
source_ids:
  - "8337"
status: draft
updated: 2026-06-10
---

# 搜狐文本匹配：基于条件LayerNorm的多任务baseline

针对6个子任务的文本匹配问题，使用条件LayerNorm（Conditional Layer Normalization）将任务类型作为条件向量注入Transformer的LayerNorm的 $\beta,\gamma$ 参数中，实现单一模型处理多个不同标准的文本匹配子任务，参数完全共享。
