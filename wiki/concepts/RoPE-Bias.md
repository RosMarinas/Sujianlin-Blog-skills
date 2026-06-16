---
type: concept
title: RoPE-Bias
aliases:
  - 旋转位置编码加偏置
definition: |
  RoPE-Bias 指的是在旋转位置编码（RoPE）的 Query 和 Key 的线性投影层中保留或加入可学习偏置项（Bias）的机制。由于旋转矩阵的存在，该偏置项在计算注意力点积时会演化为关于相对位置的非平移不变函数，并在参数训练后能够自然在长距离下呈现明显的负值衰减，从而起到强力局部化注意力和改善长度外推性的神奇效果。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-04-03-Bias项的神奇作用-RoPE-Bias-更好的长度外推性.md
source_ids:
  - 9577
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# RoPE-Bias

## Definition
RoPE-Bias 指的是在旋转位置编码（RoPE）的 Query 和 Key 的线性投影层中保留或加入可学习偏置项（Bias）的机制。由于旋转矩阵的存在，该偏置项在计算注意力点积时会演化为关于相对位置的非平移不变函数，并在参数训练后能够自然在长距离下呈现明显的负值衰减，从而起到强力局部化注意力和改善长度外推性的神奇效果。

## Details
在主流的大模型设计中，偏置项（Bias）通常由于在参数放大后作用微弱而被省略。然而，在结合了 RoPE 相对位置编码的注意力层中，偏置项扮演着截然不同的角色。
如果注意力层没有位置编码，Key 投影的偏置项会被 Softmax 的归一化约掉。但在 RoPE 机制下，投影偏置 $\boldsymbol{a}$ 和 $\boldsymbol{b}$ 会乘上旋转矩阵，注意力计算公式展开为：
$(\boldsymbol{q}_m + \boldsymbol{a})^{\top}\boldsymbol{\mathcal{R}}_{n-m}(\boldsymbol{k}_n + \boldsymbol{b})$。
随着相对位置距离 $|m-n|$ 的增加，由于偏置项各向同性性质的打破，纯偏置项内积 $\boldsymbol{a})^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{b}$ 往往被训练成一个明显的局部化衰减曲线。
这类似于在注意力矩阵上直接加上一个随距离衰减的阻尼（如 Sandwich 位置编码），从而在几乎不增加计算量和参数量的情况下，显著增强了模型在超长测试样本下的外推精度。