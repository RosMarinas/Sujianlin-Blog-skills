---
type: concept
title: Loss-Free偏置
aliases:
- Loss-Free bias
definition: 只参与 Expert 分配排序、不直接参与 Expert 输出门控的偏置项，用于以 Loss-Free 方式调节负载均衡。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-03-05-MoE环游记-3-换个思路来分配.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md
source_ids:
- '10757'
- '11619'
prerequisites:
- '[[MoE负载均衡]]'
equivalent_forms:
- '[[Loss-Free偏置更新]]'
direct_consequences:
- '[[Loss-Free通过偏置隔离均衡优化]]'
- '[[QB把负载均衡转化为分位数偏置]]'
related_formulas:
- '[[Loss-Free偏置更新]]'
- '[[QB分位数偏置公式]]'
related_methods:
- '[[用对偶偏置改写路由约束]]'
series:
- '[[MoE环游记]]'
evidence_spans:
- ev::10757::方法大意
- ev::10757::一脉相承
status: stable
updated: '2026-06-12'
---

# Loss-Free偏置

## 定义

Loss-Free 偏置是附加到 Router 分数上、只影响 Expert 选择的向量。它不乘到 Expert 输出上，因此更像路由约束的可更新状态，而不是主模型计算的一部分。

## 生成关系

这个概念连接了第三篇的 SignSGD 更新、第六篇的 QB 分位数偏置、第七篇的动态阈值和第八篇的序列级 MQB。

## 证据

- `ev::10757::方法大意`
- `ev::10757::一脉相承`