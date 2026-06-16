---
type: article_summary
title: 最小熵原理（一）：无监督学习的原理
article_id: "5448"
source_url: https://spaces.ac.cn/archives/5448
date: 2018-04-18
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-04-18-最小熵原理-一-无监督学习的原理.md
series:
  - [[最小熵原理]]
topics:
  - [[最小熵原理]]
concepts:
  - [[最小熵原理]]
  - [[信息熵]]
methods: []
evidence_spans:
  - ev::5448::无监督学习原理
  - ev::5448::信息熵定义
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-04-18-最小熵原理-一-无监督学习的原理.md
source_ids:
  - "5448"
status: draft
updated: 2026-06-10
null_evidence_reason: "First article in series establishing conceptual foundation; evidence spans for core claims will be added in later passes."
---

# 最小熵原理（一）：无监督学习的原理

## 文章核心问题

无监督学习的根本原理是什么？如何从信息论角度统一理解各种无监督学习方法？

## 主要结论

信息熵最小化（最小熵原理）是一切无监督学习的根本原理。"知识"有固有信息熵，在理解之前总有未知因素，使得表达带有冗余。信息熵最小化意味着降低这个上界，逼近固有信息熵。通过挖掘"套路"（模式/规律）来降低信息熵，是学习的本质。

## 推导结构

1. 从"去冗余"（Redundancy Reduction）论文引出最小熵原理
2. 信息熵作为学习成本的度量：$I(c) \sim -\log p_c$
3. 中英文信息熵对比：中文单字9.65比特，英文字母4.03比特
4. 论证"套路"降低信息熵：分词、语法、定式都是通过发现规律来降低学习成本
5. 引出最小熵原理的两层理解

## 关键公式

$$
\mathcal{H}_c = -\sum_{c\in\text{汉字}} p_c\log p_c \quad \text{(平均字信息熵)}
$$

## 体现的方法

无直接方法，为全系列奠定信息论基础。

## 所属系列位置

系列第一篇，为后续5篇文章提供统一的理论框架——最小熵原理。

## 与其他文章的关系

- 为[[最小熵原理（二）]]提供理论基础：用熵最小化导出词库构建
- 为[[最小熵原理（三）]]提供理论基础：用熵最小化发现句模版
- 为[[最小熵原理（四）]]提供理论基础：用成本最小化理解词向量
- 为[[最小熵原理（五）]]提供理论基础：用编码长度最小化理解聚类

## 原文证据锚点

- `ev::5448::无监督学习原理` — 最小熵原理作为无监督学习的准则
- `ev::5448::信息熵定义` — 信息熵作为学习成本的度量
