---
type: proposition
title: 梯度下降是梯度流ODE的欧拉离散化
aliases: []
statement: 梯度下降更新可以理解为梯度流 ODE 的欧拉数值解。
assumptions:
  - 步长足够小
  - 损失函数可微
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
source_ids:
  - "5655"
requires:
  - [[梯度流ODE公式]]
proof_route: 由对应 evidence span 中的源文推导抽取；本页保留结论层节点，公式细节见 requires。
methods:
  - [[把优化算法解释为动力系统离散化]]
limits:
  - 当前只在本批次源文范围内稳定，跨系列推广需另行验证。
examples: []
evidence_spans:
  - ev::5655::GD与ODE
status: stable
updated: 2026-06-10
---

# 梯度下降是梯度流ODE的欧拉离散化

## 命题

梯度下降更新可以理解为梯度流 ODE 的欧拉数值解。

## 证明路线

由对应 evidence span 中的源文推导抽取；本页保留结论层节点，公式细节见 requires。

## 证据

- `ev::5655::GD与ODE`
