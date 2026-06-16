---
type: concept
title: Unigram分词
aliases:
- Unigram Tokenization
definition: 基于Unigram语言模型的分词方法，每个子词独立概率 $p(w)$，通过Viterbi解码找到最大概率切分方案。
standard_notation: $P(\boldsymbol{w}) = p(w_1)p(w_2)\cdots p(w_k)$, $\boldsymbol{w}^*
  = \mathop{\text{argmax}}_{\boldsymbol{w}\in\Omega(S)} P(\boldsymbol{w})$
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
source_ids:
- '9768'
prerequisites:
- - - concept::Viterbi算法
- - - concept::语言模型
related_methods:
- - - method::Viterbi Sampling
status: draft
updated: '2026-06-12'
---

# Unigram分词

## 核心定义
Unigram分词模型假设每个子词独立出现，通常直接输出最大概率的切分方案。具体来说，假设 $\boldsymbol{w}=(w_1,w_2,\cdots,w_k)$ 代表一个切分方案，对应的打分为 $P(\boldsymbol{w})=p(w_1)p(w_2)\cdots p(w_k)$，$\Omega(S)$ 代表句子 $S$ 所有可能的切分方案的集合，那么分词算法可以描述为：
$$
\boldsymbol{w}^* = \mathop{\text{argmax}}_{\boldsymbol{w}\in \Omega(S)}P(\boldsymbol{w})
$$

## 关键性质与计算方法
所有切分方案 $\Omega(S)$ 构成一个有向无环图（DAG，Directed Acyclic Graph）。求解最大概率的分词方案可以通过Viterbi算法在线性时间内来完成，所以这个确定性的输出过程也被称之为“Viterbi Decoding”。

在Viterbi Decoding中，核心判据在于保留截止到当前位置的最优切分方案。如果新切分方案分数（概率对数）大于历史最优分数，则进行覆盖。

## 与其他概念/方法的关系

由于Unigram模型天然带有概率，自然可以导出随机采样的形式，用来在训练阶段引入带有随机性的分词结果，增强语言模型的容错能力：

1. **Subword Regularization**：一种已有的随机分词方案，其思路非常简单直接：先搜索出 $P(\boldsymbol{w})$ 最大的 $n$ 个分词方案 $\boldsymbol{w}^*_1,\boldsymbol{w}^*_2,\cdots,\boldsymbol{w}^*_n$（$n$-best segmentations），然后构建如下分布：
   $$
   p_i = \frac{P(\boldsymbol{w}^*_i)^{\alpha}}{\sum\limits_{j=1}^n P(\boldsymbol{w}^*_j)^{\alpha}}
   $$
   对这 $n$ 个方案进行依概率采样，其中 $\alpha > 0$ 是一个超参数。尽管搜索的理论复杂度也是线性的，但明显比只找 top1 的 Viterbi Decoding 要大很多（理论上是 $n$ 倍复杂度），导致开启随机采样后速度显著下降。

2. **Viterbi Sampling**：一种更高效的随机采样方案。在Viterbi解码的基础上引入基于 Sigmoid 函数的二元接受率，将确定性的条件判断变为依概率的随机采样。这使得最大概率切分依然大概率被采出，在近似保持切分方案排序的同时，实现在线性时间内的轻量级随机分词，速度远优于标准的 Subword Regularization。

## 具体实例
- **BytePiece**：基于Unigram模型，通过Viterbi算法寻找最大概率的分词方案，并且在其最新版本内置了基于 Viterbi Sampling 的随机分词功能。
- **SentencePiece**：内部实现了标准的 Subword Regularization 算法，支持对 $n$-best 方案进行采样。
