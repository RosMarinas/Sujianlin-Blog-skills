---
type: concept
definition: The Chomsky Hierarchy Evaluation Benchmark is a task suite proposed in
  "Neural Networks and the Chomsky Hierarchy" (Google, 2022) for testing length extrapolation.
  Unlike standard language model evaluations which have strong locality bias, CHE
  tasks follow fixed computational rules over arbitrarily long inputs, making it a
  rigorous test for true extrapolation ability.
title: CHE Benchmark
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

# CHE Benchmark (Chomsky Hierarchy Evaluation Benchmark)

## Definition
The Chomsky Hierarchy Evaluation Benchmark is a task suite proposed in "Neural Networks and the Chomsky Hierarchy" (Google, 2022) for testing length extrapolation. Unlike standard language model evaluations which have strong locality bias, CHE tasks follow fixed computational rules over arbitrarily long inputs, making it a rigorous test for true extrapolation ability.

## Task Categories and Difficulty Levels

### Regular (R) — Simplest
- **Even Pairs**: Given a binary sequence, determine if the count of "ab" and "ba" 2-grams is even (equivalent to checking if first and last characters match)
- **Modular Arithmetic (Simple)**: Evaluate arithmetic expressions with {0, 1, 2, 3, 4}, operators {+, -, x}, output modulo 5 (no parentheses)
- **Parity Check**: Given a binary sequence, determine if the count of 'b' is even
- **Cycle Navigation**: Given a ternary sequence (0=+0, 1=+1, 2=-1), output the final position modulo 5

### Deterministic Context-Free (DCF) — Intermediate
- **Modular Arithmetic**: Like Simple but with parentheses for complex expressions
- **Reverse String**: Given a binary sequence, output its reversal
- **Solve Equation**: Given an equation with unknown z, solve for z modulo 5 (guaranteed solution)
- **Stack Manipulation**: Given a binary string and a sequence of POP/PUSH operations, output the final stack

### Context-Sensitive (CS) — Hardest
- **Binary Addition**: Add two binary numbers from character-level serial input
- **Binary Multiplication**: Multiply two binary numbers from character-level serial input
- **Compute Sqrt**: Compute floor(sqrt(n)) from binary input
- **Duplicate String**: Output the input sequence duplicated (deceptively simple, actually CS)
- **Missing Duplicate**: Given a duplicate string with one missing character, predict the missing character
- **Odds First**: Reorder sequence to odd-indexed followed by even-indexed characters
- **Bucket Sort**: Sort an n-element sequence of values

## Key Ranking Results
Model performance ranking on CHE (ordered worst to best):
```
Transformer (R^-) < RNN (R) < LSTM (R^+) < Stack-RNN (DCF) < Tape-RNN (CS)
```

Transformer performs worst even with optimized position encoding.

## Key Experimental Findings
- **ALIBI fails**: The local-attention-based method that excels on language model tasks shows no advantage on CHE tasks, confirming that its LM success is due to language tasks' inherent locality
- **Randomized training helps**: Across all position encoding types, randomized positional training improves CHE performance
- **RoPE + randomized > ALIBI**: On CHE, RoPE with randomized training outperforms ALIBI (reversing the typical LM result)
- **Bucket Sort**: Randomized training achieves 100% accuracy on Bucket Sort for the first time
- **Not yet combined**: The combination of log n scaling attention with randomized training on CHE has not been tested

## Related Pages
- [Length Extrapolation](../concepts/length_extrapolation.md)
- [Randomized Positional Training](../concepts/randomized_positional_training.md)