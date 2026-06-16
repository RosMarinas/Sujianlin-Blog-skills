---
type: article_summary
title: 两个多元正态分布的KL散度、巴氏距离和W距离
article_id: "8512"
source_url: https://spaces.ac.cn/archives/8512
date: 2021-07-08
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
series:
  - [[信息论工具]]
topics:
  - [[信息论基础]]
concepts:
  - [[KL散度]]
  - [[巴氏距离]]
  - [[Wasserstein距离]]
  - [[正态分布]]
methods:
  - [[高斯分布KL散度公式]]
  - [[高斯分布巴氏距离公式]]
  - [[高斯分布W距离公式]]
evidence_spans:
  - ev::8512::多维高斯概率密度
  - ev::8512::高斯KL散度解析解
  - ev::8512::高斯巴氏距离解析解
  - ev::8512::高斯W距离两个版本等价性
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
source_ids:
  - "8512"
status: draft
updated: 2026-06-10
---

# article-8512: 两个多元正态分布的KL散度、巴氏距离和W距离

## 文章核心问题
两个多元正态分布之间的KL散度、巴氏（Bhattacharyya）距离和Wasserstein距离的显式解析表达式是什么？如何推导？

## 主要结论
1. KL散度解析解为$KL(p\|q)=\frac{1}{2}[(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)^{\top}\boldsymbol{\Sigma}_q^{-1}(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)-\log\det(\boldsymbol{\Sigma}_q^{-1}\boldsymbol{\Sigma}_p)+\text{Tr}(\boldsymbol{\Sigma}_q^{-1}\boldsymbol{\Sigma}_p)-n]$。
2. 巴氏距离解析解为$BD(p,q)=\frac{1}{2}\log\frac{\det(\boldsymbol{\Sigma})}{\sqrt{\det(\boldsymbol{\Sigma}_p\boldsymbol{\Sigma}_q)}}+\frac{1}{8}(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)^{\top}\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)$，其中$\boldsymbol{\Sigma}=(\boldsymbol{\Sigma}_p+\boldsymbol{\Sigma}_q)/2$。
3. W距离（$\rho=2$）两个流传版本等价：版本1含$(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{1/2}$，版本2（Fréchet距离）含$(\boldsymbol{\Sigma}_p\boldsymbol{\Sigma}_q)^{1/2}$，二者迹相等。

## 推导结构
- 回顾正态分布概率密度、基本统计量和高斯积分公式
- KL散度：代入正态分布密度函数，利用迹运算和二次型期望化简
- 巴氏距离：计算$\int\sqrt{pq}$积分，利用高斯积分公式化简
- W距离：去均值化归约为协方差优化问题，通过舒尔补和拉格朗日乘子法（或分块矩阵分解法）求解$\text{Tr}(\boldsymbol{C})$的最大值
- 证明$\text{Tr}((\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{1/2})=\text{Tr}((\boldsymbol{\Sigma}_p\boldsymbol{\Sigma}_q)^{1/2})$，建立两个版本的等价性

## 关键公式
- KL散度：$KL(p\|q)=\frac{1}{2}[(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)^{\top}\boldsymbol{\Sigma}_q^{-1}(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)-\log\det(\boldsymbol{\Sigma}_q^{-1}\boldsymbol{\Sigma}_p)+\text{Tr}(\boldsymbol{\Sigma}_q^{-1}\boldsymbol{\Sigma}_p)-n]$
- 巴氏距离：$BD(p,q)=\frac{1}{2}\log\frac{\det(\boldsymbol{\Sigma})}{\sqrt{\det(\boldsymbol{\Sigma}_p\boldsymbol{\Sigma}_q)}}+\frac{1}{8}(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)^{\top}\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)$，$\boldsymbol{\Sigma}=(\boldsymbol{\Sigma}_p+\boldsymbol{\Sigma}_q)/2$
- W距离版本1：$\mathcal{W}_2^2=\|\boldsymbol{\mu}_p-\boldsymbol{\mu}_q\|^2+\text{Tr}(\boldsymbol{\Sigma}_p)+\text{Tr}(\boldsymbol{\Sigma}_q)-2\text{Tr}((\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{1/2})$
- W距离版本2（Fréchet）：$\mathcal{W}_2^2=\|\boldsymbol{\mu}_p-\boldsymbol{\mu}_q\|^2+\text{Tr}(\boldsymbol{\Sigma}_p)+\text{Tr}(\boldsymbol{\Sigma}_q)-2\text{Tr}((\boldsymbol{\Sigma}_p\boldsymbol{\Sigma}_q)^{1/2})$
- 可交换情形：$\mathcal{W}_2^2=\|\boldsymbol{\mu}_p-\boldsymbol{\mu}_q\|^2+\|\boldsymbol{\Sigma}_p^{1/2}-\boldsymbol{\Sigma}_q^{1/2}\|_F^2$
