---
type: article_summary
title: 重温SSM（四）：有理生成函数的新视角
article_id: "10180"
source_url: https://spaces.ac.cn/archives/10180
date: 2024-06-27
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-06-27-重温SSM-四-有理生成函数的新视角.md
source_html: Data/Spaces_ac_cn/raw/articles/10180/page.html
series:
  - [[重温SSM]]
topics:
  - [[状态空间模型数学基础]]
concepts:
  - [[有理传递函数]]
  - [[友矩阵]]
  - [[S4卷积核生成函数]]
methods:
  - [[有理传递函数参数化]]
  - [[生成函数化卷积核计算]]
problem_patterns:
  - [[将矩阵幂卷积转为生成函数求值]]
evidence_spans:
  - ev::10180::基础回顾::s4_to_rtf
  - ev::10180::有理函数::rational
  - ev::10180::对应关系::charpoly
  - ev::10180::惊喜突现::fft_ratio
  - ev::10180::另起炉灶::ab_params
  - ev::10180::友之矩阵::companion
  - ev::10180::初始方式::zero_init
  - ev::10180::文章小结::rtf_summary
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-27-重温SSM-四-有理生成函数的新视角.md
source_ids:
  - "10180"
status: stable
updated: 2026-06-09
---
## 文章核心问题

本文在 `revisit_ssm` 系列中的角色是：把 SSM 卷积核生成函数重新表述为有理传递函数，并用 a,b 多项式系数直接参数化训练与友矩阵推理。

## 主要结论

- 本文结论只从源文完整阅读后抽取，稳定断言均绑定到下方 evidence span。
- 它属于 [[重温SSM]] 系列和 [[状态空间模型数学基础]] 主题，服务于从 [[线性状态空间ODE]] 到 [[有理传递函数]] 的推导链。

## 推导结构

源文已完整阅读，章节为：基础回顾、有理函数、对应关系、惊喜突现、另起炉灶、友之矩阵、初始方式、实验效果、文章小结。

## 关键公式

- 相关公式页见本页 frontmatter 的 concepts/methods 以及系列页中的 staged graph。

## 体现的方法

- 本文体现的方法以 staged 方法页为准；弱泛化不提升为 stable。

## 所属系列位置

[[重温SSM]] 的第 4 篇。

## 与其他文章的关系

它与前后篇构成递进关系：HiPPO 推导 -> HiPPO 性质与离散化 -> S4 高效计算 -> RTF 有理生成函数视角。

## 原文证据锚点

- `ev::10180::基础回顾::s4_to_rtf`
- `ev::10180::有理函数::rational`
- `ev::10180::对应关系::charpoly`
- `ev::10180::惊喜突现::fft_ratio`
- `ev::10180::另起炉灶::ab_params`
- `ev::10180::友之矩阵::companion`
- `ev::10180::初始方式::zero_init`
- `ev::10180::文章小结::rtf_summary`
