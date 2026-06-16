---
type: article_summary
title: 从EMD、WMD到WRD：文本向量序列的相似度计算
article_id: "7388"
source_url: https://spaces.ac.cn/archives/7388
date: 2020-05-13
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::Earth Mover's Distance]]
  - [[concept::Wasserstein距离]]
  - [[concept::Word Mover's Distance]]
  - [[concept::Word Rotator's Distance]]
methods:
  - [[method::WMD文本相似度计算]]
  - [[method::WRD文本相似度计算]]
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
source_ids:
  - "7388"
status: draft
updated: 2026-06-10
---

# 从EMD、WMD到WRD：文本向量序列的相似度计算

本文介绍两种基于Wasserstein距离的文本向量序列相似度指标WMD和WRD。WMD使用均匀权重和欧氏距离，将一个句子的词向量"搬运"到另一个句子的词向量；WRD则利用词向量模长作为重要性权重，使用余弦距离作为传输成本，将结果归一化到[0,2]区间。两者均可推导出下界公式（WCD）用于快速过滤。
