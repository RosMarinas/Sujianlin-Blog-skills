---
type: article_summary
title: "随机分词浅探：从Viterbi Decoding到Viterbi Sampling"
article_id: "9768"
source_url: https://spaces.ac.cn/archives/9768
date: 2023-09-16
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::Viterbi算法]]
  - [[concept::Unigram分词]]
  - [[concept::中文分词]]
methods:
  - [[method::Viterbi Sampling]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
source_ids:
  - "9768"
status: draft
updated: 2026-06-10
---

# 随机分词浅探：从Viterbi Decoding到Viterbi Sampling

本文提出Viterbi Sampling，将确定性Viterbi解码中 `if score > routes[e][0]` 的硬判据替换为Sigmoid随机化判据 $\varepsilon < \sigma(\alpha(s_i - s_{i-1}))$，实现Unigram分词的随机采样。相比SentencePiece的Subword Regularization（速度降为1/4），Viterbi Sampling仅下降30%速度。
