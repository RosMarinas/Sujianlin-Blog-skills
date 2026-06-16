---
type: formula
title: NBCE概率聚合公式
aliases:
  - Naive Bayes Context Extension Formula
latex: |
  \log p(T|S_1, S_2,\cdots,S_n) = (1 + \beta)\mathcal{P}[\log p(T|S)] - \beta \log p(T) + \text{常数}
symbol_meanings:
  T: 要生成的token序列
  S_k: 给定的第 k 个独立的Context片段
  \beta: 调节上下文依赖强度的超参数（理论上等于 n - 1）
  \mathcal{P}: 概率分布的Pooling聚合方法（如最小熵Pooling）
standard_notation:
  T: token_sequence
  S: contexts_list
  beta: hyperparameter
  P: pooling_operator
conditions: |
  假定各 Context 片段之间在给定生成序列的条件下具有条件独立性（朴素贝叶斯假设），且输入概率已进行 Top-P 截断以剔除长尾噪声。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-23-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md
source_ids:
  - 9617
appears_in:
  - [spaces-9617-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度](wiki/sources/spaces-9617-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md)
  - [spaces-9632-关于NBCE方法的一些补充说明和分析](wiki/sources/spaces-9632-关于NBCE方法的一些补充说明和分析.md)
  - [spaces-9648-Naive-Bayes-is-all-you-need-?](wiki/sources/spaces-9648-Naive-Bayes-is-all-you-need-?.md)
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# NBCE概率聚合公式


## 概述

（待补充）

## Latex
$$\log p(T|S_1, S_2,\cdots,S_n) = (1 + \beta)\mathcal{P}[\log p(T|S)] - \beta \log p(T) + \text{常数}$$

## Symbol Meanings
- $T$: 要生成的token序列
- $S_k$: 给定的第 k 个独立的Context片段
- $\beta$: 调节上下文依赖强度的超参数（理论上等于 n - 1）
- $\mathcal{P}$: 概率分布的Pooling聚合方法（如最小熵Pooling）

## Conditions
假定各 Context 片段之间在给定生成序列的条件下具有条件独立性（朴素贝叶斯假设），且输入概率已进行 Top-P 截断以剔除长尾噪声。