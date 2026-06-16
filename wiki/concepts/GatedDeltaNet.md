---
type: concept
title: Gated DeltaNet
aliases:
- GDN
- Gated DeltaNet
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
- '10017'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
definition: Gated DeltaNet（GDN）是DeltaNet的扩展，引入遗忘门到Delta Rule中。它相当于在TTT的损失函数中加入L2正则项：L=1/2||Sk-v||^2
  + (1-gamma)/eta ||S||_F^2。
---

# Gated DeltaNet

## Definition

Gated DeltaNet（GDN）是DeltaNet的扩展，引入遗忘门到Delta Rule中。它相当于在TTT的损失函数中加入L2正则项：L=1/2||Sk-v||^2 + (1-gamma)/eta ||S||_F^2。

## Key Formulas

原始形式: S_t = alpha_t S_{t-1}(I - beta_t k_t k_t^T) + beta_t v_t k_t^T
Comba形式: S_t = gamma_t S_{t-1} + eta_t(v_t - S_{t-1}k_t)k_t^T

两者在数学上等价（通过重参数化）。