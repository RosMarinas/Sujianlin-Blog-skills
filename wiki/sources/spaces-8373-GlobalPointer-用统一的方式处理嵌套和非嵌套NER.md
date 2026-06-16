---
type: article_summary
title: "GlobalPointer：用统一的方式处理嵌套和非嵌套NER"
article_id: "8373"
source_url: https://spaces.ac.cn/archives/8373
date: 2021-05-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::命名实体识别]]
  - [[concept::序列标注]]
  - [[concept::RoPE相对位置编码]]
methods:
  - [[method::GlobalPointer]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md
source_ids:
  - "8373"
status: draft
updated: 2026-06-10
---

# GlobalPointer：用统一的方式处理嵌套和非嵌套NER

GlobalPointer将NER转化为 $n(n+1)/2$ 选 $k$ 的多标签分类问题，使用 $s_\alpha(i,j) = q_{i,\alpha}^\top k_{j,\alpha}$ 作为片段打分，结合RoPE注入相对位置信息。使用多标签交叉熵损失函数，解码时仅需 $s_\alpha(i,j) > 0$。在非嵌套NER上媲美CRF，嵌套NER上显著优于CRF，训练速度更快。
