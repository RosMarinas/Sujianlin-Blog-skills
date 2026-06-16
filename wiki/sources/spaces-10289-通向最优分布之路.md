---
type: article_summary
title: 通向最优分布之路：概率空间的最小化
article_id: "10289"
source_url: https://spaces.ac.cn/archives/10289
date: 2024-08-06
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-08-06-通向最优分布之路-概率空间的最小化.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[概率空间]]
  - [[凸集搜索]]
  - [[Wasserstein梯度流]]
methods:
  - [[拉格朗日乘子法]]
  - [[投影梯度下降]]
  - [[凸集搜索法]]
  - [[Wasserstein梯度流]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-08-06-通向最优分布之路-概率空间的最小化.md
source_ids:
  - "10289"
status: draft
updated: 2026-06-11
---

## 文章核心问题

当目标函数的输入是一个概率分布时，如何在其搜索空间中有效地进行优化，确保结果符合概率分布的特性。

## 主要结论

- 离散概率分布优化可通过凸集搜索实现，构造 $p_{t+\eta} = (1-\eta)p_t + \eta q_t$
- 连续概率分布优化需用变量代换和Wasserstein梯度流
- Wasserstein梯度流方程：$\frac{\partial p_t}{\partial t} = \nabla\cdot[p_t\nabla\frac{\delta\mathcal{F}[p_t]}{\delta p_t}]$

## 推导结构

1. 从无约束优化的梯度下降出发，引入投影梯度下降
2. 离散分布：凸集搜索 + onehot argmin 构造
3. 连续分布：变量代换 + 积分变换 → Wasserstein梯度流

## 关键公式

Wasserstein梯度流：$\frac{\partial p_t}{\partial t} = \nabla\cdot\left[p_t\nabla\frac{\delta \mathcal{F}[p_t]}{\delta p_t}\right]$

## 体现的方法

- 拉格朗日乘子法
- 投影梯度下降
- 凸集搜索法
- Wasserstein梯度流

## 所属系列位置

独立单篇，参考了[[梯度流]]系列和[[通向概率分布之路]]系列。

## 与其他文章的关系

与"通向概率分布之路：盘点Softmax及其替代品"（10145）紧密相关，讨论了Sparsemax等投影操作。

## 原文证据锚点

- 梯度下降回顾：搜索视角分析
- 投影下降：约束优化转化
- 离散分布凸集搜索：onehot argmin构造
- 连续分布变量代换：Wasserstein梯度流推导
