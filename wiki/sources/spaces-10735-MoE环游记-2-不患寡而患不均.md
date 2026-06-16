---
type: article_summary
title: MoE环游记：2. 不患寡而患不均
article_id: "10735"
source_url: https://spaces.ac.cn/archives/10735
date: 2025-02-21
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-02-21-MoE环游记-2-不患寡而患不均.md
source_html: Data/Spaces_ac_cn/raw/articles/10735/page.html
series:
  - "[[MoE环游记]]"
topics:
  - "[[MoE路由与负载均衡]]"
concepts:
  - "[[MoE负载均衡]]"
  - "[[Aux Loss负载均衡]]"
methods: []
problem_patterns:
  - "[[将路由选择转化为约束分配问题]]"
evidence_spans:
  - ev::10735::需求分析
  - ev::10735::辅助损失
  - ev::10735::直通估计
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-02-21-MoE环游记-2-不患寡而患不均.md
source_ids:
  - "10735"
status: draft
updated: 2026-06-09
---

# MoE环游记：2. 不患寡而患不均

## 文章核心问题

本文解释 MoE 负载均衡为什么必要，并重新推导经典 Aux Loss 为什么能作为促进均衡的训练信号。

## 主要结论

- 负载不均会造成 Dead Expert、Token Drop 和有效参数量下降。
- `F` 表示 Top-k 后的实际负载分布，`P` 是它的光滑近似。
- 经典 Aux Loss 可以从“让 `F` 接近均匀分布 `Q`”的目标出发，用 STE 推导出等效梯度。
- `F·P` 更准确地说是一个等效梯度形式，不应被理解为普通意义上越小越好的损失值。

## 推导结构

1. 从训练并行视角解释为什么要先分配算力再 Route token。
2. 定义 `p`、`f`、`P`、`F`，把负载均衡写成分布均衡。
3. 从 `||F-Q||^2` 出发，用 `P + sg[F-P]` 构造可导目标。
4. 推出其梯度等价于经典 `F·P` 形式。

## 关键公式

- [[Aux Loss负载均衡公式]]：记录经典 `F·P` 形式和它的 STE 来源。

## 体现的方法

候选方法记录在 [[_candidates]]：从不可导选择分布构造直通估计目标。

## 所属系列位置

这是系列第二篇，承接几何 MoE 公式，转入负载均衡这一核心工程和数学问题。

## 与其他文章的关系

- continues: `article::10699`
- precedes: `article::10757`
- motivates: `concept::Loss-Free偏置`

## 原文证据锚点

- `ev::10735::需求分析`：第 20-32 行说明负载不均衡的 Dead Expert 和 Token Drop 风险。
- `ev::10735::辅助损失`：第 34-49 行定义 `P`、`F` 与经典 Aux Loss。
- `ev::10735::直通估计`：第 51-74 行从 STE 推导 Aux Loss 的等效梯度，并指出它不是真正 Loss。
