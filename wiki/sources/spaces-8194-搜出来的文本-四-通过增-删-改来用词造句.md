---
type: article_summary
title: "【搜出来的文本】⋅（四）通过增、删、改来用词造句"
article_id: "8194"
source_url: https://spaces.ac.cn/archives/8194
date: 2021-02-25
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-02-25-搜出来的文本-四-通过增-删-改来用词造句.md
series: [搜出来的文本]
topics: [受限文本生成, MH采样, CGMH]
concepts: [CGMH, 增删改操作, 无监督约束文本生成]
methods: [CGMH]
problem_patterns: [用词造句, 无监督文本改写, 无监督句子纠错]
evidence_spans:
  - 8194-问题设置
  - 8194-增删改
  - 8194-转移概率
  - 8194-接受概率
  - 8194-确定目标
  - 8194-实验效果
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-25-搜出来的文本-四-通过增-删-改来用词造句.md
source_ids:
  - "8194"
status: draft
updated: 2026-06-10
---

## 文章核心问题

如何用MCMC方法实现无监督的用词造句（以及更一般的受限文本生成）？

## 主要结论

1. CGMH（Constrained Generation by Metropolis-Hastings Sampling）通过MH采样实现无监督有约束文本生成。
2. 转移概率设计为三种微调操作：增（insert）、删（delete）、改（replace），模拟人的写作润色过程。
3. 增与删互为逆操作，改与改自身互为逆操作——逆操作的存在保证任意两个状态连通。
4. 具体任务信息通过ρ(x,c)影响接受率，不依赖有监督数据。
5. 用词造句硬约束：通过固定关键词位置来保证约束条件始终满足。
6. CGMH原则上适用于任何可量化目标的文本生成任务——只要写出不依赖标签的量化指标ρ(x,c)。

## 推导结构

- 受限文本生成一般形式 ρ(x,c) = p(x)·sim(x,c)·χ(x,c)
- 三种微调操作及转移概率
- 接受概率计算
- 具体任务目标设计
- 用词造句实验效果展示
