---
type: example
title: AttnRes矩阵视角统一Residuals/HC/AttnRes
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-03-19-Attention-Residuals-回忆录.md
source_ids:
- '11664'
evidence_spans:
- ev::11664::矩阵视角
notation_mapping:
  （待从源文章提取）: （待从源文章提取）
article_id: '11664'
article: '[[（待从源文章提取）]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

## 问题

通过Attention矩阵统一理解残差连接、HC/mHC、Full AttnRes、Block AttnRes。

## 矩阵视角

均为下三角矩阵表示层间连接权重：
- Residuals: 所有元素为1（等权求和）
- HC/mHC: 元素由H矩阵的乘积构成
- Full AttnRes: 元素由phi(w, y)计算
- Block AttnRes: 分块后同Block内共享权重