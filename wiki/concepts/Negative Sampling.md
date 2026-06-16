---
type: concept
title: Negative Sampling
aliases:
- 负样本采样
- 负采样
definition: Word2Vec中的一种近似训练手段，通过将多分类Softmax转化为输入与输出的联合概率二分类打分，并随机抽取若干负样本进行计算。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-04-02-不可思议的Word2Vec-1-数学原理.md
source_ids:
- '4299'
prerequisites:
- '[[Softmax]]'
evidence_spans:
- ev::4299::训练提速
status: stable
updated: '2026-06-12'
---

# Negative Sampling

Negative Sampling (负采样) 是替代 Hierarchical Softmax 的另一种经典加速手段。

## 核心机制
它将原先估计条件概率的庞大 Softmax 输出层，简化为判断一对词是否在真实语料中共同出现的二分类（对逻辑回归建模）。对于每个训练样本，仅需更新对应的正样本和随机抽取的若干负样本的权重，从而将单步更新复杂度从 $\mathcal{O}(|V|)$ 降低至 $\mathcal{O}(N_{neg})$。