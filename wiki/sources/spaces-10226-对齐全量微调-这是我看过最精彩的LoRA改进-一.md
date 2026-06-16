---
type: article_summary
title: 对齐全量微调！这是我看过最精彩的LoRA改进（一）
article_id: "10226"
source_url: https://spaces.ac.cn/archives/10226
date: 2024-07-12
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-07-12-对齐全量微调-这是我看过最精彩的LoRA改进-一.md
source_html: Data/Spaces_ac_cn/raw/articles/10226/page.html
series:
  - "[[series::LoRA改进系列]]"
topics:
  - "[[topic::LoRA微调]]"
concepts:
  - "[[concept::LoRA]]"
  - "[[concept::LoRA-GA]]"
methods:
  - "[[method::用梯度SVD初始化LoRA]]"
problem_patterns: []
evidence_spans:
  - ev::10226::基础回顾
  - ev::10226::对齐全量
  - ev::10226::求解过程
  - ev::10226::一般结果
  - ev::10226::实验效果
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-07-12-对齐全量微调-这是我看过最精彩的LoRA改进-一.md
source_ids:
  - "10226"
status: draft
updated: 2026-06-11
---

## 文章核心问题

LoRA-GA如何通过改进初始化来对齐LoRA与全量微调的第一步更新，使得LoRA的效果更接近全量微调？

## 主要结论

1. LoRA-GA通过最小化‖A_0 A_0^T G_0 + G_0 B_0^T B_0 - G_0‖_F^2来对齐LoRA与全量微调的第一步更新后的W_1。
2. 该优化问题的解析解通过对初始梯度G_0进行SVD分解得到：取U的前r列初始化A，取V的第r+1~2r行初始化B。
3. 对于Adam优化器，理论上无法得到解析解，但可直接沿用SGD的结论，实验支持这一选择。
4. LoRA-GA在GLUE上取得了最接近全量微调的效果，数据量越少相对提升越大。

## 推导结构

基础回顾（LoRA参数化方式）→ 对齐全量（定义对齐目标函数）→ 求解过程（从对角阵到SVD的推广）→ 一般结果（LoRA-GA初始化方法）→ Adam讨论（三个可选方案）→ 实验效果（GLUE和LLAMA2-7b结果）。

## 关键公式

- LoRA参数化：W = (W_0 - A_0 B_0) + AB
- 全量SGD一步更新：W_1 = W_0 - η ∂L/∂W_0
- LoRA SGD一步更新：W_1 ≈ W_0 - η(A_0 A_0^T G_0 + G_0 B_0^T B_0)
- 对齐目标：argmin_{A_0,B_0} ‖A_0 A_0^T G_0 + G_0 B_0^T B_0 - G_0‖_F^2
- 最优解：A_0 = U_{[:,:r]}, B_0 = V_{[r:2r,:]}，其中G_0 = UΣV

## 体现的方法

- **用梯度SVD初始化LoRA**：通过对初始梯度做SVD分解来确定LoRA的A,B初始化值，使得LoRA SGD一步更新结果尽可能接近全量微调。

## 所属系列位置

[[series::LoRA改进系列]]第一篇。与[[article::10266]]互补（前者改进初始化，后者改进优化器更新规则）。基于[[article::9590]]和[[article::10001]]的LoRA基础分析。

## 与其他文章的关系

- 被[[article::10266]]引用作为LoRA-GA方法背景。
- 引用[[article::9590]]和[[article::10001]]作为LoRA基础知识。
- 与[[method::用伪逆投影优化LoRA更新]]共享"对齐全量微调"的生成动作。

## 原文证据锚点

- `ev::10226::基础回顾`：LoRA参数化方式，A,B之一全零初始化，也可非全零。
- `ev::10226::对齐全量`：对齐目标函数的定义和动机。
- `ev::10226::求解过程`：从对角阵到一般SVD的推导过程。
- `ev::10226::一般结果`：LoRA-GA初始化方法描述和Adam讨论。
- `ev::10226::实验效果`：GLUE和LLAMA2-7b实验结果。
