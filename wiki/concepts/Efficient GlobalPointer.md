---
type: concept
title: Efficient GlobalPointer
aliases:
  - 门控指针模块改进版
definition: GlobalPointer的一个参数优化改进版本，将实体识别解耦为跨实体类共享的“抽取”投影和轻量级的“分类”投影，以此大幅降低在多类别场景下的参数规模。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-25-Efficient-GlobalPointer-少点参数-多点效果.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-30-GPLinker-基于GlobalPointer的实体关系联合抽取.md
source_ids:
  - "8877"
  - "8888"
evidence_spans:
  - ev::8877::参数分解
status: stable
updated: 2026-06-12
---

# Efficient GlobalPointer

传统的GlobalPointer（GP）在处理命名实体识别（NER）时，需要为每一种实体类别 $\alpha$ 各自构建独立的投影权重 $\boldsymbol{W}_{q,\alpha}, \boldsymbol{W}_{k,\alpha}$。当实体类型增多（如CLUENER的10类或更多）时，其总参数量将以 $2MdD$（$M$ 为类别数）的速度急剧膨胀，容易出现参数更新稀疏、过拟合和GPU显存开销过大的问题。

Efficient GlobalPointer（EGP）从物理逻辑上对NER任务进行了“识别（抽取）”与“分类”的拆分。所有实体类别共用一套相同的跨度投影权重，以此在特征编码序列中识别并抽取出代表实体的通用Span片段。而各实体类别的分类消歧，则单独通过与其绑定的低维偏置或拼接向量 $\boldsymbol{w}_{\alpha}$ 来极轻量化地实现。这种参数结构的解耦与共享，在大幅削减大类别场景下模块参数量（从千万级降低到十万级）的同时，避免了过度拟合，从而在多类别、高难度的NER任务中取得了比原版GP and CRF更优越的表现。
