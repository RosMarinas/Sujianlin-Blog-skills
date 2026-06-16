---

type: formula
title: Aux Loss负载均衡公式
aliases:
- auxiliary load balancing loss
latex: \mathcal{L}_{\mathrm{aux}} = oldsymbol{F}\cdotoldsymbol{P} = \sum_{i=1}^n
  F_iP_i
symbol_meanings:
  F_i: 第 i 个 Expert 的实际硬件负载（硬分布）
  P_i: 第 i 个 Expert 的路由平滑分配概率（软分布）
standard_notation:
  convention: Use the symbols exactly as defined in `latex`; meanings are listed in
    `symbol_meanings`.
conditions: 经典简化形式依赖 `P` 是概率分布且目标分布是均匀分布；更一般的 STE 形式可放宽这些限制。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-02-21-MoE环游记-2-不患寡而患不均.md
source_ids:
- '10735'
derived_from:
- '[[Aux Loss负载均衡]]'
implies:
- '[[Aux Loss是STE均衡目标的等效梯度]]'
appears_in:
- '[[MoE环游记：2. 不患寡而患不均]]'
evidence_spans:
- ev::10735::辅助损失
- ev::10735::直通估计
status: draft
updated: '2026-06-14'
---


# Aux Loss负载均衡公式


## 概述

（待补充）

## 公式本体

```tex
\mathcal{L}_{\mathrm{aux}} = oldsymbol{F}\cdotoldsymbol{P} = \sum_{i=1}^n F_iP_i
```

## 成立条件

经典简化形式依赖 P 是概率分布且目标分布是均匀分布；更一般的 STE 形式可放宽这些限制。

## 推导来源

- `ev::10735::辅助损失`
- `ev::10735::直通估计`

## 详细说明

Aux Loss 负载均衡公式 $$\mathcal{L}_{\mathrm{aux}} = oldsymbol{F}\cdotoldsymbol{P} = \sum_{i=1}^n F_iP_i$$ 是用于应对混合专家模型（MoE）中 Expert 分配不均或算力闲置（Dead Expert）问题的经典正则化方法。在该式中，向量 $oldsymbol{F}$ 描述了离散化路由（通常由于 $	ext{argtop}_k$ 或类似策略产生）后的真实硬负载分布，而 $oldsymbol{P}$ 则是由路由器（Router）产生的归一化平滑软概率分布。由于 $oldsymbol{F}$ 本质上是不可微的，在实践中通过采用直通估计器（Straight-Through Estimator, STE）替换反向传播过程中的不可导项，从而巧妙地把 $\mathcal{L}_{\mathrm{aux}}$ 转换为促使 $oldsymbol{F}$ 逼近均匀分布目标的等效梯度。它能够作为附加的损失系数添加至整体 Loss 中，使得那些在历史批次处理中处于相对劣势（得分较低）的专家获得自适应补偿，以此保障 MoE 的实际激活参数量。
