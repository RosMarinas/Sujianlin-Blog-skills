---
type: article_summary
title: 【不可思议的Word2Vec】 3.提取关键词
article_id: "4316"
source_url: https://spaces.ac.cn/archives/4316
date: 2017-04-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-04-07-不可思议的Word2Vec-3-提取关键词.md
series:
  - [[不可思议的Word2Vec]]
concepts:
  - [[Word2Vec]]
  - [[Skip-Gram]]
  - [[Hierarchical Softmax]]
methods:
  - [[基于Word2Vec的无监督关键词提取]]
formulas:
  - [[基于点互信息PMI的相关词度量]]
examples:
  - [[spaces-4316-恒星关键词提取]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-04-07-不可思议的Word2Vec-3-提取关键词.md
source_ids:
  - "4316"
status: draft
updated: 2026-06-11
---

# 【不可思议的Word2Vec】 3.提取关键词

## 内容概要
文章从条件概率的数学视角重新定义了文本关键词，并利用 Word2Vec (Skip-Gram + Huffman Softmax) 模型给出了一种无监督、初步蕴含语义理解的关键词提取方案。

## 关键内容
1. **关键词的条件概率定义**：关键词 $w_i$ 应该是最能让人“猜到”其所在文本/句子 $s$ 的词语，即最大化条件概率 $P(s|w_i)$。
2. **朴素贝叶斯假设化简**：
   $$P(s|w_i) = P(w_1, w_2, \dots, w_n | w_i) \approx \prod_{k=1}^n P(w_k | w_i)$$
   在对数空间中计算词语对的转移对数概率和：
   $$\log P(s|w_i) = \sum_{k=1}^n \log P(w_k | w_i)$$
3. **基于 Huffman Softmax 的条件概率计算**：利用 Gensim 中 Huffman 树结构与输入词向量，通过计算沿路径分支决策概率对数，推导出基于向量内积的转移概率公式。
4. **方法特性**：
   - 相比 TF-IDF（一元模型，仅考虑词自身信息量），该方法是二元模型，考虑了词与上下文词的关联。
   - 具有神经网络的平滑能力，即使两个词在文章中没有共现，也能赋予合理概率。
   - 计算复杂度为 $\mathcal{O}(N^2)$（$N$ 为句子词数），慢于 TF-IDF 的 $\mathcal{O}(N)$。
