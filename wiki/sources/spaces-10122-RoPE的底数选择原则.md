---
type: article_summary
title: Transformer升级之路：18、RoPE的底数选择原则
article_id: "10122"
source_url: https://spaces.ac.cn/archives/10122
date: 2024-05-29
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-05-29-Transformer升级之路-18-RoPE的底数选择原则.md
series: [Transformer升级之路]
topics: [RoPE, 底数选择, 语义聚合, 位置编码]
concepts: [rope-base-selection, partial-rope]
methods: []
problem_patterns: [RoPE底数选择, 长上下文训练, 语义聚合保持]
evidence_spans:
  - 10122-期望性质
  - 10122-不等关系
  - 10122-数值求解
  - 10122-渐近估计
  - 10122-相关思考
  - 10122-部分旋转
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-05-29-Transformer升级之路-18-RoPE的底数选择原则.md
source_ids:
  - "10122"
status: draft
updated: 2026-06-09
---

## 文章核心问题

RoPE的底数b应该怎样选择？更大的训练长度是否需要更大的底数？这不仅是为了配合"先短后长"的训练策略吗？

## 主要结论

1. 从"语义聚合"期望性质出发，要求f_b(m) = Σ cos(m·b^{-2i/d}) ≥ 0对所有m∈[0,L-1]恒成立，从而导出b的下界b*随L增大而增大。
2. 数值求解给出了b*的具体值：L=4K时b*=2.7e4，L=8K时b*=8.4e4，L=1M时b*=6.5e7。
3. 渐近分析给出b* = O(L)的粗略估计。
4. 部分旋转（Partial RoPE）从该视角看可能更优——自动满足不等式，且具有更好的语义聚合能力。
5. 更大的训练长度本就应该选择更大的底数，而不单是为了配合NTK-RoPE的"先短后长"策略。
6. LLAMA3的b=500000（训练长度8K）明显偏大，可能是为更长文本预留。

## 推导结构

1. 提出RoPE的两个期望性质：远程衰减和语义聚合
2. 从语义聚合的期望性质出发推导出不等式条件
3. 数值求解b*（用暴力搜索法）
4. 渐近估计（积分近似）给出O(L)量级
5. 结合β进制类比讨论
6. 分析部分旋转及其优势

## 关键公式

语义聚合不等式: Σ cos(m·b^{-2i/d}) ≥ 0, m∈{0,...,L-1} (neq:base)

数值结果: L=4K→b*=2.7e4, L=8K→b*=8.4e4

渐近估计: b ≥ L/x₀ ≈ 2L

## 体现的方法

- 无——这是一篇理论分析文章

## 所属系列位置

第18篇，深入分析RoPE的理论性质。

## 与其他文章的关系

- 基于第1篇（Sinusoidal追根溯源）和第10篇（β进制编码）的分析
- 解释了第15篇（KeyNorm）中Partial RoPE的理论基础
- 与GPT-NeoX的部分旋转实验相关
- 与LLAMA3的RoPE底数选择相关

## 原文证据锚点

- 期望性质: 原文"期望性质"节，提出远程衰减和语义聚合两个期望性质
- 不等关系: 原文"不等关系"节，推导出语义聚合不等式(neq:base)
- 数值求解: 原文"数值求解"节，给出L=4K→b*=2.7e4等数值结果
- 渐近估计: 原文"渐近估计"节，给出b≥L/x₀≈2L的渐近估计
- 相关思考: 原文"相关思考"节，讨论β进制类比的结论b≥L，以及LLAMA3的b=500000
- 部分旋转: 原文"部分旋转"节，Partial RoPE自动满足不等式，DeepSeek MLA也应用了此设计
