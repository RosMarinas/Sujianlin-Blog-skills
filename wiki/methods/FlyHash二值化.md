---
type: method
operation_types:
  primary: "Decompose / reduce dimension"
  secondary: []
title: "FlyHash二值化"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"
source_ids:
  - "8159"
method_summary: "用固定随机二值矩阵把向量投影到更高维空间，再通过 WTA 只保留最大的 k 个激活，得到高维低激活的稀疏二值哈希。"
typical_structure: |
  1. 选择并固定随机二值投影矩阵 W。
  2. 把原始向量 x 投影为 xW。
  3. 执行 WTA，保留最大的 k 个位置为 1。
  4. 用 K 维稀疏 0/1 码作为相似检索索引。
applicability: "适用于希望用果蝇嗅觉启发的高维低激活编码进行近似相似搜索、且不想为特定数据集训练聚类中心的场景。"
examples:
  - "[[example::spaces-8159-BioWord哈希LSH]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8159::高维低激活"
---

# FlyHash二值化

## 适用问题

适用于希望用果蝇嗅觉启发的高维低激活编码进行近似相似搜索、且不想为特定数据集训练聚类中心的场景。

## 核心变换

连续向量 -> 随机升维投影 -> WTA 稀疏二值码。

## 典型步骤

1. 选择并固定随机二值投影矩阵 W。
2. 把原始向量 x 投影为 xW。
3. 执行 WTA，保留最大的 k 个位置为 1。
4. 用 K 维稀疏 0/1 码作为相似检索索引。

## 直觉

升维增加可分性，低激活控制存储和检索成本；二者合在一起解释了果蝇启发哈希相对普通随机投影的方向。

## 边界

FlyHash 依赖足够高的随机投影维度保证效果；它不同于 BioHash 的数据自适应中心学习。

## 例子

- 8159 将 FlyHash 描述为随机投影加 WTA：投影到 K 维后把最大的 k 个元素置 1，其余置 0。

## 证据

- `ev::8159::高维低激活`
- `Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md`
- 读取章节: FlyHash
