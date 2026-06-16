---
type: article_summary
title: "让炼丹更科学一些（三）：SGD的终点损失收敛"
article_id: "11480"
source_url: "https://spaces.ac.cn/archives/11480"
date: "2025-12-16"
category: "Mathematics"
source_markdown: "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md"
source_html: "Data/Spaces_ac_cn/raw/articles/11480/page.html"
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
  - "ev::11480::找出位置"
  - "ev::11480::准备工作"
  - "ev::11480::关键等式"
  - "ev::11480::完成证明"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md"
source_ids:
  - "11480"
status: draft
updated: "2026-06-09"
---

# 让炼丹更科学一些（三）：SGD的终点损失收敛

## 文章核心问题

先用 Jensen 解释轨迹平均权重，再引入终点值与尾部平均差异的恒等式。

## 主要结论

终点损失界与平均损失界同形但通常多出对数因子，静态和 1/sqrt(t) 学习率都稍慢于平均损失情形。

## 推导结构

1. 从前文或基础 SGD 迭代式定位当前要改进的结论。
2. 使用距离平方恒等式、凸性、期望、加权平均或辅助序列构造完成推导。
3. 将上界解释为学习率策略选择的约束。

## 关键公式

- [[终点平均恒等式]] 是本文最适合进入公式层的核心对象。

## 体现的方法

- [[通过恒等式重写优化轨迹]]：把参数距离的代数恒等式转化为损失上界。

## 所属系列位置

把平均损失收敛转化为训练终点的损失收敛。

## 与其他文章的关系

- belongs_to: [[让炼丹更科学一些]]
- belongs_to: [[SGD收敛与学习率调度]]

## 原文证据锚点

- `ev::11480::找出位置`
- `ev::11480::准备工作`
- `ev::11480::关键等式`
- `ev::11480::完成证明`
