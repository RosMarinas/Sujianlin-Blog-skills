---
type: article_summary
title: "输入梯度惩罚与参数梯度惩罚的一个不等式"
article_id: "8796"
source_url: https://spaces.ac.cn/archives/8796
date: 2021-12-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-12-11-输入梯度惩罚与参数梯度惩罚的一个不等式.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[输入梯度惩罚]]"
  - "[[参数梯度惩罚]]"
  - "[[梯度惩罚不等式]]"
evidence_spans:
  - "ev::8796::不等式最终形式"
  - "ev::8796::不等式推导"
  - "ev::8796::推导过程分量形式"
  - "ev::8796::原论文解读批评"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-12-11-输入梯度惩罚与参数梯度惩罚的一个不等式.md
source_ids:
  - "8796"
status: draft
updated: 2026-06-12
---

# 输入梯度惩罚与参数梯度惩罚的一个不等式

## Summary

本文介绍并证明了输入梯度惩罚∥∇_x f∥²与参数梯度惩罚∥∇_θ f∥²之间的一个不等式，指出参数梯度惩罚隐式包含输入梯度惩罚，从而SGD的隐式梯度正则化会倾向于选择复杂度更小的模型。

## Key Claims

1. 对l层MLP，成立不等式: ∥∇_x f∥²(∑(1+∥h^(t)∥²)/(∥W^(t)∥²∥∇_x h^(t)∥²)) ≤ ∥∇_θ f∥²。
2. 证明通过对每个参数层分别证明不等式再求和完成，核心是矩阵求导的分量形式推导。
3. SGD的隐式梯度正则化（对参数的梯度惩罚）通过此不等式传递为对输入的梯度惩罚，进而控制模型复杂度（Dirichlet能量）。
4. 原论文称初始化时∥W^(t)∥接近于0是错误的，实际正交初始化下谱范数为1。

## Key Formulas

- 最终不等式: ∥∇_x f∥²·∑((1+∥h^(t)∥²)/(∥W^(t)∥²∥∇_x h^(t)∥²)) ≤ ∥∇_θ f∥²
- 对单层权重的不等式: ∥∇_x f∥²(∥h^(t)∥²/(∥W^(t)∥²∥∇_x h^(t)∥²)) ≤ ∥∇_{W^(t)} f∥²

## Connections

本文的输入梯度惩罚与7234中对抗训练等价于梯度惩罚的结果直接相关。参数梯度惩罚则与7469中梯度裁剪（控制梯度大小）和8634优化器设计都涉及对梯度大小的控制。
