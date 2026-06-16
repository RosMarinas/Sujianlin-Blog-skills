---
type: concept
title: TTT框架
aliases:
- Test Time Training
- Online Learning视角RNN
- TTT
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
definition: TTT（Test Time Training）将序列模型的构建视为在线学习问题：将(K, V)视作语料对，通过优化器更新来构建RNN。核心思想是将历史数据压缩到固定大小的模型参数S_t中。
---

# TTT框架

## Definition

TTT（Test Time Training）将序列模型的构建视为在线学习问题：将(K, V)视作语料对，通过优化器更新来构建RNN。核心思想是将历史数据压缩到固定大小的模型参数S_t中。

## Key Formula

o_t = f(S_t; q_t), S_t = S_{t-1} - η_t ∇L(f(S_{t-1}; k_t), v_t)

## 统一视角

TTT框架统一了多种线性Attention模型：
- 原始线性Attention: f(S;k)=Sk, L=-v^T(Sk), η=1
- RetNet: 加L2正则项 (1-γ)/2 ||S||_F^2
- DeltaNet: L=1/2 ||Sk - v||^2 (平方损失)