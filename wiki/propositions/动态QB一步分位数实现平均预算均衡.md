---
type: proposition
title: 动态QB一步分位数实现平均预算均衡
aliases: []
statement: 去掉每个 Token 必须激活固定 `k` 个 Expert 的约束后，动态激活版 QB 可以用每个 Expert 分数的 `1-k/n` 分位数一步得到负载均衡阈值。
assumptions:
  - "只要求每个 Expert 的总激活次数为 `mk/n`"
  - "动态激活通过 `s_ij - beta_j > 0` 决定"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-02-23-MoE环游记-7-动态激活极简解.md
source_ids:
  - "11626"
requires:
  - "[[动态专家激活]]"
  - "[[Quantile Balancing]]"
proof_route: 删除行约束后，对偶目标只剩 `beta_j`；每个 `beta_j` 的一维目标在第 `mk/n` 与第 `mk/n+1` 大元素之间取最优。
methods:
  - "[[用分位数求解负载均衡偏置]]"
limits:
  - 直接用当前 batch 最优分位数可能过拟合当前批次，实践中需要 EMA 或旧偏置先路由。
examples: []
evidence_spans:
  - ev::11626::动态激活
  - ev::11626::一步求解
status: stable
updated: 2026-06-09
---

# 动态QB一步分位数实现平均预算均衡

## 命题

动态 QB 的简洁性来自放弃每 Token 固定 `k` 的硬约束，只保留总预算和负载均衡约束。

## 证据

- `ev::11626::动态激活`
- `ev::11626::一步求解`
