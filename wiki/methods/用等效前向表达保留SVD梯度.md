---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: 用等效前向表达保留SVD梯度
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-04-26-SVD的导数.md
source_ids:
  - 10878
method_summary: 把 SVD 结果替换成前向值相同但梯度路径更明确的表达式，使自动求导框架得到目标梯度。
typical_structure: |
  1. 先用矩阵微分推导目标 SVD 表达的梯度形式。
  2. 构造前向值与原 SVD 输出等价的复合表达式。
  3. 对只应作为常量的奇异向量或中间项施加 stop-gradient。
  4. 让自动求导沿等效表达式反传，得到期望的原矩阵梯度。
applicability: 适用于需要把表示学习结构、矩阵分解或可导矩阵层进行等价改写的场景。
tools: 
related_methods: 
examples:
  - [[spaces-10878-SVD等效前向梯度]]
status: stable
updated: 2026-06-12
problem_patterns: 
evidence_spans:
  - ev::10878::梯度一
  - ev::10878::梯度三
---





# 用等效前向表达保留SVD梯度

## 适用问题

需要在深度学习框架中使用 SVD 或奇异向量相关表达式，但默认自动求导路径与手推矩阵微分目标不一致，或需要阻断部分中间量梯度。

## 核心变换

把 SVD 结果替换成前向值相同、但梯度路径被显式设计过的表达式，使自动求导框架沿等效前向得到目标梯度。

## 典型步骤

1. 先通过微分确定目标梯度
2. 寻找前向值相同的线性复合表达
3. 对奇异向量等量 stop_gradient
4. 交给自动求导计算原矩阵梯度

## 直觉

自动求导只看计算图，不理解“这个前向等价式只是为了保留某条梯度”。通过改写前向表达并冻结不应反传的量，可以把手推微分结果编码进计算图。

## 边界

该方法依赖已经手工确认的等效前向和目标梯度；如果奇异值重合、SVD 不可微或推导条件不满足，页面只支持作为候选实现技巧，不应承诺稳定梯度。

## 例子

- [[spaces-10878-SVD等效前向梯度]]

## 证据

- `ev::10878::梯度一`
- `ev::10878::梯度三`
