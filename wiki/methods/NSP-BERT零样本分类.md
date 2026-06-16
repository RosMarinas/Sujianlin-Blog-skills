---
type: method
title: "NSP-BERT零样本分类"
aliases:
  - "NSP-BERT"
  - "NSP Zero Shot"
operation_types:
  primary: "Construct auxiliary sequence"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-09-10-曾被嫌弃的预训练任务NSP-做出了优秀的Zero-Shot效果.md
source_ids:
  - "8671"
method_summary: "利用BERT的NSP预训练任务做Zero Shot分类：输入为第一句，候选类别Prompt为第二句，判断语义连贯性。"
typical_structure: |
  1. 构建半句对：(输入句子, 候选类别Prompt)
  2. NSP模型判断是否连贯
  3. 选择连贯性最高的类别
applicability: "零样本文本分类，NLU任务"
tools:
  - NSP
  - Prompt模板
related_methods: []
examples:
  - [[article::8671]]
status: draft
updated: 2026-06-13
---

## 适用问题

零样本文本分类，包括情感分类、主题分类、实体链接等NLU任务。无需任何标注数据，仅利用BERT的NSP预训练能力。

## 核心变换

**输入**：待分类文本$x$ + 候选类别集合$C$
**输出**：与$x$最连贯的类别$c^*$

将输入文本作为第一句，为每个候选类别$c$构建包含类别名的Prompt作为第二句（如"这很可能是体育新闻"）。使用BERT的NSP模型判断两句是否连贯，选择连贯性最高的类别：
$$
c^* = \arg\max_{c \in C} \text{NSP}(x, \text{Prompt}(c))
$$

## 典型步骤

1. **准备候选类别**：为每个类别构造自然语言Prompt（如"这很可能是体育新闻"、"这很可能是娱乐新闻"）
2. **构建句子对**：原始文本作为第一句[CLS] x [SEP]，类别Prompt作为第二句
3. **NSP评分**：利用BERT的NSP头计算第一句和第二句的连贯性得分
4. **选择最优**：选取得分最高的类别作为预测结果
5. **（可选）多轮判断**：在实体链接等任务中，逐一判断候选实体与文本的连贯性

## 直觉

NSP任务的本质是判断两个句子是否在原文中相邻——这要求模型理解两段文本的语义连贯性。分类任务中，如果输入文本确实属于某个类别，那么输入+"这个类别描述"应该构成一个语义连贯的句子对。例如"姚明在NBA打球"+"这很可能是体育新闻"是连贯的，而"姚明在NBA打球"+"这很可能是娱乐新闻"则不连贯。NSP-BERT正是利用了这一特性，将分类转化为语义连贯性判断。

与PET（MLM方式）相比，NSP-BERT的优势是不需要设计Mask位置，直接使用完整的句子对输入。

## 边界

- 依赖NSP头的质量：RoBERTa和后续模型（如BERT-wwm-ext）不支持NSP，需使用含NSP的原始BERT
- Prompt设计对效果有显著影响，需要一定的人工经验
- 目前主要在中文FewCLUE和DuEL 2.0上验证，英文和其他语言效果尚待验证
- 与有监督微调相比，零样本效果仍有差距，适合作为无标注数据场景的基线
- 模型规模对效果有影响，大规模模型通常效果更好

## 例子

- 情感分类：输入"这电影真好看" + Prompt"这很可能是正面的" / "这很可能是负面的"
- 主题分类：输入"姚明在NBA打球" + 候选为"体育"、"娱乐"、"科技"等
- 实体链接（DuEL 2.0）：输入文本+候选实体描述，判断文本是否提及该实体

## 证据

- ev::8671::NSP-BERT核心思路：将输入作为第一句、类别Prompt作为第二句，NSP判断连贯性
- ev::8671::Prompt设计方案：常见NLU任务的Prompt模板（情感、主题、NLI、实体链接等）
- ev::8671::中文FewCLUE实验效果：NSP-BERT在零样本分类任务上的表现
