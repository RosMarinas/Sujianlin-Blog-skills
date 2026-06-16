---
type: concept
title: Viterbi算法
aliases:
- Viterbi Decoding
definition: 在有向无环图上寻找最大概率路径的动态规划算法，用于Unigram分词的解码。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
source_ids:
- '9768'
related_methods:
- - - method::Viterbi Sampling
status: draft
updated: '2026-06-12'
---

# Viterbi算法

Viterbi算法（在分词中常被称为 Viterbi Decoding）是一种在有向无环图（DAG）上以线性复杂度寻找最大概率路径的动态规划算法。在自然语言处理的Unigram分词模型中，它被广泛用于寻找全局最优的确定性分词方案。

## 数学定义

在Unigram分词模型中，假设 $\boldsymbol{w}=(w_1,w_2,\cdots,w_k)$ 代表一个切分方案，对应的打分为各个子词概率的乘积：$P(\boldsymbol{w})=p(w_1)p(w_2)\cdots p(w_k)$。设 $\Omega(S)$ 代表句子 $S$ 所有可能的切分方案的集合，所有切分方案 $\Omega(S)$ 构成一个有向无环图（DAG）。Viterbi算法的核心目标可描述为求解：
$$
\boldsymbol{w}^* = \mathop{\text{argmax}}_{\boldsymbol{w}\in \Omega(S)}P(\boldsymbol{w})
$$
这可以通过Viterbi算法在线性时间内来完成，有效避免了对 $\Omega(S)$ 指数级空间的暴力穷举。

## 核心实现与性质

在典型的分词实现（如BytePiece）中，算法的核心在于遍历文本并不断更新到达每一个字（节点）的历史最优解。其状态转移的关键代码逻辑如下：
```python
score = routes[s][0] + v
if score > routes[e][0]:
    routes[e] = score, s
```
在这里，`if score > routes[e][0]:` 这一句是Viterbi Decoding的关键，它代表保留截止到当前位置的最优切分方案。其中 `score` 是新切分方案分数（概率对数），`routes[e][0]` 是历史最优分数，如果新方案的概率对数总和更优，则直接覆盖历史状态。

## 关联概念

- **Viterbi Sampling**：传统的 Viterbi Decoding 总是直接输出最大概率的切分方案，是一个确定性的输出。如果将上述核心判据 `if score > routes[e][0]:` 替换为基于新旧方案得分差值的 Sigmoid 函数 $\sigma(\alpha(s_i - s_{i-1}))$ 进行随机判定（类似 MCMC 算法的接受率设计），就可以得到效率接近 Viterbi Decoding 且能保持近似保序性质的随机分词算法 **Viterbi Sampling**。
- **Subword Regularization**：在机器翻译等任务中，为了增强模型的容错能力，需要引入带有随机性的分词结果。直接对 N-best Viterbi 进行按概率分布采样的原始 Subword Regularization 算法复杂度较高，而基于 Viterbi 算法改造的 Viterbi Sampling 是其更高效的平替方案。
