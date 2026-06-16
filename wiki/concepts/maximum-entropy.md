---
title: 最大熵原理
definition: 在所有满足给定约束的分布中，熵最大的分布是对未知事件最客观的认知。
type: concept
status: deprecated
replaced_by: '[[concept::最大熵原理]]'
updated: '2026-06-12'
deprecation_reason: Merged into concept::最大熵原理 as part of Pass A node boundary repair.
  Shadow node with duplicate content.
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# 最大熵原理

## Definition
在所有满足给定约束的分布中，熵最大的分布是对未知事件最客观的认知。

## Key Result
在所有均值为0、方差为1的分布中，标准正态分布的熵最大。

## Application in Generative Models
EAE模型使用最大熵原理将自编码器变为生成模型: 通过BN约束隐变量均值为0、方差为1，然后最大化隐变量熵。

## Related Sources
- [[sources/spaces-7343-EAE]]