---
type: article_summary
title: MoE环游记：3. 换个思路来分配
article_id: "10757"
source_url: https://spaces.ac.cn/archives/10757
date: 2025-03-05
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-03-05-MoE环游记-3-换个思路来分配.md
source_html: Data/Spaces_ac_cn/raw/articles/10757/page.html
series:
  - "[[MoE环游记]]"
topics:
  - "[[MoE路由与负载均衡]]"
concepts:
  - "[[Loss-Free偏置]]"
  - "[[MoE负载均衡]]"
methods:
  - "[[用对偶偏置改写路由约束]]"
problem_patterns:
  - "[[将路由选择转化为约束分配问题]]"
evidence_spans:
  - ev::10757::方法大意
  - ev::10757::手搓梯度
  - ev::10757::一脉相承
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-03-05-MoE环游记-3-换个思路来分配.md
source_ids:
  - "10757"
status: draft
updated: 2026-06-09
---

# MoE环游记：3. 换个思路来分配

## 文章核心问题

本文讨论如何绕开 Aux Loss 权重难调的问题，用一个只参与路由排序的偏置项实现负载均衡。

## 主要结论

- Loss-Free 不改变 Router 原始打分的门控值，而是在 Expert 分配时加入偏置 `b`。
- `b_i` 的更新方向由当前负载分布 `F_i` 和目标均匀分布 `1/n` 的差决定。
- 该方案的关键不是“没有损失”，而是把负载均衡参数和 LM Loss 优化参数隔离。
- RMS Norm 更新可以保留误差相对大小，通常比 SignSGD 更自适应。

## 推导结构

1. 比较 Aux Loss 和分配方式改写两条路线。
2. 引入 `argtop_k rho + b`。
3. 从不可导负载均衡目标用 STE 推出 `b` 的更新方向。
4. 解释 Loss-Free 与 Aux Loss 的连续性和参数隔离价值。

## 关键公式

- [[Loss-Free偏置更新]]：以 `b <- b - gamma sign(F-Q)` 记录核心更新。

## 体现的方法

- [[用对偶偏置改写路由约束]]：把约束从主模型参数转移到只影响分配的偏置项。

## 所属系列位置

这是系列第三篇，从 Aux Loss 转入 Loss-Free 路线，是后续动态激活、QB 和 MQB 的偏置形式基础。

## 与其他文章的关系

- continues: `article::10735`
- precedes: `article::10815`
- motivates: `concept::动态专家激活`

## 原文证据锚点

- `ev::10757::方法大意`：第 20-30 行说明引入偏置项并保持训练推理形式一致。
- `ev::10757::手搓梯度`：第 32-59 行从负载分布目标推出 SignSGD 更新。
- `ev::10757::一脉相承`：第 75-83 行指出本质是隔离 Aux Loss 和 LM Loss 的优化参数。
