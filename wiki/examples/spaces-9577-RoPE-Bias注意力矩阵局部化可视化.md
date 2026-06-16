---
type: example
title: spaces-9577-RoPE-Bias注意力矩阵局部化可视化
article_id: 9577
article: |
  [spaces-9577-Bias项的神奇作用-RoPE-+-Bias-=-更好的长度外推性](wiki/sources/spaces-9577-Bias项的神奇作用-RoPE-+-Bias-=-更好的长度外推性.md)
section: 实验结果
claim: 开启投影Bias项的RoPE注意力矩阵在超长测试样本下能够自动呈现显著的局部化衰减趋势
notation_mapping:
  Bias: Projection layer bias terms a and b
  Attention_decay: Attention value drop-off curve over distance
steps:
  - 构建基于 GAU-α 架构的模型，在序列长度为 512 的数据集上进行常规自回归预训练。
  - 实验组开启 Query 和 Key 投影层的 Bias 项，对照组关闭（其他层的 Bias 均保持去掉状态）。
  - 训练完成后，使用同一个超长文本样本进行前推，将输入长度拉长到 4096，并绘制某一层自注意力权重矩阵的值随相对距离的分布图。
  - 无 Bias 的对照模型在超过 512 距离后，其注意力数值开始异常上升，失去了局部化，导致长度外推崩溃。
  - 有 Bias 的实验模型，其注意力矩阵在长距离上始终呈现非常明显的单调衰减趋势（尤其在靠近输入的层），证明偏置项在 RoPE 作用下被自动训练成了局部化阻尼器。
used_concepts:
  - [RoPE-Bias](wiki/concepts/RoPE-Bias.md)
source_span: ev::9577::bias_extrapolation_vis
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-04-03-Bias项的神奇作用-RoPE-Bias-更好的长度外推性.md
source_ids:
  - 9577
status: draft
updated: 2026-06-12
---

# spaces-9577-RoPE-Bias注意力矩阵局部化可视化

## Claim
开启投影Bias项的RoPE注意力矩阵在超长测试样本下能够自动呈现显著的局部化衰减趋势

## Section
实验结果

## Notation Mapping
- $Bias$: Projection layer bias terms a and b
- $Attention\_decay$: Attention value drop-off curve over distance

## Steps
1. 构建基于 GAU-α 架构的模型，在序列长度为 512 的数据集上进行常规自回归预训练。
2. 实验组开启 Query 和 Key 投影层的 Bias 项，对照组关闭（其他层的 Bias 均保持去掉状态）。
3. 训练完成后，使用同一个超长文本样本进行前推，将输入长度拉长到 4096，并绘制某一层自注意力权重矩阵的值随相对距离的分布图。
4. 无 Bias 的对照模型在超过 512 距离后，其注意力数值开始异常上升，失去了局部化，导致长度外推崩溃。
5. 有 Bias 的实验模型，其注意力矩阵在长距离上始终呈现非常明显的单调衰减趋势（尤其在靠近输入的层），证明偏置项在 RoPE 作用下被自动训练成了局部化阻尼器。