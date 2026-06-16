---
type: method
title: "Keras版Word2Vec实现"
aliases:
  - "Keras Word2Vec"
operation_types:
  primary: "Rewrite / identity transform"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-08-06-不可思议的Word2Vec-6-Keras版的Word2Vec.md
source_ids:
  - "4515"
method_summary: "在Keras中使用Embedding层和Lambda层实现CBOW+负采样的Word2Vec训练框架。"
typical_structure: |
  1. Embedding词表映射
  2. Lambda层取上下文均值
  3. Dense层做负采样二分类
applicability: "词向量训练，NLP基础词表示学习"
tools:
  - 负采样
  - 降采样
related_methods: []
examples:
  - [[article::4515]]
status: draft
updated: 2026-06-13
---

## 适用问题

在Keras框架中训练词向量（Word Embedding），为NLP任务提供预训练的词语分布式表示。

## 核心变换

**输入**：语料中的词语序列（已分词）
**输出**：每个词的128维向量表示

使用CBOW（Continuous Bag-of-Words）架构：用上下文词向量均值预测目标词。配合负采样（Negative Sampling）将多分类softmax简化为二分类。

## 典型步骤

1. **统计词频**：遍历语料构建词频表，剔除频数低于`min_count`（默认10）的低频词
2. **降采样**：对高频词（词频>$subsample\_t=1e-5$）按概率$P(\text{丢弃}) = 1 - \sqrt{t/f(w)}$进行降采样，加速训练并提升词向量质量
3. **构建CBOW样本**：取上下文窗口（默认5）内词的Embedding向量，用Lambda层求和取均值
4. **负采样**：目标词+16个随机负样本组成二分类任务，使用Dense层进行判别
5. **训练**：Adam优化器迭代1-2轮即可获得高质量词向量

## 直觉

CBOW的核心假设：一个词的含义可以由其上下文词的组合来推断。通过训练模型用上下文预测目标词，词向量被迫编码上下文的共现统计信息。

负采样将原本需要softmax遍历整个词表的巨大计算量（$O(|V|)$），简化为对目标词和少量负样本的二分类（$O(k)$，$k=16$），训练效率大幅提升。这与Word2Vec原始实现一致。

降采样抑制了"的"、"了"等高频无意义词对训练的主导，让模型更多关注有语义含量的词语。

## 边界

- 纯CBOW架构，未实现Skip-gram（但可等价替换）
- 依赖外部分词，词向量质量受分词准确度影响
- 使用MongoDB数据源，需适配自己的语料格式
- 上下文窗口大小（默认5）需根据语料特点调整
- Keras 2.0.6+，兼容tensorflow/theano/cntk后端

## 例子

- 词嵌入维度128，窗口5，负采样16，min_count=10，subsample_t=1e-5
- 数据生成器以句子为单位分批处理，每批20句，随机采样上下文-目标对
- 加载"word2vec"命名Embedding层的权重即可获取预训练词向量

## 证据

- ev::4515::CBOW+负采样Keras实现：Embedding层词表映射、Lambda层上下文均值、Dense层二分类的完整框架
- ev::4515::降采样公式：$P(\text{丢弃}) = subsample\_t/j + (subsample\_t/j)^{0.5}$（来自Word2Vec源码）
- ev::4515::代码参数：word_size=128, window=5, nb_negative=16, min_count=10, subsample_t=1e-5
