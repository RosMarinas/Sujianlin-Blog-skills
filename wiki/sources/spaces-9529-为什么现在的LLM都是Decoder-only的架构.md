---
type: article_summary
title: 为什么现在的LLM都是Decoder-only的架构？
article_id: 9529
source_url: https://spaces.ac.cn/archives/9529
date: 2023-03-17
category: Big-Data
source_markdown: |
  Data/Spaces_ac_cn/markdown/Big-Data/2023-03-17-为什么现在的LLM都是Decoder-only的架构.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-17-为什么现在的LLM都是Decoder-only的架构.md
source_ids:
  - 9529
status: draft
updated: 2026-06-12
---

# 为什么现在的LLM都是Decoder-only的架构？

本文探讨了为什么现在的LLM主流都选择Decoder-only架构，并从注意力矩阵的“秩”这一偏理论的角度进行分析。
作者指出，所有NLP任务都可以从“Encoder-Decoder”的视角来理解，区别在于Encoder、Decoder的注意力模式以及是否共享参数。
作者在10亿参数规模的模型上做了GPT和UniLM的对比实验，结果显示对于同样的输入输出，UniLM（双向注意力输入）相比GPT并无任何优势，甚至某些任务更差。
由此推论，输入部分的注意力改为双向不会带来收益，Encoder-Decoder架构的优势很可能只是源于参数翻倍。
究其物理原因，双向注意力的Attention矩阵是由低秩分解加softmax而来，由于低秩瓶颈会导致表达能力下降；而Decoder-only的Attention矩阵是一个下三角阵，对角线必然都是正数，其行列式必然为正数，因此Decoder-only架构的Attention矩阵一定是满秩的，在理论上具有更强的表达能力。
此外，作者还基于这一发现，提出了将双向注意力模型（如BERT）中的注意力矩阵在多头或层间截断为正向/反向单向注意力的改进思路，实验表明该正反向混合注意力在MLM任务上能取得比全双向注意力略好的效果。