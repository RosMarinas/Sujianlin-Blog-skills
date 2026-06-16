---
type: proposition
title: TTT框架从在线学习视角统一了序列模型
aliases:
  - TTT Unifies Sequence Models
statement: TTT框架将序列模型构建视为在线学习问题，通过优化器更新来构建RNN，统一了线性Attention、RetNet、DeltaNet等模型。不同模型对应不同的模型架构f和损失函数L选择。
assumptions:
  - "(K,V)被视为语料对用于训练模型f"
  - "优化器更新（如SGD）本质上是一个RNN"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
source_ids:
  - "10017"
  - "11320"
evidence_spans:
  - "ev::10017::测试时训练"
  - "ev::10017::除旧迎新"
status: draft
updated: 2026-06-10
---

# TTT框架从在线学习视角统一了序列模型

## 内容

TTT框架提供了构建序列模型的指导原则：RNN的核心目标是将历史数据压缩到固定大小的State中，这与训练模型将数据压缩到权重的过程高度契合。不同的f和L选择对应不同的具体模型。
