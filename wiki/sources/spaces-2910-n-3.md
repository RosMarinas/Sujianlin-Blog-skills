---
type: article_summary
title: 从费马大定理谈起（九）：n=3
article_id: "2910"
source_url: https://spaces.ac.cn/archives/2910
date: 2014-09-01
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-09-01-从费马大定理谈起-九-n-3.md
series:
  - [[从费马大定理谈起]]
topics: []
concepts:
  - [[无穷下降法]]
  - [[艾森斯坦整数]]
methods:
  - [[无穷下降法]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-09-01-从费马大定理谈起-九-n-3.md
source_ids:
  - "2910"
status: draft
updated: 2026-06-10
---

## 文章核心问题

使用艾森斯坦整数和无穷下降法证明费马大定理在 $n=3$ 时成立。

## 主要结论

- 方程 $x^3+y^3+z^3=0$ 在 $\mathbb{Z}[\omega]$ 中没有 $xyz \neq 0$ 的解。
- 证明结构类似于 $n=4$ 的第二个证明（第六篇），使用了引入单位数系数和完全分解 $y^3+z^3$ 的技巧。
- 关键工具：艾森斯坦整数中的模 $1-\omega$ 分析 + 唯一分解 + 无穷下降法。

## 推导结构

1. **引理**: 若 $\varepsilon_1 x^3 + \varepsilon_2 y^3 + \varepsilon_3 z^3 = 0$ 且 $\xi \mid x,\ \xi \nmid yz$，则方程可化为 $\varepsilon x^3 + y^3 + z^3 = 0$。
2. **主体证明**:
   - 首先证明 $\xi \mid xyz$（模 9 同余分析）。
   - 设 $(x,y,z)$ 是 $\varepsilon x^3 + y^3 + z^3 = 0$ 中 $N(x)$ 最小的解。
   - 判断 $\xi^2 \mid x$。
   - 完全分解 $-\varepsilon x^3 = (y+z)(y+z\omega)(y+z\omega^2)$。
   - 分析三因子中 $\xi$ 的次数分布。
   - 利用唯一分解将各因子写为立方数的伴随。
   - 通过恒等式 $(y+z)+(y+z\omega)\omega+(y+z\omega^2)\omega^2=0$ 构造新解 $(\xi r,s,t)$。
   - $N(\xi r) < N(x)$ 与最小性矛盾。

## 关键公式

$$
-\varepsilon x^3 = (y+z)(y+z\omega)(y+z\omega^2)
$$

$$
\varepsilon_1 \xi^3 r^3 + (\varepsilon_2 \omega) s^3 + (\varepsilon_3 \omega^2) t^3 = 0
$$

$$
\varepsilon' \xi^3 r^3 + s^3 + t^3 = 0
$$

## 体现的方法

- 艾森斯坦整数中的模 $1-\omega$ 同余分析。
- 扩展数域中的完全分解（$y^n+z^n$ 在分圆整数环中的分解）。
- 无穷下降法。
- 引入单位数统一处理多个方程形式。

## 所属系列位置

系列第九篇，完成 $n=3$ 的证明。

## 与其他文章的关系

- 依赖第八篇艾森斯坦整数的概念和性质。
- 证明结构模仿第六篇 $n=4$ 的第二个证明。
- 第十篇继续使用艾森斯坦整数求 $x^3+y^3=z^3+w^3$ 的参数化解。

## 原文证据锚点

- 引理：第 22-33 行
- 主体证明：第 36-89 行
- 与 $n=4$ 证明的类比：第 16-18 行
