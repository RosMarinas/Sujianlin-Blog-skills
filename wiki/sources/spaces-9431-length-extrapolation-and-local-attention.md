---
type: article_summary
title: "Transformer升级之路：7、长度外推性与局部注意力"
article_id: "9431"
source_url: https://spaces.ac.cn/archives/9431
date: 2023-01-12
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
series: [Transformer升级之路]
topics: [长度外推, 局部注意力]
concepts: [Length Extrapolation, Local Attention]
methods: [ALIBI, KERPLE, Sandwich, XPOS]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
source_ids:
  - "9431"
status: draft
updated: 2026-06-09
---

# Transformer升级之路：7、长度外推性与局部注意力

## 文章核心问题
Transformer长度外推失败的根因是什么？能否通过简单方法大幅提升长度外推能力？主流长度外推方法的核心机制是什么？

## 主要结论
- 训练和预测之间存在两个不一致导致长度外推失败：(1) 预测使用训练中未见过的位置编码（即使Sinusoidal/RoPE等函数式编码，其高频振荡也使外推不可预测），(2) 预测处理的token比训练多，增加了注意力熵，使注意力分布更加均匀。
- 提出的"超强基线"方案极为简单：预测时应用Attention Mask，限制每个token只看到训练长度窗口内的token。这同时解决了两个问题——限制token数量（解决熵问题），且位置相对于当前token计数，不使用未训练的位置。
- 该基线达到接近SOTA的结果，成为"超强基线"，大多数后续工作几乎无法在此基础上改进。
- 分析四种主要长度外推方法（ALIBI、KERPLE、Sandwich、XPOS）后得出结论：所有这些方法本质上都是局部注意力基线的变体。
- 核心结论：**所有有效的语言模型长度外推方法本质上都是局部注意力的变体**。局部注意力是关键机制，而非位置编码的具体形式。

## 推导结构
首先诊断Transformer长度外推失败的两个根本原因（位置编码不一致和注意力熵不一致），然后提出极简的Attention Mask基线解决方案。接着分析四种主流方法（ALIBI、KERPLE、Sandwich、XPOS），分别展示它们如何等价于局部注意力机制的变体：ALIBI通过在softmax前添加线性偏置实现"平滑版"硬掩码；KERPLE用可训练参数泛化距离惩罚函数；Sandwich通过Sinusoidal内积实现振荡衰减；XPOS通过指数衰减因子配合Blockwise Causal Attention确认局部注意力是关键机制。

## 关键公式
- Attention Mask机制: 限制每个token只看到训练长度窗口内的token
- ALIBI偏置: $-\lambda|m-n|$（在softmax前加入）
- KERPLE泛化: $-\lambda_1 |m-n|^{\lambda_2}$ 或 $-\lambda_1 \log(1+\lambda_2|m-n|)$
- Sandwich: $PE(pos_m)^{\top}PE(pos_n)$ 加入注意力分数
- XPOS衰减: $Q_m \leftarrow \xi^m Q_m$, $K_n \leftarrow \xi^{-n} K_n$

## 体现的方法
- ALIBI: 在softmax前添加线性距离偏置 $-\lambda|m-n|$
- KERPLE: 使用可训练参数 $r_1, r_2$ 泛化距离惩罚函数（幂函数或对数形式）
- Sandwich: 将Sinusoidal位置编码内积加入注意力分数
- XPOS: 在RoPE基础上引入指数衰减因子 $\xi^m$ 和 $\xi^{-n}$

## 所属系列位置
Transformer升级之路系列第7篇，系统分析长度外推问题。

## 与其他文章的关系
本文是整个系列中长度外推主题的开篇之作。诊断的两大不一致（位置编码和注意力熵）为第8篇（位置鲁棒性与Randomized Positional Training）和第9篇（HWFA）的问题分析和方案设计提供了理论框架。核心结论"局部注意力是关键机制"贯穿了后续所有长度外推相关研究。

## 原文证据锚点
- 两大不一致诊断和分析：位置编码不一致和注意力熵不一致
- Attention Mask基线在长度外推上接近SOTA的表现
- ALIBI、KERPLE、Sandwich、XPOS被证明是局部注意力变体
- 核心结论：所有有效长度外推方法本质上都是局部注意力变体
