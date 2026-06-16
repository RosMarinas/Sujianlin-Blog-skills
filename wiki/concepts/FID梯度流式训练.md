---
title: 直接以FID为Loss：从梯度计算到流式训练
definition: FID（Frechet Inception Distance）是视觉生成模型的关键评价指标。本文从理论上分析了将FID作为损失函数训练生成模型的困难，并提出EMA流式近似方案来克服小Batch
  Size导致的梯度偏差问题。
type: concept
source_url: https://spaces.ac.cn/archives/11738
date: '2026-05-08'
author: 苏剑林
tags:
- FID
- FD Loss
- 流式训练
- 梯度计算
- 生成模型
status: draft
updated: '2026-06-12'
source_ids:
- '11738'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-05-08-直接以FID为Loss-从梯度计算到流式训练.md
---

# 直接以FID为Loss：从梯度计算到流式训练

## 概述
FID（Frechet Inception Distance）是视觉生成模型的关键评价指标。本文从理论上分析了将FID作为损失函数训练生成模型的困难，并提出EMA流式近似方案来克服小Batch Size导致的梯度偏差问题。

## 核心思想
1. FID可导：所有运算（均值、协方差、矩阵平方根）均可导。
2. 小Batch困难：协方差非线性计算需要大Batch，否则估计有偏。
3. 等效损失技巧：利用stop gradient将全局统计量注入每个小Batch的损失。
4. EMA流式近似：滑动平均维护全局统计量，实现每步可更新。

## 关键公式
Frechet Distance: F = ||mu_p - mu_q||^2 + tr(Sigma_p + Sigma_q - 2(Sigma_p^{1/2} Sigma_q Sigma_p^{1/2})^{1/2})
梯度计算涉及正定对称矩阵的平方根和逆平方根。

## 与其他工作的关系
- 对比学习也有类似的跨样本运算batch size问题。
- 损失归一化来自《多任务学习漫谈（一）》。
- 流式思想来自"流式幂迭代"系列。