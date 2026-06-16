---
type: series
title: MoE环游记
aliases:
  - MoE Tour
article_ids:
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
source_ids:
  - "10699"
  - "10735"
  - "10757"
  - "10815"
  - "10945"
  - "11619"
  - "11626"
  - "11760"
series_goal: 从 Dense FFN 的几何近似出发，逐步推导 MoE 路由、负载均衡、动态激活和序列级均衡方案。
entry_roles:
  "10699": 几何路由入口
  "10735": Aux Loss 与 STE 推导
  "10757": Loss-Free 偏置
  "10815": 动态专家数
  "10945": 均匀分布反思
  "11619": Top-k QB 最优分配
  "11626": 动态 QB 一步分位数
  "11760": MQB 序列级均衡
key_concepts:
  - "[[MoE几何路由]]"
  - "[[MoE负载均衡]]"
  - "[[Loss-Free偏置]]"
  - "[[Quantile Balancing]]"
  - "[[Moving Quantile Balancing]]"
key_methods:
  - "[[从计算节省目标重写模型结构]]"
  - "[[用对偶偏置改写路由约束]]"
  - "[[用分位数求解负载均衡偏置]]"
  - "[[用分布估计近似滑动分位数]]"
reading_paths:
  - "[[MoE环游记阅读路径]]"
status: draft
updated: 2026-06-14
---

# MoE环游记

## 系列问题

这个系列试图回答：MoE 的路由为什么可以被理解为一种几何近似，负载均衡为什么困难，以及如何从 Aux Loss、Loss-Free、QB 到 MQB 逐步把均衡约束转成更可控的路由偏置。

## 有序文章

1. [[MoE环游记：1. 从几何意义出发]]：从 FFN 分块和向量求和近似推导 [[MoE几何路由]]。
2. [[MoE环游记：2. 不患寡而患不均]]：把负载均衡写成 `F` 接近均匀分布 `Q` 的目标，并解释 [[Aux Loss负载均衡]]。
3. [[MoE环游记：3. 换个思路来分配]]：引入 [[Loss-Free偏置]]，把均衡参数和主模型参数隔离。
4. [[MoE环游记：4. 难处应当多投入]]：用阈值式偏置实现 [[动态专家激活]]。
5. [[MoE环游记：5. 均匀分布的反思]]：通过 [[Shared Expert]] 和 [[Fine-Grained Expert]] 说明均匀分布不是唯一目标。
6. [[MoE环游记：6. 最优分配促均衡]]：把 Top-k 均衡写成线性规划并推导 [[Quantile Balancing]]。
7. [[MoE环游记：7. 动态激活极简解]]：去掉每 Token 固定 `k` 的约束，得到动态 QB 的一步分位数解。
8. [[MoE环游记：8. 强制序列级均衡]]：用 [[Moving Quantile Balancing]] 把 QB 推到序列级局部均衡。

## 递进结构

前四篇从模型形式和路由训练角度推进，第五篇反思“均匀是否最优”，后三篇转入优化问题和分位数偏置。系列的主线不是某一个 MoE 实现，而是把路由选择中的离散约束逐步改写为可解释、可更新、尽量不干扰主任务的偏置。

## 已知边界

- 本批只覆盖 1-8 篇，不扩展到 DeepSeek V4、Hash Routing 或 Transformer 升级系列。
- MQB 是否必要以及最佳干预强度仍是开放问题，保留为 failure/probe 项而不是稳定结论。

## 与 LLM 架构主线的桥接

MoE 环游记在 LLM 相关网络中承担“稀疏 FFN 容量扩展”角色：[[Transformer架构与归一化]] 解释 Attention/Norm/FFN 结构如何改，[[LLM架构与上下文扩展]] 解释上下文和递归结构如何扩展，而本系列解释如何在 FFN 容量上用路由约束、偏置和分位数估计控制专家使用。
