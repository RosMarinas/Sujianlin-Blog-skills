---
type: concept
definition: Rotary Position Embedding (RoPE) is a position encoding technique that
  encodes absolute position with a rotation matrix and naturally incorporates explicit
  relative position dependency in self-attention formulation. Introduced in the RoFormer
  model.
title: 旋转式位置编码
aliases: []
sources:
- （待从源文章提取）
source_ids:
- （待从源文章提取）
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: deprecated
replaced_by: '[[concept::RoPE相对位置编码]]'
updated: '2026-06-12'
deprecation_reason: Merged into concept::RoPE相对位置编码 as part of Pass A node boundary
  repair. Same mathematical object (RoPE/Rotary Position Embedding) under different
  node names.
---

# 旋转式位置编码 (Rotary Position Embedding, RoPE)

## Overview
Rotary Position Embedding (RoPE) is a position encoding technique that encodes absolute position with a rotation matrix and naturally incorporates explicit relative position dependency in self-attention formulation. Introduced in the RoFormer model.

## Mechanism
RoPE encodes the position of a token by multiplying its query and key representations by a rotation matrix that depends on the token's absolute position. When calculating attention scores (dot product of queries and keys), the absolute positions mathematically combine to form the relative position (distance) between tokens.
Specifically, for a token at position $m$, its representation vector is viewed as complex numbers or 2D pairs, and a rotation of angle $m\theta$ is applied. For higher dimensions, it's concatenated as blocks.

## Properties
- Acts as an absolute position encoding but functions effectively as a relative position encoding.
- Possesses long-term decay: the dot product of two vectors decays as their relative distance increases.
- Fully compatible with Linear Attention because it modifies the query and key vectors before the dot product, rather than modifying the attention matrix.

## Applications
- RoFormer
- Various large language models (LLaMA, etc.)
- Linear Attention implementations

## Sources
- [spaces-8265-博采众长的旋转式位置编码](../sources/spaces-8265-博采众长的旋转式位置编码.md)