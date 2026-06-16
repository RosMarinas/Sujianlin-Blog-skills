---
title: 如何训练你的准确率？
source_id: 9098
type: source
url: https://spaces.ac.cn/archives/9098
author: 苏剑林
date: 2022-06-01
category: 信息时代
tags: [accuracy-optimization, cross-entropy, loss-function, classification, theoretical-analysis]
license: CC BY-NC-SA
abstract: 评述EXACT论文的直接优化准确率方法，并从理论角度分析为什么交叉熵也能很好地优化准确率。核心发现：当p(y|x)接近1时，交叉熵与准确率光滑近似的一阶等价关系（log x ≈ x-1）。交叉熵的优势在于对错误分类样本的惩罚更大（无穷大 vs 最大值1），使其更关注错误样本。提出了优秀损失函数的设计原则：先找到评估指标的光滑近似，再将错误方向的误差拉大到无穷大。
key_contributions:
  - EXACT论文（正态分布重参数化优化准确率）的评述与批评
  - 交叉熵与准确率光滑近似在训练后期的等价性证明
  - 交叉熵对错误样本更大惩罚的优势分析
  - 优秀损失函数设计原则（光滑近似+错误方向无穷大）
  - 温度参数在损失函数中的关键作用
---
