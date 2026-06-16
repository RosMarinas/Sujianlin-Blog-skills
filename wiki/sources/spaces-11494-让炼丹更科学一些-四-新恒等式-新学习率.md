---
type: article_summary
title: "让炼丹更科学一些（四）：新恒等式，新学习率"
article_id: "11494"
source_url: "https://spaces.ac.cn/archives/11494"
date: "2025-12-26"
category: "Mathematics"
source_markdown: "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md"
source_html: "Data/Spaces_ac_cn/raw/articles/11494/page.html"
series:
  - "[[让炼丹更科学一些]]"
topics:
  - "[[SGD收敛与学习率调度]]"
concepts:
  - "[[SGD平均损失收敛]]"
  - "[[SGD终点损失收敛]]"
methods:
  - "[[通过恒等式重写优化轨迹]]"
problem_patterns:
  - "[[从平均损失结论转向终点损失结论]]"
evidence_spans:
  - "ev::11494::新恒等式"
  - "ev::11494::一般结论"
  - "ev::11494::加速收敛"
  - "ev::11494::变分之法"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md"
source_ids:
  - "11494"
status: draft
updated: "2026-06-09"
---

# 让炼丹更科学一些（四）：新恒等式，新学习率

## 文章核心问题

用加权版终点恒等式得到更强的一般终点损失界，再用线性衰减把速率提升到 O(1/sqrt(T))。

## 主要结论

终点收敛最快的学习率应随总训练步数动态变化；线性衰减在该理论中获得支撑。

## 推导结构

1. 从前文或基础 SGD 迭代式定位当前要改进的结论。
2. 使用距离平方恒等式、凸性、期望、加权平均或辅助序列构造完成推导。
3. 将上界解释为学习率策略选择的约束。

## 关键公式

- [[加权终点恒等式]] 是本文最适合进入公式层的核心对象。

## 体现的方法

- [[通过恒等式重写优化轨迹]]：把参数距离的代数恒等式转化为损失上界。

## 所属系列位置

推广终点-平均恒等式，并由此解释线性衰减学习率的终点最优性。

## 与其他文章的关系

- belongs_to: [[让炼丹更科学一些]]
- belongs_to: [[SGD收敛与学习率调度]]

## 原文证据锚点

- `ev::11494::新恒等式`
- `ev::11494::一般结论`
- `ev::11494::加速收敛`
- `ev::11494::变分之法`
