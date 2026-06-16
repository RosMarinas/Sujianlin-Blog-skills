---
type: topic
title: MoE路由与负载均衡
aliases:
  - MoE routing and load balancing
scope: MoE 中 Expert 选择、Router 打分、负载均衡、动态激活和序列级均衡的推导与方法。
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
series:
  - "[[MoE环游记]]"
concepts:
  - "[[MoE几何路由]]"
  - "[[MoE负载均衡]]"
  - "[[Aux Loss负载均衡]]"
  - "[[Loss-Free偏置]]"
  - "[[动态专家激活]]"
  - "[[Shared Expert]]"
  - "[[Fine-Grained Expert]]"
  - "[[Quantile Balancing]]"
  - "[[Moving Quantile Balancing]]"
formulas:
  - "[[MoE基本路由公式]]"
  - "[[Aux Loss负载均衡公式]]"
  - "[[Loss-Free偏置更新]]"
  - "[[QB分位数偏置公式]]"
  - "[[MQB分桶EMA公式]]"
propositions:
  - "[[Aux Loss是STE均衡目标的等效梯度]]"
  - "[[Loss-Free通过偏置隔离均衡优化]]"
  - "[[QB把负载均衡转化为分位数偏置]]"
  - "[[动态QB一步分位数实现平均预算均衡]]"
  - "[[MQB用分桶EMA近似序列级分位数]]"
methods:
  - "[[用对偶偏置改写路由约束]]"
  - "[[用分位数求解负载均衡偏置]]"
  - "[[用分布估计近似滑动分位数]]"
problem_patterns:
  - "[[将路由选择转化为约束分配问题]]"
  - "[[在均衡与主任务效果之间调节干预强度]]"
reading_paths:
  - "[[MoE环游记阅读路径]]"
open_questions:
  - 序列级均衡在多大程度上必要，仍需实验判定。
status: draft
updated: 2026-06-09
---

# MoE路由与负载均衡

## 范围

本主题收纳 `MoE环游记` 1-8 篇中关于路由选择和负载均衡的内容：从几何路由、Aux Loss、Loss-Free，到 QB、动态激活和 MQB。它不收纳通用 Transformer 结构升级，也不收纳未读的 MoE 后续文章。

## 核心链条

[[MoE几何路由]] 给出 Router 选择 Expert 的几何解释；[[MoE负载均衡]] 暴露 Dead Expert 和 Token Drop 问题；[[Aux Loss负载均衡]] 和 [[Loss-Free偏置]] 是两类均衡路线；[[Quantile Balancing]] 将偏置求解转成分位数问题；[[Moving Quantile Balancing]] 则试图把全局均衡推进到序列级。

## 稳定结论

- [[Aux Loss是STE均衡目标的等效梯度]]：经典 Aux Loss 的可信解释是等效梯度，而不是普通损失值。
- [[Loss-Free通过偏置隔离均衡优化]]：偏置只参与分配，减少对主任务梯度的直接干扰。
- [[QB把负载均衡转化为分位数偏置]]：Top-k 负载均衡可由对偶变量和分位数更新刻画。

## 批次外边界

Hash Routing、DeepSeek V4 tid2eid、更多 MoE 论文和推理系统优化不在本批中提升为稳定节点。
