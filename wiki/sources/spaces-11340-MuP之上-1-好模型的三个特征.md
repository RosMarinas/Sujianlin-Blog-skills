---
type: article_summary
title: MuP之上：1. 好模型的三个特征
article_id: "11340"
source_url: https://spaces.ac.cn/archives/11340
date: 2025-10-21
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-10-21-MuP之上-1-好模型的三个特征.md
source_html: Data/Spaces_ac_cn/raw/articles/11340/page.html
series:
  - "[[MuP之上]]"
topics:
  - "[[矩阵优化]]"
  - "[[MuP稳定性与矩阵优化]]"
concepts:
  - "[[MuP稳定性三条件]]"
  - "[[RMS尺度]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
problem_patterns: []
evidence_spans:
  - ev::11340::三个条件
  - ev::11340::平稳依赖
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-21-MuP之上-1-好模型的三个特征.md
source_ids:
  - "11340"
status: draft
updated: 2026-06-10
---

# MuP之上：1. 好模型的三个特征

## 文章核心问题

本文把“好模型”抽象为前向稳定、依赖稳定和更新稳定三个条件，并用 RMS 尺度统一描述模型输出、输入扰动和参数更新的量级。

## 主要结论

- 稳定训练不是单一初始化或学习率问题，而是模型前向、输入依赖和参数更新共同满足尺度稳定。
- 用 max/sup 而非期望来消去输入，可以得到更偏保守且更适合大模型安全训练的稳定性指标。

## 推导结构

1. 定义 RMS 尺度。
2. 提出三个稳定性条件。
3. 逐一分析条件对架构、反向传播和优化器的约束。
4. 讨论 max/sup 与期望分析的差异。

## 关键公式

- [[MuP稳定性三条件公式]]

## 体现的方法

- [[用稳定性指标约束优化器缩放]]

## 所属系列位置

MuP之上第 1 篇，定义后续层参数和优化器推导的指标体系。

## 与其他文章的关系

- connects_to: `article::11729`
- motivates: `article::11605`

## 原文证据锚点

- `ev::11340::三个条件`
- `ev::11340::平稳依赖`
