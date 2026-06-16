---
type: article_summary
title: "从SamplePairing到mixup：神奇的正则项"
article_id: "5693"
source_url: https://spaces.ac.cn/archives/5693
date: 2018-07-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-07-07-从SamplePairing到mixup-神奇的正则项.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[mixup正则化]]"
  - "[[SamplePairing]]"
evidence_spans:
  - "ev::5693::mixup线性正则诠释"
  - "ev::5693::SamplePairing对称性"
  - "ev::5693::函数方程推导"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-07-07-从SamplePairing到mixup-神奇的正则项.md
source_ids:
  - "5693"
status: draft
updated: 2026-06-12
---

# 从SamplePairing到mixup：神奇的正则项

## Summary

SamplePairing和mixup是两种图像数据扩增方法，但本文论证其本质是正则化手段：通过要求模型对混合输入输出混合标签，迫使模型接近线性函数，从而降低过拟合风险。

## Key Claims

1. SamplePairing要求(εx_a + (1-ε)x_b)的标签为εy_a + (1-ε)y_b，实际是在要求模型是线性函数。
2. 函数方程 εf(x_a) + (1-ε)f(x_b) = f(εx_a + (1-ε)x_b) 的唯一解是线性函数。
3. mixup相当于在所有效果相近的模型中，选择最接近线性函数的那一个——即模型过滤器。

## Key Formulas

- mixup约束: εy_a + (1-ε)y_b = f(εx_a + (1-ε)x_b)
- 代入y=f(x)得: εf(x_a) + (1-ε)f(x_b) = f(εx_a + (1-ε)x_b)

## Connections

mixup作为正则化手段与对抗训练（7234）中梯度惩罚有相似作用机制：都通过约束模型的行为来提升泛化性。与L2正则（7681）不同，mixup约束的是函数的整体线性度而非参数范数。
