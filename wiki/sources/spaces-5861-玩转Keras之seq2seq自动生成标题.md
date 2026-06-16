---
type: article_summary
title: 玩转Keras之seq2seq自动生成标题
article_id: "5861"
source_url: https://spaces.ac.cn/archives/5861
date: 2018-09-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-09-01-玩转Keras之seq2seq自动生成标题.md
source_html: Data/Spaces_ac_cn/raw/articles/5861/page.html
series: []
topics:
  - "[[topic::Seq2Seq]]"
concepts:
  - "[[concept::Seq2Seq]]"
  - "[[concept::Beam Search]]"
  - "[[concept::Teacher Forcing]]"
methods:
  - "[[method::用Seq2Seq+Attention生成标题]]"
problem_patterns: []
evidence_spans:
  - ev::5861::基本结构
  - ev::5861::beam_search
  - ev::5861::Attention
  - ev::5861::先验知识
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-09-01-玩转Keras之seq2seq自动生成标题.md
source_ids:
  - "5861"
status: draft
updated: 2026-06-11
---

## 文章核心问题

如何使用Keras实现seq2seq模型，自动根据新闻文章内容生成标题？

## 主要结论

1. Seq2seq的基本结构：encoder将输入编码为固定向量，decoder递归解码，训练采用Teacher Forcing策略。
2. Attention是seq2seq标配模块，使解码器每一步可以回顾原文局部信息。
3. Beam Search在每步保留top_k个最优候选，是贪心搜索和全局最优的折中方案。
4. 引入文章词集的0/1向量作为先验分布，有助于加快收敛、生成更稳定的标题。
5. 基于80万篇新闻语料训练的双层双向LSTM encoder + 双层单向LSTM decoder模型可生成可读标题。

## 推导结构

seq2seq简介（基本结构、训练过程、beam search）→ seq2seq提升（Attention、先验知识引入）→ Keras参考（基本实现、mask、解码端）。

## 关键公式

- seq2seq概率建模：p(Y|X)=p(Y_1|X)p(Y_2|X,Y_1)...p(Y_T|X,Y_1,...,Y_{T-1})
- 先验分布融合：y_hat = s⊗χ + t, y_new = (y+y_hat)/2
- 概率输出：p_i = e^{y_i}/Σ e^{y_i}

## 体现的方法

- **用Seq2Seq+Attention生成标题**：使用双向LSTM encoder和单向LSTM decoder，配合Attention机制和文章词集先验分布，实现seq2seq标题自动生成。

## 所属系列位置

独立文章。

## 与其他文章的关系

- 与[[article::7124]]同属文本生成领域（本文为无条件/基于内容的生成，7124为条件生成）。
- 与[[article::5743]]的GRU编码器可复用——本文的双向LSTM encoder与GRU encoder结构相似。
- 与[[concept::Conditional Layer Normalization]]的关联：可在decoder中结合CLN实现带条件的标题生成。

## 原文证据锚点

- `ev::5861::基本结构`：Seq2seq的encoder-decoder结构和Teacher Forcing训练。
- `ev::5861::beam_search`：Beam Search解码算法的原理。
- `ev::5861::Attention`：Attention使解码器回顾原文局部信息。
- `ev::5861::先验知识`：文章词集先验分布的引入方法。
