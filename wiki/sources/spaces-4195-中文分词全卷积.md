---
type: article_summary
title: "【中文分词系列】 6. 基于全卷积网络的中文分词"
article_id: "4195"
source_url: https://spaces.ac.cn/archives/4195
date: 2017-01-13
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-01-13-中文分词系列-6-基于全卷积网络的中文分词.md
series:
  - [[wiki/series/中文分词系列.md]]
concepts:
  - [[concept::中文分词]]
  - [[concept::全卷积网络]]
  - [[concept::字标注分词]]
methods:
  - [[method::基于全卷积网络的字标注序列建模]]
evidence_spans:
  - ev::4195::FCN分词结构
  - ev::4195::变长批训练
  - ev::4195::硬解码干预
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-01-13-中文分词系列-6-基于全卷积网络的中文分词.md
source_ids:
  - "4195"
status: draft
updated: 2026-06-11
---

# 【中文分词系列】 6. 基于全卷积网络的中文分词

本文探讨了利用一维全卷积网络（FCN）进行有监督中文分词的方法。模型不使用循环神经网络（RNN）或池化操作，保持输入输出长度一致，并在 Viterbi 解码阶段引入硬解码干预，使得深度学习网络与词典干预相结合。

## 核心内容

- **CNN 序列建模优势**：
  1. 一维卷积本质上等价于局部字级 n-gram 提取，相对于 RNN 结构在序列提取上非常自然。
  2. 卷积的权值共享反映了文本特征的“平移不变性”（如前置空格不改变后面词的判定）。
  3. CNN 的矩阵乘法结构在 GPU 加速方面显着快于 RNN/LSTM。
- **全卷积网络架构**：
  - 输入：字 ID 变长序列（填充为 Batch 内等长）。
  - Embedding 层（128维） $\to$ 一维卷积 1（核大小 3，128维，ReLU，SAME 填充） $\to$ 一维卷积 2（核大小 3，32维，ReLU，SAME 填充） $\to$ 一维卷积 3（核大小 3，4维，SAME 填充） $\to$ Softmax 激活输出四个标签（S、B、M、E）概率。
- **变长 Batch 训练优化**：
  - 在 TensorFlow 框架下，为支持句子变长训练并避免长文本截断，先将训练文本按长度排序，每个 Batch 内部使用完全等长的句子，Batch 大小取决于当前句长的变动边界。
- **硬解码干预（结合词典）**：
  - 为解决深度学习模型在专有名词、新词外推上的不足，在 Viterbi 解码求最优路径前，通过查找用户词典，将特定词段对应的 S、B、M、E 概率乘以指定倍数，干预最终路径的选择。
