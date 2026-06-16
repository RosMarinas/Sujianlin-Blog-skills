---
type: example
title: spaces-11605-MuP版Muon最速下降
aliases: []
article_id: '11605'
article:
- - MuP之上：2. 线性层与最速下降
section: 求解过程
claim: 在谱范数更新稳定性约束下，用一阶损失近似和 SVD 求得 MuP 版 Muon 更新。
notation_mapping:
  W: boldsymbol{W}
  G: boldsymbol{G}
  eta: eta
  msign: msign
steps:
- 把更新稳定性写成谱范数约束
- 将损失一阶近似
- 令更新量为标量乘方向
- 用 SVD 与核范数对偶求最优方向
used_concepts:
- - - MuP稳定性三条件
- - - 谱范数
used_formulas:
- - - 线性层谱范数稳定性公式
- - - MuP版Muon最速下降公式
used_methods:
- - - 用稳定性指标约束优化器缩放
problem_pattern: null
source_span: ev::11605::求解过程
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-02-15-MuP之上-2-线性层与最速下降.md
source_ids:
- '11605'
status: stable
updated: '2026-06-12'
---

# spaces-11605-MuP版Muon最速下降

## 所在文章

[[MuP之上：2. 线性层与最速下降]]

## 原始问题

在谱范数更新稳定性约束下，用一阶损失近似和 SVD 求得 MuP 版 Muon 更新。

## 推导步骤

1. 把更新稳定性写成谱范数约束
2. 将损失一阶近似
3. 令更新量为标量乘方向
4. 用 SVD 与核范数对偶求最优方向

## 证据锚点

- `ev::11605::求解过程`