---
type: article_summary
title: MoE环游记：5. 均匀分布的反思
article_id: "10945"
source_url: https://spaces.ac.cn/archives/10945
date: 2025-05-16
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-05-16-MoE环游记-5-均匀分布的反思.md
source_html: Data/Spaces_ac_cn/raw/articles/10945/page.html
series:
  - "[[MoE环游记]]"
topics:
  - "[[MoE路由与负载均衡]]"
concepts:
  - "[[Shared Expert]]"
  - "[[Fine-Grained Expert]]"
  - "[[MoE负载均衡]]"
methods: []
problem_patterns:
  - "[[在均衡与主任务效果之间调节干预强度]]"
evidence_spans:
  - ev::10945::共享专家
  - ev::10945::非均匀性
  - ev::10945::细颗粒度
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-05-16-MoE环游记-5-均匀分布的反思.md
source_ids:
  - "10945"
status: draft
updated: 2026-06-09
---

# MoE环游记：5. 均匀分布的反思

## 文章核心问题

本文反思“均匀负载是否总是最优”，并通过 Shared Expert 与 Fine-Grained Expert 解释 MoE 中合理非均匀性的价值。

## 主要结论

- Shared Expert 固定激活一小部分专家，把共同知识集中起来，让 Routed Expert 更专注。
- Shared Expert 可被理解为 Routed Expert 的均值或残差基准，有助于使几何近似中的正交假设更合理。
- 现实知识分布并不均匀，单纯追求全体 Expert 的均匀分布未必是效果最优。
- Fine-Grained Expert 在参数量和激活量不变时扩大组合空间，但也会增加负载均衡和通信成本。

## 推导结构

1. 从 Shared Expert 的公式形式进入。
2. 给出残差、共同知识压缩和几何均值三种理解。
3. 用比例因子平衡 Shared 与 Routed Expert。
4. 从非均匀性解释 Fine-Grained Expert 的收益和边界。

## 关键公式

- Shared Expert 的比例因子估计仍依赖 [[MoE基本路由公式]] 的 Expert 求和结构。

## 体现的方法

候选方法记录在 [[_candidates]]：用结构拆分表达合理的非均匀负载。

## 所属系列位置

这是系列第五篇，在连续几篇负载均衡之后补上反思：均衡是效率约束，不一定是知识分布的最终目标。

## 与其他文章的关系

- continues: `article::10815`
- precedes: `article::11619`
- contrasts_with: `concept::MoE负载均衡`

## 原文证据锚点

- `ev::10945::共享专家`：第 20-34 行定义 Shared Expert 并说明参数量和推理成本不变。
- `ev::10945::非均匀性`：第 84-95 行指出均匀分布未必最优，Routed Expert 均匀更多是效率折中。
- `ev::10945::细颗粒度`：第 97-110 行解释 Fine-Grained Expert 的组合多样性和覆盖视角。
