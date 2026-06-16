---
type: article_summary
title: "CAN：借助先验分布提升分类性能的简单后处理技巧"
article_id: "8728"
source_url: https://spaces.ac.cn/archives/8728
date: 2021-10-22
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-10-22-CAN-借助先验分布提升分类性能的简单后处理技巧.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::文本分类]]
  - [[concept::先验分布]]
methods:
  - [[method::CAN后处理]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-10-22-CAN-借助先验分布提升分类性能的简单后处理技巧.md
source_ids:
  - "8728"
status: draft
updated: 2026-06-10
---

# CAN：借助先验分布提升分类性能的简单后处理技巧

CAN（Classification with Alternating Normalization）是一种利用先验分布修正低置信度分类结果的后处理技巧。方法：用top-k熵识别低置信度样本，然后交替执行行间标准化（匹配先验分布）和行内标准化（保持概率归一化），逐个修正低置信度样本。类别数越多，效果越明显。
