---
type: example
title: 标准Attention的核技巧线性化推导实例
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
source_ids:
- '7921'
evidence_spans:
- ev::7921::泰勒展开
- ev::7921::指数定义
notation_mapping:
  （待从源文章提取）: （待从源文章提取）
article_id: '7921'
article: '[[（待从源文章提取）]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

## 问题

将标准Attention的e^{q·k}转化为线性Attention的phi(q)·varphi(k)形式。

## 方法一：泰勒展开

e^{q·k} = ∑(q·k)^m/m!
phi(q) = [1, q, ⊗^2 q/√2!, ..., ⊗^n q/√n!]^T
varphi(k) = [1, k, ⊗^2 k/√2!, ..., ⊗^n k/√n!]^T

## 方法二：指数定义

e^{q·k} = lim (1+q·k/n)^n
phi(q) = ⊗^n [1, q/√n]
varphi(k) = ⊗^n [1, k/√n]

## 方法三：Performer随机投影

e^{q·k} = E_{w~N(0,I)}[e^{w·q-||q||^2/2} * e^{w·k-||k||^2/2}]