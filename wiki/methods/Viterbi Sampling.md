---

type: method
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
title: Viterbi Sampling
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-10-无监督分词和句法分析-原来BERT还可以这样用.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-13-大词表语言模型在续写任务上的一个问题及对策.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
source_ids:
  - 9768
method_summary: 将确定性Viterbi解码的硬判据替换为Sigmoid随机化判据，实现Unigram分词的轻量级随机采样
typical_structure: |
  1. 在基于有向无环图的序列解码过程中，按序遍历节点及其可能的前驱状态
  2. 评估当前到达某节点的新切分路径得分 $s_i$ 与历史最优得分 $s_{i-1}$
  3. 将确定性的严格大小比较判据替换为随机判据：以概率 $P = \sigma(\alpha(s_i - s_{i-1}))$ 决定是否接受新方案
  4. 最终回溯生成一条随机采样的解码路径
applicability: Unigram模型的分词随机化、Subword Regularization、增强语言模型泛化能力，适用于需要快速生成多样化合理切分结果的序列解码任务。
tools: 
related_methods: 
examples:
  - [[article::9768]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::9768::相比SentencePiece的Subword Regularization（N-best采样），Viterbi Sampling仅在Viterbi解码基础上替换了比较判据，成为极其轻量级的随机采样算法，且能够保持最大概率切分不变
  - ev::9768::复杂度下降与自然兼容：原文分析指出 Viterbi Sampling 是对 Viterbi 解码的极小修改，使得复杂度仍保持为与确定性解码同一量级。
---

## 适用问题

在语言模型训练或文本增强中，为了提升模型对词表切分边界的鲁棒性和泛化能力（如 Subword Regularization），需要对确定性最优分词引入随机扰动，但传统的基于 N-best 的采样方法计算复杂度高（大幅降低分词速度），需要一种保持线形时间复杂度且轻量级的随机分词算法。

## 核心变换

将 Viterbi 算法更新历史最优得分时的确定性硬判据（大小比较）变换为基于 Sigmoid 函数的软判据（随机接受）。
$$
r_i = \left\{\begin{aligned}&\,1\,, \,\, \varepsilon < \sigma(\alpha(s_i - s_{i-1})) \\ &\,0\,, \,\, \text{else}\end{aligned}\right.
$$
其中 $s_i$ 是新方案得分，$s_{i-1}$ 是当前记录的最优得分，$\varepsilon \sim U[0,1]$ 为均匀随机数，$\alpha > 0$ 为控制随机程度的温度超参数。

## 典型步骤

1. 构建文本所有可能切分方案的有向无环图（DAG），并初始化各位置的最优得分和回溯指针。
2. 按序遍历文本位置，枚举当前位置所有匹配的词缀，计算到达当前位置的新候选切分得分 $s_i$。
3. 比较新候选得分 $s_i$ 与已记录的得分 $s_{i-1}$，计算接受概率 $\sigma(\alpha(s_i - s_{i-1}))$ 并生成随机数判定是否接受。若接受，则更新该位置的记录得分与回溯指针。
4. 遍历完成后，从末端根据回溯指针生成最终的分词路径。

## 直觉

Viterbi解码通过每次比较保留局部最优，本质上是一个贪心覆盖的过程。通过将“新方案如果更好就一定替换”改为“新方案如果更好就有较大概率替换，即便差一点也有小概率替换”，这就引入了像 MCMC（马尔可夫链蒙特卡洛）中 Metropolis-Hastings 算法那样的随机游走机制。由于 Sigmoid 的单调递增性，原来最优的方案依然对应最大被采样到的概率，自然继承了原路径优劣的排序。

## 边界

- **不严格保序**：由于更新过程中带有马尔可夫性质的随机覆盖，这种采样未被严格证明在全局分布上完美匹配 N-best 的概率分布，更多是作为一种高效的近似。
- **温度参数依赖**：超参数 $\alpha$ 需要精心调节，当 $\alpha \to \infty$ 时退化为标准 Viterbi，当 $\alpha \to 0$ 时则变为完全随机游走，可能产生大量不合理的碎片切分。

## 例子

- **BytePiece随机分词**：在 BytePiece 库中内置了该算法，仅需将内部的 `if score > routes[e][0]` 判定改为基于带有 $\alpha$ 的随机条件，使得在速度仅下降约 30% 的情况下实现了随机分词。

## 证据

- **ev::9768::复杂度下降与自然兼容**：原文分析指出 Viterbi Sampling 是对 Viterbi 解码的极小修改，使得复杂度仍保持为与确定性解码同一量级。
