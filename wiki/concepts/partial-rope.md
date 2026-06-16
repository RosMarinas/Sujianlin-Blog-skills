---
type: concept
definition: Partial RoPE（部分旋转位置编码）是指对Attention的Q、K向量只对部分维度施加RoPE旋转，剩余维度保持不变的编码方式。这种设计最早在GPT-NeoX中应用，后来在DeepSeek的MLA中得到了关键性的使用。
title: Partial RoPE (部分旋转位置编码)
status: draft
created: '2026-06-09'
tags:
- RoPE
- 部分旋转
- 位置编码
- 语义聚合
related_articles:
- 10122
- 10907
- 11111
related_concepts:
- rotary-position-embedding
- mla
- rope-base-selection
evidence_spans:
- 10122-部分旋转
- 11111-部分旋转
- 10907-实验
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## 核心定义

Partial RoPE（部分旋转位置编码）是指对Attention的Q、K向量只对部分维度施加RoPE旋转，剩余维度保持不变的编码方式。这种设计最早在GPT-NeoX中应用，后来在DeepSeek的MLA中得到了关键性的使用。

数学上，以只旋转一半维度为例，其频率为：
- i < d/4: θ_i = b^{-4i/d}（旋转）
- i ≥ d/4: θ_i = 0（不旋转）

## 关键性质

1. **兼顾位置与语义**：NoPE部分负责语义聚合（关注内容相关性），RoPE部分负责位置编码，两者互补。
2. **自动满足语义聚合不等式**：Partial RoPE使 Σ cos(mθ_i) ≥ 0 对所有m、b恒成立，从理论看具有更好的语义聚合能力。
3. **效果不逊于完整RoPE**：实验显示Partial RoPE的效果可能略优于完整RoPE（GQA1-256-PR Loss=2.711 vs GQA1-256 Loss=2.72）。
4. **为MLA提供基础**：Partial RoPE允许将主要计算置于NoPE部分，这是MLA能够实现双重投影的理论前提。
5. **历史渊源**：最早在GPT-NeoX中被实验使用，但当时未被充分理解。

## 为什么有效

从RoPE底数选择原则的视角看，完整RoPE的部分维度在训练圈数不足时会出现OOD问题（低频维度）。Partial RoPE通过在一些维度上完全取消旋转，使这些维度不受圈数约束，自动保持非负的语义聚合。

此外，Partial RoPE可以理解为一种"层间的NoPE与RoPE交替"——不仅可在维度层面部分旋转，也可在层层面让NoPE层占多数。

## 实验验证

- GQA1-256: Loss=2.72（完整RoPE）
- GQA1-256-PR: Loss=2.711（Partial RoPE，192 NoPE + 64 RoPE）
- MLA的核心设计就是Partial RoPE（128+64中的128是NoPE，64是RoPE）

## 出现位置

- [第18篇](/archives/10122) "部分旋转"节首次系统分析
- [第20篇](/archives/10907) 实验验证Partial RoPE的实际效果
- [第21篇](/archives/11111) 作为MLA最优性的理论大前提

## 原文证据

- 原文10122"部分旋转"节：指出Partial RoPE自动满足语义聚合不等式(eq:neq:base)
- 原文10122"部分旋转"节：提到DeepSeek MLA应用了Partial RoPE
- 原文11111"部分旋转"节：断言"Partial RoPE效果不逊色于甚至可能优于完全体RoPE"
- 原文10907 Part I：GQA1-256-PR(Loss=2.711)优于GQA1-256(Loss=2.72)的实验证据