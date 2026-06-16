---
type: concept
title: "WoBERT"
aliases:
  - "Word-based BERT"
definition: "以词为颗粒度的中文BERT预训练模型，通过前分词+字词混合词表实现提速不掉点。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "7758"
related_methods:
  - [[method::WoBERT词级预训练]]
status: draft
updated: 2026-06-13
---

WoBERT（Word-based BERT）是以词为颗粒度的中文BERT预训练模型。通过前分词（jieba）+字词混合词表（2万词），基于RoBERTa-wwm-ext继续预训练。字embedding的平均作为词embedding初始化。相比字级BERT，序列更短速度更快，在不需要精确边界的NLU任务上效果基本不降，实现提速不掉点的目标。 词级别模型还可以缓解文本生成中的Exposure Bias问题（序列越短递归步数越少），以及降低词义的不确定性。
