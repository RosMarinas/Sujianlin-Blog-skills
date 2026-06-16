---
type: article_summary
title: 从费马大定理谈起（六）：n=4（2）
article_id: "2858"
source_url: https://spaces.ac.cn/archives/2858
date: 2014-08-19
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-08-19-从费马大定理谈起-六-n-4-2.md
series:
  - [[从费马大定理谈起]]
topics: []
concepts: []
methods:
  - [[无穷下降法]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-08-19-从费马大定理谈起-六-n-4-2.md
source_ids:
  - "2858"
status: draft
updated: 2026-06-10
---

## 文章核心问题

给出费马大定理 $n=4$ 的另一种证明形式：直接证明 $\varepsilon x^4 + y^4 = z^4$ 在 $\mathbb{Z}[i]$ 中无解。这个形式更接近一般 $n$ 为奇素数时的证明思路。

## 主要结论

- 方程 $\varepsilon x^4 + y^4 = z^4$（$\varepsilon$ 是单位数）在 $\mathbb{Z}[i]$ 中无全非 0 解。
- 该证明通过引入单位数 $\varepsilon$ 避免了第五篇中需要枚举 4 种单位数情况的繁琐。
- 关键技巧：利用 $\mathbb{Z}[i]$ 中 $z^4 - y^4$ 的完全分解 $z^4 - y^4 = (z+y)(z-y)(z+yi)(z-yi)$。

## 推导结构

1. **引理**: 若 $\varepsilon_1 x'^4 + \varepsilon_2 y'^4 + \varepsilon_3 z'^4 = 0$ 有解，则经整理可得 $\varepsilon x^4 + y^4 = z^4$ 且 $\xi^2 \mid x$。
2. **证明主体**: 设 $(x,y,z)$ 是 $\varepsilon x^4 + y^4 = z^4$ 中 $x$ 含 $\xi$ 次数最小的一组解。
3. 利用 $z^4 - y^4$ 的四项完全分解，分析各因子中 $\xi$ 的次数分布。
4. 通过构造新解 $(\xi^{m-1}u, s, t)$ 导出矛盾（无穷下降法）。

## 关键公式

$$
z^4 - y^4 = (z+y)(z-y)(z+yi)(z-yi)
$$

$$
\varepsilon x^4 = (z+y)(z-y)(z+yi)(z-yi)
$$

$$
\varepsilon' \xi^{4m-4} u^4 + s^4 = t^4
$$

## 体现的方法

- 引入单位数系数以简化情况枚举。
- 对 $z^n \pm y^n$ 在扩展数域中的完全分解。
- 无穷下降法（构造范数更小的新解）。
- 同余分析与 $\xi$ 次数分析相结合。

## 所属系列位置

系列第六篇，$n=4$ 证明的改进版本。

## 与其他文章的关系

- 是第五篇 $n=4$ 证明的补充和推广，形式更接近第九篇 $n=3$ 证明。
- 本文的引入单位数技巧在第九篇中直接复用。
- 展示了"加强命题"在无穷下降法中的应用。

## 原文证据锚点

- 引理证明：第 18-53 行
- 核心分解和矛盾导出：第 56-119 行
- 与一般 $n$ 证明的关联：第 121-123 行
