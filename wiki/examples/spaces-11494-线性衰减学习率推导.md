---
type: example
title: spaces-11494-线性衰减学习率推导
aliases: null
article_id: '11494'
article: '[[让炼丹更科学一些（四）：新恒等式，新学习率]]'
section: 变分之法
claim: 连续化收敛上界并用变分法反推线性衰减。
notation_mapping:
  eta_t: "source \eta_t"
  T: source T
steps:
- 定位要控制的损失差
- 代入对应恒等式
- 用原文条件完成放缩或构造
used_concepts:
- '[[SGD终点损失收敛]]'
used_formulas:
- '[[线性衰减学习率]]'
used_methods:
- '[[用变分法反推学习率]]'
problem_pattern: '[[将经验学习率策略转化为收敛界优化问题]]'
source_span: ev::11494::变分之法
evidence_spans:
- ev::11494::变分之法
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md
source_ids:
- '11494'
status: stable
updated: '2026-06-12'
---

# spaces-11494-线性衰减学习率推导

## 所在文章

[[让炼丹更科学一些（四）：新恒等式，新学习率]]

## 原始问题

连续化收敛上界并用变分法反推线性衰减。

## 推导步骤

1. 使用原文 `变分之法` 章节中的等式或不等式。
2. 代入对应学习率、权重或辅助序列定义。
3. 得到可解释的损失界或学习率形式。

## 结论

该例子支撑 [[用变分法反推学习率]]。

## 证据锚点

- `ev::11494::变分之法`