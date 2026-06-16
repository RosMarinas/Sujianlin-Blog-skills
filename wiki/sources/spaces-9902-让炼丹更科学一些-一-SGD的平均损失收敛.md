---
type: article_summary
title: "让炼丹更科学一些（一）：SGD的平均损失收敛"
article_id: "9902"
source_url: "https://spaces.ac.cn/archives/9902"
date: "2023-12-19"
category: "Big-Data"
source_markdown: "Data/Spaces_ac_cn/markdown/Big-Data/2023-12-19-让炼丹更科学一些-一-SGD的平均损失收敛.md"
source_html: "Data/Spaces_ac_cn/raw/articles/9902/page.html"
series:
  - "[[让炼丹更科学一些]]"
topics:
  - "[[SGD收敛与学习率调度]]"
concepts:
  - "[[SGD平均损失收敛]]"
methods:
  - "[[通过恒等式重写优化轨迹]]"
problem_patterns:
  - "[[将经验学习率策略转化为收敛界优化问题]]"
evidence_spans:
  - "ev::9902::结论初探"
  - "ev::9902::证明过程"
  - "ev::9902::域内投影"
  - "ev::9902::假设分析"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2023-12-19-让炼丹更科学一些-一-SGD的平均损失收敛.md"
source_ids:
  - "9902"
status: draft
updated: "2026-06-09"
---

# 让炼丹更科学一些（一）：SGD的平均损失收敛

## 文章核心问题

在凸性、梯度有界、学习率非增和有界凸域假设下，证明投影 SGD 的平均损失与理论最优损失之间可由学习率策略控制。

## 主要结论

核心不等式给出 O(1/sqrt(T)) 型平均损失收敛；投影步骤用于把理论中的有界性假设落到迭代轨迹上。

## 推导结构

1. 从前文或基础 SGD 迭代式定位当前要改进的结论。
2. 使用距离平方恒等式、凸性、期望、加权平均或辅助序列构造完成推导。
3. 将上界解释为学习率策略选择的约束。

## 关键公式

- [[SGD平均损失界]] 是本文最适合进入公式层的核心对象。

## 体现的方法

- [[通过恒等式重写优化轨迹]]：把参数距离的代数恒等式转化为损失上界。

## 所属系列位置

建立有界凸集与投影 SGD 下的平均损失收敛基线。

## 与其他文章的关系

- belongs_to: [[让炼丹更科学一些]]
- belongs_to: [[SGD收敛与学习率调度]]

## 原文证据锚点

- `ev::9902::结论初探`
- `ev::9902::证明过程`
- `ev::9902::域内投影`
- `ev::9902::假设分析`
