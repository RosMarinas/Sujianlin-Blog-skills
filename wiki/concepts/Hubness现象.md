---
type: concept
title: "Hubness现象"
aliases: ["聚集现象"]
definition: "在高维空间随机样本中，少数数据点频繁出现在众多其他点的最近邻列表中的聚集现象，通常表现为距离或密度中心的点具有极大的Hub值。"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2022-06-28-维度灾难-之Hubness现象浅析.md"
source_ids: ["9147"]
evidence_spans: []
status: draft
null_evidence_reason: "Concept created via batch script, detailed evidence span defered."
updated: "2026-06-12"
---

# Hubness现象

## 定义
在高维空间随机样本中，少数数据点频繁出现在众多其他点的最近邻列表中的聚集现象，通常表现为距离或密度中心的点具有极大的Hub值。

## 关键性质
在高维空间中，由于体积分布向边缘集中，某些点会自然成为众多其他点的最近邻（Hub），而大量点则成为反Hub（Antihub）。Hubness现象的数学根源在于高维距离度量的集中效应：随着维数增加，所有点对之间的距离趋于相等，微小的方差波动导致部分点成为更近的邻居中心。这一现象在生成模型采样（导致样本多样性下降）和最近邻检索（导致部分样本被过度召回）中有直接负面影响，但也可用于设计基于Hub值加权的采样筛选策略。
