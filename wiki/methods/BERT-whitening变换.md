---
type: method
operation_types:
  primary: "Decompose / reduce dimension"
  secondary: []
title: "BERT-whitening变换"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2021-01-11-你可能不需要BERT-flow-一个线性变换媲美BERT-flow.md"
  - "Data/Spaces_ac_cn/markdown/Big-Data/2021-04-11-无监督语义相似度哪家强-我们做了个比较全面的评测.md"
source_ids:
  - "8069"
  - "8321"
method_summary: "对句向量先减去语料均值，再用协方差矩阵的 SVD 白化矩阵做线性变换，使向量分布近似零均值、单位协方差，并可顺带降维缓解各向异性。"
typical_structure: |
  1. 收集待处理句向量并计算均值。
  2. 计算去中心化向量的协方差矩阵并做 SVD 分解。
  3. 用 U Lambda^{-1/2} 构造白化变换，必要时只保留前 k 维。
  4. 在语义相似度或检索任务中用变换后的向量计算相似度。
applicability: "适用于无监督句向量各向异性明显、需要用简单后处理改善相似度排序或降低检索维度的场景。"
examples:
  - "[[article::8069]]"
  - "[[article::8321]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8069::白化操作"
  - "ev::8321::白化操作"
---

# BERT-whitening变换

## 适用问题

适用于无监督句向量各向异性明显、需要用简单后处理改善相似度排序或降低检索维度的场景。

## 核心变换

句向量集合 -> 去中心化与协方差 SVD -> 白化/降维后的句向量集合。

## 典型步骤

1. 收集待处理句向量并计算均值。
2. 计算去中心化向量的协方差矩阵并做 SVD 分解。
3. 用 U Lambda^{-1/2} 构造白化变换，必要时只保留前 k 维。
4. 在语义相似度或检索任务中用变换后的向量计算相似度。

## 直觉

BERT-flow 试图把向量分布变成标准正态；该页面的证据显示，在线性层面直接把均值和协方差标准化已经能捕捉这一核心，并且计算成本更低。

## 边界

主要支持无监督或未被特定监督目标校准的句向量；已有监督优化的 SimBERT 类向量可能被默认白化破坏，需要单独验证。

## 例子

- 在 8069 的 BERT-whitening 中，向量先减均值，再乘以由协方差 SVD 得到的白化矩阵；8321 的评测进一步观察到 whitening 且降维在多组无监督中文相似度实验中有工程价值。

## 证据

- `ev::8069::白化操作`
- `ev::8321::白化操作`
- `Data/Spaces_ac_cn/markdown/Mathematics/2021-01-11-你可能不需要BERT-flow-一个线性变换媲美BERT-flow.md`
- `Data/Spaces_ac_cn/markdown/Big-Data/2021-04-11-无监督语义相似度哪家强-我们做了个比较全面的评测.md`
- 读取章节: 标准化协方差矩阵、评测情况
