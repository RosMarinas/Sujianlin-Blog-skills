---
type: concept
title: "MLM预训练"
aliases:
  - "Masked Language Model"
  - "掩码语言模型"
definition: "BERT等模型的预训练任务，随机mask部分token并通过上下文预测被mask的token。"
standard_notation: "$P(x_i|x_{\setminus i})$"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "7764"
  - "8671"
related_methods:
  - [[method::BERT MLM小样本学习]]
  - [[method::NSP-BERT零样本分类]]
status: draft
updated: 2026-06-13
---

MLM（Masked Language Model）是BERT的核心预训练任务：随机mask输入文本中15%的token，让模型根据双向上下文预测被mask的token。MLM不仅是一个预训练任务，本身也具有实用价值。本文介绍了利用MLM做小样本学习（PET范式）和利用NSP做零样本分类两种预训练任务的创新应用，展示了预训练的巨大潜力。 事实证明，MLM不仅是一个预训练工具，本身也能直接用于文本纠错、文本生成、小样本分类等多种实际任务。
