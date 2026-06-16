---
type: concept
title: Gated Attention Unit
aliases:
  - GAU
definition: GAU（Gated Attention Unit，门控注意力单元）是Google提出的一种新型Transformer变体模块。它将自注意力机制（Self-Attention）与门控线性单元（GLU）紧密结合为一个单一的神经网络层，实现了注意力机制与前馈网络（FFN）的彻底融合。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-11-门控注意力单元-GAU-还需要Warmup吗.md
source_ids:
  - "8934"
  - "8990"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Gated Attention Unit

## Definition
GAU（Gated Attention Unit，门控注意力单元）是Google提出的一种新型Transformer变体模块。它将自注意力机制（Self-Attention）与门控线性单元（GLU）紧密结合为一个单一的神经网络层，实现了注意力机制与前馈网络（FFN）的彻底融合。

## Explanation
标准的Transformer采用Attention层和FFN层交替堆叠的形式。GAU打破了这一常规：
- **层融合**：其基本形式为 $\boldsymbol{O} = (\boldsymbol{U} \odot \boldsymbol{A}\boldsymbol{V})\boldsymbol{W}_o$，其中 $\boldsymbol{U}$ 和 $\boldsymbol{V}$ 是输入特征通过门控线性分支生成的映射。
- **注意力弱化与单头化**：由于门控机制本身的表征能力极强，GAU中的注意力矩阵得到了极大的简化，摒弃了常规的Softmax，改为非概率式的 $\text{relu}^2$ 归一化。并且GAU仅需单个注意力头（Single Head, $h=1$），便能达到甚至超越传统的12头自注意力的效果，大幅降低了存储得分矩阵所需的空间复杂度（从 $bhn^2$ 降为 $bn^2$）。
GAU可以在同等参数量下组成层数翻倍的FLASH-Quad模型，在训练速度和性能上均优于标准Transformer。
