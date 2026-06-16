---
type: concept
title: CBOW
aliases:
- Continuous Bag-of-Words
definition: Word2Vec中的一种训练架构，通过周围上下文词的叠加表示来预测当前中心词的条件概率分布。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-04-02-不可思议的Word2Vec-1-数学原理.md
source_ids:
- '4299'
prerequisites:
- '[[Word2Vec]]'
evidence_spans:
- ev::4299::训练提速
status: stable
updated: '2026-06-12'
---

# CBOW

CBOW (Continuous Bag-of-Words) 是 Word2Vec 的核心训练方案之一。其基本思想是“周围词叠加起来预测当前词”，即利用上下文词向量之和（或平均）来预测中心词。

## 特点
由于将上下文的表示进行了叠加（Bag-of-Words 属性），CBOW 忽略了上下文词汇的顺序信息。CBOW 相比 Skip-Gram 训练速度更快，但在低频词表示上略逊一筹。