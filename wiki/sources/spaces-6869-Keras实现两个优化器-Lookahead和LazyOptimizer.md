---
type: article_summary
title: "Keras实现两个优化器：Lookahead和LazyOptimizer"
article_id: "6869"
source_url: https://spaces.ac.cn/archives/6869
date: 2019-07-30
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-07-30-Keras实现两个优化器-Lookahead和LazyOptimizer.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[Lookahead优化器]]"
  - "[[LazyOptimizer]]"
evidence_spans:
  - "ev::6869::Lookahead步骤"
  - "ev::6869::LazyOptimizer原理"
  - "ev::6869::LazyOptimizer实验"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-30-Keras实现两个优化器-Lookahead和LazyOptimizer.md
source_ids:
  - "6869"
status: draft
updated: 2026-06-12
---

# Keras实现两个优化器：Lookahead和LazyOptimizer

## Summary

本文用Keras实现了Lookahead和LazyOptimizer两种优化器。Lookahead通过k步前向更新加1步回退的慢权重策略稳定训练；LazyOptimizer通过仅更新被采样到参数的动量来解决Embedding层过拟合问题。

## Key Claims

1. Lookahead不是独立优化器，而是使用现有优化器的方案：备份权重→用优化器更新k步→插值回退。
2. LazyOptimizer解决带动量优化器下未采样词的Embedding仍被动量更新导致的过拟合问题。
3. LazyOptimizer通过判断梯度是否为0来近似判断词是否被采样，实现简单有效。
4. IMDB实验中LazyOptimizer(Adam)将验证准确率从83.7%提升到84.9%以上。

## Key Formulas

- Lookahead更新: θ ← θ + α(θ̃ - θ)，其中θ̃是k步快速更新后的权重

## Connections

Lookahead与梯度裁剪（7469）有相似动机：都是通过约束更新行为来稳定训练。LazyOptimizer与AdamW（7681中讨论）同属优化器改进方向，但解决的是不同问题。
