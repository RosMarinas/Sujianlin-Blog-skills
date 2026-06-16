---
type: article_summary
title: 概率分布的熵归一化（Entropy Normalization）
article_id: "8829"
source_url: https://spaces.ac.cn/archives/8829
date: 2021-12-24
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-12-24-概率分布的熵归一化-Entropy-Normalization.md
series:
  - [[熵归一化与熵不变性]]
topics:
  - [[信息论基础]]
  - [[概率分布构建]]
concepts:
  - [[熵归一化]]
  - [[信息熵]]
methods:
  - [[幂次变换熵归一化]]
evidence_spans:
  - ev::8829::幂次变换保持单调性
  - ev::8829::熵归一化牛顿迭代
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-12-24-概率分布的熵归一化-Entropy-Normalization.md
source_ids:
  - "8829"
status: draft
updated: 2026-06-10
---

# article-8829: 概率分布的熵归一化（Entropy Normalization）

## 文章核心问题
是否存在类似L2 Normalization的变换，可以直接对概率分布进行操作，在保持原始分布主要特性（如单调性）的同时，将分布的熵精确调整为指定值？

## 主要结论
1. 幂次变换 $\tilde{p}_i = p_i^{\gamma} / \sum_j p_j^{\gamma}$ 是满足要求的变换：它保持分布的单调性（若 $p_i > p_j$ 则有 $\tilde{p}_i > \tilde{p}_j$），且当 $\gamma$ 从 $0$ 递增到 $\infty$ 时，熵从 $\log n$ 递减到 $0$。
2. 给定目标熵 $\mathcal{H}^*$，$\gamma$ 的求解不存在解析解，但可以通过牛顿迭代法高效求解，通常迭代3-4次即可收敛。
3. 熵归一化可用于控制分布的稀疏程度，可能替代 Sparsemax、top-k/top-p 采样等操作，或用于缓解梯度消失问题。

## 推导结构
- 从信息熵定义 $\mathcal{H} = -\sum_i p_i \log p_i$ 出发，明确熵的取值范围 $[0, \log n]$
- 选择幂次变换 $\tilde{p}_i = p_i^{\gamma} / \sum_i p_i^{\gamma}$，证明其保持单调性且能覆盖整个熵区间
- 推导变换后熵的表达式：$\mathcal{H}_{\gamma} = \log\sum_i p_i^{\gamma} - \gamma\sum_i p_i^{\gamma}\log p_i / \sum_i p_i^{\gamma}$
- 在 $\gamma=1$ 处泰勒展开，得到牛顿迭代公式：$\gamma \leftarrow 1 + (\mathcal{H}^* - \mathcal{H}) / (\mathcal{H}^2 - \mathbb{E}[(\log p_i)^2])$
- 提供 Numpy 参考代码验证迭代收敛性

## 关键公式
- 信息熵：$\mathcal{H} = -\sum_i p_i \log p_i = \mathbb{E}[-\log p_i]$
- 幂次变换：$\tilde{p}_i = p_i^{\gamma} / \sum_j p_j^{\gamma}$
- 熵在 $\gamma=1$ 处的展开：$\mathcal{H}_{\gamma} \approx \mathcal{H}_1 + (\mathcal{H}_1^2 - \mathbb{E}[(\log p_i)^2])(\gamma - 1)$
- 牛顿迭代：$\gamma \leftarrow 1 + (\mathcal{H}^* - \mathcal{H}) / (\mathcal{H}^2 - \mathbb{E}[(\log p_i)^2])$
