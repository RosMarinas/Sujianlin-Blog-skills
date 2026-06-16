---
type: article_summary
title: MoE环游记：8. 强制序列级均衡
article_id: "11760"
source_url: https://spaces.ac.cn/archives/11760
date: 2026-05-22
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2026-05-22-MoE环游记-8-强制序列级均衡.md
source_html: Data/Spaces_ac_cn/raw/articles/11760/page.html
series:
  - "[[MoE环游记]]"
topics:
  - "[[MoE路由与负载均衡]]"
concepts:
  - "[[Moving Quantile Balancing]]"
  - "[[Quantile Balancing]]"
methods:
  - "[[用分布估计近似滑动分位数]]"
problem_patterns:
  - "[[在均衡与主任务效果之间调节干预强度]]"
evidence_spans:
  - ev::11760::滑动分位
  - ev::11760::分桶估计
  - ev::11760::延伸思考
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-05-22-MoE环游记-8-强制序列级均衡.md
source_ids:
  - "11760"
status: draft
updated: 2026-06-09
---

# MoE环游记：8. 强制序列级均衡

## 文章核心问题

本文追问如何用 Loss-Free 的方式实现序列级负载均衡，并从 QB 推导出 Moving Quantile Balancing。

## 主要结论

- 既有 Loss-Free 偏置主要实现全局 batch 意义下的均衡，不能直接保证序列内部均衡。
- 对动态激活 MoE，序列维度上的分位数偏置可以给出局部最优阈值，但直接 Cumulative/Moving Quantile 成本高。
- MQB 用分桶 one-hot + EMA 估计局部分布，再由累积概率近似分位数，使序列级偏置可并行近似。
- 完美序列级均衡会明显损伤效果，实际应通过 `lambda` 控制干预强度。

## 推导结构

1. 回顾 Aux Loss、Loss-Free、QB 与动态 QB。
2. 比较局部中心化和测试时训练式偏置更新。
3. 从动态 QB 的序列分位数出发，提出 CQB/MQB。
4. 用直方图分桶和 EMA 将非线性 Quantile 近似为可维护的局部分布估计。
5. 说明 Top-k 情况下可叠加全局 QB，并讨论干预强度。

## 关键公式

- [[MQB分桶EMA公式]]：记录分桶 EMA 估计局部分位数的核心流程。

## 体现的方法

- [[用分布估计近似滑动分位数]]：把不可增量更新的 Quantile 改写为可递推的分布估计。

## 所属系列位置

这是当前批次的第八篇，把 MoE 负载均衡从全局 batch 约束推进到序列级局部约束。

## 与其他文章的关系

- continues: `article::11626`
- generalizes: `concept::Quantile Balancing`
- motivates: `problem_pattern::在均衡与主任务效果之间调节干预强度`

## 原文证据锚点

- `ev::11760::滑动分位`：第 68-78 行从 Cumulative Quantile 推到 Moving Quantile。
- `ev::11760::分桶估计`：第 80-109 行给出分桶 one-hot、EMA 和分位数估计流程。
- `ev::11760::延伸思考`：第 147-155 行指出强序列均衡的效果损伤与干预强度控制。
