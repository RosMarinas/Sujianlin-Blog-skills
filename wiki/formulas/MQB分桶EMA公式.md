---

type: formula
title: MQB分桶EMA公式
aliases:
- Moving Quantile Balancing histogram EMA
latex: ar{h}_{i,j}=\gammaar{h}_{i-1,j}+(1-\gamma)h_{i,j}
symbol_meanings:
  ar{h}_{i,j}: 局部分布概率的EMA值
  \gamma: EMA衰减因子
  h_{i,j}: 路由分数经One-hot离散化后的指示向量
standard_notation:
  convention: Use the symbols exactly as defined in `latex`; meanings are listed in
    `symbol_meanings`.
conditions: Router 分数需要映射到可分桶区间；分桶数和 EMA 系数控制近似精度与状态成本。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-05-22-MoE环游记-8-强制序列级均衡.md
source_ids:
- '11760'
derived_from:
- '[[Moving Quantile Balancing]]'
implies:
- '[[MQB用分桶EMA近似序列级分位数]]'
appears_in:
- '[[MoE环游记：8. 强制序列级均衡]]'
evidence_spans:
- ev::11760::分桶估计
status: draft
updated: '2026-06-14'
---


# MQB分桶EMA公式


## 概述

（待补充）

## 公式本体

```tex
ar{h}_{i,j}=\gammaar{h}_{i-1,j}+(1-\gamma)h_{i,j}
```

## 成立条件

Router 分数需要映射到可分桶区间；分桶数和 EMA 系数控制近似精度与状态成本。

## 推导来源

- `ev::11760::分桶估计`

## 详细说明

MQB（Moving Quantile Balancing）分桶 EMA 公式 $$ar{h}_{i,j}=\gammaar{h}_{i-1,j}+(1-\gamma)h_{i,j}$$ 是一种用于大型混合专家模型（MoE）中在保持因果律（Causal）和推理效率的前提下，强制实现序列级负载均衡的关键估算策略。针对传统的量化分位数计算（Quantile）难以进行增量更新、复杂度较高的问题，MQB 采用“直方图近似”的线性化思想：首先通过 Sigmoid 函数与均匀离散化，将各 Expert 的路由分数映射到 $b$ 个特定的区间桶中转化为 One-Hot 向量 $h_{i,j}$，然后沿着序列维度 $i$ 计算其指数滑动平均（EMA）。借由累积的概率分布 $ar{h}_{i,j}$，网络能在线性时间开销下读出特定阈值（如 $1-k/n$）对应的局部分位数偏置。这一操作像 SWA 类似平滑了局部评分的异常高峰，有效抑制了“Token 倾向于集中被分给少数固定专家”的极端不均衡现象。
