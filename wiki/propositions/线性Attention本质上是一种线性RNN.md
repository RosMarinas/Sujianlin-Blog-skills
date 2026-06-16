---
type: proposition
title: 线性Attention本质上是一种线性RNN
aliases:
  - Linear Attention as Linear RNN
statement: Causal线性Attention的递归形式o_t = S_t q_t, S_t = S_{t-1} + v_t k_t^T等价于一个以S_t为状态的线性RNN（对状态的依赖是线性的）。
assumptions:
  - "去掉Softmax中的exp和归一化"
  - "Causal掩码（下三角矩阵）"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
  - "10017"
evidence_spans:
  - "ev::10017::最初的模样"
status: draft
updated: 2026-06-10
---

# 线性Attention本质上是一种线性RNN

## 内容

Causal线性Attention可以写成线性RNN形式S_t = S_{t-1} + v_t k_t^T, o_t = S_t q_t，每步复杂度为O(d^2)常数，总复杂度O(nd^2)。这种线性RNN的"线性"指的是对状态S_t的依赖是线性的（S只出现一次方），对输入的依赖可以是非线性的。
