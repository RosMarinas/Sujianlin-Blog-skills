---
type: concept
title: Riccati方程
aliases:
- Riccati Equation
- 黎卡提方程
definition: 形如 a'(x) - a^2(x) = g(x) 的一阶非线性微分方程，与二阶线性变系数微分方程具有等价性，常在二阶变系数常微分方程算子分解时出现。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2012-11-30-算子与线性常微分方程-下.md
source_ids:
- '1794'
prerequisites:
- '[[算子法求解线性常微分方程]]'
equivalent_forms: []
direct_consequences:
- '[[算子分解法]]'
related_formulas: []
related_methods:
- '[[算子分解法]]'
series:
- '[[算子与线性常微分方程系列]]'
evidence_spans:
- ev::1794::变系数分解困难
status: draft
updated: '2026-06-12'
---

# Riccati方程

Riccati方程是一类经典的一阶非线性常微分方程，形如：
$$a'(x) - a^2(x) = g(x)$$

在试图将变系数线性微分算子进行分解时：
$$D^2 + g(x) = (D - a(x))(D + a(x))$$

由于算子的不可交换性，有对易关系：
$$(D - a(x))(D + a(x)) = D^2 - a^2(x) + a'(x)$$

对齐系数后，算子分解成功的条件是满足 Riccati 方程。引入代换：
$$a(x) = -\frac{u'}{u}$$

该非线性一阶方程可以转化为二阶线性常微分方程：
$$u'' + g(x)u = 0$$

这表明求解 Riccati 方程特解与求解原二阶线性微分方程在难度上是完全等价的，形成了分解上的闭环。