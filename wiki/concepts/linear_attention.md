---
type: concept
definition: 线性Attention是一类旨在将标准Transformer中Self-Attention的 $O(N^2)$ 复杂度降低为 $O(N)$（线性复杂度）的模型。它通常通过定义核函数（kernel
  feature maps）或激活函数 $\phi(q)$ 和 $\phi(k)$，使得 $qi \cdot kj$ 的指数可被分解或近似，从而利用结合律先计算
  $kj$ 与 $vj$ 的乘积。
title: Linear Attention
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

# Linear Attention

## Definition
线性Attention是一类旨在将标准Transformer中Self-Attention的 $O(N^2)$ 复杂度降低为 $O(N)$（线性复杂度）的模型。它通常通过定义核函数（kernel feature maps）或激活函数 $\phi(q)$ 和 $\phi(k)$，使得 $q_i \cdot k_j$ 的指数可被分解或近似，从而利用结合律先计算 $k_j$ 与 $v_j$ 的乘积。

## Bottlenecks
根据《从Performer到线性Attention》，线性Attention面临两个主要瓶颈：
1. **低秩问题 (Low Rank)**：因为 $\tilde{Q}\tilde{K}^\top$ 的秩不超过投影维度 $m$，往往需要增大 key_size ($m > d$) 来逼近标准Attention的表达能力。
2. **缺乏稀疏性 (Sparsity)**：线性Attention生成的注意力矩阵通常较稠密，难以像标准Attention的softmax那样集中在少数token上，往往退化为平均池化。