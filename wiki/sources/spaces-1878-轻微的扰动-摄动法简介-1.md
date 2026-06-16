---
type: article_summary
title: 轻微的扰动——摄动法简介(1)
article_id: "1878"
source_url: https://spaces.ac.cn/archives/1878
date: 2013-01-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2013-01-16-轻微的扰动-摄动法简介-1.md
series: ['[[摄动法简介系列]]']
topics: ['[[topic::摄动与ODE求解数学基础]]']
concepts: ['[[摄动法]]']
methods: ['[[摄动级数展开法]]']
problem_patterns: []
evidence_spans: ['ev::1878::摄动法思想', 'ev::1878::代数方程']
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-01-16-轻微的扰动-摄动法简介-1.md
source_ids:
  - "1878"
status: draft
updated: 2026-06-11
---

## 文章核心问题
引入摄动法（微扰理论）的基本哲学和基本步骤，并以一个可求精确解但求根公式复杂的代数三次方程为例展示摄动近似求解的有效性。

## 主要结论
摄动法的核心是在精确解出的简单基础模型上，将微小扰动的影响以小参数的幂级数形式逐步累加进去。对于方程 $
arepsilon x^3+x^2=p^2$，假设解为 $x = p + a_1 
arepsilon + a_2 
arepsilon^2 + \dots$，代入并对应各项系数为 0，可以求得二阶近似解 $x pprox p - 
rac{p^2}{2}
arepsilon + 
rac{5p^3}{8}
arepsilon^2$，这为数值求解提供了极其优秀的逼近值。

## 推导结构
1. **概念引入**：阐述摄动法在天体力学（二体与N体扰动）和量子力学中的思想根源。
2. **设定方程例子**：考虑 $
arepsilon x^3+x^2=p^2$，以 $
arepsilon$ 为小参数。
3. **提出幂级数假设**：在 $
arepsilon=0$ 的精确解 $x=p$ 的基础上，假设解为 $x = p + a_1
arepsilon + a_2
arepsilon^2 + \dots$。
4. **系数级数代回**：代入方程展开，在 $
arepsilon$ 和 $
arepsilon^2$ 阶数上对齐系数。
5. **求解级数系数**：解出方程组求得 $a_1, a_2$，给出二阶级数近似式并作数值对比证明精确度。

## 关键公式
- 级数假设: $x=p+a_1 
arepsilon +a_2 
arepsilon^2 +a_3 
arepsilon^3+\dots$
- 求解级数近似: $x=p-
rac{p^2}{2} 
arepsilon+
rac{5p^3}{8}
arepsilon^2$

## 体现的方法
- `[[摄动级数展开法]]`：将求解函数/变量表达为小参数的幂级数代回方程，逐阶求解线性系数的微扰方法。

## 所属系列位置
本篇为《摄动法简介系列》的第一篇，作为摄动法在代数方程应用中的奠基性引入。

## 与其他文章的关系
- 算子系列中常数变易法的哲学基础与摄动法一脉相承 `[[wiki/sources/spaces-1791-算子与线性常微分方程-上.md]]`。
- 微分方程中摄动的应用扩展至 `[[wiki/sources/spaces-1909-轻微的扰动-摄动法简介-2.md]]`。

## 原文证据锚点
- `ev::1878::摄动法思想`：第1段和第2段关于忽略微小项求近似模型再逐渐累加微小影响的思想陈述。
- `ev::1878::代数方程`：第3段到第5段代数方程 $
arepsilon x^3+x^2=p^2$ 的二阶近似推导和数值验证过程。
