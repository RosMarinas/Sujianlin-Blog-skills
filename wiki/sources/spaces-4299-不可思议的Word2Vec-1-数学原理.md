---
type: article_summary
title: 【不可思议的Word2Vec】 1.数学原理
article_id: "4299"
source_url: https://spaces.ac.cn/archives/4299
date: 2017-04-02
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-04-02-不可思议的Word2Vec-1-数学原理.md
series:
  - [[不可思议的Word2Vec]]
concepts:
  - [[Word2Vec]]
  - [[Skip-Gram]]
  - [[CBOW]]
  - [[Hierarchical Softmax]]
  - [[Negative Sampling]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-04-02-不可思议的Word2Vec-1-数学原理.md
source_ids:
  - "4299"
status: draft
updated: 2026-06-11
---

# 【不可思议的Word2Vec】 1.数学原理

## 内容概要
文章探讨了著名的词向量生成工具 Word2Vec 的基本情况与数学原理。作者指出，虽然 Word2Vec 作为语言模型来说过于粗糙，但其背后的两种训练方案（CBOW 和 Skip-Gram）与两套加速手段（层次 Softmax 和负采样）的结合大有用途。本系列文章将聚焦于 “Skip-Gram + 层次 Softmax” 的组合，该组合对条件概率 $P(w_{others}|w_t)$ 进行直接建模，在关键词抽取和逻辑推理中具有独特的应用价值。

## 关键内容
1. **Word Analogy 特性**：例如 `king - man ≈ queen - woman` 的线性特性，尽管 Mikolov 认为这展现了语义推理能力，但在实际小语料中较难复现，本系列更关注可复现性高的其他用途。
2. **四个备选模型**：Word2Vec 由两套训练方案（CBOW/Skip-Gram）和两套提速手段（层次 Softmax/负样本采样）组合而成。
3. **条件概率建模**：
   - CBOW 建模周围词叠加预测当前词：$P(w_t|Context)$。
   - Skip-Gram 建模当前词分别预测周围词：$P(w_{others}|w_t)$。
4. **加速机制**：
   - 层次 Softmax：通过 Huffman 树将预测概率复杂度从 $\mathcal{O}(|V|)$ 降至 $\mathcal{O}(\log_2 |V|)$。
   - 负采样：通过联合概率 $P(w_t, Context)$ 的二分类打分近似全局分类。
