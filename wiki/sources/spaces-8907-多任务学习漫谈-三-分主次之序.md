---
type: article_summary
title: 多任务学习漫谈（三）：分主次之序
article_id: "8907"
source_url: https://spaces.ac.cn/archives/8907
date: 2022-02-14
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-02-14-多任务学习漫谈-三-分主次之序.md
series:
  - [[多任务学习漫谈]]
topics:
  - [[多任务学习与优化]]
concepts:
  - [[多任务学习]]
methods:

evidence_spans:
  - ev::8907::主次型多任务学习
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-14-多任务学习漫谈-三-分主次之序.md
source_ids:
  - "8907"
status: draft
updated: 2026-06-10
---
# 多任务学习漫谈（三）：分主次之序

## 文章核心问题

当多目标不是平等而是有主次之分（主任务为主、辅助任务仅不退化即可）时，如何设计梯度更新方向？

## 主要结论

主次型多任务学习转化为约束优化问题：max_u ⟨u,g_0⟩ - 0.5||u||^2 s.t. ⟨u,g_i⟩≥0。对偶后等价于求解 min_{λ_i≥0} ||g_0 + ∑ λ_i g_i||^2。主次型与平行型共享Frank-Wolfe框架但结构不同。正则项和带噪学习均可视为主次型多任务学习的特例。

## 推导结构

1. 主次型多任务学习的目标形式化
2. 拉格朗日乘子法转化为min-max
3. Minimax定理交换次序
4. n=1情形的解析解
5. Frank-Wolfe迭代求解
6. 与平行型的对比表格
7. 应用：正则项、带噪学习

## 关键公式

min_{λ_i≥0} ||g_0 + ∑ λ_i g_i||^2 — 对偶问题
γ = relu(-⟨g_0,g_1⟩)/||g_1||^2 — 单辅助任务的解析解

## 所属系列位置

多任务学习系列第三篇，推广到主次型场景。

## 原文证据锚点

- ev::8907::主次型多任务学习 — 主次型多任务学习的形式化
- ev::8907::正则项连接 — L2正则作为主次型多任务的实例
