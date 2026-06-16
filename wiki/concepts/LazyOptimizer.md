---
type: concept
title: "LazyOptimizer"
aliases:
  - "Lazy Optimizer"
  - "延迟优化器"
definition: "一种针对Embedding层的优化器改进方案，仅更新当前batch中被采样到的参数的动量，避免未采样词的Embedding被历史动量反复更新导致的过拟合。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-30-Keras实现两个优化器-Lookahead和LazyOptimizer.md
source_ids:
  - "6869"
prerequisites:
  - "[[动量优化器]]"
  - "[[Embedding层]]"
equivalent_forms: []
related_formulas: []
related_methods: []
evidence_spans:
  - "ev::6869::LazyOptimizer原理"
  - "ev::6869::LazyOptimizer实验"
status: draft
updated: 2026-06-12
---
# LazyOptimizer

## Definition

带动量的优化器（如Adam）中，未采样词的Embedding梯度为0但动量不为0，因此仍被更新，导致过拟合。LazyOptimizer通过判断梯度是否为0来近似判断词是否被采样，仅当梯度非零时才更新对应动量。IMDB实验中LazyOptimizer(Adam)将验证准确率从83.7%提升到84.9%。这一优化器特别适用于Embedding层很大的模型（尤其是以词为单位的模型），通过减少Embedding更新频率让模型重点优化其余部分。
