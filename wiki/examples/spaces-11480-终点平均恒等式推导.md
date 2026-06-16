---
type: example
title: spaces-11480-终点平均恒等式推导
aliases: null
article_id: '11480'
article: '[[让炼丹更科学一些（三）：SGD的终点损失收敛]]'
section: 关键等式
claim: 用尾部累积平均推导终点值与平均值之间的恒等式。
notation_mapping:
  q_t: source q_t
  T: source T
steps:
- 定位要控制的损失差
- 代入对应恒等式
- 用原文条件完成放缩或构造
used_concepts:
- '[[SGD终点损失收敛]]'
used_formulas:
- '[[终点平均恒等式]]'
used_methods:
- '[[通过恒等式重写优化轨迹]]'
problem_pattern: '[[将经验学习率策略转化为收敛界优化问题]]'
source_span: ev::11480::关键等式
evidence_spans:
- ev::11480::关键等式
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md
source_ids:
- '11480'
status: stable
updated: '2026-06-12'
---

# spaces-11480-终点平均恒等式推导

## 所在文章

[[让炼丹更科学一些（三）：SGD的终点损失收敛]]

## 原始问题

用尾部累积平均推导终点值与平均值之间的恒等式。

## 推导步骤

1. 使用原文 `关键等式` 章节中的等式或不等式。
2. 代入对应学习率、权重或辅助序列定义。
3. 得到可解释的损失界或学习率形式。

## 结论

该例子支撑 [[通过恒等式重写优化轨迹]]。

## 证据锚点

- `ev::11480::关键等式`