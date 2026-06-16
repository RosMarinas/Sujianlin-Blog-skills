---
type: method
operation_types:
  primary: "Rewrite / identity transform"
  secondary: []
title: "Sentence-BERT训练与拼接特征"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2021-07-19-用开源的人工标注数据来增强RoFormer-Sim.md"
source_ids:
  - "8541"
method_summary: "把两个句子的向量 u、v 及差异特征 |u-v| 拼接后送入分类器，使监督训练同时观察语义相关度和邻近差异。"
typical_structure: |
  1. 分别编码句子对得到 u 与 v。
  2. 构造拼接特征 [u, v, |u-v|]。
  3. 用拼接特征训练句子对二分类或三分类任务。
  4. 将监督信号回传到编码器，增强相似度任务表现。
applicability: "适用于有人工标注句子对、需要通过交叉编码式特征强化句向量模型微调的语义相似度任务。"
examples:
  - "[[article::8541]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8541::特征拼接"
---

# Sentence-BERT训练与拼接特征

## 适用问题

适用于有人工标注句子对、需要通过交叉编码式特征强化句向量模型微调的语义相似度任务。

## 核心变换

句子对向量 -> [u, v, |u-v|] 拼接特征 -> 监督分类训练。

## 典型步骤

1. 分别编码句子对得到 u 与 v。
2. 构造拼接特征 [u, v, |u-v|]。
3. 用拼接特征训练句子对二分类或三分类任务。
4. 将监督信号回传到编码器，增强相似度任务表现。

## 直觉

直接优化余弦只表达一个相似度标量；拼接 u、v 和差异项能让分类器看到更丰富的比较维度。

## 边界

该方法依赖标注句子对；原文讨论的是相似度相关中文人工标注数据，不支持无标注场景直接套用。

## 例子

- 8541 在监督句向量增强中说明 Sentence-BERT 的拼接特征 [u, v, |u-v|] 能缓解标注噪声并增强微调。

## 证据

- `ev::8541::特征拼接`
- `Data/Spaces_ac_cn/markdown/Big-Data/2021-07-19-用开源的人工标注数据来增强RoFormer-Sim.md`
- 读取章节: 出乎意料
