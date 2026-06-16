---
type: article_summary
title: "层次分解位置编码，让BERT可以处理超长文本"
article_id: "7947"
source_url: https://spaces.ac.cn/archives/7947
date: 2020-12-04
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-12-04-层次分解位置编码-让BERT可以处理超长文本.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::位置编码]]
  - [[concept::层次分解位置编码]]
  - [[concept::Transformer]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-12-04-层次分解位置编码-让BERT可以处理超长文本.md
source_ids:
  - "7947"
status: draft
updated: 2026-06-10
---

# 层次分解位置编码，让BERT可以处理超长文本

本文提出层次分解位置编码方法，将位置 $(i-1) \times n + j$ 分解为 $(i, j)$ 二元组，编码为 $\alpha u_i + (1-\alpha) u_j$，其中基底 $u_i$ 由原始前 $n$ 个位置编码反推。可使BERT最大处理长度从512扩展到 $512^2 \approx 26万$，在bert4keras中通过 `hierarchical_position=True` 一键启用。
