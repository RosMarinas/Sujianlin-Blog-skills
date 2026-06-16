---
type: article_summary
title: 从一个单位向量变换到另一个单位向量的正交矩阵
article_id: "8453"
source_url: https://spaces.ac.cn/archives/8453
date: 2021-06-05
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-06-05-从一个单位向量变换到另一个单位向量的正交矩阵.md
source_html: null
series: []
topics:
  - "[[矩阵计算]]"
concepts:
  - "[[正交矩阵]]"
  - "[[Householder变换]]"
  - "[[单位向量变换]]"
methods:
  - "[[用Householder变换构造向量变换的正交矩阵]]"
problem_patterns: []
evidence_spans:
  - ev::8453::二维
  - ev::8453::多维
  - ev::8453::化简
  - ev::8453::代码
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-06-05-从一个单位向量变换到另一个单位向量的正交矩阵.md
source_ids:
  - "8453"
status: draft
updated: 2026-06-10
---

## 文章核心问题

给定两个任意$d$维单位向量$\boldsymbol{a},\boldsymbol{b}$，如何构造一个正交矩阵$T$使得$\boldsymbol{b}=T\boldsymbol{a}$？

## 主要结论

1. 从二维情况出发，通过正交分解构造标准正交基$Q$，在基下旋转$R$，得到$T=QRQ^\top$。旋转和镜面反射两种选择导致不同结果。
2. 多维情况下，通过补全标准正交基$\tilde{Q}=(Q,E)$，在二维子空间做旋转、其余维度做恒等变换：$T=\tilde{Q}\begin{pmatrix}R&0\\0&I\end{pmatrix}\tilde{Q}^\top$。
3. 化简后发现$\boldsymbol{E}\boldsymbol{E}^\top=\boldsymbol{I}-\boldsymbol{Q}\boldsymbol{Q}^\top$消去了随机性，得到确定性结果。
4. 最终得到三种显式解，其中最简单的形式为：$T=\frac{(\boldsymbol{a}+\boldsymbol{b})(\boldsymbol{a}+\boldsymbol{b})^\top}{1+\boldsymbol{a}^\top\boldsymbol{b}}-\boldsymbol{I}$，即Householder变换的变体。

## 推导结构

二维情况（正交分解、旋转/反射矩阵）→ 多维情况（补全正交基、块对角变换）→ 化简（消去随机基、得到显式闭式解）→ 三个解（旋转版本、Householder版本、对称版本）→ 代码验证。

## 关键公式

- 二维基础：$\boldsymbol{a}=Q(1,0)^\top$, $\boldsymbol{b}=Q(\cos\theta,\sin\theta)^\top$, $\boldsymbol{T}=QRQ^\top$
- 通用解1（旋转）：$\boldsymbol{T}=I+2\boldsymbol{b}\boldsymbol{a}^\top-\frac{(\boldsymbol{a}+\boldsymbol{b})(\boldsymbol{a}+\boldsymbol{b})^\top}{1+\cos\theta}$
- 通用解2（Householder）：$\boldsymbol{T}=I-\frac{(\boldsymbol{a}-\boldsymbol{b})(\boldsymbol{a}-\boldsymbol{b})^\top}{1-\cos\theta}=I-2\frac{(\boldsymbol{a}-\boldsymbol{b})(\boldsymbol{a}-\boldsymbol{b})^\top}{\|\boldsymbol{a}-\boldsymbol{b}\|^2}$
- 对称形式解：$\boldsymbol{T}=\frac{(\boldsymbol{a}+\boldsymbol{b})(\boldsymbol{a}+\boldsymbol{b})^\top}{1+\boldsymbol{a}^\top\boldsymbol{b}}-\boldsymbol{I}$

## 体现的方法

- **用Householder变换构造向量变换的正交矩阵**：通过将问题转化为向量差方向的镜面反射，导出最简单的闭式解。

## 所属系列位置

独立文章，属于线性代数的实用技巧。

## 与其他文章的关系

- Householder变换也是[[spaces-11563-DeltaNet的核心逆矩阵的元素总是在-1-1-内]]中证明连乘形式时使用的投影算子基础。
- 与正交矩阵、谱范数等矩阵计算概念形成基础工具集。

## 原文证据锚点

- `ev::8453::二维`：二维情况的正交分解和旋转/反射矩阵构造。
- `ev::8453::多维`：多维情况的补全正交基和块对角变换。
- `ev::8453::化简`：显式闭式解的推导过程和三种解。
- `ev::8453::代码`：代码实现和正确性验证。
