---
type: concept
title: 字词混合Embedding
aliases:
  - word-character hybrid embedding
  - 混合Embedding
definition: 一种将字级别表示的灵活性与预训练词向量的语义丰富性结合的位置对齐式特征表征方法。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-06-03-基于DGCNN和概率图的轻量级信息抽取模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-08-20-开源一版DGCNN阅读理解问答模型-Keras版.md
source_ids:
  - "6671"
  - "6906"
evidence_spans:
  - ev::6671::字词混合
status: stable
updated: 2026-06-12
---

# 字词混合Embedding

在中文NLP任务中，若完全以词为输入单位，容易受到分词工具切分边界错误的影响；而若完全以字为输入单位，单个字往往缺乏足够的先验语义特征。字词混合Embedding设计了一种对齐融合方案。

首先，对输入语句进行分词，并通过预训练的Word2Vec等词向量模型提取出各个词对应的向量表示。为了实现字词序列长度的对齐，将每一个词的词向量沿词长度维度进行重复复制，使其与问句中字的位置相匹配。接着，将对齐后的词向量序列经过一个线性投影层变换到与字向量相同的维度，然后与随机初始化的字Embedding向量直接相加。在网络训练过程中，冻结Word2Vec词向量，只对投影矩阵和字Embedding进行更新，从而保留了先验语义并赋予字特征极高的微调灵活性。
