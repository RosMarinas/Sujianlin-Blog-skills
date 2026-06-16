---
type: article_summary
title: "从三角不等式到Margin Softmax"
article_id: "8656"
source_url: https://spaces.ac.cn/archives/8656
date: 2021-09-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-09-01-从三角不等式到Margin-Softmax.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[Margin Softmax]]"
  - "[[AM-Softmax]]"
  - "[[三角不等式与排序]]"
evidence_spans:
  - "ev::8656::三角不等式定义"
  - "ev::8656::分类与排序矛盾"
  - "ev::8656::三角不等式推导margin"
  - "ev::8656::AM-Softmax导出"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-09-01-从三角不等式到Margin-Softmax.md
source_ids:
  - "8656"
status: draft
updated: 2026-06-12
---

# 从三角不等式到Margin Softmax

## Summary

本文从距离的三角不等式出发，定量分析了分类任务与排序任务的不等价性，推导了margin的必要性，并自然导出AM-Softmax的loss形式。

## Key Claims

1. 分类要求样本靠近类中心（d(z,c)最小），排序要求类内距<类间距（d(z₁,z₃) < d(z₁,z₂))。
2. 通过三角不等式可导出margin的存在：d(z₁,c₁) + d(z₃,c₁) + d(z₂,c₂) < d(z₁,c₂)，多出的项即为margin。
3. margin ≈ 类平均直径，可作为超参数调整。
4. 从三角不等式可自然导出AM-Softmax: log(1+∑e^{s·[cos(z₁,cᵢ)+m-cos(z₁,c₁)]})

## Key Formulas

- Margin条件: d(z₁,c₁) + m < d(z₁,c₂) (∀c₂ ≠ c₁)
- AM-Softmax Loss: log(1+∑_{i≠1} e^{s·[cos(z₁,cᵢ)+m-cos(z₁,c₁)]})
- margin ≈ 类平均直径: m ≈ d(z₃,c₁) + d(z₂,c₂)

## Connections

本文的Margin Softmax与7708中Logits Adjustment的几何理解（少样本类分配更大margin）直接相关。三角不等式视角与9070中logsumexp的L约束不等式（∥logsumexp(x)-logsumexp(y)∥ ≤ ∥x-y∥_∞）同属不等式工具在ML中的应用。
