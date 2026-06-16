---
type: article_summary
title: Transformer升级之路：16、"复盘"长度外推技术
article_id: "9948"
source_url: https://spaces.ac.cn/archives/9948
date: 2024-01-26
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-01-26-Transformer升级之路-16-复盘-长度外推技术.md
series: [Transformer升级之路]
topics: [长度外推, 综述, ReRoPE, YaRN, NTK-RoPE, KeyNorm, HWFA, Dynamic Scaling]
concepts: [length-extrapolation, rerope, yarn, ntk-aware-scaled-rope, key-normalization, dynamic-scaling]
methods: [rerope-window-extension, leaky-rerope, ntk-aware-scaled-rope, key-normalization, positional-interpolation, yarn, dynamic-scaling, hybrid-window-full-attention]
problem_patterns: [长度外推, 相对位置OOD, 外推税, 远程依赖保持]
evidence_spans:
  - 9948-问题定义
  - 9948-旋转位置
  - 9948-窗口截断
  - 9948-位置内插
  - 9948-保近压远
  - 9948-转圈视角
  - 9948-一些插曲
  - 9948-拒绝交税
  - 9948-另起炉灶
  - 9948-其他思路
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-01-26-Transformer升级之路-16-复盘-长度外推技术.md
source_ids:
  - "9948"
status: draft
updated: 2026-06-09
---

## 文章核心问题

系统性地"复盘"过去一年长度外推技术的发展，串联各方法背后的思想，分析免训练长度外推的关键。

## 主要结论

1. 免训练长度外推的要领是"保近压远"——保证局部不失真、压缩远处不越界。
2. "转圈视角"揭示了更本质的OOD问题：关键不是位置编号是否越界，而是单位圆上的点是否被充分训练过——高频维度因转圈多而训练充分，低频维度需内插。
3. YaRN从转圈视角出发，通过圈数阈值τ决定各维度的内插比例，外加log scale因子，效果仅次于Leaky ReRoPE但实现最简单。
4. 所有免训练方法都存在"外推税"（训练长度内效果变差），Dynamic Scaling和CLEX可减轻此问题。
5. "另起炉灶"路线（HWFA、KeyNorm）通过修改架构实现不修改模型的外推。
6. 长度外推依然很神秘——许多方法可能跟架构绑定，ReRoPE在训练时使用反而无外推能力。

## 推导结构

1. 问题定义：Train Short, Test Long；评测应以不牺牲远程依赖为前提
2. RoPE为何成为主流位置编码
3. 窗口截断方案及Attention Sinks发现
4. 位置内插（PI）及其局限
5. "保近压远"的ReRoPE/Leaky ReRoPE
6. "转圈视角"分析OOD本质
7. 从NTK-RoPE到YaRN的发展
8. "外推税"与Dynamic Scaling
9. "另起炉灶"的HWFA和KeyNorm
10. 其他相关工作

## 关键公式

YaRN: θ_i^new = [γ_i + (1-γ_i)L_train/L_test]θ_i, γ_i由圈数r_i决定

NTK-RoPE: κ = (L_test/L_train)^{d/(d-2)}

Dynamic Scaling: s(pos) = max(L_train, pos+1) / L_train

## 体现的方法

- 综述了PI, NTK-RoPE, NTK-RoPE-mixed, ReRoPE, Leaky ReRoPE, YaRN, Dynamic Scaling, HWFA, KeyNorm等全部主流方法

## 所属系列位置

第16篇，是对第7-15篇（整个长度外推专题）的总结性复盘。

## 与其他文章的关系

- 直接回顾了第7-15篇所有长度外推相关文章的发现
- 介绍了YaRN、CLEX、Self-Extend、Attention Sinks等外部工作
- 讨论了NTK-RoPE的起源（Bowen Peng）和其在免训练外推中的里程碑意义

## 原文证据锚点

- 问题定义: 原文"问题定义"节，提出远程依赖评测方案
- 旋转位置: 原文"旋转位置"节，讨论RoPE为何成为主流
- 窗口截断: 原文"窗口截断"节，Attention Sinks的发现（开头Token的重要性）
- 位置内插: 原文"位置内插"节，位置内插的局部分辨率失真问题
- 保近压远: 原文"保近压远"节，ReRoPE/Leaky ReRoPE的原理
- 转圈视角: 原文"转圈视角"节，单位圆训练的圈数分析
- 一些插曲: 原文"一些插曲"节，NTK-RoPE和YaRN的起源与推导
- 拒绝交税: 原文"拒绝交税"节，外推税和Dynamic Scaling的概念
- 另起炉灶: 原文"另起炉灶"节，HWFA和KeyNorm的事前修改路线
- 其他思路: 原文"其他思路"节，讨论了训练时扰动、调小base等
