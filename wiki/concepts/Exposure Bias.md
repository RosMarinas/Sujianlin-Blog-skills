---
type: concept
title: Exposure Bias
aliases: []
definition: Exposure Bias是指Seq2Seq模型在训练时使用Teacher Forcing（上一步用真实标签），在测试时使用自生成结果，这种训练-测试不一致导致的误差累积现象。本质上是局部归一化模型的问题。
standard_notation: 
prerequisites: Seq2Seq、Teacher Forcing
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

# Exposure Bias

Exposure Bias是指Seq2Seq模型在训练时使用Teacher Forcing（上一步用真实标签），在测试时使用自生成结果，这种训练-测试不一致导致的误差累积现象。本质上是局部归一化模型的问题。

## 相关文章

本批次中涉及该概念的多篇文章请参见各文章摘要页面。

Exposure Bias在Seq2Seq中的具体表现：训练时使用Teacher Forcing（已知真实前文），推理时使用模型生成的前文。这种不一致导致误差累积，beam size越大可能效果越差。缓解方法包括随机替换Decoder输入和对抗训练。
