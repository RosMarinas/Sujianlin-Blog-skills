---
type: article_summary
title: 记录一次半监督的情感分析
article_id: "4374"
source_url: https://spaces.ac.cn/archives/4374
date: 2017-05-04
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-05-04-记录一次半监督的情感分析.md
source_html: Data/Spaces_ac_cn/raw/articles/4374/page.html
series: []
topics:
  - "[[topic::文本情感分类]]"
concepts:
  - "[[concept::半监督情感分析]]"
methods:
  - "[[method::用语言模型预训练做半监督学习]]"
problem_patterns: []
evidence_spans:
  - ev::4374::思路
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-05-04-记录一次半监督的情感分析.md
source_ids:
  - "4374"
status: draft
updated: 2026-06-11
---

## 文章核心问题

能否通过语言模型预训练（无标签数据）来提取文本特征，从而在极少标注样本（1000条）下实现有效的文本情感分类？

## 主要结论

1. 用语言模型预训练Embedding层和LSTM层后，仅用1000个标注样本训练Dense分类层（仅1001个参数），在IMDB上达到73.04%准确率。
2. 通过自我训练（self-training）将预测结果作为伪标签迭代训练，准确率可提升至73.48%。
3. 该方法验证了用语言模型提取文本特征的半监督学习思路的可行性，类似于图像领域的自编码预训练。

## 推导结构

思路（LM预训练+LSTM+少量标注样本）→ 过程（代码实现和训练细节）→ 点评（结果分析和改进方向）。

## 关键公式

无关键公式。核心策略：用ngram语言模型预训练LSTM编码器，固定编码器后仅训练Dense分类层，然后通过自我训练迭代提升。

## 体现的方法

- **用语言模型预训练做半监督学习**：通过大规模无监督语言模型预训练提取文本特征，再用少量标注样本微调分类层，实现半监督文本分类。

## 所属系列位置

独立文章。

## 与其他文章的关系

- 同属情感分类领域，与[[article::4293]]互补（4293改进损失函数，4374改进训练策略）。
- 预训练策略与[[article::9787]]的预训练思想本质一致——用预训练补充数据驱动的先验知识。
- 与[[article::7124]]的CLN类似，都利用预训练模型的编码能力做下游任务。

## 原文证据锚点

- `ev::4374::思路`：半监督情感分析的思路和LM预训练策略。
