---
type: series
title: "重新思考学习率与Batch Size"
aliases:
  - "learning-rate batch-size scaling"
article_ids:
  - "11260"
  - "11280"
  - "11285"
  - "11301"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-01-重新思考学习率与Batch-Size-一-现状.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md"
source_ids:
  - "11260"
  - "11280"
  - "11285"
  - "11301"
series_goal: "用二阶近似和平均场方法解释学习率与 Batch Size 在 SGD、SignSGD、Muon、Adam/EMA 中的尺度关系。"
entry_roles:
  "11260": "建立二阶近似框架，把最优学习率写成更新量一阶矩和二阶矩的函数，并回顾 SGD 的 Batch Size 尺度律。"
  "11280": "用平均场近似替代 SignSGD/SoftSignSGD 中复杂的分布积分，得到显式 Batch Size 依赖。"
  "11285": "把平均场近似迁移到 Muon 的矩阵符号更新，说明其学习率-Batch Size 关系近似 SignSGD。"
  "11301": "分析动量/EMA 对优化器尺度律的影响，得出动量约等于放大有效 Batch Size。"
key_concepts:
  - "[[学习率-Batch Size尺度律]]"
  - "[[平均场近似学习率分析]]"
  - "[[EMA等效批量放大]]"
  - "[[Surge现象]]"
key_methods:
  - "[[用平均场近似替代复杂期望计算]]"
  - "[[用等效Batch Size解释动量降噪]]"
reading_paths:
  - "[[学习率与Batch Size尺度律阅读路径]]"
status: draft
updated: "2026-06-10"
---

# 重新思考学习率与Batch Size

## 系列核心问题

这个系列把学习率、Batch Size、优化器非线性更新和动量机制统一到“更新量统计量如何随 Batch Size 改变”的分析框架中。

## 文章顺序

1. [[重新思考学习率与Batch Size（一）：现状]]：建立二阶近似和 SGD 基线。
2. [[重新思考学习率与Batch Size（二）：平均场]]：用平均场简化 SignSGD/SoftSignSGD 推导。
3. [[重新思考学习率与Batch Size（三）：Muon]]：把平均场迁移到矩阵符号更新。
4. [[重新思考学习率与Batch Size（四）：EMA]]：把动量解释为有效 Batch Size 放大。

## 概念递进

[[学习率-Batch Size尺度律]] -> [[平均场近似学习率分析]] -> [[EMA等效批量放大]] -> [[Surge现象]]。

## 反复出现的方法

- [[用平均场近似替代复杂期望计算]]
- [[用等效Batch Size解释动量降噪]]

## Bridge Pass 预记录

本系列的新方法与既有 SGD 收敛系列、Muon 矩阵优化系列存在候选连接：平均场期望近似连接到 [[用期望消去采样依赖]]，EMA 有效批量连接到 [[用稳定性指标约束优化器缩放]]。这些连接当前只提升到 tentative，等待下一轮公式级 Bridge Pass D。
