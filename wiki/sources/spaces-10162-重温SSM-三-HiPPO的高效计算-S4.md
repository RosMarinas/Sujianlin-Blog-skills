---
type: article_summary
title: 重温SSM（三）：HiPPO的高效计算（S4）
article_id: "10162"
source_url: https://spaces.ac.cn/archives/10162
date: 2024-06-20
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md
source_html: Data/Spaces_ac_cn/raw/articles/10162/page.html
series:
  - [[重温SSM]]
topics:
  - [[状态空间模型数学基础]]
concepts:
  - [[S4卷积核生成函数]]
  - [[对角加低秩分解]]
methods:
  - [[生成函数化卷积核计算]]
  - [[对角加低秩与Woodbury加速]]
problem_patterns:
  - [[将矩阵幂卷积转为生成函数求值]]
evidence_spans:
  - ev::10162::基本框架::s4_legs
  - ev::10162::指数衰减::s4_memory
  - ev::10162::离散格式::s4_bilinear
  - ev::10162::卷积运算::kernel
  - ev::10162::生成函数::dft
  - ev::10162::从幂到逆::kernel_generating_function
  - ev::10162::特征向量::unstable_diagonalization
  - ev::10162::对角低秩::woodbury
  - ev::10162::点睛之笔::dlr
  - ev::10162::最后冲刺::s4_kernel
  - ev::10162::文章小结::s4_summary
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md
source_ids:
  - "10162"
status: stable
updated: 2026-06-09
---
## 文章核心问题

本文在 `revisit_ssm` 系列中的角色是：解释 S4 如何用 HiPPO-LegS 矩阵、双线性离散化、卷积核生成函数和对角加低秩分解获得高效并行计算。

## 主要结论

- 本文结论只从源文完整阅读后抽取，稳定断言均绑定到下方 evidence span。
- 它属于 [[重温SSM]] 系列和 [[状态空间模型数学基础]] 主题，服务于从 [[线性状态空间ODE]] 到 [[有理传递函数]] 的推导链。

## 推导结构

源文已完整阅读，章节为：基本框架、指数衰减、离散格式、卷积运算、生成函数、从幂到逆、特征向量、对角低秩、点睛之笔、最后冲刺、草草收尾、文章小结。

## 关键公式

- 相关公式页见本页 frontmatter 的 concepts/methods 以及系列页中的 staged graph。

## 体现的方法

- 本文体现的方法以 staged 方法页为准；弱泛化不提升为 stable。

## 所属系列位置

[[重温SSM]] 的第 3 篇。

## 与其他文章的关系

它与前后篇构成递进关系：HiPPO 推导 -> HiPPO 性质与离散化 -> S4 高效计算 -> RTF 有理生成函数视角。

## 原文证据锚点

- `ev::10162::基本框架::s4_legs`
- `ev::10162::指数衰减::s4_memory`
- `ev::10162::离散格式::s4_bilinear`
- `ev::10162::卷积运算::kernel`
- `ev::10162::生成函数::dft`
- `ev::10162::从幂到逆::kernel_generating_function`
- `ev::10162::特征向量::unstable_diagonalization`
- `ev::10162::对角低秩::woodbury`
- `ev::10162::点睛之笔::dlr`
- `ev::10162::最后冲刺::s4_kernel`
- `ev::10162::文章小结::s4_summary`
