---

type: formula
title: Loss-Free偏置更新
aliases:
- Loss-Free bias update
latex: \boldsymbol{b}\leftarrow \boldsymbol{b}-\gamma\operatorname{sign}(\boldsymbol{F}-\boldsymbol{Q})
symbol_meanings:
  F: 当前 Expert 负载分布
  Q: 目标负载分布
  b: 路由排序偏置向量
  gamma: 偏置更新学习率
standard_notation:
  b: 路由排序偏置向量
  F: 当前 Expert 负载分布
  Q: 目标负载分布
  gamma: 偏置更新学习率
conditions: 先用旧偏置完成当前 batch 路由，再根据当前负载统计更新偏置；偏置不直接乘到 Expert 输出上。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-03-05-MoE环游记-3-换个思路来分配.md
source_ids:
- '10757'
derived_from:
- '[[Loss-Free偏置]]'
implies:
- '[[Loss-Free通过偏置隔离均衡优化]]'
appears_in:
- '[[MoE环游记：3. 换个思路来分配]]'
- '[[MoE环游记：4. 难处应当多投入]]'
evidence_spans:
- ev::10757::手搓梯度
status: draft
updated: "2026-06-14"
---

# Loss-Free偏置更新


## 概述

（待补充）

## 公式

```tex
\boldsymbol{b}\leftarrow \boldsymbol{b}-\gamma\operatorname{sign}(\boldsymbol{F}-\boldsymbol{Q})
```
或者通过 STE (Straight-Through Estimator) 导出的直接梯度形式：
```tex
\nabla_{\boldsymbol{b}}\mathcal{L}_{\text{aux}} = \boldsymbol{F} - \boldsymbol{Q}
```

## 作用与原理

Loss-Free 负载均衡策略不改变 Router 原有的打分结果 $\boldsymbol{\rho}$，而是通过引入一个独立于输入的偏置项 $\boldsymbol{b}$ 来改变 $\mathop{\text{argtop}}_k$ 的分配方式。具体来说，将 MoE 的路由决策条件从 $\mathop{\text{argtop}}_k \boldsymbol{\rho}$ 替换为 $\mathop{\text{argtop}}_k (\boldsymbol{\rho} + \boldsymbol{b})$。

在实际执行时，分配给对应 Expert 的特征权重仍然是原始的概率 $\rho_i$，而不是加偏置后的 $\rho_i + b_i$。其前向计算公式为：
$$
\boldsymbol{y} = \sum_{i\in \mathop{\text{argtop}}_k (\boldsymbol{\rho} + \boldsymbol{b})} \rho_i \boldsymbol{e}_i
$$
这意味着偏置 $\boldsymbol{b}$ 仅仅参与决定哪个 Expert 被选中（即分配选择过程），而完全不参与 MoE 的前向加权求和计算。因此，它不会直接改变主模型的输出，避免了对语言模型本身的 Loss 造成负面干扰（即 Loss-Free），同时对 $\boldsymbol{b}$ 的正负性没有任何要求。

在优化 $\boldsymbol{b}$ 时，定义当前 Expert 的实际负载分布期望为 $\boldsymbol{F}$，理想的目标分布为均匀分布 $\boldsymbol{Q}=(1/n, 1/n, \cdots, 1/n)$。通过最小化两者差距 $\mathcal{L}_{\text{aux}} = \frac{1}{2}\Vert\boldsymbol{F} - \boldsymbol{Q}\Vert^2$，并利用 STE 将 $\boldsymbol{b}$ 作为不可导变量 $\boldsymbol{F}$ 的同增减光滑近似，求导可得梯度为 $\boldsymbol{F} - \boldsymbol{Q}$。

实际应用中，通常直接根据符号函数 $\operatorname{sign}(\boldsymbol{F}-\boldsymbol{Q})$ 和学习率 $\gamma$ 对其进行更新：当某个 Expert 的当前实际负载高于目标分布时，降低其偏置（从而降低该 Expert 下一步被选中的概率）；当负载低于目标时，则提高偏置。训练完成后，$\boldsymbol{b}$ 作为一个与输入无关的固定参数向量，可以无缝直接应用于推理阶段，完美解决了以往类似方法（如 BASE Layer）中训练和推理不一致的问题。
