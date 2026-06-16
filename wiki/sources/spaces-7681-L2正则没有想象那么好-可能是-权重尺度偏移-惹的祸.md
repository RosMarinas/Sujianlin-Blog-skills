---
type: article_summary
title: "L2正则没有想象那么好？可能是"权重尺度偏移"惹的祸"
article_id: "7681"
source_url: https://spaces.ac.cn/archives/7681
date: 2020-08-14
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-08-14-L2正则没有想象那么好-可能是-权重尺度偏移-惹的祸.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[权重尺度偏移不变性]]"
  - "[[WEISSI正则]]"
  - "[[AdamW优化器]]"
evidence_spans:
  - "ev::7681::L2正则理解"
  - "ev::7681::AdamW不等价"
  - "ev::7681::权重尺度偏移"
  - "ev::7681::WEISSI推导"
  - "ev::7681::WEISSI正则形式"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-14-L2正则没有想象那么好-可能是-权重尺度偏移-惹的祸.md
source_ids:
  - "7681"
status: draft
updated: 2026-06-12
---

# L2正则没有想象那么好？可能是"权重尺度偏移"惹的祸

## Summary

本文指出神经网络的正齐次性（ReLU等激活函数）导致模型对权重尺度偏移具有不变性，但L2正则对尺度偏移敏感，导致L2正则降低却不提升泛化性能。提出了WEISSI正则（log范数）来解决这一不协调问题。

## Key Claims

1. 模型对∏γ_l=1的权重尺度偏移具有不变性（正齐次性使然）。
2. L2正则∑∥W_l∥²对尺度偏移敏感，因此存在一组等价模型具有更小L2但无泛化提升。
3. WEISSI正则∑log∥W_l∥₂的梯度对尺度偏移不变，解决了不协调问题。

## Key Formulas

- 正齐次性: εφ(x) = φ(εx)对ReLU及光滑近似成立
- WEISSI正则: L_reg = λ₁∑log∥W_l∥₂ + λ₂∑∥W_l/∥W_l∥₂∥₁
- L2正则下最优尺度偏移: ∥W̃_l∥ = (∏∥W_l∥)^{1/L}

## Connections

本文的AdamW讨论与6869中LazyOptimizer同为优化器的改进方向。权重尺度偏移概念与8747中BERT初始化标准差的选择（控制前向传播方差尺度）有相似的分析方法。
