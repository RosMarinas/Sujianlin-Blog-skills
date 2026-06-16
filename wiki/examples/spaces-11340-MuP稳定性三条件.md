---
type: example
title: spaces-11340-MuP稳定性三条件
aliases: []
article_id: '11340'
article:
- - MuP之上：1. 好模型的三个特征
section: 三个条件
claim: 用 RMS 和 max/sup 写出前向、依赖、更新三类稳定性指标。
notation_mapping:
  f: boldsymbol{f}
  omega: boldsymbol{omega}
  RMS: Vert cdot Vert_RMS
steps:
- 定义 RMS 尺度
- 写出三类稳定性指标
- 用 max/sup 消去输入变量
- 将后续分析转化为参数和更新约束
used_concepts:
- - - MuP稳定性三条件
- - - RMS尺度
used_formulas:
- - - MuP稳定性三条件公式
used_methods:
- - - 用稳定性指标约束优化器缩放
problem_pattern: null
source_span: ev::11340::三个条件
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-21-MuP之上-1-好模型的三个特征.md
source_ids:
- '11340'
status: stable
updated: '2026-06-12'
---

# spaces-11340-MuP稳定性三条件

## 所在文章

[[MuP之上：1. 好模型的三个特征]]

## 原始问题

用 RMS 和 max/sup 写出前向、依赖、更新三类稳定性指标。

## 推导步骤

1. 定义 RMS 尺度
2. 写出三类稳定性指标
3. 用 max/sup 消去输入变量
4. 将后续分析转化为参数和更新约束

## 证据锚点

- `ev::11340::三个条件`