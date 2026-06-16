---
type: concept
title: BERT-whitening
definition: 一种无监督特征分布校正技术，通过线性变换消除句向量特征相关性并统一各分量方差。
sources: ["Data/Spaces_ac_cn/markdown/Mathematics/2021-01-11-你可能不需要BERT-flow-一个线性变换媲美BERT-flow.md"]
source_ids: ["8069"]
aliases: ["BERT白化", "句向量白化"]
status: stable
updated: 2026-06-12
---

# BERT-whitening

## 定义
BERT-whitening 是一种将无监督句向量进行中心化去均值，并使用对称变换矩阵进行方差平权缩放，以达到各向同性基底分布的后处理方法。

## 优势与原理
相较于复杂的 BERT-flow 模型，白化操作只需要简单的线性代数计算。利用数据集计算句向量的均值 $\\boldsymbol{\\mu}$ 与协方差 $\\boldsymbol{\\Sigma}$，通过 SVD 特征值分解直接构建白化核。保留前 $k$ 个大特征值分量便可以无损进行高效的主成分（PCA）降维，在节省内存和极大提升匹配效果上具有显著的工程价值。