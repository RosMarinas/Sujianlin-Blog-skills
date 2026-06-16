---
type: article_summary
title: 关于“微分”的理解
article_id: "1815"
source_url: https://spaces.ac.cn/archives/1815
date: 2012-12-14
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2012-12-14-关于-微分-的理解.md
series: []
topics: ['[[topic::实分析]]']
concepts: ['[[一阶微分形式不变性]]']
methods: []
problem_patterns: []
evidence_spans: ['ev::1815::微分本质', 'ev::1815::形式不变性']
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-12-14-关于-微分-的理解.md
source_ids:
  - "1815"
status: draft
updated: 2026-06-11
---

## 文章核心问题
厘清高等数学中“微分”概念的物理与数学本质，解答“微分 $dx$ 和 $dy$ 是不是必须很小”等常见直观误区，并解释复合函数微分一阶形式不变性的潜规则。

## 主要结论
微分 $dy$ 被定义为 $dy = f'(x) dx$，其中自变量的微分 $dx$ 恰好等于自变量的增量 $\Delta x$。由于增量 $\Delta x$ 可以是任意大的实数，因此微分 $dy$ 和 $dx$ 在数学定义上不一定很小，可以取任意大值。它在 $\Delta x$ 很小时代表增量的主项（线性逼近）。复合函数中，以不同变量为自变量求微分所得的 $dy$ 之间在形式上保持形式不变性（$dy = f'(u) du$），虽然其具体代数项相差二阶无穷小量，但记号上的省略不会引起混乱。

## 推导结构
1. **微分的定义**：说明 $\Delta y = dy + o(\Delta x) = f'(x) \Delta x + o(\Delta x)$，即微分是增量的线性主项。
2. **误差控制**：引入高阶无穷小项记号 $o(\Delta x)$ 的实际物理意义：存在常数 $k$ 使得误差满足 $|\Delta y - dy| \le k \Delta x^2$。
3. **大小误区澄清**：指出在 $y=x$ 时 $dx = \Delta x$，当 $\Delta x$ 很大时 $dx$ 同样很大，证明 $dy = f'(x) dx$ 也可以任意大。
4. **一阶形式不变性辨析**：分析复合函数 $y=f(g(x))$ 中以 $x$ 为变量的微分 $dy = f'(u)u'dx$ 与以 $u$ 为变量的微分 $dy = f'(u)du$ 的关系，指出它们在记号下的等价性与潜规则。

## 关键公式
- 增量近似: $\Delta y = dy + o(\Delta x) = f'(x) \Delta x + o(\Delta x)$
- 微分形式: $dy = f'(x) dx$

## 体现的方法
无。本文为概念辨析文章。

## 所属系列位置
无。独立数学基本概念辨析。

## 与其他文章的关系
- 增量的线性主项逼近是微积分的核心，这也是 `[[wiki/sources/spaces-1878-轻微的扰动-摄动法简介-1.md]]` 等微扰展开在物理学中将增量取为主项逐步修正的哲学基础。

## 原文证据锚点
- `ev::1815::微分本质`：第3段到第5段说明 $dy=f'(x)dx$ 以及 $dx=\Delta x$ 可以任意大的推导。
- `ev::1815::形式不变性`：第6段到第8段讨论复合函数微分形式不变性矛盾与“潜规则”消解。
