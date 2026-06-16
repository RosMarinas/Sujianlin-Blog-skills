---
type: proposition
title: Word2Vec层次Softmax中的条件概率计算公式
aliases: []
statement: 在 Word2Vec 的 Skip-Gram 模型中，采用层次 Softmax 近似时，给定输入词 w_i 时预测输出词 w_k 的对数条件概率可以表示为在 Huffman 树路径上所有分叉节点的二分类概率对数之和：\log P(w_k | w_i) = -\sum_{node \in \text{Path}(w_k)} \log(1 + e^{-(-1)^d \boldsymbol{x}_{w_i}^\top \boldsymbol{\theta}_{node}})
assumptions: ["使用 Skip-Gram 架构", "采用 Huffman 二叉树进行分叉概率的近似表示"]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-04-07-不可思议的Word2Vec-3-提取关键词.md
source_ids:
  - '4316'
proof_route: |
  1. 将预测输出词 $w_k$ 的多分类问题转化为在其对应的 Huffman 树路径上沿各分支做二分类决策的过程。
  2. 在路径上的每个分叉节点，将输入词向量 $\boldsymbol{x}_{w_i}$ 与该节点的权重向量 $\boldsymbol{\theta}_{node}$ 做内积，经过 Sigmoid 激活得到向左或向右分叉的概率。
  3. 根据 Huffman 编码 $d \in \{0, 1\}$ 表示的实际走向，化简概率对数表达式得到单节点概率为 $-\log(1+e^{-(-1)^d \boldsymbol{x}_{w_i}^\top \boldsymbol{\theta}_{node}})$。
  4. 将整个路径上所有节点的条件对数概率相加，即得到 $\log P(w_k | w_i)$。
evidence_spans: ["ev::4316::数学定义"]
status: draft
updated: 2026-06-11
---

# Word2Vec层次Softmax中的条件概率计算公式

该命题建立了 Skip-Gram 词嵌入表示与层次 Softmax 二叉决策树的概率桥梁。
