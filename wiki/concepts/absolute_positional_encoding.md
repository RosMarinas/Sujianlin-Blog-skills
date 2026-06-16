---
type: concept
title: Absolute Positional Encoding
aliases:
  - 绝对位置编码
definition: 绝对位置编码是将与 Token 绝对物理坐标编号相关的编码向量以相加或相乘的形式直接融入到输入词嵌入（Token Embedding）中的一种位置特征注入机制。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-03-让研究人员绞尽脑汁的Transformer位置编码.md
source_ids:
  - "8130"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Absolute Positional Encoding

## Definition
绝对位置编码是将与 Token 绝对物理坐标编号相关的编码向量以相加或相乘的形式直接融入到输入词嵌入（Token Embedding）中的一种位置特征注入机制。

## Explanation
在自注意力架构中，所有 Token 的计算都是对称且无顺序关联的，需要显式注入位置。绝对位置编码直接在词表征 $\boldsymbol{x}_k$ 上加上位置向量 $\boldsymbol{p}_k$，主要有四类实现形式：
- **可训练式**：如 BERT 和 GPT，将位置编码作为参数矩阵随训练学习，无法自然外推，但可通过层次分解改进。
- **三角函数式 (Sinusoidal)**：如 Transformer 原始设计，通过固定频率的 $\sin$ 和 $\cos$ 函数生成，具备良好的相对距离平移映射几何性质。
- **递归式/FLOATER**：用神经网络或神经微分方程（ODE）建模迭代演化关系。
- **相乘式**：采用逐位相乘 $\boldsymbol{x}_k \otimes \boldsymbol{p}_k$ 替代相加，能获得一定的拟合效果提升。
