---
type: proposition
title: MQB用分桶EMA近似序列级分位数
aliases: []
statement: MQB 通过对 Router 分数做分桶 one-hot 和序列 EMA 维护局部分布，从而近似每个位置的序列级分位数偏置。
assumptions:
  - "Router 分数可映射到有限区间并离散化"
  - "EMA 可作为局部分布估计"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-05-22-MoE环游记-8-强制序列级均衡.md
source_ids:
  - "11760"
requires:
  - "[[Moving Quantile Balancing]]"
  - "[[MQB分桶EMA公式]]"
proof_route: 直接滑动 Quantile 难以增量更新；分布可以增量估计，因此将分位数估计转化为直方图分布估计，再沿序列做 EMA。
methods:
  - "[[用分布估计近似滑动分位数]]"
limits:
  - 完美序列级均衡可能损伤主任务效果，需要用 `lambda` 控制干预强度。
examples: []
evidence_spans:
  - ev::11760::分桶估计
  - ev::11760::延伸思考
status: stable
updated: 2026-06-09
---

# MQB用分桶EMA近似序列级分位数

## 命题

MQB 的核心是把不可增量的 Quantile 计算转化为可递推的分布估计。它牺牲精确性换取可并行和可维护的序列级均衡偏置。

## 证据

- `ev::11760::分桶估计`
- `ev::11760::延伸思考`
