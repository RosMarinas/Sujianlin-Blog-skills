---
title: 梯度视角下的LoRA：简介、分析、猜测及推广
definition: 从梯度角度理解LoRA，讨论其两种等效实现的计算复杂度，从优化器视角实现LoRA（投影梯度），并提出加性分解的LoRA变体。
type: concept
source_url: https://spaces.ac.cn/archives/9590
date: '2023-04-17'
author: 苏剑林
tags:
- LoRA
- 梯度
- 低秩分解
- 参数高效微调
- AdaFactor
status: draft
updated: '2026-06-12'
source_ids:
- '9590'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2023-04-17-梯度视角下的LoRA-简介-分析-猜测及推广.md
---

# 梯度视角下的LoRA：简介、分析、猜测及推广

## 概述
从梯度角度理解LoRA，讨论其两种等效实现的计算复杂度，从优化器视角实现LoRA（投影梯度），并提出加性分解的LoRA变体。

## 核心思想
1. LoRA的两种实现方式：(2) Y = X(W0+AB) 需算完整梯度，费显存；(3) Y = XW0 + XAB 高效。
2. 优化器视角：从全量梯度投影得到A、B的梯度，可降低优化器状态显存。
3. 随机投影猜想：每步随机初始化低秩向量做投影，平均意义上等价于SGD。
4. 加性分解：用A*1 + 1*B替代A*B，秩可能为2，表达能力更强。

## 与AdaFactor的联系
LoRA的低秩分解与AdaFactor优化器的低秩分解在思想上相似。