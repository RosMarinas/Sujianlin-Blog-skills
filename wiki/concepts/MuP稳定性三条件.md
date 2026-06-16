---
type: concept
title: MuP稳定性三条件
aliases: []
definition: 用前向稳定性、依赖稳定性和更新稳定性三组 Θ(1) 指标约束模型、输入扰动和参数增量。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-21-MuP之上-1-好模型的三个特征.md
- Data/Spaces_ac_cn/markdown/Big-Data/2026-02-15-MuP之上-2-线性层与最速下降.md
- Data/Spaces_ac_cn/markdown/Big-Data/2026-03-02-MuP之上-3-特殊情况特殊处理.md
- Data/Spaces_ac_cn/markdown/Big-Data/2026-04-24-MuP之上-4-坚守参数的稳定性.md
source_ids:
- '11340'
- '11605'
- '11647'
- '11729'
related_methods:
- - - 用稳定性指标约束优化器缩放
evidence_spans:
- ev::11340::三个条件
- ev::11729::问题背景
status: draft
updated: '2026-06-13'
---

# MuP稳定性三条件

## 定义

MuP稳定性三条件是源文提出的“好模型”约束：前向稳定性、依赖稳定性和更新稳定性都应保持 `Theta(1)`。它们分别约束模型输出量级、输出对输入变化的依赖量级，以及参数更新对输出造成的变化量级。

## 激活场景

该概念用于把架构、初始化、优化器、反向传播稳定性放到统一标度分析中。源文把 `f(x;omega)` 看作一层、一个块或整个模型，并通过对输入取最大值来得到关于参数 `omega` 与增量 `Delta omega` 的约束。

## 关键关系

前向稳定性要求 `max_x ||f(x;omega)||_RMS=Theta(1)`；依赖稳定性要求输入变化导致输出变化的比例为 `Theta(1)`，它也约束雅可比谱范数和反向传播；更新稳定性要求 `max_x ||f(x;omega+Delta omega)-f(x;omega)||_RMS=Theta(1)`，用于指导学习率、增量范数和最速下降式优化器缩放。在线性层例子中，源文将这三者转化为谱范数尺度 `sqrt(d_out/d_in)` 的参数与更新约束。

## 相关方法

- [[用稳定性指标约束优化器缩放]]

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2025-10-21-MuP之上-1-好模型的三个特征.md`
- `Data/Spaces_ac_cn/markdown/Big-Data/2026-04-24-MuP之上-4-坚守参数的稳定性.md`
- `ev::11340::三个条件`
- `ev::11729::问题背景`
