---
type: formula
title: Hutchinson迹估计公式
latex: \text{Tr}(\boldsymbol{A}) = \mathbb{E}_{\boldsymbol{u} \sim p(\boldsymbol{u})} \left[ \boldsymbol{u}^T \boldsymbol{A} \boldsymbol{u} \right]
symbol_meanings:
  \boldsymbol{A}: 实数二次方阵
  \boldsymbol{u}: 多元独立同分布随机变量向量
  \mathbb{E}: 概率论中的期望算子
  \text{Tr}: 矩阵的迹算子（对角线求和）
standard_notation: \text{Tr}(\boldsymbol{A}) = \mathbb{E}_{\boldsymbol{u} \sim p(\boldsymbol{u})} \left[ \boldsymbol{u}^T \boldsymbol{A} \boldsymbol{u} \right]
conditions: 随机向量的均值必须为 0，且协方差矩阵满足 \mathbb{E}[\boldsymbol{u} \boldsymbol{u}^T] = \boldsymbol{I}（例如标准多元正态分布或 Rademacher 分布）。
appears_in:
  - "6482"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-03-21-细水长flow之可逆ResNet-极致的暴力美学.md
source_ids:
  - "6482"
status: draft
updated: 2026-06-12
---

# Hutchinson迹估计公式

## 概述

Hutchinson 迹估计公式是蒙特卡洛随机化近似算法中对大型隐式矩阵的迹进行估计的基础公式。由于直接求迹需要计算出矩阵的所有对角线元素（这需要完全计算出矩阵本身，开销巨大），Hutchinson 估计利用：
$$
\text{Tr}(A) = \text{Tr}(A \mathbb{E}[uu^T]) = \mathbb{E}[\text{Tr}(A u u^T)] = \mathbb{E}[u^T A u]
$$
在实际训练中，通过采样少量的向量 $u$ 进行单次或多次计算 $u^T A u$，即可获得迹的无偏估计。在可逆残差网络中，该公式将复杂的 $J_g^n$ 迹计算化为链式向量偏导数乘法，从而避免了全雅可比矩阵的显式计算，是实现高效可逆 ResNet 最大似然估计的关键桥梁。
