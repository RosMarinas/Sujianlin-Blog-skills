---
type: concept
title: Skip-Gram
aliases: []
definition: Word2Vec中的一种训练架构，通过当前中心词预测周围上下文词的条件概率分布。
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

# Skip-Gram

Skip-Gram 是 Word2Vec 的两种核心训练方案之一。其基本思想是“当前词分别来预测周围词”，即给定中心词 $w_t$，预测其上下文窗口内的词 $w_{t+j}$。

## 数学表达
对于给定的序列 $w_1, w_2, \dots, w_T$，Skip-Gram 的目标是最大化平均对数条件概率：
$$\mathcal{L} = \frac{1}{T}\sum_{t=1}^T \sum_{-c \le j \le c, j \ne 0} \log P(w_{t+j} | w_t)$$
其中 $c$ 为上下文窗口的大小。