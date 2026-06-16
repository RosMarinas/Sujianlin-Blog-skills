---
type: proposition
title: WGAN L约束命题
aliases: []
statement: WGAN判别器必须满足Lipschitz约束||D||_L<=1，可以通过谱归一化、梯度惩罚或梯度归一化实现
assumptions: ["D为神经网络", "激活函数导数绝对值不超过1"]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
source_ids: ["6051", "8757"]
proof_route: WGAN目标W(P_r,P_g)=sup_{|f|_L=1}E_{P_r}[f]-E_{P_g}[f]要求|f|_L<=1。SN: ||W||_2约束; GP: (||grad f||-1)^2; GN: f/||grad f||自动满足
methods: [["谱归一化满足L约束"], ["梯度惩罚满足L约束"], ["梯度归一化满足L约束"]]
evidence_spans: []
status: draft
updated: 2026-06-11
---

## 陈述

WGAN判别器必须满足Lipschitz约束||D||_L<=1，可以通过谱归一化、梯度惩罚或梯度归一化实现

## 假设
- D为神经网络
- 激活函数导数绝对值不超过1

## 证明路线

WGAN目标W(P_r,P_g)=sup_{|f|_L=1}E_{P_r}[f]-E_{P_g}[f]要求|f|_L<=1。SN: ||W||_2约束; GP: (||grad f||-1)^2; GN: f/||grad f||自动满足