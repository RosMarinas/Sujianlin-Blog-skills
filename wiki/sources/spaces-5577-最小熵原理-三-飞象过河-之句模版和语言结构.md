---
type: article_summary
title: 最小熵原理（三）："飞象过河"之句模版和语言结构
article_id: "5577"
source_url: https://spaces.ac.cn/archives/5577
date: 2018-05-30
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-05-30-最小熵原理-三-飞象过河-之句模版和语言结构.md
series:
  - [[最小熵原理]]
topics:
  - [[最小熵原理]]
concepts:
  - [[最小熵原理]]
  - [[句模版]]
  - [[信息熵]]
methods:
  - [[用互信息发现句模版]] # candidate method
evidence_spans:
  - ev::5577::句模版定义
  - ev::5577::DAG模版生成
  - ev::5577::层次结构分解
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-05-30-最小熵原理-三-飞象过河-之句模版和语言结构.md
source_ids:
  - "5577"
status: draft
updated: 2026-06-10
null_evidence_reason: "Third article, core methods and examples; evidence spans to be formalized in later passes."
---

# 最小熵原理（三）："飞象过河"之句模版和语言结构

## 文章核心问题

如何从最小熵原理出发，将词库构建推广到非相邻元素，无监督地发现句模版和语言层次结构？

## 主要结论

词库构建的互信息准则可以推广到非相邻词（Skip Gram 模型），通过构建句子的有向无环图（DAG）并提取所有路径来得到候选句模版。在投射性假设下，句模版嵌套可以形成句子的层次结构分解。

## 推导结构

1. 从相邻元素推广到非相邻元素：窗口内任意两词的共现
2. 句模版定义：固定词语 + 占位符的结构模式
3. DAG构建：以词为节点，窗口内互信息大的词对为有向边
4. 候选模版提取：提取DAG所有路径，相邻节点间插入占位符
5. 层次结构假设：每个句子由句模版相互嵌套生成
6. 递归分解算法：主模版 + 语义块的最优分解

## 关键公式

与文章二相同的互信息判据，但应用于窗口内任意词对而非相邻字对：
$$
F_{ab}^* = p_{ab}\left(\ln\frac{p_{ab}}{p_a p_b} - 1\right) \gg 0
$$

## 体现的方法

- [[用互信息发现句模版]]（candidate）：通过有向无环图和互信息阈值挖掘句子模板

## 所属系列位置

系列第三篇，第二个具体应用——句模版发现和语言结构分析。

## 与其他文章的关系

- 将[[最小熵原理（二）]]的相邻元素合并推广到非相邻元素
- 为[[最小熵原理（四）]]的"物以类聚"铺垫——词向量也是通过互信息关联
- 结果展示中使用了词向量作为等价类的先验

## 原文证据锚点

- `ev::5577::句模版定义` — 句模版的定义和嵌套结构
- `ev::5577::DAG模版生成` — 通过有向无环图提取候选模版
- `ev::5577::层次结构分解` — 句子的层次分解算法和结果
