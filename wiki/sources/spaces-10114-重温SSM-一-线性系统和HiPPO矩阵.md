---
type: article_summary
title: 重温SSM（一）：线性系统和HiPPO矩阵
article_id: "10114"
source_url: https://spaces.ac.cn/archives/10114
date: 2024-05-24
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
source_html: Data/Spaces_ac_cn/raw/articles/10114/page.html
series:
  - [[重温SSM]]
topics:
  - [[状态空间模型数学基础]]
concepts:
  - [[线性状态空间ODE]]
  - [[HiPPO矩阵]]
  - [[HiPPO-LegS]]
methods:
  - [[正交基投影推导状态动力学]]
problem_patterns:
  - [[将在线记忆转为有限维系数动力学]]
evidence_spans:
  - ev::10114::基本形式::linear_ode
  - ev::10114::一般框架::projection_coefficients
  - ev::10114::邻近窗口::legt_matrix
  - ev::10114::整个区间::legs_matrix
  - ev::10114::延伸思考::hippo_bottom_up
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
source_ids:
  - "10114"
status: stable
updated: 2026-06-09
---
## 文章核心问题

本文在 `revisit_ssm` 系列中的角色是：从在线函数逼近和正交投影推导出线性状态空间 ODE，并给出 HiPPO-LegT 与 HiPPO-LegS 矩阵。

## 主要结论

- 本文结论只从源文完整阅读后抽取，稳定断言均绑定到下方 evidence span。
- 它属于 [[重温SSM]] 系列和 [[状态空间模型数学基础]] 主题，服务于从 [[线性状态空间ODE]] 到 [[有理传递函数]] 的推导链。

## 推导结构

源文已完整阅读，章节为：基本形式、有限压缩、线性初现、一般框架、请勒让德、邻近窗口、整个区间、延伸思考、文章小结。

## 关键公式

- 相关公式页见本页 frontmatter 的 concepts/methods 以及系列页中的 staged graph。

## 体现的方法

- 本文体现的方法以 staged 方法页为准；弱泛化不提升为 stable。

## 所属系列位置

[[重温SSM]] 的第 1 篇。

## 与其他文章的关系

它与前后篇构成递进关系：HiPPO 推导 -> HiPPO 性质与离散化 -> S4 高效计算 -> RTF 有理生成函数视角。

## 原文证据锚点

- `ev::10114::基本形式::linear_ode`
- `ev::10114::一般框架::projection_coefficients`
- `ev::10114::邻近窗口::legt_matrix`
- `ev::10114::整个区间::legs_matrix`
- `ev::10114::延伸思考::hippo_bottom_up`
