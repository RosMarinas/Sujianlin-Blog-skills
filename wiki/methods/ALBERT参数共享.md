---
type: method
title: "ALBERT参数共享"
aliases:
  - "ALBERT"
  - "A Lite BERT"
operation_types:
  primary: "Decompose / reduce dimension"
  secondary:
    - "Structure-expose by factorization"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-10-29-用ALBERT和ELECTRA之前-请确认你真的了解它们.md
source_ids:
  - "7846"
method_summary: "BERT的参数共享版本，所有Transformer层共享同一组参数，大幅减少参数量。"
typical_structure: |
  1. y=f(f(...f(x)))层间参数共享
  2. Embedding矩阵分解VH
  3. 仅在大规格下效果有提升
applicability: "模型体积受限的场景"
tools:
  - 参数共享
  - 矩阵分解
related_methods: []
examples:
  - [[article::7846]]
status: draft
updated: 2026-06-13
---

## 适用问题

需要减少模型参数量或模型体积的场景，如部署到存储受限设备、快速实验迭代。ALBERT通过参数共享和Embedding分解大幅压缩参数量。

## 核心变换

**输入**：标准BERT架构（$n$层Transformer，每层参数独立）
**输出**：参数共享的轻量变体

将原本各层独立的参数替换为全局共享：
$$
y = f_n(f_{n-1}(\cdots(f_1(x)))) \quad\rightarrow\quad y = f(f(\cdots(f(x))))
$$
即所有$n$层使用同一组参数$f$，参数量减少到原来的$1/n$。同时将Embedding矩阵分解为$VH$，其中$V$为小维度（典型值128），进一步压缩词嵌入参数量。

## 典型步骤

1. **加载ALBERT模型**：使用`build_transformer_model`加载预训练权重，指定`model='albert'`
2. **前向计算**：逐层执行相同的Transformer层（参数共享不影响计算图结构，仅减少参数存储）
3. **Embedding分解**：先通过小矩阵$V$映射到低维，再通过$H$映射回原始维度
4. **微调或下游任务**：与标准BERT相同流程，但注意小规格版本（tiny/small/base）效果不如同规格BERT

## 直觉

参数共享本质是一种**强正则化**手段。每层被迫学习相同的变换，限制了模型的表达能力，但同时也减少了过拟合风险。在大规模模型（xxlarge）中，参数量冗余大，共享带来的正则化效果反而能提升泛化性能。对小模型而言，表达能力已经受限，参数共享进一步削弱了模型容量，因此效果不如同规格BERT。

Embedding分解的直觉：词表通常很大（数万），但每个词的语义可以压缩到低维空间（如128维），先降维再升维的矩阵分解减少了参数量，且信息损失有限。

## 边界

- **不加速推理**：参数共享仅减少参数量（存储），前向计算仍需逐层执行，因此推理速度与同规格BERT相同，甚至因Embedding分解略慢
- **仅大规格有效**：不到xlarge版本没必要用ALBERT，同一速度的ALBERT效果比BERT差，同一效果的ALBERT速度比BERT慢
- **需要MLM权重时不可用**：ALBERT主体是Encoder，不保留MLM预测头，若需用MLM做文本生成或纠错，应选标准BERT
- 若只需体积小，可考虑BERT tiny/small版，速度相同且效果更优

## 例子

- ALBERT-xxlarge在GLUE等基准上稳定超越BERT-large，但需更大显存
- base版ALBERT训练速度仅比BERT base快10%~20%，显存缩小幅度类似
- 加载ALBERT权重后放开参数共享约束（当BERT用），效果有进一步提升（参考实验：article 7187）

## 证据

- ev::7846::ALBERT参数共享机制：$y=f(f(\cdots(f(x)))$将$n$层参数压缩为1层
- ev::7846::Embedding分解VH：小维度$V$（典型128）压减词表参数量
- ev::7846::规格对比：tiny/small/base不如同规格BERT，仅xxlarge稳定超越BERT-large
- ev::7846::推理速度：参数共享不加速前向计算
