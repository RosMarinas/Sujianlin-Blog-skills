---
type: concept
title: "ALBERT"
aliases:
  - "A Lite BERT"
definition: "参数共享的BERT变体，通过层间参数共享和Embedding矩阵分解减少参数量。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "7846"
related_methods:
  - [[method::ALBERT参数共享]]
status: draft
updated: 2026-06-13
---

ALBERT（A Lite BERT）是BERT的参数共享变体，所有Transformer层共享同一组参数，配合Embedding矩阵分解大幅减少参数量。但参数共享不加速推理过程，且小规格ALBERT效果不如同规格BERT。只有xxlarge版才能稳定超越BERT-large。使用时需要注意：如果不到xlarge版，没必要用ALBERT。ALBERT的主要价值在于模型体积小，适合存储和分发受限的场景。
