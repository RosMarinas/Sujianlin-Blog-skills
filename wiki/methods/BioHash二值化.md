---
type: method
operation_types:
  primary: "Decompose / reduce dimension"
  secondary: []
title: "BioHash二值化"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"
source_ids:
  - "8159"
method_summary: "先用数据集自身学习 K 个聚类中心，再把每个向量编码为距离最近的 k 个中心为 1 的稀疏二值向量，以数据自适应的方式完成向量二值化。"
typical_structure: |
  1. 对向量集合训练 K 个聚类中心。
  2. 按归一化内积或实现中指定的距离度量比较样本与中心。
  3. 选出每个样本最接近的 k 个中心。
  4. 把对应位置置 1，其余置 0，得到稀疏哈希向量。
applicability: "适用于待检索向量集固定、希望用数据自适应中心替代纯随机投影来获得更稀疏二值索引的相似搜索场景。"
examples:
  - "[[example::spaces-8159-BioWord哈希LSH]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8159::高维低激活"
---

# BioHash二值化

## 适用问题

适用于待检索向量集固定、希望用数据自适应中心替代纯随机投影来获得更稀疏二值索引的相似搜索场景。

## 核心变换

连续向量集合 -> 聚类中心基底和 WTA 选择 -> 稀疏二值哈希码。

## 典型步骤

1. 对向量集合训练 K 个聚类中心。
2. 按归一化内积或实现中指定的距离度量比较样本与中心。
3. 选出每个样本最接近的 k 个中心。
4. 把对应位置置 1，其余置 0，得到稀疏哈希向量。

## 直觉

相比 LSH 的无数据随机超平面，BioHash 让哈希基底由当前数据集决定，所以二值码更像为该检索库定制的稀疏表示。

## 边界

该方法依赖训练数据分布；当检索库变化很大时，需要重新学习中心。原文也指出算法细节中距离归一化与归属判定的处理并不完全一致。

## 例子

- 8159 将 BioHash 概括为先 K-Means 得到 K 个中心，再把每个向量映射为最近 k 个类为 1 的 K 维 0/1 向量。

## 证据

- `ev::8159::高维低激活`
- `Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md`
- 读取章节: BioHash、FlyHash
