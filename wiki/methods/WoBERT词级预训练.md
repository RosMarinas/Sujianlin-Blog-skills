---
type: method
title: "WoBERT词级预训练"
aliases:
  - "Word-based BERT"
operation_types:
  primary: "Rewrite / identity transform"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-09-18-提速不掉点-基于词颗粒度的中文WoBERT.md
source_ids:
  - "7758"
method_summary: "以词为颗粒度的中文BERT预训练，使用前分词+字词混合词表，基于RoBERTa-wwm-ext继续预训练。"
typical_structure: |
  1. 构建包含2万中文词的词表
  2. pre_tokenize+最大匹配分词
  3. 字embedding平均初始化词embedding
  4. MLM继续预训练
applicability: "中文NLU任务，文本分类，需要提速的场景"
tools:
  - jieba分词
  - MLM预训练
  - RoBERTa初始化
related_methods: []
examples:
  - [[article::7758]]
status: draft
updated: 2026-06-13
---

## 适用问题

中文NLU任务中，需要在不降低效果的前提下提升预训练/推理速度的场景。通过将预训练颗粒度从字提升到词，减少序列长度从而加速。

## 核心变换

**输入**：标准字级别BERT（RoBERTa-wwm-ext）
**输出**：词级别WoBERT（基于jieba分词 + 字词混合词表）

将预训练和推理的颗粒度从单字提升为"词"。编码时先分词再将词序列输入模型，每个词对应一个token（而非每个字对应一个token）。词表由2万常见中文词（选自jieba词库）+ 原始字表组成。

## 典型步骤

1. **构建词表**：基于jieba分词统计，选取约2万常见中文词，与原始字表合并成字词混合词表
2. **初始化词Embedding**：新词对应的Embedding用其所含字的Embedding平均初始化
3. **配置Tokenizer**：增加`pre_tokenize`参数，编码时先用jieba分词，再按最大匹配将词映射到词表
4. **继续预训练**：基于RoBERTa-wwm-ext权重，在24G单卡上继续训练100万步（序列长度512，batch_size=256，学习率5e-6）
5. **下游微调**：与标准BERT相同流程，Tokenizer使用`pre_tokenize=True`

## 直觉

中文中词是比字更自然的语义单元。"字"作为基本单元时，"中国"需要2个token处理，序列长度翻倍，计算量随序列长度的平方增长（Transformer自注意力）。改用"词"后序列长度显著缩短。虽然词表变大（加了2万词），但实际序列中每个词对应的语义信息更丰富，模型可以更快地捕捉短语级的语义模式。

## 边界

- 依赖分词质量（使用jieba），分词的错误会传递到下游任务
- 词表容量有限（2万词），未覆盖的词退回到字级别
- 词级预训练需要继续预训练而非从零训练（基于RoBERTa-wwm-ext初始化）
- 效果与字级别BERT持平或略优，主要优势在速度
- 提供基于NEZHA的WoNEZHA版本

## 例子

- IFLYTEK分类任务：WoBERT效果与RoBERTa-wwm-ext持平，速度提升30%-50%
- TNEWS分类任务：WoBERT效果略优于字级别BERT
- 推理阶段序列长度减少约50%-60%（中文平均词长约2-3字）

## 证据

- ev::7758::字词混合词表：2万常见中文词 + 原始字表的混合词表设计
- ev::7758::字Embedding平均初始化词Embedding：利用已有字向量初始化新词向量
- ev::7758::pre_tokenize分词配置：Tokenizer的pre_tokenize参数支持前分词再编码
- ev::7758::效果与速度对比：IFLYTEK/TNEWS上效果持平或略优，速度提升明显
