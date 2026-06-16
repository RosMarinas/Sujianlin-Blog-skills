---
type: concept
title: Mixed Chunk Attention
aliases:
  - MCA
definition: Mixed Chunk Attention（MCA，分块混合注意力）是Google在高效Transformer设计中提出的一种自注意力线性化技术。它将长输入序列划分为多个不重叠的小块，在块内进行局部的全注意力计算（二次复杂度），而在块之间通过低秩线性注意力算子进行全局特征交互（线性复杂度）。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
source_ids:
  - "8934"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Mixed Chunk Attention

## Definition
Mixed Chunk Attention（MCA，分块混合注意力）是Google在高效Transformer设计中提出的一种自注意力线性化技术。它将长输入序列划分为多个不重叠的小块，在块内进行局部的全注意力计算（二次复杂度），而在块之间通过低秩线性注意力算子进行全局特征交互（线性复杂度）。

## Explanation
对于长序列 $n$，如果直接计算注意力，其时间与空间复杂度为 $\mathcal{O}(n^2)$。MCA通过局部-全局分块混合设计破解了此瓶颈（如取块大小 $c=256$）：
- **局部块注意力**：每个块单独做局部的自注意力计算，复杂度为 $\mathcal{O}(nc)$，正比于序列长度。
- **全局线性注意力**：跨块利用线性自注意力实现信息的低秩全局传递，复杂度亦为线性，且在Causal（解码器）模式下能通过累加和（cumsum）形式保持完全平行的快速训练，空间复杂度低至 $b(n/c)se$，极大节省了显存。
MCA兼顾了局部相关性占主导的自然语言物理先验，同时在大尺度文本长度下保持了绝对线性的高运行速度。
