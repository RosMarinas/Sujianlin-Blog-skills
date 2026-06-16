---
type: article_summary
title: Seq2Seq+前缀树：检索任务新范式（以KgCLUE为例）
article_id: "8802"
source_url: https://spaces.ac.cn/archives/8802
date: 2021-12-17
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-12-17-Seq2Seq-前缀树-检索任务新范式-以KgCLUE为例.md
series:
  - [[GlobalPointer与联合抽取]]
topics:
  - [[联合抽取]]
concepts:
  - [[前缀树约束解码]]
  - [[前瞻策略]]
methods:
  - [[基于前缀树约束的Seq2Seq解码]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-12-17-Seq2Seq-前缀树-检索任务新范式-以KgCLUE为例.md
source_ids:
  - "8802"
---

# Seq2Seq+前缀树：检索任务新范式（以KgCLUE为例）

本文提出了利用“Seq2Seq + 前缀树”的联合框架来解决检索和实体链接任务的新范式。传统的向量检索（如使用Faiss）往往需要海量显存来存储向量，而该方案将待检索的候选集构建为一棵前缀树（Trie），利用前缀树在解码时动态地将不合规的Token预测概率置为零，以此确保生成结果必然是数据库中存在的条目。

以KgCLUE（中文知识图谱问答）为例，模型输入为自然语言问题，输出为拼接后的三元组 `Subject [SEP] Predicate [SEP] Meaning`。为了解决贪心搜索导致的局部最优及Exposure Bias问题，文章提出了一种“前瞻（Lookahead）”策略，基于最长公共子序列（LCS）动态评估候选词对原句的覆盖率，并用于缩放当前Token的输出对数概率，大幅提升了检索精度。
