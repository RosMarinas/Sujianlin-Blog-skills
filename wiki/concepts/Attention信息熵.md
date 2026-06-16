---
type: concept
title: Attention信息熵
aliases:
  - 注意力分布熵
definition: |
  Attention信息熵是度量注意力机制所输出的离散概率分布不确定性及信息量的指标。注意力分布越均匀，信息熵越大；越集中于少数Token，信息熵越接近零。它是解释模型初始化避免梯度消失、对比学习中温度参数缩放作用的理论工具。
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-04-25-注意力和Softmax的两点有趣发现-鲁棒性和信息量.md
source_ids:
  - 9593
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Attention信息熵

## Definition
Attention信息熵是度量注意力机制所输出的离散概率分布不确定性及信息量的指标。注意力分布越均匀，信息熵越大；越集中于少数Token，信息熵越接近零。它是解释模型初始化避免梯度消失、对比学习中温度参数缩放作用的理论工具。

## Details
在基于 Softmax 归一化的注意力中，输出分布的信息熵为 $H = -\sum p_i \log p_i \in [0, \log n]$。
从熵和信息论的角度可以很好地指导大模型的设计与优化：
1. **梯度消失与均匀初始化**：如果模型初始化阶段 logits 偏大，Softmax 分布会过度接近 one-hot 状态，使 Attention 熵直接趋于 0。这相当于信息空间被压缩，导致优化器无法从中榨取任何梯度信息，产生无法训练的现象。因此必须将 logits 初始化在合理的小范围以保持高熵。
2. **温度参数的物理意义**：在对比学习中，直接计算的余弦相似度如果用 $\tau=1$ 缩放，其分布的信息熵下界较大（约为 $\log n - 0.4745$），这使得可榨取的信息量被极大限制。通过引入微小的温度参数 $\tau \ll 1$，可以将熵的下界拉近到 0，释放更多的渐近信息空间，从而加速模型的判别性训练。