---
type: article_summary
title: 中位数（Median）简介
article_id: 11693
source_url: "https://spaces.ac.cn/archives/11693"
date: 2026-03-31
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2026-03-31-中位数-Median-简介.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[中位数]]
  - [[几何中位数]]
  - [[坐标中位数]]
  - [[崩溃点]]
methods:
  - [[Weiszfeld迭代法]]
evidence_spans:
  - ev::11693::基本性质
  - ev::11693::优化视角
  - ev::11693::高维空间
  - ev::11693::继续推广
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-03-31-中位数-Median-简介.md
source_ids:
  - 11693
status: draft
updated: 2026-06-11
---

# 中位数（Median）简介

## 文章核心问题

中位数的定义、抗干扰性质（崩溃点），并在优化视角下（L1范数最小化）推广到高维空间得到几何中位数，给出Weiszfeld迭代的原理。

## 主要结论

- **基本性质**: 中位数崩溃点为50%，显著高于均值的0崩溃点，对异常值有强抗干扰能力，但计算复杂度较高。
- **优化视角**: 均值对应L2损失最小化，中位数对应L1损失最小化，这解释了中位数防异常值干扰的机制。
- **高维空间**: 通过优化表征可将中位数推广到高维空间得到几何中位数（Fermat点），但无解析解，需用Weiszfeld迭代求解。
- **继续推广**: 几何中位数可进一步推广到L_alpha损失最小化，坐标中位数（Coordinate-wise Median）则通过逐分量计算一维中位数得到。

