---
type: article_summary
title: "殊途同归的策略梯度与零阶优化"
article_id: "7737"
source_url: https://spaces.ac.cn/archives/7737
date: 2020-09-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-09-15-殊途同归的策略梯度与零阶优化.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[策略梯度]]"
  - "[[零阶优化]]"
  - "[[零阶梯度]]"
evidence_spans:
  - "ev::7737::策略梯度目标"
  - "ev::7737::排序不等式证明"
  - "ev::7737::采样估计梯度"
  - "ev::7737::降低方差baseline"
  - "ev::7737::零阶梯度定义"
  - "ev::7737::貌离神合证明"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-09-15-殊途同归的策略梯度与零阶优化.md
source_ids:
  - "7737"
status: draft
updated: 2026-06-12
---

# 殊途同归的策略梯度与零阶优化

## Summary

本文介绍了处理不可导优化目标的两种方法——策略梯度和零阶优化，并通过数学推导证明在处理同一类优化问题时两者基本等价，揭示了不同优化方法在深层的统一性。

## Key Claims

1. 策略梯度通过排序不等式用期望E[∑p(y|x)r(y_t,y)]替代含argmax的原始目标。
2. 零阶梯度定义为∇̃_x f(x) = E_u[(f(x+εu)-f(x))/ε · u]，无需函数的可导性。
3. 两者都需采样估计梯度且都有baseline降方差技术。
4. 通过划分全空间和示性函数技巧可证明零阶梯度近似等于策略梯度。

## Key Formulas

- 策略梯度: ∇_θ R = E[r(y_t,y) ∇_θ log p_θ(y|x)]
- 零阶梯度: ∇̃_x f(x) = E_u[(f(x+εu)-f(x))/ε · u]
- 最优baseline: b = E[r(y_t,y)] (策略梯度) / b = E[f(x+εu)∥u∥²]/E[∥u∥²] (零阶优化)

## Connections

本文的统一视角与8796中讨论的SGD隐式梯度正则化有深层联系：都指向优化算法的内在偏差。策略梯度与7708中从光滑指标导出梯度的思路一致——都是需要"梯度替代物"。
