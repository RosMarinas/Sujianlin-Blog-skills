---
type: article_summary
title: 缓存与效果的极限拉扯：从MHA、MQA、GQA到MLA
article_id: "10091"
source_url: https://spaces.ac.cn/archives/10091
date: 2024-05-13
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-05-13-缓存与效果的极限拉扯-从MHA-MQA-GQA到MLA.md
series:

topics:
  - [[Transformer架构]]
concepts:
  - [[KV Cache]]
  - [[MLA]]
methods:

evidence_spans:
  - ev::10091::MHA-MQA-GQA-MLA演变
  - ev::10091::RoPE兼容
  - ev::10091::恒等变换技巧
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-05-13-缓存与效果的极限拉扯-从MHA-MQA-GQA到MLA.md
source_ids:
  - "10091"
status: draft
updated: 2026-06-10
---
# 缓存与效果的极限拉扯：从MHA、MQA、GQA到MLA

## 文章核心问题

注意力机制如何一步步演进以减少KV Cache同时保持效果？MLA的设计思路是什么？

## 主要结论

MQA（所有头共享KV）将KV Cache减少到1/h，GQA（分组共享）是MHA到MQA的过渡。MLA的核心创新不是低秩投影（GQA本质上也是），而是将投影后的结果通过不同投影矩阵恢复各头KV，再利用恒等变换在推理时等效为MQA，从而大幅压缩KV Cache（DeepSeek-V2取d_c=512）。额外采用混合RoPE策略解决位置编码兼容问题。

## 推导结构

1. MHA的KV Cache瓶颈
2. MQA单头共享KV
3. GQA分组共享KV
4. MLA的低秩潜在投影设计
5. 推理时的恒等变换技巧
6. 混合RoPE方案
7. Q的低秩投影辅助

## 关键公式

c_i = x_i W_c ∈ R^{d_c} — 低秩潜在向量
推理时：q_t k_i^T = x_t (W_q W_k^T) c_i^T — 恒等变换将多头k合并为共享c

## 与其他文章的关系

- 连接到Transformer升级之路系列
- 连接到概念:位置编码、概念:RoPE、概念:Attention

## 原文证据锚点

- ev::10091::MHA-MQA-GQA-MLA演变 — 四种注意力机制的对比
- ev::10091::恒等变换技巧 — MLA推理的恒等变换
- ev::10091::RoPE兼容 — MLA的混合RoPE方案
