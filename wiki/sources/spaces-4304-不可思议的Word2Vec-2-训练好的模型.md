---
type: article_summary
title: 【不可思议的Word2Vec】 2.训练好的模型
article_id: "4304"
source_url: https://spaces.ac.cn/archives/4304
date: 2017-04-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-04-03-不可思议的Word2Vec-2-训练好的模型.md
series:
  - [[不可思议的Word2Vec]]
concepts:
  - [[Word2Vec]]
  - [[Skip-Gram]]
  - [[Hierarchical Softmax]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-04-03-不可思议的Word2Vec-2-训练好的模型.md
source_ids:
  - "4304"
status: draft
updated: 2026-06-11
---

# 【不可思议的Word2Vec】 2.训练好的模型

## 内容概要
文章发布并介绍了一个由作者训练完成的中文平衡语料 Word2Vec 完整模型。该模型基于 800 万篇微信公众号文章（包含约 650 亿词）训练而成，使用了 Python 的 Gensim 库，采用 Skip-Gram + Huffman Softmax（层次 Softmax）架构，保留了包含 Huffman 树参数在内的完整模型结构，以便在后文中提取节点条件概率。

## 关键内容
1. **完整模型保留**：为了支持后续的条件概率计算，必须保存包含 Huffman 树投影层参数的完整模型，而不仅仅是词向量。目前只有 Gensim 库支持该操作。
2. **语料与模型规格**：
   - 语料来源：微信公众号多领域文章，去重后 800 万篇。
   - 词表大小：352,196 词，采用结巴分词（使用自备的 50 万词典并关闭新词发现）。
   - 参数设置：维度 256 维，窗口大小 10，最小词频 64，迭代次数 10 次。
3. **效果演示**：演示了微信、公众号、微积分、爸爸、足球等词的 most_similar 近义词召回，结果反映了高度的可读性与现代网络流行内容特征。
