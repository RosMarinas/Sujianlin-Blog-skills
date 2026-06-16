---
type: concept
title: Decoder-only架构
aliases:
  - Causal Transformer
  - 自回归语言模型
definition: |
  一类自回归的Transformer语言模型架构（如GPT系列），其核心特点是仅包含解码器（Decoder），并在注意力计算中使用下三角掩码（Causal Mask）来防止当前Token关注到未来的Token。由于 causal mask 的存在，其注意力矩阵的行列式必然为正数，因此其注意力矩阵天然满秩，理论上比存在低秩瓶颈的双向注意力模型具有更强的特征表达能力，在同等参数量和推理成本下被证明是文本生成任务的最优选择。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-17-为什么现在的LLM都是Decoder-only的架构.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-20-为什么现在的LLM都是Decoder-only的架构-FAQ.md
source_ids:
  - 9529
  - 9547
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Decoder-only架构

## Definition
一类自回归的Transformer语言模型架构（如GPT系列），其核心特点是仅包含解码器（Decoder），并在注意力计算中使用下三角掩码（Causal Mask）来防止当前Token关注到未来的Token。由于 causal mask 的存在，其注意力矩阵的行列式必然为正数，因此其注意力矩阵天然满秩，理论上比存在低秩瓶颈的双向注意力模型具有更强的特征表达能力，在同等参数量和推理成本下被证明是文本生成任务的最优选择。

## Details
Decoder-only架构在近年来大语言模型（LLM）中占据了绝对的主导地位。与传统的Encoder-Decoder架构（如T5）或Encoder-only架构（如BERT）相比，Decoder-only在每一层中都采用单向（正向）的自回归注意力掩码。
这一结构设计带来了两项重要的理论优势：
1. **满秩保证**：双向注意力的得分矩阵通常由 $n 	imes d$ 矩阵与 $d 	imes n$ 矩阵相乘（$n \gg d$）后接 Softmax 组成，容易导致严重的低秩瓶颈。而下三角注意力掩码在 Softmax 作用后，对角线上的数值始终大于零，因此其行列式不为零，矩阵是绝对满秩的，能够提供比双向注意力更强的信息表达能力。
2. **位置编码友好**：下三角的掩码破坏了 Transformer 原生的置换不变性，相当于天然引入了从左到右的序信息，这使得它对位置编码信息的处理更加鲁棒。
在严格控制变量的实验中，同等推理开销下，引入双向注意力并没有为生成任务带来收益，这也印证了 Decoder-only 架构的高效性与优越性。