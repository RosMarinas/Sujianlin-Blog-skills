---
type: proposition
title: Aux Loss是STE均衡目标的等效梯度
aliases: []
statement: 经典 MoE Aux Loss `F·P` 可以由 `||F-Q||^2` 的 STE 可导化目标推出；它主要具有等效梯度意义，而不是普通损失值意义。
assumptions:
  - "`F` 是 Top-k 后的实际负载分布"
  - "`P` 是 `F` 的光滑近似"
  - "目标分布 `Q` 取均匀分布"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-02-21-MoE环游记-2-不患寡而患不均.md
source_ids:
  - "10735"
requires:
  - "[[Aux Loss负载均衡]]"
  - "[[Aux Loss负载均衡公式]]"
proof_route: 从 `||F-Q||^2` 出发，将不可导的 `F` 在反向传播中替换为 `P`，展开梯度后得到与 `F·P` 相同的梯度。
methods: []
limits:
  - 若直接使用未简化的 STE 形式，可以放宽 `P` 概率化和 `Q` 均匀的限制。
examples:
  - "[[spaces-10735-Aux-Loss直通估计推导]]"
evidence_spans:
  - ev::10735::直通估计
status: stable
updated: 2026-06-09
---

# Aux Loss是STE均衡目标的等效梯度

## 命题

经典 `F·P` 形式应优先被理解为 STE 均衡目标的等效梯度。它不能按普通损失的数值最小化直觉解释。

## 证据

- `ev::10735::直通估计`
