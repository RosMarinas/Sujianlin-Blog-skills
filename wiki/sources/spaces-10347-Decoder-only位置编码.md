---
type: article_summary
title: "Decoder-only的LLM为什么需要位置编码？"
article_id: "10347"
source_url: https://spaces.ac.cn/archives/10347
date: 2024-09-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-09-01-Decoder-only的LLM为什么需要位置编码.md
series:
  - "[[transformer-upgrade-path]]"
topics:
  - "[[Transformer架构]]"
concepts:
  - "[[NoPE]]"
  - "[[因果注意力置换不变性破除]]"
  - "[[方差辨位机制]]"
  - "[[乘性绝对位置编码]]"
evidence_spans:
  - "ev::10347::位置编码"
  - "ev::10347::先验认知"
  - "ev::10347::单向注意"
  - "ev::10347::方差辨位"
  - "ev::10347::不足之处"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-09-01-Decoder-only的LLM为什么需要位置编码.md
source_ids:
  - "10347"
status: draft
updated: 2026-06-10
---

# Decoder-only的LLM为什么需要位置编码？

## Summary

分析为什么Causal Attention下的NoPE（无位置编码）理论上可用但实践中仍需加位置编码：NoPE通过隐状态方差编码位置（单标量/head），分辨率不足且实现的是弱绝对位置编码，而相对位置编码提供了更高效的先验。

## Key Claims

1. 位置编码的根本作用是打破Attention的置换不变性；Causal Attention本身不具有置换不变性。
2. NoPE通过隐状态向量的方差（l2范数）编码位置——不同位置对应不同数量的value平均，方差不同。
3. NoPE实现的是乘性绝对位置编码，位置信息压缩到单标量/head——弱位置编码，长序列下位置分辨率不足。
4. NoPE缺乏远程衰减先验，大输入长度下注意力弥散。
5. Multi-Head + Multi-Layer可缓解但无法完全弥补NoPE的不足，加相对位置编码（如RoPE）仍更优。
