---
type: concept
title: SGD平均损失收敛
aliases: null
definition: SGD 迭代过程中损失的时间平均值逼近理论最优损失值的收敛结论。
prerequisites: null
equivalent_forms: null
direct_consequences: null
related_formulas:
- '[[SGD平均损失界]]'
- '[[加权终点恒等式]]'
related_methods:
- '[[通过恒等式重写优化轨迹]]'
series:
- '[[让炼丹更科学一些]]'
evidence_spans:
- ev::9902::结论初探
- ev::9902::证明过程
- ev::11469::加权平均
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2023-12-19-让炼丹更科学一些-一-SGD的平均损失收敛.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-12-让炼丹更科学一些-二-将结论推广到无界域.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-01-09-让炼丹更科学一些-五-基于梯度精调学习率.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-01-16-让炼丹更科学一些-六-自上而下的精妙构造.md
source_ids:
- '9902'
- '11469'
- '11480'
- '11494'
- '11530'
- '11540'
status: stable
updated: '2026-06-12'
---

# SGD平均损失收敛

## 核心定义

SGD 迭代过程中损失的时间平均值逼近理论最优损失值的收敛结论。

## 前置概念

主要前置是凸性一阶条件、SGD 更新式和距离平方恒等式。

## 相关公式

与 [[SGD平均损失界]]、[[加权终点恒等式]] 和 [[Warmup-Decay最优学习率]] 相关。

## 原文证据

- `ev::9902::结论初探`
- `ev::9902::证明过程`
- `ev::11469::加权平均`