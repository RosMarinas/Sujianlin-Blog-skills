---
type: concept
definition: 语言模型输出端重用输入Embedding矩阵作为投影矩阵的做法。可大幅减少参数量（词表×hiddensize级别的矩阵只需一份），但可能导致初始损失异常大。
aliases:
- Tied Embeddings
- Coupled Embeddings
- Weight Sharing
status: draft
updated: '2026-06-12'
title: 共享Embedding
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# 共享Embedding

语言模型输出端重用输入Embedding矩阵作为投影矩阵的做法。可大幅减少参数量（词表×hidden_size级别的矩阵只需一份），但可能导致初始损失异常大。

## 问题根源

初始阶段模型近似恒等映射，共享Embedding时输出分布由 p(j|i) = softmax(w_i·w_j/σ) 描述。由于 w_i·w_i = ||w_i||^2 >> 0 而 w_i·w_j ≈ 0 (i≠j)，导致初始损失 ~dσ 远超均匀分布的 log n。

## 解决对策

1. 调整初始化标准差 σ = (log n)/d
2. 在Normalization后加正交初始化投影层（BERT方案）
3. 维度打乱操作（类ShuffleNet）
4. 不共享Embedding（w_i·v_j近似为0）

## 相关概念

- [[Embedding输出头稳定性]]
- [[JL引理]]
- [[词向量模长ICF解释]]