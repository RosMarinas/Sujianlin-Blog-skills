---
type: article_summary
title: "让炼丹更科学一些（二）：将结论推广到无界域"
article_id: "11469"
source_url: "https://spaces.ac.cn/archives/11469"
date: "2025-12-12"
category: "Mathematics"
source_markdown: "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-12-让炼丹更科学一些-二-将结论推广到无界域.md"
source_html: "Data/Spaces_ac_cn/raw/articles/11469/page.html"
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
  - "ev::11469::新的思路"
  - "ev::11469::加个期望"
  - "ev::11469::单调放缩"
  - "ev::11469::加权平均"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-12-让炼丹更科学一些-二-将结论推广到无界域.md"
source_ids:
  - "11469"
status: draft
updated: "2026-06-09"
---

# 让炼丹更科学一些（二）：将结论推广到无界域

## 文章核心问题

不再除以每步学习率，而是直接求和消去中间距离项，再通过期望消除采样变量依赖。

## 主要结论

无界域下仍可得到平均损失收敛；加权平均形式给出更宽松的学习率条件。

## 推导结构

1. 从前文或基础 SGD 迭代式定位当前要改进的结论。
2. 使用距离平方恒等式、凸性、期望、加权平均或辅助序列构造完成推导。
3. 将上界解释为学习率策略选择的约束。

## 关键公式

- [[无界域加权平均界]] 是本文最适合进入公式层的核心对象。

## 体现的方法

- [[通过恒等式重写优化轨迹]]：把参数距离的代数恒等式转化为损失上界。

## 所属系列位置

去掉有界域投影，把收敛结论改写为期望意义下的无界域结果。

## 与其他文章的关系

- belongs_to: [[让炼丹更科学一些]]
- belongs_to: [[SGD收敛与学习率调度]]

## 原文证据锚点

- `ev::11469::新的思路`
- `ev::11469::加个期望`
- `ev::11469::单调放缩`
- `ev::11469::加权平均`
