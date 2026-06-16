---
type: proposition
title: "有界域投影SGD平均损失收敛"
aliases:
statement: "投影 SGD 在有界凸集、凸损失、梯度有界和学习率非增条件下满足平均损失收敛界。"
assumptions:
  - "凸损失"
  - "SGD 或文中指定的随机优化更新"
  - "原文对应章节中的学习率和梯度条件"
requires:
  - "[[SGD平均损失界]]"
  - "[[加权终点恒等式]]"
proof_route: "由距离平方恒等式出发，结合凸性、期望、加权恒等式或辅助序列构造得到上界。"
methods:
  - "[[通过恒等式重写优化轨迹]]"
limits:
  - "主要是凸优化理论结果；非凸深度网络训练只作为启发。"
examples:
evidence_spans:
  - "ev::9902::结论初探"
  - "ev::9902::域内投影"
  - "ev::9902::假设分析"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2023-12-19-让炼丹更科学一些-一-SGD的平均损失收敛.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-12-让炼丹更科学一些-二-将结论推广到无界域.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2026-01-09-让炼丹更科学一些-五-基于梯度精调学习率.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2026-01-16-让炼丹更科学一些-六-自上而下的精妙构造.md"
source_ids:
  - "9902"
  - "11469"
  - "11480"
  - "11494"
  - "11530"
  - "11540"
status: stable
updated: "2026-06-09"
---

# 有界域投影SGD平均损失收敛

## 命题表述

投影 SGD 在有界凸集、凸损失、梯度有界和学习率非增条件下满足平均损失收敛界。

## 证明路线

从基础距离恒等式进入损失上界，再根据目标选择平均、加权平均、终点恒等式或辅助序列构造。

## 适用限制

该命题保持在原文的凸优化和期望意义范围内。

## 原文证据

- `ev::9902::结论初探`
- `ev::9902::域内投影`
- `ev::9902::假设分析`
