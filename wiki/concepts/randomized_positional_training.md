---
type: concept
definition: Randomized Positional Training is a technique to enhance length generalization
  by sampling position IDs randomly from a larger range during training, instead of
  using strictly sequential integers [0, 1, ..., N-1].
title: Randomized Positional Training
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

# Randomized Positional Training

## Definition
Randomized Positional Training is a technique to enhance length generalization by sampling position IDs randomly from a larger range during training, instead of using strictly sequential integers [0, 1, ..., N-1].

## Algorithm
Given:
- N = training length (e.g., N=40 in the original paper)
- M = prediction length (e.g., M=500)
- L = a large range, L > M (e.g., L=2048, a hyperparameter)

During training, instead of using positions [0, 1, ..., N-1], randomly sample N distinct integers from {0, 1, ..., L-1}, sort them ascending, and use these as the position sequence.

```
def random_position_ids(N, L=2048):
    return np.sort(np.random.permutation(L)[:N])
```

During inference, positions can also be randomly sampled, or uniformly spaced points from [0, L) can be used (the author's experiments show uniform spacing works slightly better).

## Equivalence Class Insight
The key theoretical insight: randomized training forces the model to learn that **all sorted position sequences are equivalent**. The position sequences [1, 3, 5] and [2, 4, 8] are both just "three positions in ascending order" — the model learns the concept of sequential ordering rather than memorizing specific position values. This is the fundamental mechanism behind positional robustness.

## Refinement: Equal Mean Randomized Position Training
A refinement ensures tighter consistency between training and prediction:
- Sample n from a distribution with mean N (e.g., exponential or beta distribution)
- Take N uniformly spaced points from [0, n]
- This produces float positions, so it only works with functional position encodings (Sinusoidal, RoPE), not learned embeddings

## Requirements
- Works with any functional position encoding (Sinusoidal, RoPE)
- NOT compatible with learned/trainable position embeddings (which require discrete indices)
- Best combined with log n scaling attention for attention entropy consistency

## Related Pages
- [Positional Robustness](../concepts/positional_robustness.md)
- [Length Extrapolation](../concepts/length_extrapolation.md)
- [Equal Mean Randomized Position Training](../methods/equal_mean_randomized_position_training.md)