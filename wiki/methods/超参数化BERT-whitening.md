---
type: method
operation_types:
  primary: "Decompose / reduce dimension"
  secondary: []
title: "超参数化BERT-whitening"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2022-05-18-当BERT-whitening引入超参数-总有一款适合你.md"
source_ids:
  - "9079"
method_summary: "在 BERT-whitening 中引入 beta 控制均值去除强度、gamma 控制方差平权强度，使白化、正交旋转和降维之间可调。"
typical_structure: |
  1. 计算句向量均值和以 beta 调节后的协方差。
  2. 对协方差做 SVD 得到 U 与 Lambda。
  3. 使用 (x-beta mu) U Lambda^{-gamma/2} 得到变换向量。
  4. 通过 beta、gamma 和保留维度 k 在任务上调节效果。
applicability: "适用于默认 whitening 会损伤已监督句向量，但仍希望利用 SVD 旋转/降维能力的相似度任务。"
examples:
  - "[[article::9079]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::9079::超参数"
---

# 超参数化BERT-whitening

## 适用问题

适用于默认 whitening 会损伤已监督句向量，但仍希望利用 SVD 旋转/降维能力的相似度任务。

## 核心变换

固定白化 -> beta/gamma 参数化白化 -> 可调旋转、平权和降维。

## 典型步骤

1. 计算句向量均值和以 beta 调节后的协方差。
2. 对协方差做 SVD 得到 U 与 Lambda。
3. 使用 (x-beta mu) U Lambda^{-gamma/2} 得到变换向量。
4. 通过 beta、gamma 和保留维度 k 在任务上调节效果。

## 直觉

beta=gamma=1 是标准白化；beta=gamma=0 退化为正交旋转，不改余弦内积，因此给有监督句向量留下不劣于原表示的可能。

## 边界

需要验证具体任务上的 beta/gamma；证据不支持一组超参数通吃所有模型和数据集。

## 例子

- 9079 给出 (x-beta mu)U Lambda^{-gamma/2}，并说明 beta=gamma=0 时为不改变内积的正交变换。

## 证据

- `ev::9079::超参数`
- `Data/Spaces_ac_cn/markdown/Big-Data/2022-05-18-当BERT-whitening引入超参数-总有一款适合你.md`
- 读取章节: 方法概要、思路分析
