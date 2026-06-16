---
type: example
title: TTT统一视角下的线性Attention推导实例
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
- '10017'
evidence_spans:
- ev::10017::测试时训练
notation_mapping:
  （待从源文章提取）: （待从源文章提取）
article_id: '10017'
article: '[[（待从源文章提取）]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

## 问题

从TTT的在线学习视角推导DeltaNet、RetNet等线性Attention模型。

## 推导

TTT框架的核心：o_t = f(S_t; q_t), S_t = S_{t-1} - eta_t * ∇L(f(S_{t-1}; k_t), v_t)

### 原始线性Attention

取f(S;k)=Sk, L=-v^T(Sk), eta=1:
∇L = -v k^T
S_t = S_{t-1} + v_t k_t^T

### RetNet

加L2正则项: L = -v^T(Sk) + (1-gamma)/2 ||S||_F^2
∇L = -v k^T + (1-gamma)S
S_t = gamma * S_{t-1} + v_t k_t^T

### DeltaNet

取平方损失: L = 1/2 ||Sk - v||^2
∇L = (Sk - v)k^T
S_t = S_{t-1} - (S_{t-1}k_t - v_t)k_t^T = S_{t-1}(I - k_t k_t^T) + v_t k_t^T