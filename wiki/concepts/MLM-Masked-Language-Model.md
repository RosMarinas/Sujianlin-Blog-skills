---
title: MLM (Masked Language Model)
definition: MLM（Masked Language Model）是BERT的预训练任务：随机mask输入中的部分token，让模型根据上下文预测被mask的token。通常使用15%的mask比例，其中80%替换为[MASK]，10%保持不变，10%替换为随机token。
type: concept
aliases:
- MLM
- 掩码语言模型
- Masked Language Modeling
tags:
- pre-training
- bert
- language-model
- nlp
related_concepts:
- Dropout
- MAE
related_sources:
- spaces-8770-Dropout视角下的MLM和MAE
status: draft
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## Definition

MLM（Masked Language Model）是BERT的预训练任务：随机mask输入中的部分token，让模型根据上下文预测被mask的token。通常使用15%的mask比例，其中80%替换为[MASK]，10%保持不变，10%替换为随机token。

## Dropout Perspective

MLM可视为一种特殊Dropout：引入随机变量 $\varepsilon \sim \text{Bernoulli}(p)$，将模型从 $f(\cdots, x_i, \cdots)$ 变为 $f(\cdots, x_i\varepsilon + m(1-\varepsilon), \cdots)$，其中 $m$ 为[MASK]的Embedding。

## Training-Finetuning Inconsistency

按照Dropout理论，预训练后应调整Embedding为 $x_i p + m(1-p)$，但实际微调中直接使用原始 $x_i$。修正Embedding的加权公式：
$$
\text{Embedding}[i] \leftarrow 0.85 \times \text{Embedding}[i] + 0.15 \times (0.8 \times \text{Embedding}[m] + 0.1 \times \text{Embedding}[i] + 0.1 \times \text{Avg[Embedding]})
$$

实验表明：此修正对CLUE任务无显著提升，说明MLM不一致性问题可能被高估。

## References

- 苏剑林. "Dropout视角下的MLM和MAE：一些新的启发". 科学空间, 2021. [spaces-8770]
- Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers", NAACL 2019.