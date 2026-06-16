---
type: example
title: Softmax近似Argmax
article_id: "6620"
article: "article::函数光滑化杂谈：不可导函数的可导逼近"
section: argmax
claim: argmax算子的光滑近似可以通过softmax加权求和实现。
notation_mapping:
  - "$\boldsymbol{x} = [x_1,\dots,x_n]$": 输入向量
  - "$i$": 下标索引（从1开始）
steps:
  - "将argmax表达为序向量与onehot向量的内积：$\text{argmax}(\boldsymbol{x}) = \sum_{i=1}^n i \times \text{onehot}(\text{argmax}(\boldsymbol{x}))_i$"
  - "将onehot向量替换为softmax概率分布：$\text{argmax}(\boldsymbol{x}) \approx \sum_{i=1}^n i \times \text{softmax}(\boldsymbol{x})_i$"
  - "结果是一个接近真实下标的浮点数，可导且梯度良好"
used_concepts:
  - "concept::函数光滑化"
used_formulas:
  - "formula::SoftMax作为onehot_argmax的光滑近似"
used_methods: []
problem_pattern: "problem_pattern::非光滑函数可导化"
source_span: ev::6620::argmax
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-05-20-函数光滑化杂谈-不可导函数的可导逼近.md
source_ids:
  - "6620"
status: draft
updated: 2026-06-12
---

## 示例说明

该示例展示了如何将离散的 $\text{argmax}$ 算子转化为可导的近似。输入向量 $[2,1,4,5,3]$ 的 argmax 为4（下标从1开始），其光滑近似通过 softmax 加权序向量得到：$\sum_{i=1}^5 i \times \text{softmax}([2,1,4,5,3])_i \approx 4$。这一近似在神经网络中广泛用于需要离散输出的可导化场景，如注意力机制中的硬注意力。
