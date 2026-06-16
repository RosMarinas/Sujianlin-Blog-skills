---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: MesaNet解析解序列建模方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-03-18-时空之章-将Attention视为平方复杂度的RNN.md
source_ids:
  - 10017
method_summary: MesaNet利用线性回归的解析解构建序列模型。维护G_t和H_t两个状态，通过S_t = G_t H_t^{-1}计算输出。
typical_structure: |
  1. 将序列建模目标表达为具有时变权重的线性回归系统。
  2. 运用线性回归的最优解解析形式，得到输出公式：$o_t = G_t (H_t + \lambda_t)^{-1} q_t$。
  3. 通过递推关系维护协方差相关的状态矩阵：$G_t = \gamma_t G_{t-1} + v_t k_t^T$，$H_t = \gamma_t H_{t-1} + k_t k_t^T$。
  4. 使用共轭梯度法等数值技术高效求解涉及 $H_t^{-1}$ 的线性方程组。
applicability: 需要将问题重写为等价形式以便求解时，特别是将自回归或Attention过程改写为具有常数记忆容量的RNN结构。
examples:
  - [[article::10017]]
evidence_spans:
  - ev::10017::介绍了将Causal Attention重写为RNN的形式，阐述了通过重计算可实现O(1)空间复杂度，以及这种序列记忆形式在长文本上的瓶颈。
status: stable
updated: 2026-06-12
created: 2026-06-10
tags: 
related_articles: 
related_concepts: 
proposes: 
---

# MesaNet解析解序列建模方法

## 适用问题
需要将问题重写为等价形式以便求解时，特别是将自回归或Attention过程改写为具有常数记忆容量的RNN结构。

## 核心变换
将Attention的KV聚合过程看成是一个在线线性回归问题，从而利用线性最小二乘问题的闭式解析解作为RNN隐藏状态流转的代数引擎。

## 典型步骤
1. 将序列建模目标表达为具有时变权重的线性回归系统。
2. 运用线性回归的最优解解析形式，得到输出公式：$o_t = G_t (H_t + \lambda_t)^{-1} q_t$。
3. 通过递推关系维护协方差相关的状态矩阵：$G_t = \gamma_t G_{t-1} + v_t k_t^T$，$H_t = \gamma_t H_{t-1} + k_t k_t^T$。
4. 使用共轭梯度法等数值技术高效求解涉及 $H_t^{-1}$ 的线性方程组。

## 直觉
标准Attention像是在读每一页书时都要从头重温整本；而将其等价为一个解析解时，我们只需要维护“至今所读知识的充分统计量（协方差和交互项）”。根据解析解，我们在获取新输出时直接结合最新查询与历史的稳态表示，以此打破动态拓展内存的魔咒。

## 边界
解析解引入了协方差阵求逆 $H_t^{-1}$，通常不是三角阵，需要迭代求逆算法（如共轭梯度法）近似，且在$K=V$等特征重合时模型容易退化；表达灵活性不如传统的非线性前馈记忆机制。

## 例子
在计算Causal Attention时，将原始 $O(L^2)$ 成本的逐Token点积转换为维护一个固定的隐状态 $G_t$ 矩阵和 $H_t$ 矩阵的累积加权更新，从而可以达到恒定的 $O(1)$ 推理空间（尽管计算仍有代价）。

## 证据
- ev::10017::介绍了将Causal Attention重写为RNN的形式，阐述了通过重计算可实现O(1)空间复杂度，以及这种序列记忆形式在长文本上的瓶颈。
