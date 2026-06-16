---
type: article_summary
title: 对齐全量微调！这是我看过最精彩的LoRA改进（二）
article_id: "10266"
source_url: https://spaces.ac.cn/archives/10266
date: 2024-07-29
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-07-29-对齐全量微调-这是我看过最精彩的LoRA改进-二.md
source_html: Data/Spaces_ac_cn/raw/articles/10266/page.html
series:
  - "[[series::LoRA改进系列]]"
topics:
  - "[[topic::LoRA微调]]"
concepts:
  - "[[concept::LoRA]]"
  - "[[concept::LoRA-Pro]]"
methods:
  - "[[method::用伪逆投影优化LoRA更新]]"
problem_patterns: []
evidence_spans:
  - ev::10266::对齐全量
  - ev::10266::逐步对齐
  - ev::10266::简化目标
  - ev::10266::完整结果
  - ev::10266::最优参数
  - ev::10266::一般讨论
  - ev::10266::实验结果
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-07-29-对齐全量微调-这是我看过最精彩的LoRA改进-二.md
source_ids:
  - "10266"
status: draft
updated: 2026-06-11
---

## 文章核心问题

LoRA-Pro如何通过修改优化器更新规则来对齐LoRA与全量微调的每一步梯度，从而实现整条优化轨迹的对齐？

## 主要结论

1. LoRA-Pro修改A,B的更新规则为A_{t+1}=A_t-ηH_{A,t}, B_{t+1}=B_t-ηH_{B,t}，通过最小化‖H_A B + A H_B - G_t‖_F^2来对齐每一步更新。
2. H_A,H_B的解通过矩阵伪逆求得：H_A=G_A(BB^T)^{-1}, H_B=(A^T A)^{-1}G_B(I-B^T(BB^T)^{-1}B)。
3. 解中存在可自由选择的参数矩阵C，可通过Sylvester方程选择C使H_A,H_B对称或接近原始梯度。
4. LoRA-Pro在GLUE上超过全量微调结果，且与LoRA-GA的初始化方案互补。

## 推导结构

对齐全量（LoRA更新公式回顾）→ 逐步对齐（提出修改优化器的思路和目标函数）→ 简化目标（伪逆的最小二乘解）→ 完整结果（H_A,H_B的解析解及不变性）→ 最优参数（选择C使对称性最优）→ 一般讨论（Adam下的扩展方案）。

## 关键公式

- 全量SGD：W_{t+1} = W_t - ηG_t
- LoRA-Pro新规则：A_{t+1}=A_t-ηH_{A,t}, B_{t+1}=B_t-ηH_{B,t}
- 对齐目标：argmin_{H_A,H_B} ‖H_A B + A H_B - G‖_F^2
- 伪逆解：H = XB^T(BB^T)^{-1} 和 H = (A^T A)^{-1}A^T X
- H_A = G_A(BB^T)^{-1} + AC, H_B = (A^T A)^{-1}G_B(I - B^T(BB^T)^{-1}B) - CB

## 体现的方法

- **用伪逆投影优化LoRA更新**：通过矩阵伪逆求解H_A,H_B使LoRA每一步更新逼近全量微调，实现整条优化轨迹对齐。

## 所属系列位置

[[series::LoRA改进系列]]第二篇，与[[article::10226]]互补。LoRA-GA改进初始化，LoRA-Pro改进优化器更新规则。

## 与其他文章的关系

- 引用[[article::10226]]作为LoRA-GA方法背景，LoRA-Pro的初始化建议采用LoRA-GA方案。
- 引用[[article::10001]]讨论对称性假设。
- 与[[method::用梯度SVD初始化LoRA]]互补：一个改进初始化，一个改进更新规则。

## 原文证据锚点

- `ev::10266::对齐全量`：LoRA和全量微调SGD公式回顾。
- `ev::10266::逐步对齐`：修改优化器更新规则的思路和目标函数。
- `ev::10266::简化目标`：伪逆最小二乘解的推导。
- `ev::10266::完整结果`：H_A,H_B解析解及不变性。
- `ev::10266::最优参数`：通过Sylvester方程选择C。
- `ev::10266::一般讨论`：Adam下扩展方案和显存分析。
- `ev::10266::实验结果`：GLUE实验结果。
