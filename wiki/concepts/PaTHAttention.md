---
type: concept
title: PaTH Attention
aliases:
- PaTH
- Position-Accumulating Householder Attention
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
- '10017'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
definition: PaTH（Position Encoding via Accumulating Householder Transformations）从位置编码角度将DeltaNet反哺到Softmax
  Attention。它使用Householder矩阵的连乘来表达位置信息，是CoPE（Contextual Position Encoding）的一种。
---

# PaTH Attention

## Definition

PaTH（Position Encoding via Accumulating Householder Transformations）从位置编码角度将DeltaNet反哺到Softmax Attention。它使用Householder矩阵的连乘来表达位置信息，是CoPE（Contextual Position Encoding）的一种。

## Key Formula

使用I-ww^T（Householder矩阵）的连乘构建位置编码：
A = QK^T⊙M - (QW^T⊙M)(I+WW^T⊙M^-)^{-1}(WK^T⊙M^-)

## 特例

1. W=K时退化为DeltaNet的Attention矩阵
2. ||w||=sqrt(2)约束下等价于SoftmaxAttention(Q-DeltaNet(Q,W,W), K-DeltaNet(K,W,W), V)