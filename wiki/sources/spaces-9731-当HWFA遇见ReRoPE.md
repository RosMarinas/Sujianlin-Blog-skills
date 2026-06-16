---
type: article_summary
title: Transformer升级之路：14、当HWFA遇见ReRoPE
article_id: "9731"
source_url: https://spaces.ac.cn/archives/9731
date: 2023-08-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-08-24-Transformer升级之路-14-当HWFA遇见ReRoPE.md
series: [Transformer升级之路]
topics: [位置编码, 长度外推, HWFA, ReRoPE, 混合注意力]
concepts: [hwfa, rerope]
methods: [hybrid-window-full-attention, rerope-window-extension]
problem_patterns: [长度外推, 推理效率, 训练效果保持]
evidence_spans:
  - 9731-温故
  - 9731-知新
  - 9731-实验
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-24-Transformer升级之路-14-当HWFA遇见ReRoPE.md
source_ids:
  - "9731"
status: draft
updated: 2026-06-09
---

## 文章核心问题

ReRoPE推理成本增加的问题如何通过架构设计来缓解？能否将HWFA与ReRoPE结合实现"强强联合"？

## 主要结论

1. HWFA+ReRoPE（称为HWFA2）将训练阶段HWFA原本的Full NoPE Attention换成Full RoPE Attention，推理阶段改为Full ReRoPE Attention，大幅降低ReRoPE的额外成本。
2. HWFA2恢复了Full Attention的RoPE，放宽了Window Attention的感受野约束，允许Full Attention放在中间层且可多于1层，弥补了原HWFA的效果损失。
3. 最佳配置（w64-f2，即Window感受野64、2层Full Attention）的训练效果（49.46%）和不重复外推效果（49.36%）均接近或超过原ReRoPE。
4. HWFA2兼具ReRoPE的长外推能力和HWFA的低推理成本优势。

## 推导结构

1. 回顾HWFA（L-1层Window RoPE + 1层Full NoPE）的设计
2. 提出将Full NoPE替换为Full RoPE（训练）/ Full ReRoPE（推理）
3. 讨论Window感受野放宽、Full层数和位置调整带来的自由度
4. 实验对比不同参数组合

## 关键公式

HWFA2 = (L-1层Window RoPE Attention) + (f层Full RoPE/ReRoPE Attention)

Window感受野w̃的最佳取值约为N/L的2~4倍

## 体现的方法

- HWFA2（HWFA + ReRoPE结合）

## 所属系列位置

第14篇，解决第12篇ReRoPE的推理效率问题。

## 与其他文章的关系

- 前驱：第12篇（ReRoPE）、第9篇（HWFA原版）
- 后续独立的Zebra方法（arXiv 2312.08618）与HWFA2类似
- 第16篇（复盘）中将HWFA2与HWFA、KeyNorm等对比

## 原文证据锚点

- 温故: 原文"温故"节，回顾HWFA设计：L-1层Window RoPE + 1层Full NoPE
- 知新: 原文"知新"节，提出HWFA2，将Full NoPE替换为Full RoPE（训练）/ Full ReRoPE（推理），放宽窗口约束
- 实验: 原文"实验"节，HFWA-ReRoPE-w64-f2在训练512达49.46%，4096不重复达49.36%；最佳感受野约为N/L的2-4倍
