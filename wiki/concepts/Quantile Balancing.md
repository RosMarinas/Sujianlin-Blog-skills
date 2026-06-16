---
type: concept
title: Quantile Balancing
aliases:
- QB
definition: 从 MoE 负载均衡的最优分配对偶问题出发，用分位数求解或更新路由偏置的 Loss-Free 均衡方法。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-02-23-MoE环游记-7-动态激活极简解.md
source_ids:
- '11619'
- '11626'
prerequisites:
- '[[Loss-Free偏置]]'
- '[[MoE负载均衡]]'
equivalent_forms:
- '[[QB分位数偏置公式]]'
direct_consequences:
- '[[QB把负载均衡转化为分位数偏置]]'
- '[[动态QB一步分位数实现平均预算均衡]]'
related_formulas:
- '[[QB分位数偏置公式]]'
related_methods:
- '[[用分位数求解负载均衡偏置]]'
series:
- '[[MoE环游记]]'
evidence_spans:
- ev::11619::交替迭代
- ev::11626::一步求解
status: stable
updated: '2026-06-13'
---

# Quantile Balancing

## 定义

Quantile Balancing（QB）是把 MoE 负载均衡写成等式约束线性规划后，用分位数求解路由偏置的 Loss-Free 方法。它不通过 Aux Loss 惩罚主损失，而是让偏置只影响 Expert 排序或阈值。

## 激活场景

QB 用于希望每个 Token 选择高分 Expert、同时每个 Expert 被激活次数接近 `mk/n` 的路由场景。Top-k 版本保留“每 Token 恰好激活 `k` 个 Expert”的行约束；动态激活版去掉该行约束，只保留列方向负载约束和平均预算。

## 关键关系

在 Top-k 版本中，源文通过松弛整数规划、交换 max-min、固定一组对偶变量求另一组，得到 `alpha` 与 `beta` 的交替分位数更新；推理阶段只需 `beta`，输出为 `argtop_k(s_i-beta)`。动态版本中，`beta_j` 是第 `mk/n+1` 大分数，也即 `1-k/n` 分位数，激活条件变成 `s_{i,j}-beta_j>0`，从而一步 Quantile 得到绝对均衡的最优解。

## 证据

- `Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md`
- `Data/Spaces_ac_cn/markdown/Mathematics/2026-02-23-MoE环游记-7-动态激活极简解.md`
- `ev::11619::交替迭代`
- `ev::11626::一步求解`
