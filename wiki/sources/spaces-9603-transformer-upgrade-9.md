---
type: article_summary
title: "Transformer升级之路：9、一种全局长度外推的新思路"
article_id: "9603"
source_url: https://spaces.ac.cn/archives/9603
date: 2023-05-12
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-05-12-Transformer升级之路-9-一种全局长度外推的新思路.md
series: [Transformer升级之路]
topics: [长度外推, 混合注意力]
concepts: [Length Extrapolation]
methods: [Hybrid Window-Full Attention]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-12-Transformer升级之路-9-一种全局长度外推的新思路.md
source_ids:
  - "9603"
status: draft
updated: 2026-06-09
---

# Transformer升级之路：9、一种全局长度外推的新思路

## 文章核心问题
如何在保持全局依赖建模能力的同时实现长度外推？现有方法在GAU + Post-Norm架构上为何失败？HWFA能否成为兼容两者的唯一方案？

## 主要结论
- 提出**混合窗口-全局注意力（Hybrid Window-Full Attention, HWFA）**，是目前唯一能在Post-Norm GAU网络上同时实现长度外推和保持全局依赖的方法。
- HWFA架构：前 $L-1$ 层使用Window Attention + RoPE（窗口大小 $w$ 满足 $(w-1)(L-1)+1 \le \alpha N$），最后一层使用Full Attention + log n缩放（不加RoPE）。
- Window Attention层提供平移不变性并产生i.i.d.特征；最后一层Full Attention对这些i.i.d.特征充当全局池化/检索机制。
- 在GAU_alpha（24层，训练长度512，$w=16$）实验中：测试长度4096时repeat-context达到80.84%（baseline仅24.17%），non-repeat达到48.15%（baseline仅23.16%）。
- Even Pairs任务实现100%外推准确率，验证了真正的全局依赖能力。
- 6项消融实验确认了每个组件的重要性（RoPE、log n、Full Attention层等），具体包括：
  1. Window Attention不加RoPE: 内插和外推均下降
  2. Full Attention加RoPE: 外推下降
  3. Full Attention不加log n因子: 外推下降
  4. 全Window Attention（无Full Attention层）: 两者均下降
  5. L-2层Window + 2层Full: 外推下降
  6. $w=32$（超出训练长度约束）: 外推下降
- Pre-Norm与Post-Norm差异分析解释了为何ALIBI、Sandwich、XPOS等方法在GAU + Post-Norm上失败（Post-Norm维持更严格的有效深度，Pre-Norm有效深度更浅，表示更自然地局部化）。
- 训练精度略低于基线（48.70% vs 49.41%），大参数规模下的扩展性仍需验证。

## 推导结构
首先指出现有局部注意力方法在GAU + Post-Norm架构上失败，然后提出HWFA架构并详细说明其设计原理：Window Attention产生平移不变性和i.i.d.特征，Full Attention充当全局池化。通过6项消融实验验证各组件的必要性。分析Pre-Norm vs Post-Norm的区别，解释为何现有方法在Post-Norm上失败。最后讨论HWFA在大规模参数下的扩展性问题。

## 关键公式
- 窗口大小约束: $(w-1)(L-1)+1 \le \alpha N$，其中 $N$ 为训练长度，$\alpha \le 3/4$ 为推荐值
- Window Attention + RoPE: 前 $L-1$ 层
- Full Attention + log n缩放: 最后一层（不含RoPE）
- Log n缩放因子: $\log_m n$

## 体现的方法
- HWFA（Hybrid Window-Full Attention）: 前 $L-1$ 层使用Window Attention + RoPE，最后一层使用Full Attention + log n缩放
- 平移不变性 + i.i.d.特征用于稳定外推
- 单层Full Attention提供全局依赖能力

## 所属系列位置
Transformer升级之路系列第9篇，提出混合窗口-全局注意力架构。

## 与其他文章的关系
本文在第7篇（局部注意力是核心机制）和第8篇（位置鲁棒性方法）的基础上，提出了兼容全局依赖的长度外推方法。与第7篇的纯局部注意力方案不同，HWFA通过保留一层Full Attention同时实现了全局依赖和长度外推。与第10篇的NTK-RoPE同为GAU + Post-Norm架构上有效的零样本外推方法。

## 原文证据锚点
- HWFA在GAU_alpha上4096 repeat-context达80.84%（baseline 24.17%）
- Even Pairs任务100%外推准确率
- 6项消融实验验证各组件的必要性
- Pre-Norm与Post-Norm差异分析
- 训练精度略低于基线的扩展性担忧
