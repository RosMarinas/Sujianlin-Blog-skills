---
type: article_summary
title: "6个派生优化器的简单介绍及其实现"
article_id: "7094"
source_url: https://spaces.ac.cn/archives/7094
date: 2019-11-25
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-11-25-6个派生优化器的简单介绍及其实现.md
series:
  - "[[从动力学角度看优化算法]]"
topics:
  - "[[优化动力学]]"
concepts:
  - "[[权重衰减]]"
  - "[[层自适应优化]]"
  - "[[LAMB优化器]]"
  - "[[梯度累积]]"
  - "[[Lookahead优化器]]"
  - "[[Lazy优化器]]"
methods:
  - "[[把优化算法解释为动力系统离散化]]"
problem_patterns:
  - "[[把优化器经验现象改写为动力系统问题]]"
evidence_spans:
  - "ev::7094::基本形式"
  - "ev::7094::权重衰减"
  - "ev::7094::层自适应"
  - "ev::7094::Lookahead"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-11-25-6个派生优化器的简单介绍及其实现.md
source_ids:
  - "7094"
status: draft
updated: 2026-06-10
---

# 6个派生优化器的简单介绍及其实现

## Summary

汇总6种在已有优化器基础上改造的派生技巧：权重衰减、层自适应（LAMB）、分段线性学习率、梯度累积、Lookahead、Lazy优化器，并提供统一代码实现（bert4keras）。

## Key Claims

1. 权重衰减在自适应优化器中不等价于L2正则，前者防过拟合能力更优。
2. LAMB通过每层更新量标准化（乘参数模长）支持超大Batch Size训练。
3. 分段线性学习率可逼近任意学习率调度。
4. 梯度累积用小Batch Size达到大Batch Size效果。
5. Lookahead是"走几步后退一步"的参数插值策略。
6. Lazy优化器对Embedding层梯度稀疏化可防过拟合。
