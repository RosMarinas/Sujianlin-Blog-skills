---
type: proposition
title: SGD可近似为带噪声的SDE
aliases: []
statement: 在小批量梯度噪声近似为高斯误差时，SGD 可由带扩散项的 SDE 描述。
assumptions:
  - 小批量梯度误差可近似为噪声项
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
source_ids:
  - "5655"
requires:
  - [[SGD-SDE近似公式]]
proof_route: 由对应 evidence span 中的源文推导抽取；本页保留结论层节点，公式细节见 requires。
methods:
  - [[把优化算法解释为动力系统离散化]]
limits:
  - 当前只在本批次源文范围内稳定，跨系列推广需另行验证。
examples: []
evidence_spans:
  - ev::5655::从SGD到SDE
status: stable
updated: 2026-06-10
---

# SGD可近似为带噪声的SDE

## 命题

在小批量梯度噪声近似为高斯误差时，SGD 可由带扩散项的 SDE 描述。

## 证明路线

由对应 evidence span 中的源文推导抽取；本页保留结论层节点，公式细节见 requires。

## 证据

- `ev::5655::从SGD到SDE`
