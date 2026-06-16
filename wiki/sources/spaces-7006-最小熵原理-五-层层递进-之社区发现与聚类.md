---
type: article_summary
title: 最小熵原理（五）："层层递进"之社区发现与聚类
article_id: "7006"
source_url: https://spaces.ac.cn/archives/7006
date: 2019-10-19
category: Big-Data
source_markdown: Data/Spaces_ac_cm/markdown/Big-Data/2019-10-19-最小熵原理-五-层层递进-之社区发现与聚类.md
series:
  - [[最小熵原理]]
topics:
  - [[最小熵原理]]
concepts:
  - [[最小熵原理]]
  - [[信息熵]]
  - [[社区发现]]
methods:
  - [[用层次编码最小化实现聚类]] # candidate method
evidence_spans:
  - ev::7006::信息熵=最短编码长度
  - ev::7006::层次编码方案
  - ev::7006::InfoMap优化目标
  - ev::7006::随机游走平稳分布
sources:
  - Data/Spaces_ac_cm/markdown/Big-Data/2019-10-19-最小熵原理-五-层层递进-之社区发现与聚类.md
source_ids:
  - "7006"
status: draft
updated: 2026-06-10
null_evidence_reason: "Fifth article on InfoMap algorithm; evidence spans to be formalized in later passes."
---

# 最小熵原理（五）："层层递进"之社区发现与聚类

## 文章核心问题

如何用信息论（最小熵原理）来解释聚类问题，并推导出优雅的InfoMap聚类算法？

## 主要结论

聚类可以通过最小化层次编码的平均长度来实现。InfoMap算法将聚类问题转化为编码问题：在图上进行随机游走生成序列，然后用层次编码（类标记+类内编码）压缩该序列，使平均编码长度最小化即为最优聚类方案。该算法几乎没有超参数，易于推广到多层社区发现和重叠社区挖掘。

## 推导结构

1. 信息熵 = 最短平均编码长度（无损压缩极限）
2. 层次编码概念：类标记 + 类内编号 + 终止标记
3. 层次编码的平均长度 $L(M) = q_{\curvearrowright}H(\mathcal{Q}) + \sum_i p_{i\circlearrowright} H(\mathcal{P}^i)$
4. 随机游走：在图上模拟随机游走生成序列
5. 穿越概率 $\tau$：避免陷入局部解，使平稳分布唯一
6. InfoMap三步骤：定义转移概率、求解平稳分布、搜索使 $L(M)$ 最小的聚类方案

## 关键公式

层次编码平均长度：
$$
L(M) = q_{\curvearrowright}H(\mathcal{Q}) + \sum_i p_{i\circlearrowright} H(\mathcal{P}^i)
$$

平稳分布方程：
$$
p_{\beta} = (1-\tau)\sum_{\alpha} p_{\alpha}p_{\alpha\to\beta} + \tau\sum_{\alpha}\frac{p_{\alpha}}{n}
$$

## 体现的方法

- [[用层次编码最小化实现聚类]]（candidate）：通过最小化层次编码长度来进行无监督聚类/社区发现

## 所属系列位置

系列第五篇，第四个具体应用——社区发现与聚类。

## 与其他文章的关系

- 将信息熵重新解释为最短编码长度，是[[最小熵原理（一）]]的编码理论视角延伸
- 引入二叉树编码证明信息熵下界，比之前系列更深入地建立了信息论基础
- 实验结果中使用词向量（与[[最小熵原理（四）]]、[[更别致的词向量模型]]相关）作为聚类输入

## 原文证据锚点

- `ev::7006::信息熵=最短编码长度` — 信息熵作为最短平均编码长度的证明
- `ev::7006::层次编码方案` — 层次编码的具体机制和压缩原理
- `ev::7006::InfoMap优化目标` — $L(M)$ 的定义和最小化目标
- `ev::7006::随机游走平稳分布` — 穿越概率和随机游走的平稳分布求解
