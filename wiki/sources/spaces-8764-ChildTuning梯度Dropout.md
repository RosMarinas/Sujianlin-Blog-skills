---
type: article_summary
title: "ChildTuning：试试把Dropout加到梯度上去？"
article_id: "8764"
source_url: https://spaces.ac.cn/archives/8764
date: 2021-11-22
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-11-22-ChildTuning-试试把Dropout加到梯度上去.md
series: []
topics:
  - "[[优化动力学]]"
concepts:
  - "[[ChildTuning]]"
  - "[[梯度Dropout]]"
  - "[[Fisher信息参数重要性]]"
evidence_spans:
  - "ev::8764::ChildTuning-D"
  - "ev::8764::ChildTuning-F"
  - "ev::8764::论文推导"
  - "ev::8764::答非所问"
  - "ev::8764::个人理解"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-22-ChildTuning-试试把Dropout加到梯度上去.md
source_ids:
  - "8764"
status: draft
updated: 2026-06-10
---

# ChildTuning：试试把Dropout加到梯度上去？

## Summary

ChildTuning通过在finetune时对梯度做Dropout（或基于Fisher信息选择重要参数子集），降低过拟合风险。但本文实验表明对RoBERTa效果有限，且在Adam优化器下梯度Dropout等价于学习率缩放。

## Key Claims

1. ChildTuning-D基于Fisher信息选择top-p%参数更新，ChildTuning-F是随机梯度Dropout（保留比例p）。
2. 在Adam中，梯度Dropout长期等价于学习率乘以√p（而非方差增大）。
3. 作者的解释（SGD下Dropout扩大方差帮助逃逸局部最优点）在Adam下不成立。
4. 可能的真正原因：Dropout迫使样本信息更均匀分散在参数中（"背样本"解释），降低过拟合。
5. 实验表明在BERT上有微弱提升，在RoBERTa上几乎无效。
