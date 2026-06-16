---
type: concept
title: l2 Attention Normalization
aliases:
  - l2注意力归一化
definition: l2 注意力归一化是将常规自注意力中的 Softmax（即 $l_1$ 归一化）替换为 $l_2$ 范数归一化，以打破注意力得分概率矩阵每一行求和等于 1 的行和限制。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
source_ids:
  - "9105"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# l2 Attention Normalization

## Definition
l2 注意力归一化是将常规自注意力中的 Softmax（即 $l_1$ 归一化）替换为 $l_2$ 范数归一化，以打破注意力得分概率矩阵每一行求和等于 1 的行和限制。

## Explanation
传统 Softmax 是一种 $l_1$ 归一化：$a_{i,j} = e^{b_{i,j}} / \sum_k e^{b_{i,k}}$，使得 $\sum_j a_{i,j}=1$。虽然此性质具有概率分布的清晰解释，但导致经典相对位置编码在输入全同序列时，输出无法识别位置的理论拟合瓶颈。
替换为 $l_2$ 归一化：
$$ a_{i,j} = \frac{e^{b_{i,j}}}{\sqrt{\sum_k e^{2b_{i,k}}}} $$
此时注意力概率矩阵的每一行行和不再恒等于 1，从而能够通过“全同输入排序”探针任务，增强了自注意力的理论表示能力。
实验显示：
1. 在标准的 Attention + FFN 架构中，$l_2$ 归一化自注意力效果略逊于传统 Softmax。
2. 在 GAU 门控自注意力架构中，使用 $l_2$ 归一化能直接加速收敛，并取得优于传统归一化自注意力的表现。
