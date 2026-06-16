---
type: method
operation_types:
  primary: "Estimate / sample instead of compute"
  secondary: []
title: "随机Softmax损失函数优化"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2017-05-27-不可思议的Word2Vec-5-Tensorflow版的Word2Vec.md"
source_ids:
  - "4402"
method_summary: "在大词表 softmax 中不计算全量配分函数，而是为每个样本随机采若干负标签，与正标签组成小集合后计算局部 softmax 交叉熵。"
typical_structure: |
  1. 分析全量 softmax 梯度中配分函数 Z 带来的 O(n) 类别遍历。
  2. 把梯度均值项解释为按类别概率的期望。
  3. 为每个样本随机选取 nb_negative 个负标签。
  4. 只在正标签加负标签子集上计算 softmax 和交叉熵。
applicability: "适用于词表或类别数很大、每步完整 softmax 计算成本过高的 Word2Vec/语言模型训练。"
examples:
  - "[[article::4402]]"
status: draft
updated: 2026-06-13
evidence_spans:
  - "ev::4402::随机损失"
---

# 随机Softmax损失函数优化

## 适用问题

适用于词表或类别数很大、每步完整 softmax 计算成本过高的 Word2Vec/语言模型训练。

## 核心变换

全类别 softmax -> 负标签随机采样 -> 子集 softmax 损失。

## 典型步骤

1. 分析全量 softmax 梯度中配分函数 Z 带来的 O(n) 类别遍历。
2. 把梯度均值项解释为按类别概率的期望。
3. 为每个样本随机选取 nb_negative 个负标签。
4. 只在正标签加负标签子集上计算 softmax 和交叉熵。

## 直觉

全量梯度里的第二项是所有标签梯度的均值；用随机负样本估计这个均值，可以把每步成本固定在采样子集大小上。

## 边界

这是采样近似损失；负样本数和采样分布会影响偏差、方差和最终效果。

## 例子

- 4402 提出对每个样本随机选取若干负标签，与原标签组成 nb_negative+1 个标签，在该集合内计算 softmax 和交叉熵。

## 证据

- `ev::4402::随机损失`
- `Data/Spaces_ac_cn/markdown/Big-Data/2017-05-27-不可思议的Word2Vec-5-Tensorflow版的Word2Vec.md`
- 读取章节: loss是怎么来的
