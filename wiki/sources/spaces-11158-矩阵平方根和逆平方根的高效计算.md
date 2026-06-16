---
type: article_summary
title: 矩阵平方根和逆平方根的高效计算
article_id: "11158"
source_url: https://spaces.ac.cn/archives/11158
date: 2025-07-19
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-07-19-矩阵平方根和逆平方根的高效计算.md
source_html: null
series:
  - "[[矩阵方根计算]]"
topics:
  - "[[矩阵计算]]"
concepts:
  - "[[矩阵平方根]]"
  - "[[矩阵逆平方根]]"
  - "[[mcsgn算子]]"
  - "[[Newton-Schulz迭代]]"
  - "[[分块矩阵符号函数]]"
methods:
  - "[[用mcsgn分块恒等计算矩阵平方根]]"
  - "[[用线性递归技巧计算G·P^{-1/2}]]"
problem_patterns: []
evidence_spans:
  - ev::11158::基本概念
  - ev::11158::计算原理
  - ev::11158::求平方根
  - ev::11158::逆平方根
  - ev::11158::矩阵相乘
  - ev::11158::终极推广
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-07-19-矩阵平方根和逆平方根的高效计算.md
source_ids:
  - "11158"
status: draft
updated: 2026-06-10
---

## 文章核心问题

如何利用mcsgn（矩阵符号函数）的Newton-Schulz迭代高效计算矩阵的平方根$P^{1/2}$和逆平方根$P^{-1/2}$。

## 主要结论

1. 利用mcsgn的分块恒等式：$\text{mcsgn}\left(\begin{bmatrix}0 & P \\ I & 0\end{bmatrix}\right)=\begin{bmatrix}0 & P^{1/2} \\ P^{-1/2} & 0\end{bmatrix}$，一次迭代同时计算平方根和逆平方根。
2. 单独计算$P^{1/2}$时，通过$\boldsymbol{Y}_{t+1}=(a_{t+1}I+b_{t+1}\boldsymbol{Y}_t\boldsymbol{Z}_t+c_{t+1}(\boldsymbol{Y}_t\boldsymbol{Z}_t)^2)\boldsymbol{Y}_t$迭代，$\boldsymbol{Y}_t\boldsymbol{Z}_t$的迭代独立于$\boldsymbol{Z}_t$，数值更稳定。
3. 计算$\boldsymbol{G}\boldsymbol{P}^{-1/2}$可将$\boldsymbol{G}$作为初始值，利用线性递归性质，修改初始值$\boldsymbol{Z}_0=\boldsymbol{G}$即可，兼具数值稳定性和计算效率。
4. 推广到$\boldsymbol{Q}^{-1/2}\boldsymbol{G}\boldsymbol{P}^{-1/2}$的双边计算，公式保持简洁。

## 推导结构

基本概念（算术平方根、mcsgn回顾）→ 计算原理（分块恒等式推导、反对角结构简化）→ 求平方根（通过$Y_tZ_t$迭代避免数值问题）→ 逆平方根（$Z_t$迭代方案）→ 矩阵相乘（$G P^{-1/2}$的高效线性递归）→ 终极推广（$\boldsymbol{Q}^{-1/2}\boldsymbol{G}\boldsymbol{P}^{-1/2}$双边推广）。

## 关键公式

- mcsgn定义：$\text{mcsgn}(M)=(M^2)^{-1/2}M$
- 分块恒等式：$\text{mcsgn}\left(\begin{bmatrix}0 & A \\ B & 0\end{bmatrix}\right)=\begin{bmatrix}0 & A(BA)^{-1/2} \\ B(AB)^{-1/2} & 0\end{bmatrix}$
- 平方根：$\text{mcsgn}\left(\begin{bmatrix}0 & P \\ I & 0\end{bmatrix}\right)=\begin{bmatrix}0 & P^{1/2} \\ P^{-1/2} & 0\end{bmatrix}$
- 迭代公式：$Y_{t+1}=(a_{t+1}I+b_{t+1}Y_tZ_t+c_{t+1}(Y_tZ_t)^2)Y_t$, $Y_{t+1}Z_{t+1}=(a_{t+1}I+b_{t+1}Y_tZ_t+c_{t+1}(Y_tZ_t)^2)^2Y_tZ_t$

## 体现的方法

- **用mcsgn分块恒等计算矩阵平方根**：构建反对角分块矩阵，将平方根/逆平方根问题转化为mcsgn计算，利用Newton-Schulz迭代高效求解。
- **用线性递归技巧计算G·P^{-1/2}**：发现$Z_t$的迭代本质上是线性递归，将$G$作为初始值代入即可避免单独计算$P^{-1/2}$再乘$G$。

## 所属系列位置

[[series::矩阵方根计算]]的上篇，被[[spaces-11175-矩阵r次方根和逆r次方根的高效计算]]直接承接和推广。

## 与其他文章的关系

- 依赖[[spaces-11056-矩阵符号函数mcsgn能计算什么]]中关于mcsgn的恒等式和迭代方法。
- 被[[spaces-11175-矩阵r次方根和逆r次方根的高效计算]]推广到任意$r$次方根。
- 与Shampoo优化器中的$\boldsymbol{Q}^{-1/4}\boldsymbol{G}\boldsymbol{P}^{-1/4}$计算有潜在联系。

## 原文证据锚点

- `ev::11158::基本概念`：算术平方根的定义，mcsgn的定义和Newton-Schulz迭代回顾。
- `ev::11158::计算原理`：核心分块恒等式的推导，反对角结构的简化迭代。
- `ev::11158::求平方根`：$P^{1/2}$的迭代计算方案和代码实现。
- `ev::11158::逆平方根`：$P^{-1/2}$的迭代计算方案。
- `ev::11158::矩阵相乘`：$\boldsymbol{G}\boldsymbol{P}^{-1/2}$的高效线性递归计算方法。
- `ev::11158::终极推广`：$\boldsymbol{Q}^{-1/2}\boldsymbol{G}\boldsymbol{P}^{-1/2}$的双边推广。
