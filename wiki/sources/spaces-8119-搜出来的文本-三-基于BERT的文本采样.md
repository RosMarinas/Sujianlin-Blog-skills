---
type: article_summary
title: "【搜出来的文本】⋅（三）基于BERT的文本采样"
article_id: "8119"
source_url: https://spaces.ac.cn/archives/8119
date: 2021-01-22
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-01-22-搜出来的文本-三-基于BERT的文本采样.md
series: [搜出来的文本]
topics: [BERT, Gibbs采样, 文本采样]
concepts: [MLM+Gibbs采样, BERT马尔可夫随机场争议]
methods: [BERT MLM Gibbs采样]
problem_patterns: []
evidence_spans:
  - 8119-采样流程
  - 8119-参考代码
  - 8119-吃瓜思考
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-01-22-搜出来的文本-三-基于BERT的文本采样.md
source_ids:
  - "8119"
status: draft
updated: 2026-06-10
---

## 文章核心问题

BERT这样的双向掩码语言模型能否用于文本随机采样？如何实现？

## 主要结论

1. 将BERT的MLM模型与Gibbs采样结合即可实现文本随机采样——MLM预测条件概率p(y|x_{-i})正是Gibbs采样所需。
2. 采样流程：初始句子→随机选择位置i→Mask该位置→MLM预测概率分布→采样新token→替换。
3. 只能采样固定长度句子（Gibbs采样不改变序列长度），但可通过全部[MASK]初始化来获得不同长度的句子。
4. 原论文声称MLM模型是Markov Random Field，但这被证明是错误的，不影响BERT用于Gibbs采样的事实，但改变了理论解释。
5. 实验表明基于MLM的Gibbs采样可以生成可读的多样化文本，但也暴露出预训练语料的隐私问题。

## 推导结构

- Gibbs采样回顾 → MLM模型的对应关系
- MLM+Gibbs采样流程
- 实验效果与代码
- MLM vs MRF争议澄清
