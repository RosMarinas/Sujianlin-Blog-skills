---
title: 模型压缩 (Model Compression)
definition: 模型压缩旨在简化大模型以获得推理速度更快的小模型。通常先训练一个大模型（Predecessor），再将其压缩为小模型（Successor），相比直接训练小模型通常能获得更好的精度。
type: concept
aliases:
- 剪枝
- Pruning
- 量化
- Quantization
- 蒸馏
- Distillation
- 模型压缩
tags:
- model-compression
- efficiency
- deployment
related_methods:
- BERT-of-Theseus
- 知识蒸馏
related_sources:
- spaces-7575-BERT-of-Theseus
status: draft
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## Definition

模型压缩旨在简化大模型以获得推理速度更快的小模型。通常先训练一个大模型（Predecessor），再将其压缩为小模型（Successor），相比直接训练小模型通常能获得更好的精度。

## Common Approaches

### 1. 直接简化 (Pruning & Quantization)
- **剪枝（Pruning）**：删减大模型的部分组件（层、头、神经元等）
- **量化（Quantization）**：将模型参数从 float32 转换为 float16/int8 等更低精度格式

### 2. 重训练 (Distillation & Module Replacing)
- **蒸馏（Distillation）**：以大模型输出作为小模型训练目标，需匹配中间层输出、Attention矩阵等多重loss
- **模块替换（Module Replacing）**：如 BERT-of-Theseus，直接用Successor模块替换Predecessor对应模块，仅需下游任务loss

## Key Principles

- **可替换性**：对齐小模型与大模型的输出/中间层，使小模型能替代大模型的对应部分
- **渐进式训练**：逐步完成替换过程，而非一次性替换全部模块
- **简洁性**：模块替换方法相比蒸馏需要平衡的loss更少，实现更简洁

## References

- 苏剑林. "BERT-of-Theseus：基于模块替换的模型压缩方法". 科学空间, 2020. [spaces-7575]
- Xu et al., "BERT-of-Theseus: Compressing BERT by Progressive Module Replacing", 2020.