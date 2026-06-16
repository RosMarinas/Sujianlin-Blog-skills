---
type: concept
title: Viterbi采样
definition: "一种用于序列模型生成采样的回溯概率搜索方法，可在保持生成多样性的同时提升高概率路径生成质量。"
sources:
  - wiki/sources/spaces-9811-Viterbi采样完美采样.md
source_ids:
  - "9811"
status: draft
updated: 2026-06-12
---
Viterbi采样是一种用于BytePiece随机分词的采样算法，它在Viterbi解码的动态规划结构上，将确定性 $\max$ 操作替换为随机的基于权重的采样。

## 算法改进

旧版：$r_i = \sigma(\alpha(s_i - s_{i-1}))$（多步二选一，概率被稀释）

新版：$Z_i = Z_{i-1} + e^{\alpha s_i},\quad r_i = \varepsilon < e^{\alpha s_i}/Z_i$（水塘采样，保证概率正确）

## 关键性质

- 计算复杂度 $\mathcal{O}(lm)$，与Viterbi解码同阶
- 效果上与Subword Regularization等价（完美采样）
- $\alpha\to\infty$ 时退化为Viterbi解码

## 来源

- 9811：随机分词再探
