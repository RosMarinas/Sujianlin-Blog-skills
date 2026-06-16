---
type: concept
title: PEGASUS预训练
aliases: []
definition: 一种为生成任务设计的预训练方法，从文档中选出约n/4个句子构造伪摘要，以剩余句子为输入、选中句子为输出训练Seq2Seq模型。与下游生成任务更贴近，具有良好的小样本迁移能力。
standard_notation: 
prerequisites: Seq2Seq预训练
sources: Data/Spaces_ac_cn/markdown/... (详见具体文章)
source_ids:
  - 5542
  - 5597
  - 6877
  - 6915
  - 6920
  - 6933
  - 7196
  - 7259
  - 7500
  - 7718
  - 7809
  - 7912
  - 8128
  - 8209
  - 8739
  - 9059
evidence_spans: []
null_evidence_reason: 概念提取自多篇文章，暂未绑定具体证据跨度
status: draft
updated: 2026-06-12
---

# PEGASUS预训练

一种为生成任务设计的预训练方法，从文档中选出约n/4个句子构造伪摘要，以剩余句子为输入、选中句子为输出训练Seq2Seq模型。与下游生成任务更贴近，具有良好的小样本迁移能力。

## 相关文章

本批次中涉及该概念的多篇文章请参见各文章摘要页面。

PEGASUS预训练的核心创新：从文档中选择重要句子（通过最长公共子序列LCS度量）作为伪摘要，用剩余句子作为输入。使预训练任务与下游摘要/标题生成任务高度一致，比随机掩码预训练更适合生成任务。T5 PEGASUS将此方法应用于中文。
