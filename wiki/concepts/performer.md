---
type: concept
definition: Performer是一种高效的线性Attention架构，通过正交随机特征（FAVOR+机制）来无偏地近似softmax注意力矩阵。在《从Performer到线性Attention》一文中，作者分析了Performer的近似机制，并从中推导出了线性Attention理想的激活函数为
  $e^x$ 及其变体，从而揭示了如何超越固定的随机投影矩阵，让模型自主学习。
title: Performer
aliases: []
sources:
- （待从源文章提取）
source_ids:
- （待从源文章提取）
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
---

# Performer

## Definition
Performer是一种高效的线性Attention架构，通过正交随机特征（FAVOR+机制）来无偏地近似softmax注意力矩阵。在《从Performer到线性Attention》一文中，作者分析了Performer的近似机制，并从中推导出了线性Attention理想的激活函数为 $e^x$ 及其变体，从而揭示了如何超越固定的随机投影矩阵，让模型自主学习。