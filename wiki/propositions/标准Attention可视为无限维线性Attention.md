---
type: proposition
title: 标准Attention可视为无限维线性Attention
aliases:
  - Standard Attention as Infinite-dimensional Linear Attention
statement: 通过核技巧，存在映射phi使得exp(QK^T)=phi(Q)phi(K)^T，标准Softmax Attention可视为无限维度的线性Attention。三种实现方案：Performer随机投影、泰勒展开多项式核、指数定义法。
assumptions:
  - "核方法的近似等价性"
  - "映射phi的存在性（基于积分或级数展开）"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
source_ids:
  - "7921"
evidence_spans:
  - "ev::7921::随机投影"
  - "ev::7921::泰勒展开"
  - "ev::7921::指数定义"
status: draft
updated: 2026-06-10
---

# 标准Attention可视为无限维线性Attention

## 内容

标准Attention通过核技巧与无限维线性Attention等价。Performer随机投影基于高斯积分；泰勒展开将指数展开为多项式核；指数定义法利用极限(1+x/n)^n。这解释了标准Attention的秩不受head_size限制的原因。
