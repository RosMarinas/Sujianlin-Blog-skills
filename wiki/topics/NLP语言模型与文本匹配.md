---
type: topic
title: "NLP语言模型与文本匹配"
aliases:
  - NLP Language Models & Text Matching
scope: "NLP核心任务：文本分类、序列标注、中文分词、语言模型、文本匹配、命名实体识别、文本摘要及其相关方法"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-13-大词表语言模型在续写任务上的一个问题及对策.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-20-你的语言模型有没有-无法预测的词.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-10-22-CAN-借助先验分布提升分类性能的简单后处理技巧.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-16-搜狐文本匹配-基于条件LayerNorm的多任务baseline.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-03-P-tuning-自动构建模版-释放语言模型潜能.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-01-01-SPACES-抽取-生成-式长文本摘要-法研杯总结.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-12-04-层次分解位置编码-让BERT可以处理超长文本.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-10-无监督分词和句法分析-原来BERT还可以这样用.md
source_ids:
  - "7388"
  - "9797"
  - "9768"
  - "9762"
  - "9046"
  - "8728"
  - "8373"
  - "8337"
  - "8295"
  - "8213"
  - "8046"
  - "7947"
  - "7476"
concepts:
  - [[concept::Earth Mover's Distance]]
  - [[concept::语言模型]]
  - [[concept::中文分词]]
  - [[concept::命名实体识别]]
  - [[concept::序列标注]]
  - [[concept::Sparse Softmax]]
  - [[concept::层次分解位置编码]]
  - [[concept::Viterbi算法]]
  - [[concept::文本分类]]
  - [[concept::Unigram分词]]
  - [[concept::Tokenizer]]
  - [[concept::文本匹配]]
  - [[concept::Prompt Tuning]]
  - [[concept::MLM预训练]]
  - [[concept::文本摘要]]
  - [[concept::Copy机制]]
  - [[concept::位置编码]]
  - [[concept::条件LayerNorm]]
  - [[concept::Unargmaxable Class]]
  - [[concept::RoPE相对位置编码]]
methods:
  - [[method::GlobalPointer]]
  - [[method::P-tuning]]
  - [[method::Viterbi Sampling]]
  - [[method::SPACES摘要模型]]
  - [[method::Sparse Softmax]]
  - [[method::BIO Copy机制]]
  - [[method::CAN后处理]]
  - [[method::EMO损失函数]]
  - [[method::WMD文本相似度计算]]
  - [[method::WRD文本相似度计算]]
  - [[method::Token Healing]]
  - [[method::条件LayerNorm多任务学习]]
  - [[method::Perturbed Masking]]
  - [[method::PET范式]]
status: draft
updated: 2026-06-10
---

# NLP语言模型与文本匹配

涵盖NLP核心任务的方法与理论，包括文本分类（CAN、P-tuning）、序列标注与NER（GlobalPointer、CRF对比）、中文分词（Viterbi Sampling、Unigram、Perturbed Masking）、语言模型（Unargmaxable Class、Token Healing、位置编码延拓）、文本匹配（WMD/WRD、条件LayerNorm）、文本摘要（SPACES、BIO Copy、Sparse Softmax）以及损失函数设计（EMO）。
