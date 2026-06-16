---
type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: Match Adam Update RMS迁移法
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-09-02-为什么Adam的Update-RMS是0-2.md
source_ids:
  - 11267
method_summary: 通过匹配不同优化器之间的更新步均方根（Update RMS），实现将学习率和权重衰减率从已调优的 Adam 优化器直接无缝迁移到其他新优化器的技术。
typical_structure: |
  1. 计算或记录Adam优化器在相同模型上的Update RMS均方根，稳态下一般为0.2~0.3（例如0.2）。
  2. 在新优化器（例如Muon）的实现中，强制对更新向量进行缩放，使其RMS等于0.2。
  3. 直接复用原本为Adam调优的学习率和权重衰减等超参数。
applicability: 在大规模 LLM 训练中，需要从 Adam 迁移至 Muon 等新型正交优化器，且希望保留已有 Adam 训练超参（学习率、权重衰减）以规避重新调参的巨大算力开销。
examples:
  - [[spaces-11267-为什么Adam的Update-RMS是0-2]]
evidence_spans:
  - ev::11267::提出了将Muon的Update RMS统一成0.2，以复用Adam的学习率和权重衰减率，源于观测到Adam的稳态Update RMS约等于0.2。
status: stable
updated: 2026-06-12
---

# Match Adam Update RMS迁移法

## 适用问题
在大规模 LLM 训练中，需要从 Adam 迁移至 Muon 等新型正交优化器，且希望保留已有 Adam 训练超参（学习率、权重衰减）以规避重新调参的巨大算力开销。

## 核心变换
找到 Adam 稳态下的更新步长均方根（Update RMS）作为不变量，并将新优化器（如Muon）的更新步长缩放对齐到该不变量尺度上。

## 典型步骤
1. 计算或记录Adam优化器在相同模型上的Update RMS均方根，稳态下一般为0.2~0.3（例如0.2）。
2. 在新优化器（例如Muon）的实现中，强制对更新向量进行缩放，使其RMS等于0.2。
3. 直接复用原本为Adam调优的学习率和权重衰减等超参数。

## 直觉
如果两个优化器在参数空间中每一步行进的统计物理步长一致，那么它们的学习率和权重衰减等尺度相关超参数应该具有可迁移性。因为Adam（β1=0.9）稳态时的Update RMS通常约为0.2，把新优化器的均方根也约束为0.2相当于在同一量纲刻度下行进。

## 边界
要求新优化器的更新机制允许通过全局标量进行缩放且不破坏其本身属性（例如Muon的正交性质）。此外，如果Adam所用的超参数并非处于稳态分布或信噪比极特殊，该0.2的经验值可能需要微调。

## 例子
在 Kimi K2 的预训练中，直接将Muon优化器的Update RMS拉平为0.2，从而直接复用Adam的学习率调度方案。

## 证据
- ev::11267::提出了将Muon的Update RMS统一成0.2，以复用Adam的学习率和权重衰减率，源于观测到Adam的稳态Update RMS约等于0.2。
