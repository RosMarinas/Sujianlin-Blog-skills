---
type: article_summary
title: DeepSeek V4的tid2eid是怎么来的？
article_id: 11750
source_url: https://spaces.ac.cn/archives/11750
date: 2026-05-15
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2026-05-15-DeepSeek-V4的tid2eid是怎么来的.md
concepts:
  - [[哈希路由]]
methods:
  - [[贪心负载均衡表生成法]]
  - [[多Gram哈希路由法]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-05-15-DeepSeek-V4的tid2eid是怎么来的.md
source_ids:
  - 11750
status: draft
updated: 2026-06-11
---

# DeepSeek V4的tid2eid是怎么来的？

本文讨论了在 MoE 模型（如 DeepSeek V4）的前几层中，为实现负载均衡，使用基于 Token ID 的静态哈希路由（Hash Routing）的设计与实现细节。

## 核心内容
- **问题背景**：靠近 Embedding 层的 MoE 由于缺乏上下文，极易发生 Routing 负载不均衡。DeepSeek V4 使用 Hash Routing 代替常规 Dense 连接或动态路由。
- **贪心生成表**：描述了求解 Token Expert 分配的约束方程组的贪心算法：按 Token 出现频率自高到低进行处理，每次将 Token 的 $k$ 个专家席位分配给当前累计负载最轻的专家，从而在静态上实现完美的均分。
- **高频高偏应对**：对于频率高到无法用单个 Token 均分的极端情形，提出了利用 2-Gram 或 3-Gram 哈希路由，将路由映射维度扩展，在保证路由零计算开销的同时达成近乎均匀的负载分布。