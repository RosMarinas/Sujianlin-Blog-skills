---
type: method
operation_types:
  primary: Structure-expose by factorization
  secondary: []
title: 用条件Normalization融合外部条件
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-12-14-基于Conditional-Layer-Normalization的条件文本生成.md
source_ids:
  - 7124
method_summary: 将外部条件向量投影成 Layer Normalization 的 gamma/beta 增量，以零初始化仿射调制融合条件。
typical_structure: |
  1. 将外部输入的条件变量映射为固定维度的条件表示向量。
  2. 使用零初始化的全连接层（或其他不干扰预训练权重的变换），将条件向量分别映射到与 Layer Normalization 的 $\gamma$ 和 $\beta$ 同维度的增量。
  3. 将映射出的条件增量加到原有的 $\gamma$ 和 $\beta$ 参数上。
  4. 训练模型时，条件向量即可通过这种轻量级的偏置调制网络内部的特征分布，实现对生成过程的引导。
applicability: 需要将复杂结构分解为独立或易于计算的因子时，尤其是在使用已预训练的 Transformer 模型进行受控文本生成、Image Caption或多模态融合时。
evidence_spans:
  - ev::7124::受到图像条件BN的启发，文章提出了将外部条件向量通过全零初始化的映射矩阵变换后叠加到 Transformer 的 Layer Normalization 的 $\gamma$ 和 $\beta$ 上，实现不破坏预训练分布的条件文本生成。
examples:
  - [[spaces-7124-Conditional-Layer-Normalization条件生成]]
status: stable
updated: 2026-06-13
---

# 用条件Normalization融合外部条件

## 适用问题

需要将复杂结构分解为独立或易于计算的因子时，尤其是在使用已预训练的 Transformer 模型进行受控文本生成、Image Caption或多模态融合时。

## 核心变换

摒弃直接在输入前拼接 embedding 这种极度容易破坏预训练模型分布的做法，而是将外部全局变量柔和地转化成特定层级的仿射变换干扰量（缩放 $\gamma$ 与偏置 $\beta$）打入每一层的激活输出。

## 典型步骤

1. 将外部输入的条件变量映射为固定维度的条件表示向量。
2. 使用零初始化的全连接层（或其他不干扰预训练权重的变换），将条件向量分别映射到与 Layer Normalization 的 $\gamma$ 和 $\beta$ 同维度的增量。
3. 将映射出的条件增量加到原有的 $\gamma$ 和 $\beta$ 参数上。
4. 训练模型时，条件向量即可通过这种轻量级的偏置调制网络内部的特征分布，实现对生成过程的引导。

## 直觉

归一化层不仅用来拉平分布以帮助训练，它还定义了该层输出的方差和均值，从而实际控制了下游神经元的激活倾向。通过零初始化保证第一步是无条件恒等映射，随后逐渐让模型学会使用注入的全局方差/均值增量进行偏向性调制，实现优雅的先验条件渗透。

## 边界

依赖模型具备足够多的标准化层以便均匀散播外部条件；如果条件特征极为局部或精细（比如逐个像素的空间控制），全局的 $\gamma/\beta$ 调整可能会缺乏分辨率；零初始化如果用在太深的前向层也存在一定数值学习死区。

## 例子

在图像描述（Image Caption）中，用一个卷积网络编码整幅图片的固定长度向量作为输入。将该向量映射到文本语言模型内部每个 Layer Norm 层的 $\gamma$ 和 $\beta$ 增量中，迫使预训练的自然语言模型在描述该对象时能够参考图像偏置生成相关的单词流。

## 证据

- ev::7124::受到图像条件BN的启发，文章提出了将外部条件向量通过全零初始化的映射矩阵变换后叠加到 Transformer 的 Layer Normalization 的 $\gamma$ 和 $\beta$ 上，实现不破坏预训练分布的条件文本生成。
