---
type: method
title: UNILM统一Mask
aliases: []
operation_types:
  primary: Rewrite / identity transform
  secondary:
    - Structure-expose by factorization
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-18-从语言模型到Seq2Seq-Transformer如戏-全靠Mask.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-10-19-BERT可以上几年级了-Seq2Seq-硬刚-小学数学应用题.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-03-T5-PEGASUS-开源一个中文生成式预训练模型.md
source_ids:
  - "6933"
  - "7809"
  - "8209"
method_summary: 通过设计特殊的Attention Mask矩阵，使单个Transformer模型同时具备编码器（双向Attention）和解码器（单向Attention）的能力，将Seq2Seq任务转化为统一序列变换。
typical_structure: |
  1. 将输入和目标拼接为[CLS]输入[SEP]目标[SEP]
  2. 输入部分使用双向Attention（无Mask）
  3. 目标部分使用单向Attention（下三角Mask）
  4. 交叉部分使用全连接
  5. 可用BERT MLM权重初始化加速收敛
applicability: 适用于同语言的Seq2Seq文本生成任务，特别是标题生成、摘要生成、问题回答等。使用BERT初始化可快速收敛。
tools:
  - Attention Mask 设计
  - 统一序列变换
related_methods:
  - [[T-TA结构与共享键值防泄漏法]]
  - [[双向解码交叉注意力]]
examples:
  - [[article::6933]]
  - [[article::7809]]
  - [[article::8209]]
status: draft
updated: 2026-06-14
---

## 适用问题

标准 Seq2Seq 需要独立的编码器和解码器，参数量翻倍且初始化复杂。UNILM（Unified Language Model）通过在一个 Transformer 模型中设计不同的 Attention Mask 矩阵，让同一组参数同时扮演编码器和解码器的角色，将 Seq2Seq 任务转化为统一序列变换。

## 核心变换

**输入**：拼接序列 [CLS] 输入 [SEP] 目标 [SEP]
**输出**：目标部分的生成分布
**核心**：分区 Mask 矩阵实现双向+单向注意力的统一

将输入 $X$ 和目标 $Y$ 拼接为单序列 $[X, Y]$。Attention Mask 矩阵 $M$ 设计为：

$$
M_{ij} = \begin{cases}
0 & \text{（允许注意力）} \\
-\infty & \text{（禁止注意力）}
\end{cases}
$$

其中：
- **输入区 $X$**：双向 Mask（$X$ 内部所有位置间可互相注意）
- **目标区 $Y$**：单向 Mask（下三角，$Y$ 中位置只能注意自身及左侧的位置）
- **交叉区**：$Y$ 可注意 $X$ 的所有位置（编码器-解码器交叉注意力），$X$ 不可注意 $Y$

## 典型步骤

1. **序列拼接**：将输入和目标拼接为 [CLS] 输入 [SEP] 目标 [SEP] 格式
2. **设计分区 Mask**：根据输入区和目标区分别设置不同的注意力模式
3. **模型训练**：使用拼接序列上的语言模型损失训练，目标部分计算预测损失
4. **推理解码**：在目标区使用自回归解码，每一步只能用已生成的 token

## 直觉

核心思想：**Mask 决定角色，角色决定功能**。

同一个 Transformer 模型之所以能同时做编码和解码，唯一区别在于 Attention Mask 的几何形状。

- 编码器需要全局视野来理解输入——所以用全双向 Mask
- 解码器需要防止未来信息泄漏——所以用下三角 Mask
- 解码器需要参考输入——所以允许目标区注意输入区

这种设计的优雅之处在于：不需要额外参数、不需要独立模块、可以用预训练 BERT 权重直接初始化（因为 BERT 本身也是用特殊 Mask 训练的）。只需修改 Mask 矩阵的形状，同一个模型就在编码器和解码器之间切换。

## 边界

- 拼接序列的总长度受限于模型的 max_position_embeddings
- 仅适用于**同语言**的 Seq2Seq 任务（源语言和目标语言相同）
- 训练时使用 teacher forcing，推理时使用自回归解码
- 可用 BERT 预训练权重初始化，加速收敛——这是该方法的主要实用优势

## 例子

- 标题生成：将文章作为输入区，标题作为目标区
- 摘要生成：将原文作为输入区，摘要作为目标区
- T5-PEGASUS 使用类似的分区 Mask 思想做中文生成式预训练
- BERT 在小学数学应用题上的 Seq2Seq 微调

## 证据

- ev::6933::UNILM 分区 Mask 设计：输入区双向 + 目标区单向 + 交叉全连接
- ev::7809::BERT 作为 Seq2Seq 的初始化技巧
- ev::8209::T5-PEGASUS 的分区 Mask 预训练方法
