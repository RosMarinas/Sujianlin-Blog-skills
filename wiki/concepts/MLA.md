---
type: concept
definition: DeepSeek-V2提出的注意力机制变体，通过低秩投影将KV压缩到潜在空间，推理时利用恒等变换等效为MQA。
aliases:
- Multi-head Latent Attention
- 多头潜在注意力
status: draft
updated: '2026-06-12'
title: MLA
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# MLA

DeepSeek-V2提出的注意力机制变体，通过低秩投影将KV压缩到潜在空间，推理时利用恒等变换等效为MQA。

## 核心创新

1. 低秩投影压缩到d_c维度
2. 恒等变换在推理时合并多头KV
3. 混合RoPE解决位置编码兼容