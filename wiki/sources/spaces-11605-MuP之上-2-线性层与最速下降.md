---
type: article_summary
title: MuP之上：2. 线性层与最速下降
article_id: "11605"
source_url: https://spaces.ac.cn/archives/11605
date: 2026-02-15
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2026-02-15-MuP之上-2-线性层与最速下降.md
source_html: Data/Spaces_ac_cn/raw/articles/11605/page.html
series:
  - "[[MuP之上]]"
topics:
  - "[[矩阵优化]]"
  - "[[MuP稳定性与矩阵优化]]"
concepts:
  - "[[MuP稳定性三条件]]"
  - "[[谱范数]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
  - "[[用切空间投影改写约束最速下降]]"
problem_patterns: []
evidence_spans:
  - ev::11605::初始方差
  - ev::11605::最速下降
  - ev::11605::求解过程
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-02-15-MuP之上-2-线性层与最速下降.md
source_ids:
  - "11605"
status: draft
updated: 2026-06-10
---

# MuP之上：2. 线性层与最速下降

## 文章核心问题

本文把线性层的稳定性指标化成谱范数约束，再在更新稳定性约束下求最速下降方向，从而得到 MuP 版 Muon 更新。

## 主要结论

- 带 In Norm 的线性层三个稳定性指标都可化为谱范数或谱范数变体。
- 在谱范数约束下一阶近似损失，最速下降方向由梯度的 SVD/msign 结构给出。

## 推导结构

1. 从归一化线性层计算稳定性指标。
2. 由前向/依赖稳定性推出初始化方差尺度。
3. 把更新稳定性作为约束，线性化损失并求最速下降方向。
4. 用 SVD 和核范数对偶性得到 Muon 形式。

## 关键公式

- [[线性层谱范数稳定性公式]]
- [[MuP版Muon最速下降公式]]

## 体现的方法

- [[用稳定性指标约束优化器缩放]]
- [[用切空间投影改写约束最速下降]]

## 所属系列位置

MuP之上第 2 篇，将三条件第一次落到线性层和 Muon 更新。

## 与其他文章的关系

- specializes: `method::用稳定性指标约束优化器缩放`
- bridges: `method::用切空间投影改写约束最速下降`

## 原文证据锚点

- `ev::11605::初始方差`
- `ev::11605::最速下降`
- `ev::11605::求解过程`
