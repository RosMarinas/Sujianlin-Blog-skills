---
type: article_summary
title: 随机分词再探：从Viterbi Sampling到完美采样算法
article_id: "9811"
source_url: https://spaces.ac.cn/archives/9811
date: 2023-10-16
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-10-16-随机分词再探-从Viterbi-Sampling到完美采样算法.md
series: []
topics:
  - 采样与估计
  - 分词与BytePiece
concepts:
  - Viterbi sampling
  - reservoir sampling
  - perfect sampling
  - Subword Regularization
  - logsumexp
methods:
  - Viterbi采样
  - 完美采样
problem_patterns: []
evidence_spans:
  - "9811::问题分析"
  - "9811::解决办法"
  - "9811::完美采样"
  - "9811::Decoding"
  - "9811::Sampling"
  - "9811::文章小结"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-16-随机分词再探-从Viterbi-Sampling到完美采样算法.md
source_ids:
  - "9811"
status: draft
updated: 2026-06-10
---

## 文章核心问题

改进Viterbi Sampling随机分词算法，使其从"二选一逐步稀释概率"变为真正的"完美采样"（每种切分方案被采到的概率正比于 $e^{\alpha s_i}$）。

## 主要结论

- 旧版Viterbi Sampling因多步二选一稀释了早出现方案的概率，无法保证概率正确
- 新版引入累积权重 $Z_i$（对数形式用logsumexp），实现水塘采样（Reservoir Sampling）式的概率维持
- 数学上证明新版与Subword Regularization等价，都是"完美采样"
- 计算复杂度与Viterbi Decoding同阶，远低于Subword Regularization

## 推导结构

1. 问题诊断：旧版将多选一转化为多步二选一导致概率稀释
2. 解决方案：引入累积权重 $Z_i = Z_{i-1} + e^{\alpha s_i}$，每一步按 $e^{\alpha s_i}/Z_i$ 选新方案
3. 数学证明：由Viterbi Decoding的递归式，将 $\max$ 替换为 $\text{logsumexp}$ 即得到完美采样
4. 实际实现用logsumexp避免指数爆炸

## 关键公式

$$\text{旧版: } r_i = \sigma(\alpha(s_i-s_{i-1})) $$

$$\text{新版: } Z_i = Z_{i-1} + e^{\alpha s_i},\quad r_i = \varepsilon < e^{\alpha s_i}/Z_i$$

$$Z^{\log}(c_1,\cdots,c_l) = \text{logsumexp}\left\{ \alpha s(\overline{c_1,\cdots,c_l}),\; Z^{\log}(c_1)+\alpha s(\overline{c_2,\cdots,c_l}),\; \ldots \right\}$$

## 体现的方法

- Viterbi采样：将Viterbi解码的 $\max$ 替换为带logsumexp的随机采样
- 完美采样：保证每种切分方案按 $e^{\alpha s_i}$ 概率被选中

## 所属系列位置

BytePiece分词系列的一部分，前一篇文章是《随机分词浅探：从Viterbi Decoding到Viterbi Sampling》（9768）。

## 与其他文章的关系

Viterbi采样是本批次"采样"主题在NLP分词中的应用。与重要性采样在目标上不同（Viterbi采样要精确按权重采样，重要性采样用建议分布近似目标分布），但在"用随机性处理复杂组合问题"上精神相通。

## 原文证据锚点

- 问题分析：旧版缺陷描述
- 解决方法：水塘采样+累积权重
- 完美采样证明：完美采样-采样节
- 与Decoding的关系：Decoding节
