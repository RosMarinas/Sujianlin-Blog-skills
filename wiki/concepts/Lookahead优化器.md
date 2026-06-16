---
type: concept
title: "Lookahead优化器"
aliases:
  - "Lookahead Optimizer"
  - "k-step lookahead"
definition: "一种优化器包装方案：备份当前权重，用指定优化器更新k步得到新权重，然后将当前权重向新权重插值回退：θ ← θ + α(θ̃ - θ)。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-30-Keras实现两个优化器-Lookahead和LazyOptimizer.md
source_ids:
  - "6869"
prerequisites:
  - "[[随机梯度下降]]"
equivalent_forms: []
related_formulas: []
related_methods: []
evidence_spans:
  - "ev::6869::Lookahead步骤"
status: draft
updated: 2026-06-12
---
# Lookahead优化器

## Definition

Lookahead不是独立优化器，而是使用现有优化器的方案。三步循环：(1)备份模型权重θ；(2)从θ出发用指定优化器更新k步得θ̃；(3)更新θ←θ+α(θ̃-θ)。Hinton和Adam作者之一Jimmy Ba出现在论文作者列表中。实际效果因任务而异，并非总是有显著提升，但为优化器设计提供了新的"慢权重+快权重"思路，与动量方法有异曲同工之妙。
