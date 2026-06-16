---
type: concept
title: Embedding输出头稳定性
aliases: []
definition: Embedding 与输出头因输入域和损失函数位置特殊，需单独计算前向、依赖和更新稳定性。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-03-02-MuP之上-3-特殊情况特殊处理.md
source_ids:
- '11647'
related_methods:
- - - 用稳定性指标约束优化器缩放
evidence_spans:
- ev::11647::嵌入之层
- ev::11647::输出之头
status: draft
updated: '2026-06-12'
---

# Embedding输出头稳定性

## 定义

Embedding 与输出头因输入域和损失函数位置特殊，需单独计算前向、依赖和更新稳定性。

## 激活场景

该概念来自 MuP 之上系列对“特殊情况特殊处理”的讨论。源文指出，Embedding 层和 LM Head 虽然参数都是矩阵，但不适合直接套用普通线性层或 Muon 的谱范数最速下降，因为输入域和损失函数位置都不同。

## 关键关系

Embedding 层输入是离散 Token Id，输出是对应行向量 $\boldsymbol{E}_i$。因此它没有普通连续输入意义下的依赖稳定性；前向和更新稳定性都落在最大行 RMS 范数上，最速下降对应逐行 RMS Norm 的 Normalized SGD。LM Head 表面是线性层，但训练视角下要连同标签和交叉熵损失一起看，源文给出前向、依赖、更新三类稳定性的上界，结论也是最大行/列 RMS 范数主导，只是尺度按维度 $d$ 出现额外缩放。

## 相关方法

- [[用稳定性指标约束优化器缩放]]

## 证据

- `ev::11647::嵌入之层`
- `ev::11647::输出之头`
