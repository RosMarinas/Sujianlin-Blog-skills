---
type: concept
definition: Base-Beta Encoding is a conceptual framework linking traditional numerical
  base representations to Positional Encodings in Transformers, particularly the Rotary
  Position Embedding (RoPE) and Sinusoidal Positional Encoding.
title: Base-Beta Encoding
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

# Base-Beta Encoding ($\beta$进制编码)

## Definition
Base-Beta Encoding is a conceptual framework linking traditional numerical base representations to Positional Encodings in Transformers, particularly the Rotary Position Embedding (RoPE) and Sinusoidal Positional Encoding.

## Theoretical Equivalence
To extract the $m$-th digit (from right to left) of a number $n$ in base $\beta$, the operation is:
$$ \lfloor \frac{n}{\beta^{m-1}} \rfloor \bmod \beta $$

In Sinusoidal Encodings and RoPE, the frequencies applied to position $n$ are of the form:
$$ \cos(\frac{n}{\beta^{m-1}}), \sin(\frac{n}{\beta^{m-1}}) $$

Since sine and cosine act as continuous modulo operators, the position encoding is mathematically equivalent to representing the position token $n$ in base $\beta$ (with $\beta = 10000^{2/d}$).

## Implications for Length Extrapolation
This equivalence implies that expanding the context window is analogous to changing the number base. Positional Interpolation corresponds to scaling down $n$ (shifting decimal points), while NTK-aware Scaled RoPE corresponds to increasing the base $\beta$, which allows the model to map larger numbers using the same number of "digits" (dimensions) without severely disrupting the ordinal logic already learned.