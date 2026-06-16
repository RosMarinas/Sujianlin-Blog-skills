---
type: formula
title: "MoE基本路由公式"
aliases:
  - "MoE routing formula"
  - "MoE Top-k routing"
latex: "\boldsymbol{y} = \sum_{i\in \operatorname{argtop}_k \boldsymbol{\rho}} \rho_i \boldsymbol{e}_i"
symbol_meanings:
  "\boldsymbol{y}": "MoE 层输出向量（行向量）"
  "\boldsymbol{\rho}": "Router 输出的 n 维非负向量"
  "\rho_i": "第 i 个 Expert 的门控强度（标量）"
  "\boldsymbol{e}_i": "第 i 个 Expert 的归一化方向向量"
  "\operatorname{argtop}_k": "Top-k 选择算子"
  "k": "每 token 激活的 Expert 数量"
  "n": "Expert 总数"
standard_notation:
  convention: "行向量约定；\boldsymbol{\rho} = h(\boldsymbol{x}\boldsymbol{W}^{(R)}) 为 Router 前向计算"
conditions: |
  Expert 输出可拆解为模长和方向两部分；模长由 Router 低成本预测；方向由 Expert 高成本计算；e_i 需归一化至相同模长。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-02-08-MoE环游记-1-从几何意义出发.md
source_ids:
  - "10699"
derived_from:
  - "[[MoE几何路由]]"
implies:
  - "[[Loss-Free通过偏置隔离均衡优化]]"
appears_in:
  - "[[MoE环游记：1. 从几何意义出发]]"
  - "[[MoE环游记：2. 不患寡而患不均]]"
evidence_spans:
  - ev::10699::MoE初现
status: draft
updated: "2026-06-14"
---

## 概述

MoE 基本路由公式将 Dense FFN 分解为 $n$ 个 Expert 向量之和，Router 预测每个 Expert 的模长 $\rho_i$，选取 Top-$k$ 后与归一化方向 $\boldsymbol{e}_i$ 加权求和。该公式是 MoE 架构的核心——它将 Expert 选择解释为 Dense 模型的稀疏最佳逼近，几何意义明确。

## 公式

$$
\boldsymbol{y} = \sum_{i\in \operatorname{argtop}_k \boldsymbol{\rho}} \rho_i \boldsymbol{e}_i
$$

其中 $\boldsymbol{\rho} = h(\boldsymbol{x}\boldsymbol{W}^{(R)}) \in \mathbb{R}_{\geq 0}^n$ 为 Router 输出，$\boldsymbol{e}_i = \boldsymbol{v}_i / \|\boldsymbol{v}_i\|$ 为归一化 Expert 方向。

## 符号说明

| 符号 | 含义 |
|------|------|
| $\boldsymbol{y}$ | MoE 层输出向量 |
| $\boldsymbol{\rho}$ | Router 输出的 $n$ 维非负向量 |
| $\rho_i$ | 第 $i$ 个 Expert 的门控强度 |
| $\boldsymbol{e}_i$ | 第 $i$ 个 Expert 的归一化方向向量 |
| $k$ | 每 token 激活的 Expert 数量 |
| $\operatorname{argtop}_k$ | Top-$k$ 选择算子 |

## 来源与推导

源自对 Dense FFN 的几何分解：标准 FFN 按列分块等价于 $n$ 个 Expert 向量之和。在各 Expert 方向近似正交的假设下，挑模长最大的 $k$ 个即为 MSE 最优稀疏近似。为避免先算所有 Expert 再排序的矛盾，将 Expert 重参数化为 $\boldsymbol{v}_i = \rho_i \boldsymbol{e}_i$，$\rho_i$ 由轻量 Router 预测，选出 Top-$k$ 后再计算对应的 $\boldsymbol{e}_i$。

## 条件

- Expert 输出可拆解为模长 $\rho_i$ 和方向 $\boldsymbol{e}_i$
- $\boldsymbol{e}_i$ 归一化至相同模长（L2 Norm 或 gamma=1 的 RMS Norm）
- 近似质量依赖 Expert 方向向量近似两两正交

## 证据

- ev::10699::FFN 分块分解：Dense FFN 等价于 $n$ 个 Expert 向量之和
- ev::10699::模长排序最优性：正交假设下 Top-$k$ 是 MSE 最优近似
- ev::10699::Expert 重参数化：Router 负责模长，Expert 负责方向
