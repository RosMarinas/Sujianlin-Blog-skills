---
type: concept
definition: 自回归语言模型逐token生成时，缓存历史token的Key和Value矩阵以避免重复计算的机制。其大小随序列长度线性增长，是长文本推理的主要显存瓶颈。
aliases:
- KV缓存
status: draft
updated: '2026-06-12'
title: KV Cache
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# KV Cache

自回归语言模型逐token生成时，缓存历史token的Key和Value矩阵以避免重复计算的机制。其大小随序列长度线性增长，是长文本推理的主要显存瓶颈。