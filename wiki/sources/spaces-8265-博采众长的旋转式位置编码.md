---
type: article_summary
title: 博采众长的旋转式位置编码
article_id: "8265"
source_url: https://spaces.ac.cn/archives/8265
date: 2021-03-23
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-03-23-Transformer升级之路-2-博采众长的旋转式位置编码.md
series: [Transformer升级之路]
topics: [位置编码, RoPE]
concepts: [旋转式位置编码, RoPE, RoFormer, 线性Attention, 相对位置编码与绝对位置编码的统一]
methods: [复数域解析解, 旋转矩阵分组操作, Abel变换分析衰减趋势]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-23-Transformer升级之路-2-博采众长的旋转式位置编码.md
source_ids:
  - "8265"
status: draft
updated: 2026-06-09
---

# 博采众长的旋转式位置编码

## 文章核心问题
如何设计一种位置编码，既能像绝对位置编码那样简单易用，又能像相对位置编码那样有效捕捉相对位置信息？如何实现位置编码与线性Attention的兼容？

## 主要结论
- RoPE成功在保持绝对位置编码的简单性同时，达到了相对位置编码的效果。
- RoPE具有与Sinusoidal位置编码一致的远程衰减性。
- RoPE是目前唯一可以直接兼容应用到线性Attention上的相对位置编码。
- 在RoFormer实验中，应用RoPE的Transformer模型在长文本处理任务上表现出良好的外推性和性能提升。

## 推导结构
作者利用复数乘法的几何意义，通过旋转矩阵将绝对位置信息注入到Query和Key中。从内积包含相对位置的需求出发，在复数域求解得到解析解，将偶数维度拆分成两两分组应用旋转矩阵，使得Query和Key做内积时自动体现出相对位置。随后通过Abel变换分析验证内积结果随着相对距离增加具有衰减趋势。

## 关键公式
- RoPE旋转: $\boldsymbol{q}_m = \boldsymbol{R}_m \boldsymbol{q}$, $\boldsymbol{k}_n = \boldsymbol{R}_n \boldsymbol{k}$
- 内积结果: $\boldsymbol{q}_m^{\top} \boldsymbol{k}_n = \boldsymbol{q}^{\top} \boldsymbol{R}_{m-n} \boldsymbol{k}$
- 旋转矩阵定义: $\boldsymbol{R}_{\theta} = \bigoplus_{i=1}^{d/2} \begin{bmatrix} \cos i\theta & -\sin i\theta \\ \sin i\theta & \cos i\theta \end{bmatrix}$

## 体现的方法
- 在复数域通过求解析解，将内积中包含相对位置的需求转换为对查询/键向量施加特定旋转操作
- 将偶数维度拆分成两两分组应用旋转矩阵
- 采用Abel变换分析验证内积结果随着相对距离增加的衰减趋势

## 所属系列位置
Transformer升级之路系列第2篇，提出自研的旋转式位置编码RoPE。

## 与其他文章的关系
在第1篇Sinusoidal位置编码理论分析的基础上，本文提出了更优的旋转式位置编码RoPE，将位置编码从被动分析推进到主动设计阶段。后续第4篇在此基础上扩展到二维场景，第6篇分析其完备性。

## 原文证据锚点
- 复数域求解得到旋转矩阵形式的RoPE解析解
- RoPE与Sinusoidal位置编码的远程衰减性对比分析
- RoFormer在长文本任务上的开源验证结果
