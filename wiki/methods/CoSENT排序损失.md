---
type: method
title: CoSENT排序损失
aliases:
  - Cosine Sentence ranking loss
operation_types:
  primary: Align / calibrate by invariance
  secondary:
    - Rewrite / identity transform
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-06-CoSENT-一-比Sentence-BERT更有效的句向量方案.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-11-09-CoSENT-三-作为交互式相似度的损失函数.md
source_ids:
  - "8847"
  - "9341"
method_summary: 把句子相似度监督从分类层间接优化改写为正负句对余弦相似度的排序约束，使训练目标与检索阶段的相似度排序保持一致。
typical_structure: |
  1. 为句子对构造相似度顺序标签，而不是只构造类别标签。
  2. 用编码器得到句向量，并计算句对余弦相似度。
  3. 对所有真实相似度更高的句对，惩罚其预测相似度低于负样本对的情况。
  4. 在交互式模型中，可把余弦函数替换为任意标量打分函数 f(i,j)。
applicability: 适用于 STS、NLI 派生排序、语义检索和需要直接优化相似度顺序的双塔或交互式匹配模型。
tools:
  - 余弦相似度
  - 排序损失
  - Spearman 相关
examples:
  - [[spaces-8847-CoSENT-一-比Sentence-BERT更有效的句向量方案]]
  - [[spaces-9341-CoSENT-三-作为交互式相似度的损失函数]]
related_methods:
  - [[用互信息内积构造词向量几何]]
  - [[句向量对比学习分类训练]]
evidence_spans:
  - ev::8847::CoSENT损失函数
  - ev::9341::CoSENT通用化
status: draft
updated: 2026-06-14
---

# CoSENT排序损失

## 核心变换

CoSENT 的关键动作是把“句子对属于哪个类别”改写为“哪个句子对应该更相似”。这样训练目标直接作用在余弦相似度的相对顺序上，而不是依赖分类头学出聚类后再取中间特征。

## 边界

它要求训练样本之间存在可比较的相似度顺序。没有顺序结构的普通多分类任务不能直接套用；若改成交互式模型，也需要保证标量打分函数能承载这种排序约束。
