---
type: concept
definition: A positional encoding scheme originally introduced in the "Attention is
  All You Need" paper for the Transformer model. It uses alternating sine and cosine
  functions of varying frequencies to represent positional information.
title: Sinusoidal位置编码
aliases: []
sources:
- （待从源文章提取）
source_ids:
- （待从源文章提取）
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
---

# Sinusoidal位置编码 (Sinusoidal Position Encoding)

## Overview
A positional encoding scheme originally introduced in the "Attention is All You Need" paper for the Transformer model. It uses alternating sine and cosine functions of varying frequencies to represent positional information.

## Mechanism
The encoding for position $k$ and dimension $2i$ and $2i+1$ is defined as:
- $p_{k,2i} = \sin(k / 10000^{2i/d})$
- $p_{k,2i+1} = \cos(k / 10000^{2i/d})$

This formulation acts as an absolute position encoding but possesses properties that allow it to represent relative position information via dot products. Due to its oscillatory nature and the specific frequency structure, the dot product between embeddings of two positions decays as the distance between them increases (Long-term Decay).

## Applications
- Standard Transformer models
- Foundational text representations

## Sources
- [spaces-8231-Sinusoidal位置编码追根溯源](../sources/spaces-8231-Sinusoidal位置编码追根溯源.md)