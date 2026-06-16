---
type: proposition
title: QB把负载均衡转化为分位数偏置
aliases: []
statement: 在 Top-k MoE 中，带每 Token 激活数和每 Expert 负载约束的最优分配问题可通过对偶变量转化为分位数偏置更新。
assumptions:
  - "`mk/n` 是整数或可用近似批次处理"
  - "先用旧偏置路由，再更新偏置"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md
source_ids:
  - "11619"
requires:
  - "[[Quantile Balancing]]"
  - "[[QB分位数偏置公式]]"
proof_route: 将整数规划松弛为线性规划，交换 max-min，引入 `alpha` 和 `beta`，固定一组变量时另一组变量的最优值是相应排序的分位数。
methods:
  - "[[用对偶偏置改写路由约束]]"
  - "[[用分位数求解负载均衡偏置]]"
limits:
  - 精确全局分位数计算在大 batch 和并行训练下成本高，实际需要小批次平均或近似。
examples:
  - "[[spaces-11619-QB最优分配推导]]"
evidence_spans:
  - ev::11619::线性规划
  - ev::11619::交替迭代
status: stable
updated: 2026-06-09
---

# QB把负载均衡转化为分位数偏置

## 命题

QB 不是经验性调参，而是从约束最优分配的对偶问题中得到的偏置求解方式。

## 证据

- `ev::11619::线性规划`
- `ev::11619::交替迭代`
