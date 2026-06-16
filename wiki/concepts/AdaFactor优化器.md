---
type: concept
title: AdaFactor优化器
aliases:
- Adafactor
- Adaptive Learning Rates with Sublinear Memory Cost
definition: Google提出的省显存优化器，通过移除动量、低秩分解二阶矩估计、时变Beta2衰减和层自适应标准化，大幅减少Adam的缓存变量参数量。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-03-23-AdaFactor优化器浅析-附开源实现.md
source_ids:
- '7302'
prerequisites:
- '[[Adam优化器]]'
equivalent_forms: []
related_formulas:
- '[[AdaFactor更新公式]]'
related_methods:
- '[[把优化算法解释为动力系统离散化]]'
series:
- '[[从动力学角度看优化算法]]'
evidence_spans:
- ev::7302::抛弃动量
- ev::7302::低秩分解
- ev::7302::广义KL散度推导
- ev::7302::滑动权重
- ev::7302::层自适应
status: draft
updated: '2026-06-12'
---

# AdaFactor优化器

## Definition

AdaFactor对标准Adam做了四项改造以节省显存：
1. 抛弃动量m，只维护二阶矩v（省一半缓存）。
2. 对梯度平方矩阵做秩1分解，维护行/列两组缓存v^{(r)}、v^{(c)}而非全矩阵v。
3. 使用时变Beta2衰减β̂_{2,t}=1-t^{-c}（默认c=0.8），满足β̂_{2,1}=0, β̂_{2,∞}=1。
4. 基于参数模长标准化更新量（类似LAMB），使各层更新同步。