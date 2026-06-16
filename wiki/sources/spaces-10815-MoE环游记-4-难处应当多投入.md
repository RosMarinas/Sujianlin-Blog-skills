---
type: article_summary
title: MoE环游记：4. 难处应当多投入
article_id: "10815"
source_url: https://spaces.ac.cn/archives/10815
date: 2025-03-28
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-03-28-MoE环游记-4-难处应当多投入.md
source_html: Data/Spaces_ac_cn/raw/articles/10815/page.html
series:
  - "[[MoE环游记]]"
topics:
  - "[[MoE路由与负载均衡]]"
concepts:
  - "[[动态专家激活]]"
  - "[[Loss-Free偏置]]"
methods:
  - "[[用对偶偏置改写路由约束]]"
problem_patterns:
  - "[[在均衡与主任务效果之间调节干预强度]]"
evidence_spans:
  - ev::10815::设计思想
  - ev::10815::优化目标
  - ev::10815::文章小结
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-03-28-MoE环游记-4-难处应当多投入.md
source_ids:
  - "10815"
status: draft
updated: 2026-06-09
---

# MoE环游记：4. 难处应当多投入

## 文章核心问题

本文利用 Loss-Free 偏置的冗余自由度，把固定 Top-k 激活推广为每个 Token 动态选择 Expert 数量。

## 主要结论

- 动态 MoE 可以用阈值形式 `rho_i + b_i > 0` 替代 Top-k 排序。
- 偏置更新要同时控制 Expert 负载均衡和平均激活预算。
- 负载均衡与预算控制可以合并为让未归一化负载 `tilde F` 接近 `kQ`。
- RMS Norm 替代 sign 是一个减小震荡的通用技巧，但收益有限。

## 推导结构

1. 从 Loss-Free 的 `argtop_k rho+b` 出发。
2. 改为 `argwhere rho+b>0` 实现动态激活数量。
3. 拆分并合并负载均衡与预算控制目标。
4. 讨论初始化、相关工作和简化更新。

## 关键公式

- [[Loss-Free偏置更新]]：本文复用并改写偏置更新。

## 体现的方法

- [[用对偶偏置改写路由约束]]：用同一个偏置同时承载均衡和预算控制。

## 所属系列位置

这是系列第四篇，把 Loss-Free 从固定激活数推进到动态激活，为第七篇的动态 QB 提供直觉先导。

## 与其他文章的关系

- continues: `article::10757`
- precedes: `article::10945`
- motivates: `concept::动态专家激活`

## 原文证据锚点

- `ev::10815::设计思想`：第 22-36 行提出 `rho+b>0` 的动态激活形式。
- `ev::10815::优化目标`：第 38-64 行给出负载均衡与预算控制的偏置更新。
- `ev::10815::文章小结`：第 129-131 行总结利用 Bias 额外自由度实现动态 Expert 数目。
