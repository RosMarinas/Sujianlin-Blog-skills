---
type: proposition
title: 流式幂迭代可作为Muon的SVD近似实现
aliases: []
statement: 流式幂迭代可以把 SVD 近似维护为训练过程中的持续状态，从而作为 Muon 中矩阵符号函数的一种可扩展实现路线。
assumptions:
  - Muon 的核心运算可以从 SVD 角度理解。
  - 训练步骤之间可缓存并更新近似奇异向量状态。
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-03-12-基于流式幂迭代的Muon实现-1-初识.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-04-13-基于流式幂迭代的Muon实现-4-原理.md
source_ids:
  - "11654"
  - "11710"
requires:
  - "[[流式幂迭代]]"
  - "[[矩阵符号函数]]"
proof_route: 原文先提出用流式幂迭代近似计算 SVD，再在原理篇说明幂迭代收敛到右奇异矩阵的机制。
methods:
  - "[[将昂贵矩阵运算流式化]]"
limits:
  - 这是实现路线，不等于所有场景下都优于 Newton-Schulz。
examples: []
evidence_spans:
  - ev::11654::开篇问题
  - ev::11710::幂之迭代
status: stable
updated: 2026-06-09
---

# 流式幂迭代可作为Muon的SVD近似实现

## 命题

流式幂迭代可以把 SVD 近似维护为训练过程中的持续状态，从而作为 Muon 中 [[矩阵符号函数]] 的一种可扩展实现路线。

## 证明路线

`11654` 提出用流式幂迭代近似 SVD；`11710` 从幂迭代收敛和 QR 作用解释为什么该近似可以指向奇异向量结构。

## 适用范围

该命题支持 MVP 中的实现脉络，但不声明该方法在效率上总是优于标准实现。

## 证据

- `ev::11654::开篇问题`
- `ev::11710::幂之迭代`
