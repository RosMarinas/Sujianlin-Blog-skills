---
type: concept
definition: 2D RoPE（二维旋转式位置编码）是将RoPE（旋转式位置编码）推广到二维空间（例如图像像素的(x, y)坐标）的变体。
title: 2D RoPE
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

# 2D RoPE

## Definition
2D RoPE（二维旋转式位置编码）是将RoPE（旋转式位置编码）推广到二维空间（例如图像像素的(x, y)坐标）的变体。

## Design Conditions

2D RoPE must satisfy two key conditions:

1. **相对性 (Relativity)**: The position matrix must satisfy R_{x1,y1}^T * R_{x2,y2} = R_{x2-x1, y2-y1}. This ensures that when applied to Q and K vectors, the attention dot product depends only on relative position differences, enabling absolute-position encoding to achieve relative-position effects.

2. **可逆性 (Invertibility)**: Given R_{x,y}, it must be possible to uniquely recover (x, y). This prevents information loss about the original position. A trivial solution like R_{x,y} using only (x+y) would fail this condition since different (x,y) pairs map to the same value.

## Derivation Approaches

### Quaternion Approach (Dead-End)
A natural first attempt is generalizing from 1D RoPE's use of complex numbers to 2D using quaternions. The quaternion exponential e^{x*i*theta + y*j*theta} seemed promising, but fails because quaternion multiplication is non-commutative. For quaternions p, q: e^{p+q} != e^{p}*e^{q} in general. This means the critical property of converting multiplication to addition (needed for relative positions) is lost. The quaternion approach is a dead-end for RoPE.

### Matrix Exponential Approach (Successful)
Using matrix exponentials: R_{x,y} = exp(x*B1 + y*B2), where B1, B2 are skew-symmetric matrices satisfying:
- B1^T + B1 = 0, B2^T + B2 = 0 (skew-symmetry for relative positions)
- B1 * B2^T = B2^T * B1 (commutativity for exponential addition property)

The simplest 4x4 solution yields: R_{x,y} = block-diag(R_{x*theta}, R_{y*theta}), where each block is a 2x2 rotation matrix. This treats x and y dimensions independently — the first half of vector dimensions encode x-position via rotation, the second half encode y-position via rotation.

## Properties
- Orthogonal matrix (preserves vector norms, maintaining training stability)
- Block-diagonal structure enables efficient implementation
- Naturally extends to 3D, 4D, etc. by adding more block-diagonal groups

## Related Pages
- [Rotary Position Embedding (RoPE)](../concepts/rotary-position-embedding.md)
- [Matrix Exponential for RoPE](../methods/matrix_exponential_rope.md)