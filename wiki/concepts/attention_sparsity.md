---
type: concept
title: Attention Sparsity
aliases:
  - 注意力稀疏性
  - Sparsity of Attention
definition: |
  注意力稀疏度是描述注意力分布权重的离散集中程度的物理指标。在数学上可以通过 $l_1/l_2$ 范数之比 $S(\boldsymbol{a})$ 进行度量，该指标越小代表分布越接近 one-hot 的极端稀疏状态，即模型能更有针对性地“集中注意力”到关键 Token，是分析标准 Softmax 注意力与线性注意力表达能力差距的核心维度。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-12-12-注意力机制真的可以-集中注意力-吗.md
source_ids:
  - 9889
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Attention Sparsity

## Definition
注意力稀疏度是描述注意力分布权重的离散集中程度的物理指标。在数学上可以通过 $l_1/l_2$ 范数之比 $S(\boldsymbol{a})$ 进行度量，该指标越小代表分布越接近 one-hot 的极端稀疏状态，即模型能更有针对性地“集中注意力”到关键 Token，是分析标准 Softmax 注意力与线性注意力表达能力差距的核心维度。

## Details
注意力稀疏性在控制模型能否精确定位序列中长程依赖的关键点上起着决定性作用。
利用稀疏性度量公式 $S(\boldsymbol{a}) = \frac{\mathbb{E}[|x|]}{\sqrt{\mathbb{E}[x^2]}}$，可以对不同注意力机制的稀疏上界进行理论分析：
1. **标准 Attention 的满秩稀疏能力**：标准 Attention 使用指数激活函数 $f = \exp$，其稀疏指标 $S(\boldsymbol{a}) = \exp(-\frac{1}{2}\sigma^2\Vert\boldsymbol{q}\Vert^2)$。当参数模长或输入方差趋于无穷大时，稀疏指标可以平滑地趋近于 0，这意味着标准注意力可以实现极其稀疏的“聚焦”。
2. **线性 Attention 的稀疏性盲区**：不加激活函数的极简线性 Attention 的稀疏度存在一个较高的非零下界，这使得它无论如何拉开差距，都无法集中注意力到单个 Token。对于一般非负型线性 Attention，要获得稀疏性就必须面临由于均值接近零而引发的低秩瓶颈。这也是线性化改进效果普遍较差的根本原因之一。