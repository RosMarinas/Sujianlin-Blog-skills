---
type: concept
title: "NSP"
aliases:
  - "Next Sentence Prediction"
  - "下一句预测"
definition: "BERT的预训练任务之一，判断两个句子是否连续相邻。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "8671"
related_methods:
  - [[method::NSP-BERT零样本分类]]
status: draft
updated: 2026-06-13
---

NSP（Next Sentence Prediction）是BERT的预训练任务之一：判断两个句子是否连续相邻。虽然RoBERTa论文认为NSP有负面效果并移除它，但NSP-BERT论文展示了NSP在Zero Shot分类中的惊人效果。通过将输入作为第一句、候选类别Prompt作为第二句，NSP能判断语义连贯性实现零样本分类，在中文FewCLUE上表现优秀。 这一发现打破了NSP只是辅助预训练任务的刻板印象，展示了预训练任务本身（而非仅仅模型参数）的巨大应用价值。
