---
type: article_summary
title: "BN究竟起了什么作用？一个闭门造车的分析"
article_id: "6992"
source_url: https://spaces.ac.cn/archives/6992
date: 2019-10-11
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-10-11-BN究竟起了什么作用-一个闭门造车的分析.md
series: []
topics:
  - "[[优化动力学]]"
concepts:
  - "[[BN梯度光滑化]]"
  - "[[Lipschitz约束优化]]"
  - "[[梯度L常数]]"
evidence_spans:
  - "ev::6992::核心不等式"
  - "ev::6992::梯度下降"
  - "ev::6992::Lipschitz约束"
  - "ev::6992::梯度分析"
  - "ev::6992::柯西不等式"
  - "ev::6992::减均值除标准差"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-10-11-BN究竟起了什么作用-一个闭门造车的分析.md
source_ids:
  - "6992"
status: draft
updated: 2026-06-10
---

# BN究竟起了什么作用？一个闭门造车的分析

## Summary

从优化角度分析BN：减去均值降低神经网络梯度的Lipschitz常数，除以标准差起自适应学习率作用使各层更新同步。不同意Internal Covariate Shift的传统解释。

## Key Claims

1. 梯度Lipschitz常数L越小，可用学习率越大，训练越快越稳。
2. 减去输入均值可最小化E[(x-μ)⊗(x-μ)]的1-范数，直接降低梯度L常数。
3. 除以标准差使每个参数更新更"同步"——类似自适应学习率，消除不同层级输入量级的差异性。
4. BN应放在全连接/卷积前面（而非激活函数后面）。
5. BN后的β,γ参数为锦上添花，非必要。
