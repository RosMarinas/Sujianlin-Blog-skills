---
type: article_summary
title: BiGAN-QP：简单清晰的编码&生成模型
article_id: "6214"
source_url: https://spaces.ac.cn/archives/6214
date: 2018-12-10
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-12-10-BiGAN-QP-简单清晰的编码-生成模型.md
series:
  - "[[GAN目标函数与约束专题]]"
topics:
  - "[[GAN训练目标与约束]]"
  - "[[生成模型]]"
concepts:
  - "[[GAN-QP平方势散度]]"
  - "[[互信息]]"
methods:
  - "[[用对偶散度构造对抗生成目标]]"
problem_patterns:
  - "[[把生成模型训练改写为分布差异最小化问题]]"
evidence_spans:
  - ev::6214::BiGAN-QP目标
  - ev::6214::互信息正则
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-12-10-BiGAN-QP-简单清晰的编码-生成模型.md
source_ids:
  - "6214"
status: draft
updated: 2026-06-11
---

# BiGAN-QP：简单清晰的编码&生成模型

## 文章核心问题

把GAN-QP扩展到同时含编码器和生成器的BiGAN场景，并用重构/互信息正则稳定双向映射。

## 主要结论

- BiGAN-QP只需把GAN-QP中的单输入替换为(x,z)联合输入即可得到编码-生成双向模型。
- 重构项可解释为互信息上界，并通过stop-gradient避免破坏生成器/编码器的目标分工。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[用对偶散度构造对抗生成目标]]

## 原文证据锚点

- `ev::6214::BiGAN-QP目标`
- `ev::6214::互信息正则`
