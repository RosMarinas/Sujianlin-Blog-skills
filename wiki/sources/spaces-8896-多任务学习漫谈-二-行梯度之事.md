---
type: article_summary
title: 多任务学习漫谈（二）：行梯度之事
article_id: "8896"
source_url: https://spaces.ac.cn/archives/8896
date: 2022-02-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-02-08-多任务学习漫谈-二-行梯度之事.md
series:
  - [[多任务学习漫谈]]
topics:
  - [[多任务学习与优化]]
concepts:
  - [[梯度手术]]
methods:

evidence_spans:
  - ev::8896::帕累托最优
  - ev::8896::Frank-Wolfe算法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-08-多任务学习漫谈-二-行梯度之事.md
source_ids:
  - "8896"
status: draft
updated: 2026-06-10
---
# 多任务学习漫谈（二）：行梯度之事

## 文章核心问题

如何从梯度设计而非损失函数的角度来构建多任务学习算法？

## 主要结论

多任务学习的核心是寻找更新方向u使得所有任务的损失都不上升：⟨g_i, u⟩ ≥ 0。这等价于求帕累托稳定点。通过对偶理论，问题转化为求各任务梯度的加权凝聚的最小模长：min_α ||∑ α_i g_i||^2。可用Frank-Wolfe算法迭代求解。

## 推导结构

1. 从梯度下降视角看多任务学习
2. 帕累托最优的形式化定义
3. 最大化最小内积的光滑近似解法
4. 对偶理论：min_α ||∑ α_i g_i||^2
5. Frank-Wolfe迭代求解
6. 共享编码器场景的近似优化（上界方法）
7. 指正原论文证明错误

## 关键公式

更新方向 u = ∑ α_i g_i, 满足 ⟨g_i, u⟩ ≥ 0 ∀i
对偶问题：min_{α∈P^n} ||∑ α_i g_i||^2

## 所属系列位置

多任务学习系列第二篇，深入梯度视角。

## 原文证据锚点

- ev::8896::帕累托最优 — 多任务学习中帕累托稳定的定义
- ev::8896::Frank-Wolfe算法 — 对偶问题的迭代求解
