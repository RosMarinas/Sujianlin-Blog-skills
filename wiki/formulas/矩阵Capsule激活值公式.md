---
type: formula
title: 矩阵Capsule激活值公式
aliases: []
latex: "a_j = \\text{sigmoid}\\left( \\lambda \\left( \\beta_a - \\left(\\beta_u+\\sum_{l=1}^d \\ln \\sigma_j^l \\right)\\sum_i r_{ij}\\right)\\right)"
symbol_meanings: {"$a_j$": "类 j 的激活值", "$\\sigma_j^l$": "高斯混合模型中类 j 的第 l 维标准差", "$r_{ij}$": "归一化责任度", "$\\lambda, \\beta_a, \\beta_u$": "可学习或退火参数"}
standard_notation:
  - "a_j = \\text{sigmoid}\\left( \\lambda \\left( \\beta_a - cost_j \\right)\\right)"
conditions: 基于高斯混合模型进行Capsule聚类，假设各分量独立
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-03-02-三味Capsule-矩阵Capsule与EM路由.md
source_ids:
  - "5155"
appears_in:
  - "[[spaces-5155-三味Capsule-矩阵Capsule与EM路由]]"
evidence_spans:
  - ev::5155::激活值公式
status: stable
updated: 2026-06-14
---

## 概述

矩阵 Capsule 中基于 EM 路由的类别激活值公式。将 Capsule 姿态矩阵建模为高斯混合模型，$a_j$ 通过比较描述长度代价与激活阈值来决定第 $j$ 个类别是否被激活。

## 公式

$$
a_j = \text{sigmoid}\left( \lambda \left( \beta_a - \left(\beta_u+\sum_{l=1}^d \ln \sigma_j^l \right)\sum_i r_{ij}\right)\right)
$$

## 符号说明

- $a_j$：类别 $j$ 的激活值，sigmoid 输出在 $(0,1)$
- $r_{ij}$：低层 Capsule $i$ 对类别 $j$ 的归一化责任度（E 步）
- $\sigma_j^l$：类别 $j$ 高斯分布第 $l$ 维标准差（M 步）
- $\beta_a, \beta_u$：可学习的激活阈值和描述长度惩罚
- $\lambda$：退火系数，随训练增大使路由硬化

## 条件

基于 GMM 假设，各分量独立；需配合 EM 路由算法。

## 证据

- ev::5155::激活值公式
