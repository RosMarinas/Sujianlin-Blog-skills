---
type: article_summary
title: RSGAN：对抗模型中的“图灵测试”思想
article_id: "6110"
source_url: https://spaces.ac.cn/archives/6110
date: 2018-10-22
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-10-22-RSGAN-对抗模型中的-图灵测试-思想.md
series:
  - "[[GAN目标函数与约束专题]]"
topics:
  - "[[GAN训练目标与约束]]"
concepts:
  - "[[相对判别器]]"
  - "[[f散度]]"
methods:
  - "[[用对偶散度构造对抗生成目标]]"
problem_patterns:
  - "[[把生成模型训练改写为分布差异最小化问题]]"
evidence_spans:
  - ev::6110::RSGAN目标
  - ev::6110::相对判别解释
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-22-RSGAN-对抗模型中的-图灵测试-思想.md
source_ids:
  - "6110"
status: draft
updated: 2026-06-11
---

# RSGAN：对抗模型中的“图灵测试”思想

## 文章核心问题

RSGAN用真实样本和生成样本之间的相对得分差替代单点真假判别，形成交换联合分布的f散度。

## 主要结论

- 相对判别把判别器从绝对真假分类改成真假样本成对比较。
- 这种改写减少判别器偏置，并让生成器训练直接利用真实样本信息。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[用对偶散度构造对抗生成目标]]

## 原文证据锚点

- `ev::6110::RSGAN目标`
- `ev::6110::相对判别解释`
