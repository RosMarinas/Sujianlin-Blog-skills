---
type: concept
title: Relative Position Encoding Flaw
definition: 相对位置编码理论缺陷，指的是在仅通过修改Softmax前注意力得分计算来融入相对位置编码的Transformer中，当输入序列的所有 Token 完全相同时，模型将彻底丧失在不同空间位置上输出各异表征的能力，从而破坏了模型的“万能拟合”特性。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
source_ids:
  - "9105"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Relative Position Encoding Flaw

## Definition
相对位置编码理论缺陷，指的是在仅通过修改Softmax前注意力得分计算来融入相对位置编码的Transformer中，当输入序列的所有 Token 完全相同时，模型将彻底丧失在不同空间位置上输出各异表征的能力，从而破坏了模型的“万能拟合”特性。

## Explanation
对于全同输入序列，模型在每个位置产生的 Value 向量都是相同的 $\boldsymbol{v}_j = \boldsymbol{v}$。自注意力计算的融合步骤为 $\boldsymbol{o}_i = \sum_j a_{i,j}\boldsymbol{v}_j$。
在经典的相对位置编码（如 RoPE, T5）中，注意力矩阵 $A$ 虽融合了位置，但在 Softmax 后每一行和依然恒等于 1（$\sum_j a_{i,j}=1$）。
因此：$\boldsymbol{o}_i = (\sum_j a_{i,j})\boldsymbol{v} = \boldsymbol{v}$。这导致了每个空间位置上的输出 $\boldsymbol{o}_i$ 自始至终完全一致，模型无法拟合出像 $[1, 2, \dots, n]$ 这样有空间差异的位置标签。
要破除这个缺陷，必须改变行概率和恒等于 1 的限制（例如换用 $l_2$ 归一化自注意力或无分母归一化，如 GAU），或者在输入两端添加非词义标记符（`[CLS]` 和 `[SEP]`）来利用边界不对称性。
