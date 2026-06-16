---
type: concept
title: "GPT2"
aliases:
  - "Generative Pre-Training 2"
definition: "基于Transformer解码器的自回归语言模型，通过大规模无监督预训练获得文本生成能力。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "7292"
  - "7877"
related_methods:
  - [[method::bert4keras GPT2集成]]
  - [[method::GPT背棋谱下棋]]
status: draft
updated: 2026-06-13
---

GPT2（Generative Pre-Training 2）是基于Transformer解码器的自回归语言模型，最大版本达15亿参数。通过大规模无监督预训练获得文本生成能力，是GPT、BERT等预训练范式的重要继承者。本文介绍了在bert4keras中集成中文GPT2_ML的方法，以及使用GPT2背棋谱实现中国象棋AI的创意跨界应用。 GPT2通过从左到右的自回归方式生成文本，是GPT系列中承上启下的重要模型，证明了扩大模型规模和数据量能有效提升生成质量。
