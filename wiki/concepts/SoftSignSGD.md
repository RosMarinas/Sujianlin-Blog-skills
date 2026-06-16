---
type: concept
title: SoftSignSGD
aliases:
- softsign stochastic gradient descent
definition: 将SignSGD的符号函数替换为softsign(x,ε)=x/√(x²+ε²)的随机梯度下降变体，ε越大越接近SGD，ε越小越接近SignSGD，用于近似分析Adam优化器的epsilon效应。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-11-18-Adam的epsilon如何影响学习率的Scaling-Law.md
source_ids:
- '10563'
prerequisites:
- '[[SignSGD]]'
- '[[学习率-Batch Size尺度律]]'
equivalent_forms: []
related_formulas:
- '[[SoftSignSGD平均场学习率公式]]'
related_methods:
- '[[用平均场近似替代复杂期望计算]]'
series:
- '[[重新思考学习率与Batch Size]]'
evidence_spans:
- ev::10563::SoftSign
- ev::10563::均值估计
- ev::10563::方差估计
status: draft
updated: '2026-06-12'
---

# SoftSignSGD

## Definition

SoftSignSGD使用softsign函数替代sign函数作为梯度归一化：φ̃_B = softsign(g̃_B, ε) = g̃_B/√(g̃_B²+ε²)。当ε→0时退化为SignSGD，当ε→∞时趋近SGD。在Adam分析中，epsilon的存在使得最优学习率-Batch Size关系介于SGD和SignSGD之间，Surge现象随ε增大而弱化。