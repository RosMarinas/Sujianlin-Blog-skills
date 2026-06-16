---
type: article_summary
title: MoE环游记：1. 从几何意义出发
article_id: "10699"
source_url: https://spaces.ac.cn/archives/10699
date: 2025-02-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-02-08-MoE环游记-1-从几何意义出发.md
source_html: Data/Spaces_ac_cn/raw/articles/10699/page.html
series:
  - "[[MoE环游记]]"
topics:
  - "[[MoE路由与负载均衡]]"
concepts:
  - "[[MoE几何路由]]"
methods:
  - "[[从计算节省目标重写模型结构]]"
problem_patterns:
  - "[[将路由选择转化为约束分配问题]]"
evidence_spans:
  - ev::10699::问题定义
  - ev::10699::MoE初现
  - ev::10699::文章小结
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-02-08-MoE环游记-1-从几何意义出发.md
source_ids:
  - "10699"
status: draft
updated: 2026-06-09
---

# MoE环游记：1. 从几何意义出发

## 文章核心问题

本文从 Dense FFN 的分块表达出发，追问能否只计算少量 Expert 向量来逼近全量求和，从而解释 MoE 为什么能在参数量变大时降低计算量。

## 主要结论

- FFN 可以被改写为多个 Expert 输出向量之和。
- 在近似求和问题中，按向量模长选择 Top-k 是一个几何上直观的近似策略。
- 直接计算所有 Expert 再排序并不省算力，因此需要 Router 先低成本预测模长，再只计算被选中的 Expert 方向。

## 推导结构

1. 把 FFN 分块为多个 Expert 输出。
2. 将节省计算的问题写成选择 `k` 个向量逼近全量和的优化问题。
3. 在近似正交假设下得到按模长选择的策略。
4. 重新参数化 Expert 为模长和方向，得到 Router + Top-k 的 MoE 形式。

## 关键公式

- [[MoE基本路由公式]]：以 `argtop_k rho` 选择 Expert，并将 Router 分数用于门控。

## 体现的方法

- [[从计算节省目标重写模型结构]]：先把“少算 Expert”转成逼近 Dense 输出的问题，再由几何近似反推出 Router 的角色。

## 所属系列位置

这是 [[MoE环游记]] 的第一篇，负责建立全系列的几何解释起点。

## 与其他文章的关系

- precedes: `article::10735`
- motivates: `concept::MoE负载均衡`
- defines: `concept::MoE几何路由`

## 原文证据锚点

- `ev::10699::问题定义`：第 22-38 行提出 FFN 分块与只选 `k` 个向量逼近全量和的问题。
- `ev::10699::MoE初现`：第 58-72 行给出 Router 预测模长并 Top-k 激活的基本公式。
- `ev::10699::文章小结`：第 96-98 行总结从 Dense 最佳逼近推导 MoE 的几何意义。
