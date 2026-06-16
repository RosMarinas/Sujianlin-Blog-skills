---
type: concept
title: "Ladder Side-Tuning"
aliases:
  - "LST"
  - "梯形侧调"
definition: "在预训练大模型旁搭建小型旁支网络进行微调，大模型仅提供前向输入，反向传播仅限旁支网络。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "9138"
related_methods:
  - [[method::Ladder Side-Tuning]]
status: draft
updated: 2026-06-13
---

Ladder Side-Tuning（LST）是同时实现参数高效和训练高效的大模型微调方法。在预训练大模型旁搭建小型旁支网络（梯子），大模型参数完全冻结仅提供前向输出，反向传播仅限旁支网络。相比Adapter和P-tuning需要在全模型上反向传播，LST大幅降低了训练计算量，训练速度提升约一倍。 在CLUE中文任务上，LST在简单分类任务中效果接近全量微调，但在阅读理解等复杂任务上下降明显，表明参数高效微调仍存在提升空间。
