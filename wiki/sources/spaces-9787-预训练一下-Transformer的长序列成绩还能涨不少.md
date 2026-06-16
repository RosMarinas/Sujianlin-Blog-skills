---
type: article_summary
title: 预训练一下，Transformer的长序列成绩还能涨不少！
article_id: "9787"
source_url: https://spaces.ac.cn/archives/9787
date: 2023-10-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-10-08-预训练一下-Transformer的长序列成绩还能涨不少.md
source_html: Data/Spaces_ac_cn/raw/articles/9787/page.html
series: []
topics:
  - "[[topic::Transformer架构]]"
concepts:
  - "[[concept::LRA预训练]]"
methods:
  - "[[method::用预训练补充Transformer归纳偏置]]"
problem_patterns: []
evidence_spans:
  - ev::9787::新结论
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-08-预训练一下-Transformer的长序列成绩还能涨不少.md
source_ids:
  - "9787"
status: draft
updated: 2026-06-11
---

## 文章核心问题

Transformer在Long Range Arena（LRA）上表现不如线性RNN，这个差距是固有缺陷还是因为缺乏预训练？

## 主要结论

1. 用训练集进行MLM或GPT预训练可大幅缩小Transformer与线性RNN在LRA上的差距，Transformer的提升最为明显。
2. 该结论证实LRA上Transformer的劣势主要源于缺乏预训练补充归纳偏置，而非架构固有缺陷。
3. 预训练的重要性表明LRA任务（细粒度token如字母/像素）需要更多的归纳偏置，线性RNN天然的局域性正好贴合，而Transformer需要预训练来补充。

## 推导结构

旧背景（LRA介绍和此前模型排行）→ 新结论（预训练实验及结果）→ 分析（预训练补充归纳偏置的意义）。

## 关键公式

无关键公式。核心实验结论：Transformer+预训练的LRA成绩接近SOTA梯队。

## 体现的方法

- **用预训练补充Transformer归纳偏置**：通过预训练让Transformer适应数据特性，弥补其相比线性RNN在局域性上的归纳偏置不足。

## 所属系列位置

独立文章。

## 与其他文章的关系

- 讨论了Transformer与线性RNN（如S4、S4D、S5等）在LRA上的对比。
- 与[[topic::LoRA微调]]的关联：LoRA微调也需要预训练权重作为基础，本文说明预训练对长序列任务的重要性。

## 原文证据锚点

- `ev::9787::新结论`：预训练可大幅缩小Transformer与线性RNN在LRA上的差距。
