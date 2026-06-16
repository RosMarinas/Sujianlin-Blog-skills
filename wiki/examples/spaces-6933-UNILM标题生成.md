---
type: example
title: UNILM标题生成
aliases: []
article_id: "6933"
article: "[[spaces-6933-cong-yu-yan-mo-xing-dao-seq2seq-transformer-ru-xi-quan-kao-mask]]"
section: 实验
claim: UNILM方案使用单BERT模型+特殊Mask即可高效完成Seq2Seq标题生成，首个epoch即可生成可读标题
notation_mapping: 标准符号: [CLS],[SEP]分隔标记；segment_ids区分为0（输入）和1（目标）；源文符号一致
steps:
  - "1. input=[CLS]你想吃啥[SEP]白切鸡[SEP]"
  - "2. segment_ids: [0,0,0,0,0,0,1,1,1,1]"
  - "3. build_transformer_model(application='unilm')自动添加所需Mask"
  - "4. 目标错位：预测y[:,:-1]去匹配y_in[:,1:]"
  - "5. keep_tokens精简词表降低2万分类计算量"
  - "6. Beam Search解码"
used_concepts: ["[[UniLM]]", "[[自回归生成模型]]"]
used_formulas: ["[[Attention]]"]
used_methods: ["[[UNILM统一Mask]]"]
source_span: "ev::6933::实验"
sources:
  - Data/Spaces_ac_cn/markdown/...
source_ids:
  - "6933"
status: draft
updated: 2026-06-12
---
# UNILM标题生成

**本文来源：** 文章 6933

**所属章节：** 实验

**核心观点：** UNILM方案使用单BERT模型+特殊Mask即可高效完成Seq2Seq标题生成，首个epoch即可生成可读标题

## 推导步骤
- 1. input=[CLS]你想吃啥[SEP]白切鸡[SEP]
- 2. segment_ids: [0,0,0,0,0,0,1,1,1,1]
- 3. build_transformer_model(application='unilm')自动添加所需Mask
- 4. 目标错位：预测y[:,:-1]去匹配y_in[:,1:]
- 5. keep_tokens精简词表降低2万分类计算量
- 6. Beam Search解码

## 符号映射
标准符号: [CLS],[SEP]分隔标记；segment_ids区分为0（输入）和1（目标）；源文符号一致
