---
type: article_summary
title: Transformer升级之路：13、逆用Leaky ReRoPE
article_id: "9728"
source_url: https://spaces.ac.cn/archives/9728
date: 2023-08-14
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
series: [Transformer升级之路]
topics: [位置编码, 长度外推, Leaky ReRoPE, 训练时扰动]
concepts: [leaky-rerope, inv-leaky-rerope]
methods: [inv-leaky-rerope]
problem_patterns: [长度外推, 推理效率]
evidence_spans:
  - 9728-回顾
  - 9728-反转
  - 9728-实验
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
source_ids:
  - "9728"
status: draft
updated: 2026-06-09
---

## 文章核心问题

ReRoPE/Leaky ReRoPE虽然外推效果好，但推理成本增加。如何在不牺牲推理速度的前提下保留长度外推能力？

## 主要结论

1. InvLeaky ReRoPE（逆用Leaky ReRoPE）在训练阶段使用窗口外步长>1的Leaky ReRoPE，推理阶段退回常规RoPE，从而保持推理速度不变。
2. 实验结果显示，"Leaky ReRoPE→RoPE"的InvLeaky ReRoPE效果虽不如"RoPE→ReRoPE"，但依然超过HFWA。
3. 最优参数配置：k设置为"扩展倍数的2倍的倒数"，w设置为训练长度的1/4，b可选乘以扩展倍数。
4. 训练速度影响温和：1亿参数GAU模型上训练速度增加不到10%。

## 推导结构

1. 回顾Leaky ReRoPE的窗口内外步长设计
2. 提出"反转"思想：训练阶段窗口外使用>1的大步长，推理阶段使用=1的标准步长
3. 实验对比InvLeaky ReRoPE与之前方案的效果
4. 讨论训练速度影响

## 关键公式

训练阶段使用k=1/16, w=128的Leaky ReRoPE（窗口外步长为16）
推理阶段使用标准RoPE（窗口外步长为1）

## 体现的方法

- InvLeaky ReRoPE（逆用Leaky ReRoPE）

## 所属系列位置

第13篇，紧接第12篇ReRoPE，解决其推理效率问题。

## 与其他文章的关系

- 前驱：第12篇（ReRoPE/Leaky ReRoPE）
- 这种"训练时扰动"的思路与第8篇（位置鲁棒性）有相似之处
- 后续：第14篇（HWFA+ReRoPE）提供了另一种解决方案

## 原文证据锚点

- 回顾: 原文"回顾"节，重述Leaky ReRoPE和ReRoPE的矩阵定义
- 反转: 原文"反转"节，提出训练阶段用大步长Leaky ReRoPE的InvLeaky ReRoPE思想
- 实验: 原文"实验"节，InvLeaky ReRoPE-w128+log n在4096不重复测试中达48.32%，超过HFWA的48.15%；训练速度从330秒/千步增加到350秒/千步
