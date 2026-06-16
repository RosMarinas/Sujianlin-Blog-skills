---
type: article_summary
title: 学会提问的BERT：端到端地从篇章中构建问答对
article_id: "7630"
source_url: https://spaces.ac.cn/archives/7630
date: 2020-07-25
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-07-25-学会提问的BERT-端到端地从篇章中构建问答对.md
series: []
topics:
  - [[联合抽取]]
concepts:
  - [[UniLM]]
methods:
  - [[BERT与UniLM端到端序列生成]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-25-学会提问的BERT-端到端地从篇章中构建问答对.md
source_ids:
  - "7630"
---

# 学会提问的BERT：端到端地从篇章中构建问答对

本文探讨了利用“BERT + UniLM”的架构端到端生成“篇章 -> 答案 + 问题”问答对的实践。相比仅生成问题的传统流水线，模型将问题与答案合并为生成目标，并确定了“先生成答案，再生成问题”的生成路径，数学表征为概率建模 $P(\text{答案}, \text{问题} | \text{篇章})$。

在解码策略上，为了避免确定性束搜索带来的单调性，同时规避完全随机采样导致的无关性，本文提出了一种混合解码算法：生成答案（直到第一个 `[SEP]`）时使用随机采样，而在生成后续问题（直到第二个 `[SEP]`）时使用确定性贪心解码，从而使得所生成的问答对既具备多样性，又保证了逻辑上的严谨。
