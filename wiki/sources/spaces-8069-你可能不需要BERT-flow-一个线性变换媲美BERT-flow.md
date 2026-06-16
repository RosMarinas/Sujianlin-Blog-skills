---
type: article_summary
title: 你可能不需要BERT-flow：一个线性变换媲美BERT-flow
article_id: 8069
source_url: https://spaces.ac.cn/archives/8069
date: 2021-01-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-01-11-你可能不需要BERT-flow-一个线性变换媲美BERT-flow.md
sources: ["Data/Spaces_ac_cn/markdown/Mathematics/2021-01-11-你可能不需要BERT-flow-一个线性变换媲美BERT-flow.md"]
source_ids: ["8069"]
status: draft
updated: 2026-06-12
---

# 你可能不需要BERT-flow：一个线性变换媲美BERT-flow

## 文章核心问题
如何用更简单高效的方法解决预训练句向量空间中的各向异性（Anisotropy）分布偏差，避免使用较复杂的流（Flow）模型。

## 主要结论
句向量的各向异性表现为均值不为0且协方差矩阵极不均匀（各向异性锥形分布）。提出 BERT-whitening（白化），通过中心化和协方差矩阵标准化将向量映射为均值为 0 且协方差为单位阵的标准基，效果媲美甚至超越 BERT-flow。此外，基于 SVD 排序特征值直接截断前 $k$ 维可实现高效降维，在提速的同时甚至能获得效果提升。

## 推导结构
1. 分析余弦相似度必须建立在“标准正交基”下的假设，阐述各向同性的几何必要性。
2. 提出通过均值减法和协方差矩阵的标准白化转换 $\\tilde{\\boldsymbol{x}}_i = (\\boldsymbol{x}_i - \\boldsymbol{\mu})\\boldsymbol{W}$。
3. 利用协方差矩阵的奇异值分解（SVD）求解 $\\boldsymbol{W} = \\boldsymbol{U}\\sqrt{\\boldsymbol{\\Lambda}^{-1}}$。
4. 引入 PCA 进行降维并给出 STS-B 实验对比。

## 关键公式
- 白化转换式：$\\tilde{\\boldsymbol{x}}_i = (\\boldsymbol{x}_i - \\boldsymbol{\mu})\\boldsymbol{W}$
- 协方差 SVD：$\\boldsymbol{\Sigma} = \\boldsymbol{U}\\boldsymbol{\Lambda}\\boldsymbol{U}^{\\top}$
- 变换核计算：$\\boldsymbol{W} = \\boldsymbol{U}\\sqrt{\\boldsymbol{\\Lambda}^{-1}}$

## 体现的方法
- [[BERT-whitening变换]]：均值中心化并使用方差根逆进行缩放以消除协方差冗余。

## 与其他文章的关系
- 被 [[无监督语义相似度哪家强？我们做了个比较全面的评测]] 进一步验证。
- 为解决 whitening 对有监督模型的冲突而引入了超参数版本 [[当BERT-whitening引入超参数：总有一款适合你]]。

## 原文证据锚点
- `ev::8069::白化操作`：对应原文中利用 SVD 求解白化变换矩阵并进行降维截断的公式推导与 Numpy 代码实现。