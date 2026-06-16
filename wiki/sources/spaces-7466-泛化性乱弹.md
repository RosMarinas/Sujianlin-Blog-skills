---
type: article_summary
title: 泛化性乱弹：从随机噪声、梯度惩罚到虚拟对抗训练
article_id: "7466"
source_url: https://spaces.ac.cn/archives/7466
date: 2020-06-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-06-01-泛化性乱弹-从随机噪声-梯度惩罚到虚拟对抗训练.md
series: []
topics:
  - [[Lipschitz约束与泛化]]
  - [[概率与统计]]
concepts:
  - [[梯度惩罚]]
  - [[对抗训练]]
  - [[虚拟对抗训练]]
methods:
  - [[对抗训练方法]]
  - [[梯度惩罚正则化]]
  - [[虚拟对抗训练VAT]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-01-泛化性乱弹-从随机噪声-梯度惩罚到虚拟对抗训练.md
source_ids:
  - "7466"
status: draft
updated: 2026-06-11
---

## 文章核心问题

探索随机噪声、梯度惩罚、对抗训练等提高模型泛化性能的手段之间的内在联系。

## 主要结论

- 添加随机噪声等价于梯度惩罚（二阶近似下）
- 对抗训练 = 最坏情况噪声 + 梯度上升
- 虚拟对抗训练（VAT）利用幂迭代构造特异性噪声，可用于半监督学习

## 推导结构

1. 随机噪声的积分近似 → 拉普拉斯正则项
2. 转移目标到 $l(f(x+\varepsilon),f(x))$ → 梯度惩罚正则项
3. 监督对抗训练：$\varepsilon \sim \nabla_x l(f(x), y)$
4. 虚拟对抗训练：幂迭代求Hessian主特征向量

## 关键公式

梯度惩罚：$\int q(\varepsilon) l(f(x+\varepsilon),f(x)) d\varepsilon \approx \frac{1}{2}\sigma^2 \sum_i \lambda_i(x)\Vert \nabla_x f_i(x)\Vert^2$

## 体现的方法

梯度惩罚正则化、对抗训练方法、虚拟对抗训练VAT、幂迭代法

## 所属系列位置

独立单篇，与对抗训练系列相关。

## 与其他文章的关系

与6051（Lipschitz约束）紧密相关，都讨论梯度惩罚与泛化。

## 原文证据锚点

- 随机噪声积分近似
- 梯度惩罚推导
- 对抗训练FGM
- 虚拟对抗训练VAT
