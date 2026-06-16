---
type: article_summary
title: "为什么梯度裁剪能加速训练过程？一个简明的分析"
article_id: "7469"
source_url: https://spaces.ac.cn/archives/7469
date: 2020-06-05
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-06-05-为什么梯度裁剪能加速训练过程-一个简明的分析.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[梯度裁剪]]"
  - "[[(L0,L1)-光滑性]]"
  - "[[L-smooth条件]]"
evidence_spans:
  - "ev::7469::梯度裁剪形式"
  - "ev::7469::L约束推导"
  - "ev::7469::(L0,L1)约束"
  - "ev::7469::最优学习率"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-06-05-为什么梯度裁剪能加速训练过程-一个简明的分析.md
source_ids:
  - "7469"
status: draft
updated: 2026-06-12
---

# 为什么梯度裁剪能加速训练过程？一个简明的分析

## Summary

本文介绍ICLR 2020满分论文提出的(L0,L1)-smooth条件，它比传统L-smooth条件更宽松，能解释梯度裁剪的必要性——梯度裁剪相当于在(L0,L1)-smooth下使用最优学习率，保证每一步都有效下降。

## Key Claims

1. 传统L-smooth条件∥∇f(θ+Δθ)-∇f(θ)∥ ≤ L∥Δθ∥在四次函数f(θ)=θ⁴等场景不成立。
2. (L0,L1)-smooth条件∥∇f(θ+Δθ)-∇f(θ)∥ ≤ (L0+L1∥∇f(θ)∥)∥Δθ∥更宽松，适用范围更广。
3. 在(L0,L1)-smooth下，最优学习率η* = 1/(L0+L1∥∇f(θ)∥)，这导出了梯度裁剪公式。
4. 梯度裁剪保证每一步都有效下降，因此加速训练过程。

## Key Formulas

- 梯度裁剪(形式2): θ ← θ - η∇f(θ) × γ/(∥∇f(θ)∥+γ)
- (L0,L1)-smooth: ∥∇f(θ+Δθ)-∇f(θ)∥ ≤ (L0+L1∥∇f(θ)∥)∥Δθ∥
- 最优学习率: η* = 1/(L0+L1∥∇f(θ)∥)

## Connections

本文的(L0,L1)-smooth条件是对L-smooth的推广，L-smooth条件在7234的L约束讨论和8796的梯度惩罚不等式中都有重要应用。梯度裁剪在实践中与7888中RNN梯度爆炸的缓解方案直接相关。
