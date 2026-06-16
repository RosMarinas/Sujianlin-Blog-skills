---
type: article_summary
title: "logsumexp运算的几个不等式"
article_id: "9070"
source_url: https://spaces.ac.cn/archives/9070
date: 2022-05-10
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2022-05-10-logsumexp运算的几个不等式.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[logsumexp运算]]"
  - "[[logsumexp凸性]]"
  - "[[logsumexp Lipschitz约束]]"
evidence_spans:
  - "ev::9070::基本界"
  - "ev::9070::平均界"
  - "ev::9070::L约束"
  - "ev::9070::凸函数证明"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2022-05-10-logsumexp运算的几个不等式.md
source_ids:
  - "9070"
status: draft
updated: 2026-06-12
---

# logsumexp运算的几个不等式

## Summary

本文系统总结了logsumexp运算的四个关键不等式：基本界（与max的近似误差不超过log n）、平均界（詹森不等式导出的下界）、Lipschitz约束（在无穷范数下L=1）以及凸函数性质，为相关理论推导提供了工具集。

## Key Claims

1. 基本界: x_max < logsumexp(x) ≤ x_max + log n，误差与x无关。
2. 加权平均界: logsumexp(x) ≥ ∑p_i x_i - log∑p_i²（柯西不等式版本）。
3. logsumexp在无穷范数下满足Lipschitz常数L=1。
4. logsumexp是凸函数（H\"older不等式证明）。
5. 温度参数τ→0时，τ·logsumexp(x/τ)→max，近似精度提高。

## Key Formulas

- y > logsumexp(x)定义: logsumexp(x) = log∑ᵢ e^{xᵢ}
- 基本界: x_max < logsumexp(x) ≤ x_max + log n
- L约束: |logsumexp(x) - logsumexp(y)| ≤ |x - y|_∞
- 凸性: t·logsumexp(x) + (1-t)·logsumexp(y) ≥ logsumexp(tx + (1-t)y)

## Connections

logsumexp是交叉熵和softmax的核心运算，因此其不等式在7708（类别不平衡Loss设计）和8656（Margin Softmax）中都有隐含应用。凸性分析也常见于优化理论，如7469中L-smooth条件的凸优化背景。
