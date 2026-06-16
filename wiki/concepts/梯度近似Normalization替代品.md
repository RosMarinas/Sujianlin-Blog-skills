---
title: 通过梯度近似寻找Normalization的替代品
definition: 从RMS Norm的雅可比矩阵出发，通过保留对角线部分推导Element-wise近似函数，得到DyT(基于tanh)和DyISRU(基于sqrt)两种Normalization替代方案。
type: concept
source_url: https://spaces.ac.cn/archives/10831
date: '2025-04-02'
author: 苏剑林
tags:
- Normalization
- DyT
- ISRU
- 梯度近似
- 雅可比矩阵
status: draft
updated: '2026-06-12'
source_ids:
- '10831'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-02-通过梯度近似寻找Normalization的替代品.md
---

# 通过梯度近似寻找Normalization的替代品

## 概述
从RMS Norm的雅可比矩阵出发，通过保留对角线部分推导Element-wise近似函数，得到DyT(基于tanh)和DyISRU(基于sqrt)两种Normalization替代方案。

## 核心思想
1. RMS Norm的梯度可以精确计算，其雅可比矩阵包含非对角线元素。
2. Element-wise近似的本质是保留对角线部分。
3. 进一步消除全局范数依赖后得到ISRU形式。

## 关键推导
RMS Norm梯度: nabla_x y = (I - yy^T/d) / ||x||_RMS
对角线近似 -> DyT: y_i = sqrt(d) * tanh(x_i / (rho*sqrt(d)))
精确对角化 -> DyISRU: y_i = sqrt(d) * x_i / sqrt(x_i^2 + C)

## 相关工作
- softcap(t*tanh(x/t))可用于clip的光滑近似
- Gemma2的softcap被Gemma3的QK-norm取代