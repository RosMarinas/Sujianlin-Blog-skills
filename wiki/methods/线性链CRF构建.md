---
type: method
title: 线性链CRF构建
aliases: []
operation_types:
  primary: Decompose / reduce dimension
  secondary:
    - Structure-expose by factorization
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-05-18-简明条件随机场CRF介绍-附带纯Keras实现.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-02-07-你的CRF层的学习率可能不够大.md
source_ids:
  - "5542"
  - "7196"
method_summary: 将序列标注的k^n分类问题分解为逐标签打分和相邻标签转移打分两部分，通过利用马尔可夫假设将指数级路径求和简化为线性递归计算。
typical_structure: |
  1. 使用RNN/CNN计算逐标签分布 h(y_t;x)
  2. 定义可训练的转移矩阵 g(y_t,y_{t+1})
  3. 用递归公式（RNN封装）计算归一化因子 Z(x)
  4. 构建负对数似然损失
  5. 用Viterbi解码
applicability: 序列标注任务中需要显式建模标签间依赖关系时适用。当编码模型本身已足够强（如BERT）时，CRF的边际收益可能减小，仍需注意CRF层的学习率设置。
tools:
  - 条件随机场
  - 转移矩阵
  - Viterbi 解码
related_methods:
  - [[GlobalPointer序列标注]]
  - [[自截断解码停止]]
examples:
  - [[article::5542]]
  - [[article::7196]]
status: draft
updated: 2026-06-14
---

## 适用问题

序列标注（命名实体识别、词性标注、分词）中，标签之间存在强依赖关系——"B-PER 后应该接 I-PER 而非 I-LOC"。标准逐标签分类（Softmax）独立预测每个位置的标签，无法建模这种标签间的转移约束。CRF 通过显式建模相邻标签的转移概率来解决这一问题。

## 核心变换

**输入**：序列 $X = [x_1, \dots, x_n]$，编码器输出 $H \in \mathbb{R}^{n \times d}$
**输出**：最优标签序列 $Y = [y_1, \dots, y_n]$
**核心**：将 $k^n$ 的指数级路径空间分解为逐标签得分 + 转移得分

序列 $Y$ 的得分函数：
$$
s(X, Y) = \sum_{t=1}^n h(y_t; X) + \sum_{t=1}^{n-1} g(y_t, y_{t+1})
$$

其中 $h(y_t; X)$ 是位置 $t$ 属于标签 $y_t$ 的发射得分（由 RNN/BERT 计算），$g(y_t, y_{t+1})$ 是从标签 $y_t$ 转移到 $y_{t+1}$ 的转移得分（可训练参数矩阵 $G \in \mathbb{R}^{k \times k}$）。

条件概率：
$$
p(Y|X) = \frac{e^{s(X,Y)}}{\sum_{Y'} e^{s(X,Y')}}
$$

归一化因子 $Z(X) = \sum_{Y'} e^{s(X,Y')}$ 可通过前向算法（线性递归）高效计算。

## 典型步骤

1. **发射得分**：使用 RNN/CNN/BERT 计算每个位置 $t$ 属于每个标签 $y$ 的得分 $h(y_t; X)$
2. **转移矩阵**：定义可训练的转移矩阵 $G \in \mathbb{R}^{k \times k}$，$G_{ij}$ 表示标签 $i$ 转移到 $j$ 的得分
3. **归一化因子**：使用递归公式（RNN 封装）计算 $Z(X)$
4. **负对数似然损失**：$\mathcal{L} = -\log p(Y|X)$
5. **Viterbi 解码**：使用动态规划找出最优路径

## 直觉

核心思想：**标签之间不是独立的**。

一个简单例子：在 BIO 标注中，"B-ORG"后面几乎肯定是"I-ORG"或"O"，绝不可能是"B-PER"。逐标签 Softmax 分类完全忽略这种依赖，每个位置独立决策，结果是产生"B-ORG 后面接 B-LOC"这种荒谬的预测。

CRF 将序列标注问题重新定义为"找一条最合理的标签路径"。每条路径的得分由两部分组成：每个位置上的"发射得分"（模型认为这个位置应该是这个标签）和相邻标签间的"转移得分"（标签之间的兼容性）。归一化因子 $Z(X)$ 是所有可能路径得分的总和——由于路径总数为 $k^n$，需要使用前向算法将指数复杂度降为线性。

## 边界

- 转移矩阵 $G$ 的学习率通常应比编码器大（参见文章 7196），因为 CRF 层参数少但需要快速学习标签约束
- 当编码器足够强（如 BERT large）时，CRF 的边际收益减小——强编码器已经学会了隐式的标签依赖
- 线性链 CRF 仅考虑相邻标签的依赖，无法建模高阶标签交互
- 对于嵌套 NER，线性链 CRF 需要额外设计才能处理
- Viterbi 解码复杂度 $\mathcal{O}(nk^2)$，标签数 $k$ 较大时可能成为瓶颈

## 例子

- 中文分词：CRF 建模{B, M, E, S}（词首、词中、词尾、单字词）的转移约束
- 命名实体识别：建模 BIO/BIOS 标签之间的转移依赖
- 使用 Keras 实现 CRF 层的纯 Python 代码

## 证据

- ev::5542::CRF 条件概率公式：$p(Y|X) = e^{s(X,Y)} / \sum_{Y'} e^{s(X,Y')}$
- ev::5542::前向算法递归计算归一化因子 $Z(X)$
- ev::5542::Viterbi 解码动态规划
- ev::7196::CRF 层学习率应大于编码器层的分析和实验
