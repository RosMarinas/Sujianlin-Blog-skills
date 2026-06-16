---
type: article_summary
title: DeltaNet的核心逆矩阵的元素总是在[-1, 1]内
article_id: "11563"
source_url: https://spaces.ac.cn/archives/11563
date: 2026-01-26
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2026-01-26-DeltaNet的核心逆矩阵的元素总是在-1-1-内.md
source_html: null
series:
  - "[[线性注意力简史]]"
topics:
  - "[[矩阵计算]]"
concepts:
  - "[[下三角矩阵]]"
  - "[[Woodbury恒等式]]"
  - "[[Householder变换]]"
methods:
  - "[[用伴随矩阵计算逆矩阵元素]]"
  - "[[用数学归纳法证明矩阵性质]]"
  - "[[矩阵分块递归求逆]]"
problem_patterns: []
evidence_spans:
  - ev::11563::问题描述
  - ev::11563::数学归纳
  - ev::11563::双重计算
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-01-26-DeltaNet的核心逆矩阵的元素总是在-1-1-内.md
source_ids:
  - "11563"
status: draft
updated: 2026-06-10
---

## 文章核心问题

证明DeltaNet并行计算中出现的形如$(I + KK^\top \odot M^-)^{-1}$的三角逆矩阵的所有元素都在$[-1,1]$范围内。

## 主要结论

1. 对于$K=[k_1,\cdots,k_n]^\top\in\mathbb{R}^{n\times d}$，其中每个$k_i$模长不超过1，$M$是下三角掩码矩阵，则$(I+KK^\top\odot M^-)^{-1}\in[-1,1]^{n\times n}$严格成立。
2. 通过数学归纳法和伴随矩阵方法，可证$Y_{n,1}$满足连乘形式$-\boldsymbol{k}_1^\top(I-\boldsymbol{k}_2\boldsymbol{k}_2^\top)\cdots(I-\boldsymbol{k}_{n-1}\boldsymbol{k}_{n-1}^\top)\boldsymbol{k}_n$，进一步通过投影算子的范数有界性证得结论。
3. 从DeltaNet递归形式出发的双重计算法给出了更简洁的证明：$Y_{t,i}=-\boldsymbol{k}_i^\top\boldsymbol{H}_{i+1\to t-1}\boldsymbol{k}_t$，利用$\Vert(I-\boldsymbol{k}_i\boldsymbol{k}_i^\top)\boldsymbol{x}\Vert\leq\Vert\boldsymbol{x}\Vert$得证。

## 推导结构

问题描述（定义目标矩阵）→ 数学归纳（对角性质→伴随矩阵→连乘形式→范数有界）→ 双重计算（逆阵形式→递推展开→对比结果）。

## 关键公式

- 目标矩阵：$X = I + KK^\top\odot M^-$，$Y = X^{-1}$
- 连乘形式：$Y_{n,1} = -\boldsymbol{k}_1^\top(I-\boldsymbol{k}_2\boldsymbol{k}_2^\top)\cdots(I-\boldsymbol{k}_{n-1}\boldsymbol{k}_{n-1}^\top)\boldsymbol{k}_n$
- 投影算子：$\Vert(I-\boldsymbol{k}_i\boldsymbol{k}_i^\top)\boldsymbol{x}\Vert^2 = \Vert\boldsymbol{x}\Vert^2 + (\boldsymbol{k}_i^\top \boldsymbol{x})^2(\Vert\boldsymbol{k}_i\Vert^2 - 2) \leq \Vert\boldsymbol{x}\Vert^2$

## 体现的方法

- **用数学归纳法证明矩阵性质**：通过对矩阵规模$n$的归纳，将$Y_{n,1}\in[-1,1]$的证明转化为已知子矩阵的结论。
- **用伴随矩阵计算逆矩阵元素**：利用下三角矩阵行列式为1的特性，通过伴随矩阵显式表达逆矩阵元素。
- **用双重计算模式验证恒等式**：从DeltaNet的递归形式和并行形式分别计算，对比得出逆矩阵的显式表达式。

## 所属系列位置

与[[series::线性注意力简史]]直接相关，该逆矩阵是DeltaNet并行计算的核心。

## 与其他文章的关系

- 延续[[spaces-11072-对角-低秩-三角阵的高效求逆方法]]中关于下三角矩阵求逆的技术路线。
- 为DeltaNet及其后续工作（GDN、KDA等）提供理论基础。

## 原文证据锚点

- `ev::11563::问题描述`：目标矩阵$X$的形式化定义，$K$的行向量模长不超过1的条件。
- `ev::11563::数学归纳`：详细的数学归纳法证明过程，伴随矩阵展开和连乘形式的推导。
- `ev::11563::双重计算`：从DeltaNet递归形式的双重计算给出更简洁的证明。
