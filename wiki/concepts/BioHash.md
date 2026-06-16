---
type: concept
title: BioHash
definition: 无监督数据集特征对齐哈希算法，将 FlyHash 中的随机基底用 K-Means 质心投影进行替换。
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"]
source_ids: ["8159"]
aliases: ["Bio-Inspired Hashing"]
status: stable
updated: 2026-06-12
---

# BioHash

## 定义
BioHash 是一种基于数据集先验建模的仿生二值化算法。是对 FlyHash 随机矩阵不确定性的一种改进方案。

## 步骤与直觉
BioHash 先对训练集使用内积度量进行 K-Means 无监督聚类，获取 $K$ 个质心。由于这些质心凝聚了原样本的结构，以质心作为投影方向，能够比 FlyHash 中的随机方向捕获更丰富的各向异性特征。计算投影后再通过 WTA 强稀疏激活为二值特征，以保证高效率与检索准确性。