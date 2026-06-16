---
type: article_summary
title: 细水长flow之TARFLOW：流模型满血归来？
article_id: 10667
source_url: "https://spaces.ac.cn/archives/10667"
date: 2025-01-17
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-01-17-细水长flow之TARFLOW-流模型满血归来.md
series: []
topics:
  - [[生成模型]]
concepts:
  - [[Normalizing Flow]]
  - [[仿射耦合层]]
  - [[TARFLOW]]
methods:
  - [[流模型去噪采样]]
evidence_spans:
  - ev::10667::模型回顾
  - ev::10667::仿射耦合
  - ev::10667::核心改进
  - ev::10667::加噪去噪
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-01-17-细水长flow之TARFLOW-流模型满血归来.md
source_ids:
  - 10667
status: draft
updated: 2026-06-11
---

# 细水长flow之TARFLOW：流模型满血归来？

## 文章核心问题

探讨Normalizing Flow（流模型）的生成效果和自回归架构改进，引入Causal Transformer和空间维度的Patchify耦合，结合去噪自编码器实现流模型生成质量的满血回归。

## 主要结论

- **模型回顾**: 流模型通过可逆逆函数以及雅可比行列式计算使得最大似然积分直接可算。
- **仿射耦合**: 仿射耦合层通过局部划分和下三角雅可比矩阵，同时满足了可逆性和雅可比行列式易算性。
- **核心改进**: TARFLOW将仿射耦合推广到空间维度上的多块划分，配合Causal Transformer实现自回归流。
- **加噪去噪**: 基于去噪自编码器性质，流模型加噪训练后的概率密度梯度直接对应理论最优去噪方向。

