---
type: topic
title: Attention效率与归一化
aliases:
  - Attention Efficiency and Normalization
scope: 本主题关注Transformer架构中的自注意力计算瓶颈优化、自注意力层的计算效率改进（如线性注意力、门控注意力与分块混合注意力）、不同层归一化策略（Pre-Norm与Post-Norm）的稳定性与表达力对比，以及位置编码（绝对与相对位置编码）的数学演化与拟合缺陷。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-05-25-Google新作Synthesizer-我们还不够了解自注意力.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-07-修改Transformer结构-设计一个更快更好的MLM模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-03-让研究人员绞尽脑汁的Transformer位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-09-线性Transformer应该不是你要等的那个模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-11-门控注意力单元-GAU-还需要Warmup吗.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-21-RoFormerV2-自然语言理解的极限探索.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-29-为什么Pre-Norm的效果不如Post-Norm.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
source_ids:
  - "7325"
  - "7430"
  - "7661"
  - "8130"
  - "8610"
  - "8934"
  - "8990"
  - "8998"
  - "9009"
  - "9105"
concepts:
  - [[concept:Attention Low Rank Bottleneck]]
  - [[concept:Talking-Heads Attention]]
  - [[concept:Google Synthesizer]]
  - [[concept:T-TA (Transformer-based Text Autoencoder)]]
  - [[concept:Gated Attention Unit]]
  - [[concept:Mixed Chunk Attention]]
  - [[concept:RoFormerV2]]
  - [[concept:Pre-Norm vs Post-Norm]]
  - [[concept:Relative Position Encoding Flaw]]
  - [[concept:Absolute Positional Encoding]]
  - [[concept:Relative Positional Encoding]]
  - [[concept:l2 Attention Normalization]]
methods:
  - [[method:增大key_size解除注意力低秩瓶颈]]
  - [[method:Talking-Heads Attention 混合注意力分布]]
  - [[method:Synthesizer静态注意力生成]]
  - [[method:T-TA结构与共享键值防泄漏法]]
  - [[method:门控注意力与FFN的融合方法 (GAU)]]
  - [[method:分块混合注意力自注意力线性化 (MCA)]]
  - [[method:RoFormerV2 结构极简与有监督多任务预训练]]
  - [[method:动态残差缩放稳定收敛法]]
  - [[method:l2 注意力归一化方法]]
status: draft
updated: 2026-06-12
---

# Attention效率与归一化

## Scope
本主题关注Transformer架构中的自注意力计算瓶颈优化、自注意力层的计算效率改进（如线性注意力、门控注意力与分块混合注意力）、不同层归一化策略（Pre-Norm与Post-Norm）的稳定性与表达力对比，以及位置编码（绝对与相对位置编码）的数学演化与拟合缺陷。

## Summary
在Transformer架构的发展历程中，自注意力（Self-Attention）和层归一化（Layer Normalization）是决定模型速度、显存占用、训练稳定性和拟合表达能力的核心模块。本主题汇集了对这些底层算子的优化与改进研究：
1. **注意力效率与表示瓶颈**：包括解耦 key_size 与 head_size 消除低秩瓶颈、多头融合的 Talking-Heads、以及静态/无交互注意力 Synthesizer。此外还包括门控注意力单元（GAU）与 FFN 的深度融合设计，以及结合局部与全局局部注意力的 Mixed Chunk Attention（MCA）线性化自注意力方案（FLASH）。
2. **归一化与稳定性**：探讨了 Pre-Norm 与 Post-Norm 的深度退化差异，分析了 GAU 在初始化时的特征对角化缩放原理，并提供了动态残差缩放等稳定 Post-Norm 从零预训练的技术。
3. **位置编码演化与缺陷**：系统梳理了绝对与相对位置编码的设计演化（如 Shaw、XLNet、T5、DeBERTa、RoPE），并深入剖析了概率归一化自注意力在全同输入下的空间分辨缺陷，提出了以 $l_2$ 归一化为代表的对策。
