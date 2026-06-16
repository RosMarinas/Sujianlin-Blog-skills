---
type: concept
title: Short Conv线性注意力
aliases: '[Short Convolution in Linear Attention, 短卷积线性注意力]'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
source_ids:
- '11320'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
definition: 现代线性Attention模型在Q/K/V前加的Short Conv（通常kernel_size=2的1D卷积）。其核心作用是将TTT的配对从"预测自己"(k_t,
  v_t)转化为NTP式"预测周围"(k_{t-1}, v_t)。
---

# Short Conv线性注意力

## Definition

现代线性Attention模型在Q/K/V前加的Short Conv（通常kernel_size=2的1D卷积）。其核心作用是将TTT的配对从"预测自己"(k_t, v_t)转化为NTP式"预测周围"(k_{t-1}, v_t)。

## 关键洞察

Short Conv的作用不是简单的深度增加或Token-Mixing增强，而是解决TTT框架中键值同源导致的表达能力瓶颈。当K=V时TTT退化，即使K≠V但同源时，可学信息也有限。

## 实验发现

给K加Short Conv效果最显著，给Q/V加虽然有一定作用但远不如K。