---
type: proposition
title: SVD分解具有聚类语义
aliases: []
statement: 在概率分解视角下，SVD 式矩阵分解可解释为行类、列类和类间关系的组合。
assumptions:
  - 矩阵元素可转为非负转移概率
  - 低维类别假设成立
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-01-26-SVD分解-二-为什么SVD意味着聚类.md
source_ids:
  - "4216"
requires:
  - [[线性自编码器矩阵分解公式]]
proof_route: 由源文局部推导抽取；公式细节见 requires。
methods:
  - [[用矩阵分解重写表示学习结构]]
limits:
  - 早期 SVD 系列偏解释性，严格定理仍以低秩近似系列为准。
examples: []
evidence_spans:
  - ev::4216::SVD分解是怎么聚类的
status: stable
updated: 2026-06-10
---

# SVD分解具有聚类语义

## 命题

在概率分解视角下，SVD 式矩阵分解可解释为行类、列类和类间关系的组合。

## 证据

- `ev::4216::SVD分解是怎么聚类的`
