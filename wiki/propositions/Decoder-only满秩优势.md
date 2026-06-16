---
type: proposition
title: Decoder-only满秩优势
aliases:
  - Decoder-only Full-rank Advantage
statement: |
  在LLM中，Decoder-only架构由于在计算Self-Attention时使用了下三角掩码，使其注意力权重矩阵在经过Softmax后行列式必然为正数，因此必然满秩；而双向注意力矩阵则会因为低秩相乘而在 $n \gg d$ 时产生严重的低秩瓶颈。
assumptions:
  - 序列长度 $n$ 显著大于注意力头的 head_size $d$
  - 注意力计算公式包含 Softmax 归一化步骤
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-17-为什么现在的LLM都是Decoder-only的架构.md
source_ids:
  - 9529
proof_route:
  - 写出双向注意力矩阵为 $\text{Softmax}(Q K^{\top})$，其中 $Q K^{\top}$ 为两 $n \times d$ 矩阵相乘，秩不超过 $d$。由于 $n \gg d$，此大矩阵具有低秩特性，尽管 Softmax 有升秩作用，但在深层模型中秩衰减依然显著（低秩瓶颈）。
  - 对于 Decoder-only 模型，注意力掩码为下三角阵，使得注意力权重矩阵 $A$ 同样为下三角阵。
  - 下三角矩阵的对角线元素为 $A_{ii} = \text{Softmax}(s_i)_i$，由于 Softmax 输出必然为正数，因此其对角线元素全为正数：$A_{ii} > 0$。
  - 计算下三角矩阵的行列式：$\det(A) = \prod_{i=1}^n A_{ii} > 0$。
  - 因为行列式非零，注意力权重矩阵 $A$ 必然是满秩的，理论上拥有比双向注意力更强的信息交互和表达能力。
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Decoder-only满秩优势

## Statement
在LLM中，Decoder-only架构由于在计算Self-Attention时使用了下三角掩码，使其注意力权重矩阵在经过Softmax后行列式必然为正数，因此必然满秩；而双向注意力矩阵则会因为低秩相乘而在 $n \gg d$ 时产生严重的低秩瓶颈。

## Assumptions
- 序列长度 $n$ 显著大于注意力头的 head_size $d$
- 注意力计算公式包含 Softmax 归一化步骤

## Proof Route
1. 写出双向注意力矩阵为 $\text{Softmax}(Q K^{\top})$，其中 $Q K^{\top}$ 为两 $n \times d$ 矩阵相乘，秩不超过 $d$。由于 $n \gg d$，此大矩阵具有低秩特性，尽管 Softmax 有升秩作用，但在深层模型中秩衰减依然显著（低秩瓶颈）。
2. 对于 Decoder-only 模型，注意力掩码为下三角阵，使得注意力权重矩阵 $A$ 同样为下三角阵。
3. 下三角矩阵的对角线元素为 $A_{ii} = \text{Softmax}(s_i)_i$，由于 Softmax 输出必然为正数，因此其对角线元素全为正数：$A_{ii} > 0$。
4. 计算下三角矩阵的行列式：$\det(A) = \prod_{i=1}^n A_{ii} > 0$。
5. 因为行列式非零，注意力权重矩阵 $A$ 必然是满秩的，理论上拥有比双向注意力更强的信息交互和表达能力。