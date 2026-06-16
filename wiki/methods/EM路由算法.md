---
type: method
operation_types:
  primary: "Estimate / sample instead of compute"
  secondary: []
title: "EM路由算法"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2018-03-02-三味Capsule-矩阵Capsule与EM路由.md"
source_ids:
  - "5155"
method_summary: "把矩阵 Capsule 的路由过程改写为高斯混合模型式聚类：在候选父 Capsule 间估计分配、均值、方差与激活值，迭代得到更稳定的路由结果。"
typical_structure: |
  1. 将低层 Capsule 通过变换矩阵投票到高层 Capsule 空间。
  2. 用 GMM/EM 思路在高层 Capsule 间估计软分配。
  3. 根据分配更新每个高层 Capsule 的均值、方差和聚类代价。
  4. 用信息熵或聚类不确定性相关量计算激活值并进入下一轮路由。
applicability: "适用于矩阵 Capsule 中需要用可导聚类替代动态路由、同时利用激活值表达父 Capsule 是否成立的场景。"
examples:
  - "[[example::EM路由算法应用实例]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::5155::新版路由"
  - "ev::5155::激活值"
---

# EM路由算法

## 适用问题

适用于矩阵 Capsule 中需要用可导聚类替代动态路由、同时利用激活值表达父 Capsule 是否成立的场景。

## 核心变换

低层 Capsule 投票 -> GMM/EM 聚类迭代 -> 高层 Capsule 姿态矩阵与激活值。

## 典型步骤

1. 将低层 Capsule 通过变换矩阵投票到高层 Capsule 空间。
2. 用 GMM/EM 思路在高层 Capsule 间估计软分配。
3. 根据分配更新每个高层 Capsule 的均值、方差和聚类代价。
4. 用信息熵或聚类不确定性相关量计算激活值并进入下一轮路由。

## 直觉

路由本质上是在判断哪些低层投票属于同一个上层对象；用 GMM 使这一判断变成软聚类估计，激活值则反映聚类是否集中。

## 边界

证据只支持矩阵 Capsule 语境下的 EM 路由；它不是通用 EM 算法页面，也不应脱离 Capsule 投票结构泛化。

## 例子

- 5155 解释 Matrix Capsule 的新点包括矩阵表示、GMM 聚类和 Capsule 版卷积，并把新版路由描述为 GMM 配合激活值的迭代过程。

## 证据

- `ev::5155::新版路由`
- `ev::5155::激活值`
- `Data/Spaces_ac_cn/markdown/Big-Data/2018-03-02-三味Capsule-矩阵Capsule与EM路由.md`
- 读取章节: GMM模型简介、路由现、激活值
