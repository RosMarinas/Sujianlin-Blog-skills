---
type: article_summary
title: 最小熵原理（二）：“当机立断”之词库构建
article_id: "5476"
source_url: https://spaces.ac.cn/archives/5476
date: 2018-04-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-04-24-最小熵原理-二-当机立断-之词库构建.md
series:
  - [[最小熵原理]]
topics:
  - [[最小熵原理]]
concepts:
  - [[最小熵原理]]
  - [[信息熵]]
  - [[点互信息PMI]]
methods:
  - [[用互信息发现词语边界]] # candidate method
evidence_spans:
  - ev::5476::平均字信息熵
  - ev::5476::互信息近似
  - ev::5476::词库构建算法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-04-24-最小熵原理-二-当机立断-之词库构建.md
source_ids:
  - "5476"
status: draft
updated: 2026-06-10
null_evidence_reason: "Second article, core derivations and algorithm; evidence spans will be formalized in later passes."
---

# 最小熵原理（二）："当机立断"之词库构建

## 文章核心问题

如何从最小熵原理出发，无监督地从原始语料中构建词库？

## 主要结论

通过最小化平均字信息熵 $\mathcal{L} = \mathcal{H}/l$，可以导出词库构建的互信息准则。点互信息 $PMI(a,b) = \ln(p_{ab}/(p_a p_b))$ 大于1是合并相邻字为词的必要条件。基于此给出了一个四步词库构建算法：统计频率、互信息切分、频率截断、子词去冗。

## 推导结构

1. 定义平均字信息熵 $\mathcal{L} = \mathcal{H}/l$，论证分词降低学习成本
2. 局部化分析：合并相邻元素 $a,b$ 后 $\mathcal{L}$ 的变化量 $\Delta \mathcal{L} = -\mathcal{F}_{ab}/l$
3. 泰勒展开近似：$\mathcal{F}_{ab} \approx p_{ab}(\ln(p_{ab}/(p_a p_b)) - 1)$
4. 得出准则：$F_{ab}^* \gg 0$ 即 $PMI > 1$ 时合并
5. 四步词库构建算法
6. 一元分词的新熵诠释 + 动态规划

## 关键公式

$$
\mathcal{L} = \frac{\mathcal{H}}{l} = \frac{-\sum_i p_i\log p_i}{\sum_i p_i l_i} \quad \text{(平均字信息熵)}
$$

$$
\mathcal{F}_{ab} \approx F_{ab}^* = p_{ab}\left(\ln\frac{p_{ab}}{p_a p_b} - 1\right) \quad \text{(合并判据近似)}
$$

## 体现的方法

- [[用互信息发现词语边界]]（candidate）：通过最大化相邻字互信息发现词语边界

## 所属系列位置

系列第二篇，第一个具体应用——词库构建。

## 与其他文章的关系

- 基于[[最小熵原理（一）]]的理论框架
- 方法被[[最小熵原理（三）]]推广到非相邻词的句模版发现
- 与现有[[用互信息内积构造词向量几何]]共享互信息作为核心工具

## 原文证据锚点

- `ev::5476::平均字信息熵` — 分词降低平均字信息熵（$\mathcal{L}$从9.65降到7.2比特）
- `ev::5476::互信息近似` — $\mathcal{F}_{ab}$的泰勒展开近似导出PMI准则
- `ev::5476::词库构建算法` — 四步词库构建算法
