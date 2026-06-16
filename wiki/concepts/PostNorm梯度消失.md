---
type: concept
title: "PostNorm梯度消失"
aliases:
  - "Post-LN Gradient Vanishing"
  - "残差指数衰减"
definition: "Post Norm结构x_{t+1}=Norm(x_t+F_t(x_t))在初始化阶段相当于除以√2，递归后残差直路贡献被指数衰减，越靠近输入层的梯度越小。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-08-模型优化漫谈-BERT的初始标准差为什么是0-02.md
source_ids:
  - "8747"
prerequisites:
  - "[[Layer Norm]]"
  - "[[残差连接]]"
equivalent_forms:
  - "[[PreNorm vs PostNorm]]"
related_methods:
  - "[[使用Warmup预热训练]]"
evidence_spans:
  - "ev::8747::PostNorm指数衰减"
  - "ev::8747::LN加剧梯度消失"
status: draft
updated: 2026-06-12
---

# PostNorm梯度消失

## Definition

Post Norm在初始化阶段假设x与F(x)方差均为1时，x+F(x)方差为2，Norm操作相当于除以√2。递归后x_l = x₀/2^{l/2} + ∑F_i(x_i)/2^{(l-i+1)/2}，残差直路被指数衰减。但Post Norm利于Finetune（梯度消失保护底层预训练参数）且各层输出方差一致。Pre Norm无指数衰减问题但各层方差递增。
