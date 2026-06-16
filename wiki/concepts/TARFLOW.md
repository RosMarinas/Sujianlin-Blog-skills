---
type: concept
title: TARFLOW
definition: 一种结合了Causal Transformer自回归架构和多块划分仿射耦合层的自回归流模型（Normalizing Flow），在空间维度（Patchify）上进行划分并高效地建模图像相关性。
standard_notation: "\text{TARFLOW}"
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-01-17-细水长flow之TARFLOW-流模型满血归来.md
source_ids:
- 10667
prerequisites:
- - - Normalizing Flow
- - - 仿射耦合层
status: draft
updated: '2026-06-12'
---

# TARFLOW

## 定义

TARFLOW 是源文介绍的 Transformer AutoRegressive Flow：它仍属于 Normalizing Flow，但把仿射耦合层推广为多块划分，并用 Causal Transformer 高效建模 $\boldsymbol{x}_{<k}$ 到第 $k$ 块参数的依赖。源文强调，TARFLOW 让流模型在视觉生成任务上重新接近当前强模型的效果。

## 激活场景

本概念用于连接流模型基础、仿射耦合层和图像 Patchify。Method 页讨论 TARFLOW 采样、去噪或多块自回归耦合时，需要知道它不是文本 LLM 的自回归建模，而是为了满足耦合层可逆结构而产生的块顺序依赖。

## 关键关系

源文中的核心公式将输入划分为 $[\boldsymbol{x}_1,\dots,\boldsymbol{x}_n]$，对 $k>1$ 使用
$$
\boldsymbol{h}_k=\exp(\boldsymbol{\gamma}_k(\boldsymbol{x}_{<k}))\otimes\boldsymbol{x}_k+\boldsymbol{\beta}_k(\boldsymbol{x}_{<k}).
$$
这种结构继承了仿射耦合的可逆性和对数雅可比行列式可加性。TARFLOW 的关键改进是选择空间维度 Patchify，并利用 Transformer 不依赖 CNN 局部排列的特点来建模块之间的相关性。

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2025-01-17-细水长flow之TARFLOW-流模型满血归来.md`
