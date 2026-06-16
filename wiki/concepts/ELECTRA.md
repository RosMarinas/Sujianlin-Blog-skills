---
type: concept
title: "ELECTRA"
aliases: []
definition: "使用生成器-判别器架构的预训练模型，生成器做MLM，判别器判断token是否被替换。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "7846"
related_methods:
  - [[method::ELECTRA预训练]]
status: draft
updated: 2026-06-13
---

ELECTRA使用生成器-判别器架构进行预训练：小型生成器做MLM预测被mask的token，用预测结果替换原文；判别器判断每个token是否被替换。虽然预训练效率提高（速度约为BERT的4倍），但从理论和实验角度分析，ELECTRA存在缺陷：判别器可能退化为常数函数，且下游任务效果并未显著超越BERT。中文任务评测也证实了这一点。 中文任务上ELECTRA与同级别BERT相差无几，未见碾压式优势。如果下游任务需要使用MLM权重（如文本生成），则不宜使用ELECTRA。
