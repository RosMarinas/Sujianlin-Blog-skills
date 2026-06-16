---
type: concept
title: RMS尺度
aliases: []
definition: Root Mean Square 尺度，把向量模长归一到每个元素平均量级，用于比较不同维度模型中的激活和更新。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-21-MuP之上-1-好模型的三个特征.md
source_ids:
- '11340'
related_methods:
- - - 用稳定性指标约束优化器缩放
evidence_spans:
- ev::11340::三个条件
status: draft
updated: '2026-06-12'
---

# RMS尺度

## 定义

Root Mean Square 尺度，把向量模长归一到每个元素平均量级，用于比较不同维度模型中的激活和更新。

## 激活场景

源文在讨论“好模型的三个特征”时引入 RMS 尺度，用于跨宽度比较激活、输入扰动和参数更新的平均元素量级。它比直接使用 $\ell_2$ 模长更适合神经网络层分析，因为多数激活函数是 element-wise 的，稳定性关心的是每个元素看到的平均尺度。

## 关键关系

对 $\boldsymbol{x}=(x_1,\dots,x_d)$，源文定义
$$
\Vert\boldsymbol{x}\Vert_{RMS}=\sqrt{\frac{1}{d}\sum_i x_i^2}=\frac{\Vert\boldsymbol{x}\Vert_2}{\sqrt{d}}.
$$
基于这个尺度，源文写出前向稳定性、依赖稳定性和更新稳定性三个条件，均要求相关 RMS 量级为 $\Theta(1)$。因此 RMS 尺度不仅是记号，也决定了 MuP 之上系列如何比较不同宽度模型、如何分析 Embedding、LM Head 和线性层的初始化及学习率缩放。

## 相关方法

- [[用稳定性指标约束优化器缩放]]

## 证据

- `ev::11340::三个条件`
