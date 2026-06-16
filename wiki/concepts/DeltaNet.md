---
type: concept
title: DeltaNet
aliases: '[Delta Rule线性注意力, DeltaNet]'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
source_ids:
- '10017'
- '11320'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
definition: DeltaNet是基于Delta Rule（Widrow-Hoff算法）的线性Attention模型。它将TTT框架中的损失函数从内积改为平方损失L=1/2||Sk
  - v||^2，实现"除旧迎新"的效果。
---

# DeltaNet

## Definition

DeltaNet是基于Delta Rule（Widrow-Hoff算法）的线性Attention模型。它将TTT框架中的损失函数从内积改为平方损失L=1/2||Sk - v||^2，实现"除旧迎新"的效果。

## Key Formula

S_t = S_{t-1} - (S_{t-1}k_t - v_t)k_t^T = S_{t-1}(I - k_tk_t^T) + v_tk_t^T

## 核心思想

- "先减后加"：先移除模型对k_t的旧认知，再根据(k_t,v_t)补充新认知
- Delta Rule源自1960年代的Least Mean Square算法
- 仍属于线性RNN（对S的依赖是线性的）