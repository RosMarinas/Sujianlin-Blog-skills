---
type: article_summary
title: 梯度下降和EM算法：系出同源，一脉相承
article_id: "4277"
source_url: https://spaces.ac.cn/archives/4277
date: 2017-03-23
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2017-03-23-梯度下降和EM算法-系出同源-一脉相承.md
series:
  - "[[概率与统计模型]]"
topics:
  - "[[概率与统计推断]]"
concepts:
  - "[[EM算法]]"
  - "[[梯度下降]]"
  - "[[最大似然]]"
  - "[[交叉熵]]"
methods:
  - "[[近似曲线迭代法]]"
evidence_spans:
  - "ev::4277::em_as_approximation_method"
  - "ev::4277::kmeans_em_derivation"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-03-23-梯度下降和EM算法-系出同源-一脉相承.md
source_ids:
  - "4277"
status: draft
updated: 2026-06-13
---

## 文章核心问题

梯度下降法和EM算法（最大期望算法）在方法论上是否具有统一的思想根源？如何用"构造近似曲线/曲面逼近原目标函数"的统一框架重新理解它们？

## 主要结论

1. 梯度下降法和EM算法本质上同源：都是用简单函数在局部近似原目标函数，通过迭代优化近似函数来逼近最优解。
2. 梯度下降法是用开口向上的二次抛物线（一阶近似+固定曲率）做近似，EM算法是为了满足概率约束（非负、归一化）而选择其他形式的近似函数。
3. pLSA中的EM算法：在含隐变量的概率模型中，通过构造$Q$函数（利用贝叶斯后验作为常数权重）将log-sum项线性化，使得带约束的优化变为可解析求解。
4. K-Means中的EM算法：通过光滑max函数近似$\min$操作，利用指数族加权平均实现聚类中心的交替优化。

## 推导结构

1. 牛顿法→梯度下降法：从二阶近似退化为固定曲率一阶近似
2. 最大似然与交叉熵的关系
3. pLSA中的EM算法构造
4. K-Means中EM算法的光滑近似推导

## 关键公式

梯度下降：$x_{n+1}=x_n-hf'(x_n)$；EM的Q函数：$S'_n=-\sum\tilde{p}(x,y)\sum_z C_{x,y,z,n}\log p(x|z)p(z|y)$

## 体现的方法

- **近似曲线迭代法**：用简单函数（二次抛物线、线性化Q函数等）局部代替原目标函数，迭代求解代理函数的最优值。

## 所属系列位置

属于《概率与统计模型》系列的方法论文章，连接优化算法与概率统计。

## 与其他文章的关系

- [[5239 从最大似然到EM算法：一致的理解方式]]：另一视角理解EM算法，5239侧重于KL散度交替最小化视角。
