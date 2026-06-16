---
type: formula
title: 基于点互信息PMI的相关词度量
aliases: []
latex: \text{Score}(y|x) = \log P(y|x) - \alpha \log P(y)
symbol_meanings:
  x: 输入的中心词
  y: 候选的相关词
  P(y|x): 在给定 x 情况下 y 的条件概率，由 Word2Vec 模型估计
  P(y): 词 y 在语料中的边际概率
  \alpha: 频次调节参数，略小于 1 (常用 0.9) 以给高频词更高权重
standard_notation: Score(y|x)
conditions: 使用 Skip-Gram 结合 Hierarchical Softmax 模型进行转移概率的估计
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-05-01-不可思议的Word2Vec-4-不一样的-相似.md
source_ids:
- '4368'
appears_in:
- '[[spaces-4368-不可思议的Word2Vec-4-不一样的-相似]]'
evidence_spans:
- ev::4368::互信息定义
status: draft
updated: '2026-06-14'
---

# 基于点互信息PMI的相关词度量

## 概述

该公式用于估计给定词（中心词 $x$）与候选词（相关词 $y$）之间的语义相关程度。在 Word2Vec 的常规应用中，通常使用余弦相似度（Cosine Similarity）来寻找相似词。余弦相似度由于排除了向量模长的影响，主要描述的是词语上下文分布的“相对一致性”或“结构上的可替换性”（例如，在多数句式结构中“广州”可以直接被“深圳”或“东莞”替换）。然而，这种可替换性无法直接体现词汇在实际场景中的内在组合关联。

为了挖掘诸如“广州”与“白云机场”、“白云山”这类在句法上不能互相替换，但在实际语境中经常共同出现的本地强关联词，需要引入互信息（Mutual Information）作为度量标准。互信息的数学定义为 $\log \frac{p(x,y)}{p(x)p(y)} = \log p(y|x) - \log p(y)$。互信息得分越大，说明 $x$ 和 $y$ 经常搭配一起出现，其共现概率远超它们各自独立出现的概率乘积。

在具体的 Word2Vec 模型实现中，该相关度评分的计算可以拆解为两个主要部分：
1. **条件概率估计 $\log P(y|x)$**：这一项可以完全由 Word2Vec 中的 Skip-Gram 结合 Hierarchical Softmax（Huffman Softmax）模型给出。计算时，提取中心词的词向量以及候选词在 Huffman 树中对应路径的内部节点向量，计算内积并汇总 Softmax 路径上的对数概率（Log-Likelihood）。
2. **边缘概率惩罚 $-\alpha \log P(y)$**：公式中的这一项用于消除语料中高频词带来的优势（在代码实现中常体现为减去该词频次的对数，即 `-np.log(word.count)`）。如果只看条件概率，系统极易召回类似于“的”、“是”等极高频但缺乏实际语义关联的停用词。通过引入衰减系数 $\alpha$，可以适度微调对高低频词的惩罚权重，从而精准提取出最具代表性的高相关实体词。
