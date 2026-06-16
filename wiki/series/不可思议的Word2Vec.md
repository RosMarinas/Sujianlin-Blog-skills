---
type: series
title: 不可思议的Word2Vec
aliases:
  - 【不可思议的Word2Vec】
article_ids:
  - "4299"
  - "4304"
  - "4316"
  - "4368"
  - "4402"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-04-02-不可思议的Word2Vec-1-数学原理.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-04-03-不可思议的Word2Vec-2-训练好的模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-04-07-不可思议的Word2Vec-3-提取关键词.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-05-01-不可思议的Word2Vec-4-不一样的-相似.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-05-27-不可思议的Word2Vec-5-Tensorflow版的Word2Vec.md
source_ids:
  - "4299"
  - "4304"
  - "4316"
  - "4368"
  - "4402"
series_goal: 从原理、模型、到实际应用（关键词提取、相似与相关词计算、TensorFlow自定义Softmax损失）全面且深层次地剖析与实现Word2Vec模型。
entry_roles:
  "4299": 数学原理介绍，提出两套训练方案与两套加速方案的结合
  "4304": 基于微信公众号平衡语料训练好的Gensim模型发布与演示
  "4316": 基于条件概率与贝叶斯假设，提出一种基于Word2Vec的无监督关键词提取算法
  "4368": 分析余弦相似度与互信息的区别，利用Skip-Gram模型估算点互信息PMI以寻找相关词
  "4402": 用TensorFlow实现Word2Vec，并提出随机Softmax损失(random softmax loss)并与NCE、Sampled Softmax进行对比实验
key_concepts:
  - [[Word2Vec]]
  - [[Skip-Gram]]
  - [[CBOW]]
  - [[Hierarchical Softmax]]
  - [[Negative Sampling]]
  - [[点互信息PMI]]
key_methods:
  - [[基于Word2Vec的无监督关键词提取]]
  - [[基于Word2Vec计算相关词]]
  - [[随机Softmax损失函数优化]]
reading_paths:
  - [[不可思议的Word2Vec阅读路径]]
status: draft
updated: 2026-06-14
---

# 【不可思议的Word2Vec】系列

该系列详细探讨了 Word2Vec 词向量的底层数学原理、完整模型的提取与发布、以及若干基于条件概率和层次 Softmax 的“不可思议”的实际用途。内容涵盖：

1. **数学原理**：CBOW/Skip-Gram 与 层次 Softmax/负采样的排列组合，以及对 $P(w_{others}|w_t)$ 的建模。
2. **模型发布**：发布了基于 800 万微信公众号平衡语料训练的包含 Huffman 投影参数的完整模型。
3. **关键词提取**：利用朴素贝叶斯假设将关键词定义为最大化文本条件概率 $P(s|w_i)$ 的词，并用 Huffman 树计算。
4. **相关性相似度**：区分了余弦相似度（结构可替换性）与点互信息相关度（语义相关），并通过 Skip-Gram 估计相关度。
5. **TensorFlow 实现与 Loss 创新**：使用 TensorFlow 编写底层模型，并提出随机 Softmax 损失，通过采样梯度期望降低计算瓶颈。

## 与 LLM 表示层的关系

这条线是 LLM embedding 与检索理解的前史：它先解释 Word2Vec 如何从预测任务得到词向量，再展示关键词、相关词和随机 Softmax 损失等工程落点。与 [[更别致的词向量模型]] 相比，本系列更偏“模型训练与应用”，后者更偏“互信息几何解释”。

## 阅读路径判断

这条 series 的阅读顺序应保持原始编号：先读 4299 理解 CBOW/Skip-Gram 与两类加速，再读 4304 看完整模型产物，之后读 4316/4368 两个应用分支，最后读 4402 的 TensorFlow 实现与随机 Softmax 损失。

## 与相邻 series 的分工

- 与 [[更别致的词向量模型]] 的区别：本系列更像“Word2Vec 模型如何训练和使用”，更别致系列更像“词向量内积到底在拟合什么统计量”。
- 与 [[CoSENT]] 的连接：Word2Vec 解释词级 embedding 的训练和相似性，CoSENT 解释句级 embedding 如何直接优化排序。
- 与 LLM embedding 的连接：这里的关键词提取、相关词和随机采样损失是后续 embedding 检索、负采样和相似度学习的早期工程原型。

## 搜索入口

- 查 Word2Vec 数学原理：4299。
- 查关键词提取：4316。
- 查相关词/PMI 相似：4368。
- 查随机 Softmax/NCE 对比：4402。
