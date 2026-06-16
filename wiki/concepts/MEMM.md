---
type: concept
title: MEMM
aliases:
- Maximum Entropy Markov Model
- 最大熵马尔可夫模型
definition: 一种序列标注概率图模型，将序列概率分解为逐步条件概率（局部归一化），与CRF的区别在于归一化方式不同——MEMM局部归一化，CRF全局归一化。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-02-24-CRF用过了-不妨再了解下更快的MEMM.md
source_ids:
- '7213'
prerequisites:
- '[[条件随机场CRF]]'
equivalent_forms: []
related_formulas: []
related_methods: []
evidence_spans:
- ev::7213::更朴素的MEMM
- ev::7213::两者关系
- ev::7213::MEMM的优劣
status: draft
updated: '2026-06-12'
---

# MEMM

## Definition

MEMM将序列标注概率分解为：P(y|x) = P(y₁|x)∏_{k=2}^n P(y_k|x,y_{k-1})。每步P(y_k|x,y_{k-1}) = e^{g(y_{k-1},y_k)+f(y_k;x)} / ∑e^{g(y_{k-1},y_k)+f(y_k;x)}。相比CRF可完全并行，速度快，但label bias问题和效果略逊。Bi-MEMM（双向平均）可缓解不对称性。