---
title: 模型自噬紊乱 (MAD)
definition: Model Autophagy Disorder，生成模型反复用自身生成的数据迭代训练导致多样性丧失和质量崩溃。
type: concept
status: draft
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# 模型自噬紊乱 (MAD)

## Definition
Model Autophagy Disorder，生成模型反复用自身生成的数据迭代训练导致多样性丧失和质量崩溃。

## Mechanism
- 截断技巧加速多样性丧失（方差以λ比率衰减）
- 即使无截断技巧，有限样本下均值也会偏移
- 只有持续引入新鲜真实数据才能避免退化

## Related Sources
- [[sources/spaces-9687-生成模型MAD]]