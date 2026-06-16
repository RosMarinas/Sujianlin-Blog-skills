---
type: article_summary
title: Transformer升级之路：15、Key归一化助力长度外推
article_id: "9859"
source_url: https://spaces.ac.cn/archives/9859
date: 2023-11-20
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-11-20-Transformer升级之路-15-Key归一化助力长度外推.md
series: [Transformer升级之路]
topics: [位置编码, 长度外推, Key归一化, Attention机制]
concepts: [key-normalization, cosine-attention]
methods: [key-normalization]
problem_patterns: [长度外推, Attention泛化, cos训练不充分]
evidence_spans:
  - 9859-最初动机
  - 9859-先看结果
  - 9859-原理分析
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-20-Transformer升级之路-15-Key归一化助力长度外推.md
source_ids:
  - "9859"
status: draft
updated: 2026-06-09
---

## 文章核心问题

能否通过修改Attention的归一化方式来改善长度外推能力？

## 主要结论

1. KeyNorm（对Attention的Key序列做L2归一化）显著提升长度外推能力——KNA在4096不重复测试中达47.69%，远超Baseline的23.16%。
2. 核心原因是：模型倾向于优先增大||k_j||而非调整cos(q_i,k_j)，导致cos训练不充分；KeyNorm强制模型充分训练cos。
3. KeyNorm+RoPE的组合是必要的——KeyNorm+NoPE无长度外推能力。
4. KeyNorm是"事前修改"方案，外推时不需修改模型，且没有局部约束，比ALIBI等更有Scale Up潜力。
5. KeyNorm似乎"免疫"已有RoPE外推技巧（NTK、YaRN叠加后提升不大），但本身已具备较强外推能力。

## 推导结构

1. 从替代Scaled Dot-Product Attention的归一化方式的动机出发
2. 引出QNA（QueryNorm）、KNA（KeyNorm）、CosA三种变体
3. 实验发现KNA意外具有长度外推能力
4. 从几何角度分析：s(j|i) = ||q_i|| ||k_j|| cos(q_i,k_j)，KeyNorm强制训练cos
5. 断言：cos(q_i,k_j)训练不充分是Attention无法长度外推的主要原因

## 关键公式

KNA: o_i = Σ exp(q_i · k̃_j) v_j / Σ exp(q_i · k̃_j), k̃_j = k_j / ||k_j||

CosA: o_i = Σ exp(λ cos(q_i,k_j)) v_j / Σ exp(λ cos(q_i,k_j))

## 体现的方法

- Key Normalization（KeyNorm）长度外推方法

## 所属系列位置

第15篇，独立于ReRoPE路线的新发现。

## 与其他文章的关系

- 原理分析引出第16篇（复盘）的系统性讨论
- 与HWFA同属"事前修改"类别
- KeyNorm+NoPE无外推能力，说明RoPE在其中的关键作用
- 与2010.04245 (Query-Key Normalization for Transformers)和2302.05442 (Scaling ViT to 22B)相关

## 原文证据锚点

- 最初动机: 原文"最初动机"节，从替换Scale方式引出QNA/KNA/CosA
- 先看结果: 原文"先看结果"节，KNA在4096不重复测试中达47.69%，远超Baseline的23.16%
- 原理分析: 原文"原理分析"节，给出s(j|i)的几何分解，断言cos训练不充分是主因
