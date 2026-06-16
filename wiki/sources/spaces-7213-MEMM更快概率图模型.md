---
type: article_summary
title: "CRF用过了，不妨再了解下更快的MEMM？"
article_id: "7213"
source_url: https://spaces.ac.cn/archives/7213
date: 2020-02-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-02-24-CRF用过了-不妨再了解下更快的MEMM.md
series: []
topics: []
concepts:
  - "[[MEMM]]"
  - "[[全局归一化vs局部归一化]]"
  - "[[标签偏置]]"
  - "[[Bi-MEMM]]"
evidence_spans:
  - "ev::7213::回顾CRF"
  - "ev::7213::更朴素的MEMM"
  - "ev::7213::两者关系"
  - "ev::7213::MEMM的优劣"
  - "ev::7213::双向MEMM"
  - "ev::7213::思考与拓展"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-02-24-CRF用过了-不妨再了解下更快的MEMM.md
source_ids:
  - "7213"
status: draft
updated: 2026-06-10
---

# CRF用过了，不妨再了解下更快的MEMM？

## Summary

介绍MEMM（最大熵马尔可夫模型）与CRF的区别：MEMM采用局部归一化因此更快但效果略逊，提出Bi-MEMM缓解不对称性，并讨论MEMM在大标签空间和高阶关联场景下的拓展优势。

## Key Claims

1. MEMM将序列概率分解为逐步条件概率（局部归一化），CRF对整个序列打分后全局softmax（全局归一化）。
2. MEMM可完全并行（比CRF快25%-150%），但效果通常不如CRF。
3. Label bias（局部归一化导致的训练-预测不一致）可通过Bi-MEMM（双向平均）缓解。
4. 强编码模型下CRF与Bi-MEMM持平，弱编码模型下CRF优约0.5%。
5. MEMM的优势：易于拓展到大标签空间（低秩分解转移矩阵）和高阶关联。
