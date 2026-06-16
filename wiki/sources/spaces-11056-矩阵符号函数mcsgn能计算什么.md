---
type: article_summary
title: 矩阵符号函数mcsgn能计算什么？
article_id: "11056"
source_url: https://spaces.ac.cn/archives/11056
date: 2025-06-23
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-06-23-矩阵符号函数mcsgn能计算什么.md
source_html: null
series: []
topics:
  - "[[矩阵计算]]"
  - "[[矩阵优化]]"
concepts:
  - "[[mcsgn算子]]"
  - "[[msign算子]]"
  - "[[代数Riccati方程]]"
  - "[[Sylvester方程]]"
  - "[[矩阵平方根]]"
methods:
  - "[[用mcsgn解代数Riccati方程]]"
  - "[[用分块矩阵变换推导矩阵恒等式]]"
problem_patterns: []
evidence_spans:
  - ev::11056::两种符号
  - ev::11056::分块恒等
  - ev::11056::第一例子
  - ev::11056::第二例子
  - ev::11056::第三例子
  - ev::11056::第四例子
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-23-矩阵符号函数mcsgn能计算什么.md
source_ids:
  - "11056"
status: draft
updated: 2026-06-10
---

## 文章核心问题

矩阵符号函数mcsgn除了求解Sylvester方程外，还能计算哪些矩阵量？系统整理mcsgn相关的恒等式和应用。

## 主要结论

1. mcsgn与msign的区别：msign具有正交不变性（将奇异值变成1），mcsgn具有相似不变性（将特征值变$\pm1$）；对称矩阵时两者相等。
2. mcsgn的分块恒等式可用于求解代数Riccati方程：$\boldsymbol{X}\boldsymbol{D}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} - \boldsymbol{A}\boldsymbol{X} - \boldsymbol{C} = \boldsymbol{0}$。
3. 通过mcsgn可计算：Sylvester方程的解（第一例子）、矩阵平方根和逆平方根（第二例子）、msign本身（第三例子）。
4. 一般恒等式：$\text{mcsgn}\left(\begin{bmatrix}0 & C \\ D & 0\end{bmatrix}\right)=\begin{bmatrix}0 & C(DC)^{-1/2} \\ D(CD)^{-1/2} & 0\end{bmatrix}$对任意形状$C,D$成立。

## 推导结构

两种符号（msign与mcsgn的定义和区别）→ 分块恒等（从代数Riccati方程出发的mcsgn恒等式）→ 几个结果（四个具体例子的恒等式推导）。

## 关键公式

- msign：$\text{msign}(M) = (MM^\top)^{-1/2}M = M(M^\top M)^{-1/2}$
- mcsgn：$\text{mcsgn}(M) = (M^2)^{-1/2}M = M(M^2)^{-1/2}$
- 一般恒等式：$\text{mcsgn}\left(\begin{bmatrix}0 & C \\ D & 0\end{bmatrix}\right)=\begin{bmatrix}0 & C(DC)^{-1/2} \\ D(CD)^{-1/2} & 0\end{bmatrix}$
- 代数Riccati方程：$\boldsymbol{X}\boldsymbol{D}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} - \boldsymbol{A}\boldsymbol{X} - \boldsymbol{C} = \boldsymbol{0}$

## 体现的方法

- **用mcsgn解代数Riccati方程**：通过分块矩阵变换将Riccati方程的解嵌入mcsgn计算，利用Newton-Schulz迭代高效求解。
- **用分块矩阵变换推导矩阵恒等式**：通过精心构造的分块矩阵和相似变换，推导矩阵运算的恒等关系，将复杂问题转化为已知计算。

## 所属系列位置

独立文章，是矩阵符号函数理论的基础性整理。

## 与其他文章的关系

- 被[[spaces-11158-矩阵平方根和逆平方根的高效计算]]依赖，使用mcsgn的恒等式和迭代方法。
- 与[[series::msign算子的Newton-Schulz迭代]]系列互补，msign是mcsgn的变体。
- 与[[spaces-10592-Muon优化器赏析-从向量到矩阵的本质跨越]]中msign算子相关（对称矩阵时msign=mcsgn）。

## 原文证据锚点

- `ev::11056::两种符号`：msign与mcsgn的定义、区别、适用范围。
- `ev::11056::分块恒等`：从代数Riccati方程出发推导mcsgn的分块恒等式。
- `ev::11056::第一例子`：$D=0$时mcsgn解Sylvester方程。
- `ev::11056::第二例子`：$A=B=0,D=I$时mcsgn计算矩阵平方根和逆平方根。
- `ev::11056::第三例子`：$A=B=0,D=C^\top$时mcsgn计算msign。
- `ev::11056::第四例子`：一般恒等式$\text{mcsgn}\left(\begin{bmatrix}0&C\\D&0\end{bmatrix}\right)=\begin{bmatrix}0&C(DC)^{-1/2}\\D(CD)^{-1/2}&0\end{bmatrix}$。
