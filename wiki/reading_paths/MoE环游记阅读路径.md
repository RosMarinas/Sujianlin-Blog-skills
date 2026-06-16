---
type: reading_path
title: MoE环游记阅读路径
aliases:
  - MoE Tour reading path
goal: 按推导顺序理解 MoE 路由从几何直觉到序列级均衡的演化。
audience: 已了解 Transformer/FFN 基本结构，但需要系统理解 MoE 路由和负载均衡的读者。
ordered_nodes:
  - "[[MoE环游记]]"
  - "[[MoE环游记：1. 从几何意义出发]]"
  - "[[MoE环游记：2. 不患寡而患不均]]"
  - "[[MoE环游记：3. 换个思路来分配]]"
  - "[[MoE环游记：4. 难处应当多投入]]"
  - "[[MoE环游记：5. 均匀分布的反思]]"
  - "[[MoE环游记：6. 最优分配促均衡]]"
  - "[[MoE环游记：7. 动态激活极简解]]"
  - "[[MoE环游记：8. 强制序列级均衡]]"
source_ids:
  - "10699"
  - "10735"
  - "10757"
  - "10815"
  - "10945"
  - "11619"
  - "11626"
  - "11760"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-02-08-MoE环游记-1-从几何意义出发.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-02-21-MoE环游记-2-不患寡而患不均.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-03-05-MoE环游记-3-换个思路来分配.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-03-28-MoE环游记-4-难处应当多投入.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-05-16-MoE环游记-5-均匀分布的反思.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-02-23-MoE环游记-7-动态激活极简解.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-05-22-MoE环游记-8-强制序列级均衡.md
prerequisites:
  - Transformer FFN
  - Top-k routing
checkpoints:
  - 为什么 Router 可以被解释为低成本预测 Expert 模长？
  - 为什么 `F·P` 是等效梯度而不是普通损失？
  - Loss-Free 偏置为什么能隔离负载均衡和主任务优化？
  - QB 的分位数偏置从哪个约束优化问题来？
  - MQB 为什么需要分桶 EMA，而不是直接滑动 Quantile？
next_paths: []
status: draft
updated: 2026-06-09
---

# MoE环游记阅读路径

## 阅读顺序

先读第一篇建立 [[MoE几何路由]]，再读第二、三篇比较 [[Aux Loss负载均衡]] 和 [[Loss-Free偏置]]。第四、五篇分别给出动态激活和非均匀分布反思。最后三篇集中读 [[Quantile Balancing]]、[[动态专家激活]] 和 [[Moving Quantile Balancing]]。

## 检查点

读完这条路径后，应能解释：MoE 路由为什么可被看成约束分配问题，为什么负载均衡不应直接等同于“所有场景都均匀”，以及 QB/MQB 如何把均衡约束转化为偏置或分位数估计。
