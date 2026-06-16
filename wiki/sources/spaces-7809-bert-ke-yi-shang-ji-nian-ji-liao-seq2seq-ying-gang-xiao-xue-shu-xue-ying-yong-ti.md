---
type: article_summary
title: BERT可以上几年级了？Seq2Seq"硬刚"小学数学应用题
article_id: "7809"
source_url: https://spaces.ac.cn/archives/7809
date: 2020-10-19
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-10-19-BERT可以上几年级了-Seq2Seq-硬刚-小学数学应用题.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-10-19-BERT可以上几年级了-Seq2Seq-硬刚-小学数学应用题.md
source_ids:
  - "7809"
status: draft
updated: 2026-06-12
---

## 文章核心问题
使用BERT+UniLM的Seq2Seq模型将小学数学应用题转换为可执行数学表达式，实现端到端的自动解题。

## 主要结论
在ape210k数据集上，Base模型达到72.35%准确率，Large模型达到75.01%准确率，显著超过原论文报告的70.20%。

## 推导结构
1. ape210k数据集分析（题目、表达式、答案）
2. 表达式前处理（百分数、带分数、去括号）
3. BERT+UniLM Seq2Seq模型
4. 效果评估
5. 标准化输出（整数/小数/分数判断，SymPy符号运算）

## 关键公式
（以数据处理和实验结果为主）

## 体现的方法
BERT+UniLM数学表达式生成方法、表达式标准化与Simplification方法、SymPy分数保持方法

## 所属系列位置
独立文章，属于Seq2Seq应用（数学推理）系列

## 与其他文章的关系
核心方法源自[6933]的UNILM思路；可结合[7259]的Exposure Bias缓解方法进一步优化

## 原文证据锚点
数据集示例、实验结果表格、SymPy代码