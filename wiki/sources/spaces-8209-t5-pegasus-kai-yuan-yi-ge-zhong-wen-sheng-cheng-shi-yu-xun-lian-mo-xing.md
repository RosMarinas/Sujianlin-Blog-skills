---
type: article_summary
title: T5 PEGASUS：开源一个中文生成式预训练模型
article_id: "8209"
source_url: https://spaces.ac.cn/archives/8209
date: 2021-03-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-03-03-T5-PEGASUS-开源一个中文生成式预训练模型.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-03-T5-PEGASUS-开源一个中文生成式预训练模型.md
source_ids:
  - "8209"
status: draft
updated: 2026-06-12
---

## 文章核心问题
以mT5为基础，结合中文Tokenizer改进和PEGASUS式伪摘要预训练任务，开源中文生成式预训练模型T5 PEGASUS。

## 主要结论
T5 PEGASUS在CSL和LCSTS上达到已知模型中的SOTA；拥有出色的小样本学习能力，即使只有10个标注样本也能微调出可用的摘要模型。

## 推导结构
1. Tokenizer改进：融入分词、完善词表
2. 预训练任务：伪摘要（PEGASUS思路）——选出约n/4个句子与剩余句子构造(原文,摘要)对
3. 训练参数与配置
4. 实验评测（CSL、LCSTS）
5. 小样本学习能力

## 关键公式
（以数据预处理和实验结果为主）

## 体现的方法
PEGASUS伪摘要预训练方法、中文生成式预训练模型构建方法、基于词颗粒度的Tokenizer优化方法

## 所属系列位置
独立文章，属于中文生成式预训练模型系列

## 与其他文章的关系
基于[6933]的UniLM思想；使用[6915]的bert4keras框架；与[7259]的Seq2Seq优化相关；基于[7718]等的经验

## 原文证据锚点
预训练数据构建示意图、CSL/LCSTS结果表格、小样本结果表格