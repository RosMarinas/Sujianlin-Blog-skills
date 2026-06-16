---
type: formula
title: KL散度公式
aliases: '["KL divergence formula"]'
latex: KL(p\|q)=\frac{1}{2}\left[(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)^{\top}\boldsymbol{\Sigma}_q^{-1}(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)-\log\det(\boldsymbol{\Sigma}_q^{-1}\boldsymbol{\Sigma}_p)+\text{Tr}(\boldsymbol{\Sigma}_q^{-1}\boldsymbol{\Sigma}_p)-n\right]
symbol_meanings:
  mu_p: p的均值
  mu_q: q的均值
  Sigma_p: p的协方差
  Sigma_q: q的协方差
  Tr: 迹
standard_notation: KL(p||q)
conditions: p,q均为正态分布
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
source_ids:
- '['
- '"'
- '8'
- '5'
- '1'
- '2'
- '"'
- ']'
evidence_spans: '[]'
status: draft
updated: '2026-06-14'
appears_in:
- '['
- '"'
- '8'
- '5'
- '1'
- '2'
- '"'
- ']'
---

## 概述

$$KL(p\|q)=\frac{1}{2}\left[(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)^{\top}\boldsymbol{\Sigma}_q^{-1}(\boldsymbol{\mu}_p-\boldsymbol{\mu}_q)-\log\det(\boldsymbol{\Sigma}_q^{-1}\boldsymbol{\Sigma}_p)+\text{Tr}(\boldsymbol{\Sigma}_q^{-1}\boldsymbol{\Sigma}_p)-n\right]$$