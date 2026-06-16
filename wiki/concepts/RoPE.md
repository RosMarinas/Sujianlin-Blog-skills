---
type: concept
definition: 旋转式位置编码（Rotary Position Embedding, RoPE）是一种通过绝对位置编码的方式实现相对位置编码的设计。它对q,k向量按维度对进行旋转操作，使得内积结果只依赖于位置差。
title: 旋转式位置编码 (RoPE)
aliases:
- RoPE
- Rotary Position Embedding
- 旋转位置编码
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
- Data/Spaces_ac_cn/markdown/Mathematics/2021-06-02-我们可以无损放大一个Transformer模型吗-一.md
source_ids:
- '8978'
- '8444'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: deprecated
replaced_by: '[[concept::RoPE相对位置编码]]'
updated: '2026-06-12'
deprecation_reason: Merged into concept::RoPE相对位置编码 as part of Pass A node boundary
  repair. Orphan page (no node linked to it).
---

# 旋转式位置编码 (RoPE)

## Definition

旋转式位置编码（Rotary Position Embedding, RoPE）是一种通过绝对位置编码的方式实现相对位置编码的设计。它对q,k向量按维度对进行旋转操作，使得内积结果只依赖于位置差。

## Key Property

对于任意正交矩阵Omega，R_m = Omega^m都是广义的RoPE。RoPE对应的相对位置矩阵是严格的三角阵，位置差即为矩阵元素值。

## 相关方法

- ReRoPE、Leaky ReRoPE：RoPE的窗口外推变体
- InvLeaky ReRoPE：训练反用Leaky ReRoPE，推理退化为标准RoPE
- NTK-aware Scaled RoPE：通过修改底数实现零样本外推