---
type: article_summary
title: 重温SSM（二）：HiPPO的一些遗留问题
article_id: "10137"
source_url: https://spaces.ac.cn/archives/10137
date: 2024-06-05
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-06-05-重温SSM-二-HiPPO的一些遗留问题.md
source_html: Data/Spaces_ac_cn/raw/articles/10137/page.html
series:
  - [[重温SSM]]
topics:
  - [[状态空间模型数学基础]]
concepts:
  - [[HiPPO-LegS]]
  - [[线性状态空间ODE]]
methods:
  - [[正交基投影推导状态动力学]]
problem_patterns:
  - [[将在线记忆转为有限维系数动力学]]
evidence_spans:
  - ev::10137::离散格式::discretization
  - ev::10137::尺度等变::legs
  - ev::10137::长尾衰减::polynomial
  - ev::10137::计算高效::od
  - ev::10137::傅立叶基::fourier_legs
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-05-重温SSM-二-HiPPO的一些遗留问题.md
source_ids:
  - "10137"
status: stable
updated: 2026-06-09
---
## 文章核心问题

本文在 `revisit_ssm` 系列中的角色是：补全 HiPPO 离散化、LegS 尺度等变、多项式长尾衰减和 O(d) 计算性质。

## 主要结论

- 本文结论只从源文完整阅读后抽取，稳定断言均绑定到下方 evidence span。
- 它属于 [[重温SSM]] 系列和 [[状态空间模型数学基础]] 主题，服务于从 [[线性状态空间ODE]] 到 [[有理传递函数]] 的推导链。

## 推导结构

源文已完整阅读，章节为：离散格式、输入转换、LegT版本、LegS版本、优良性质、尺度等变、长尾衰减、计算高效、傅立叶基、文章小结。

## 关键公式

- 相关公式页见本页 frontmatter 的 concepts/methods 以及系列页中的 staged graph。

## 体现的方法

- 本文体现的方法以 staged 方法页为准；弱泛化不提升为 stable。

## 所属系列位置

[[重温SSM]] 的第 2 篇。

## 与其他文章的关系

它与前后篇构成递进关系：HiPPO 推导 -> HiPPO 性质与离散化 -> S4 高效计算 -> RTF 有理生成函数视角。

## 原文证据锚点

- `ev::10137::离散格式::discretization`
- `ev::10137::尺度等变::legs`
- `ev::10137::长尾衰减::polynomial`
- `ev::10137::计算高效::od`
- `ev::10137::傅立叶基::fourier_legs`
