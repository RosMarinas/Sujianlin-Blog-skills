---
type: concept
definition: Key Normalization（KeyNorm）是一种对Attention的Key序列进行L2归一化的事前修改方案。它将每个Key向量
  kj 替换为 k̃j = kj / ||kj||，消除Key向量模长的影响，迫使模型通过调整 cos(qi, kj) 来表达注意力权重。
title: Key Normalization (KeyNorm)
status: draft
created: '2026-06-09'
tags:
- Attention
- 归一化
- 长度外推
- Key序列
related_articles:
- 9859
- 9948
related_concepts:
- length-extrapolation
- cosine-attention
- rotary-position-embedding
evidence_spans:
- 9859-最初动机
- 9859-先看结果
- 9859-原理分析
- 9948-另起炉灶
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## 核心定义

Key Normalization（KeyNorm）是一种对Attention的Key序列进行L2归一化的事前修改方案。它将每个Key向量 k_j 替换为 k̃_j = k_j / ||k_j||，消除Key向量模长的影响，迫使模型通过调整 cos(q_i, k_j) 来表达注意力权重。

KeyNorm属于"事前修改"类别——在训练阶段引入，推理阶段不做任何修改即可实现长度外推。

## 关键性质

1. **显著的免修改长度外推**：KNA在4096不重复测试中达47.69%，远超Baseline的23.16%。
2. **训练效果不降反升**：KNA在训练长度512上准确率49.60%，略超Baseline的49.41%。
3. **RoPE依赖**：KeyNorm只有与RoPE配合才体现长度外推能力，KeyNorm+NoPE无效。
4. **非局部约束**：与ALIBI、KERPLE等不同，KeyNorm没有局部注意力约束，更有Scale Up潜力。
5. **对事后外推技巧的"免疫"**：叠加NTK、YaRN等提升不大（重复测试有提升，不重复测试提升不显著）。
6. **长文本继续训练友好**：不需要选择PI还是ABF等策略，"啥也不改就行"。

## 原理分析

从几何角度看，标准Attention的打分可分解为：

s(j|i) = q_i · k_j = ||q_i|| ||k_j|| cos(q_i, k_j)

模型有两个途径提高某个位置j的重要性：
1. 增大 ||k_j||（模长，表达绝对重要性）
2. 增大 cos(q_i, k_j)（夹角，表达相对交互）

由于维度灾难，高维空间中显著改变夹角比改变模长更难，模型会优先选择增大模长。这导致cos(q_i, k_j)训练不充分——这是Attention无法长度外推的主要原因。

KeyNorm消除了途径1，强制模型充分训练cos(q_i, k_j)，从而促进了长度外推。

## 实验表现

- KNA + RoPE: 训练512达49.60%，4096重复61.08%，4096不重复47.69%
- KNA + log n: 训练512达49.58%，4096不重复46.40%
- CosA + log n: 训练512达49.67%，4096不重复48.95%

## 出现位置

- [第15篇](/archives/9859) 全文
- [第16篇](/archives/9948) "另起炉灶"节作为重要事前修改方案讨论

## 原文证据

- 原文9859"最初动机"节：从替换Scale方式的动机引出QNA、KNA、CosA
- 原文9859"先看结果"节：KNA在4096不重复测试中达47.69%
- 原文9859"原理分析"节：给出s(j|i)的几何分解（eq:sdpa）
- 原文9859"原理分析"节：断言"cos(q_i,k_j)的训练不充分是Attention无法长度外推的主要原因"
- 原文9948"另起炉灶"节：将KeyNorm置于框架中讨论

## 相关变体

- **KNA** (Key-Normalized Attention): 只对Key做L2归一化
- **QNA** (Query-Normalized Attention): 只对Query做L2归一化
- **CosA** (Cosine Attention): 对Query和Key都做L2归一化，加可学习scale因子λ