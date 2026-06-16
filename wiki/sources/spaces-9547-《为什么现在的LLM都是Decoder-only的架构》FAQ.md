---
type: article_summary
title: 《为什么现在的LLM都是Decoder-only的架构？》FAQ
article_id: 9547
source_url: https://spaces.ac.cn/archives/9547
date: 2023-03-20
category: Big-Data
source_markdown: |
  Data/Spaces_ac_cn/markdown/Big-Data/2023-03-20-为什么现在的LLM都是Decoder-only的架构-FAQ.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-20-为什么现在的LLM都是Decoder-only的架构-FAQ.md
source_ids:
  - 9547
status: draft
updated: 2026-06-12
---

# 《为什么现在的LLM都是Decoder-only的架构？》FAQ

本文是针对前作《为什么现在的LLM都是Decoder-only的架构？》一文发布后读者的反馈和疑问进行的集中解答。
主要问题包括：
1. $n \gg d$ 在实际LLM中是否成立：作者解释在多头注意力中 $d$ 是head_size而不是hidden_size，因此预训练长度 $n$ 远大于 $d$ 大致上是成立的。
2. 相比GPT，BERT在理解任务上更好的原因：BERT和GPT的预训练任务不同，无法进行公平比较。
3. 双向注意力的局限性波及范围：作者澄清其结论仅适用于“在生成任务上的Encoder引入双向注意力不会带来收益”，并不表示双向注意力在所有任务上都糟糕。
4. 与T5和UL2结论是否矛盾：指出UL2中两者参数量不同，而T5的实验流程（包含微调阶段）与本文直接对比预训练Loss的流程不同，可能导致差异。
5. 三角注意力掩码（Causal Mask）对位置编码的影响：三角形掩码不仅带来秩的提升，还打破了Transformer的置换不变性，直接引入了序的关系，能够更好地处理位置编码信息。