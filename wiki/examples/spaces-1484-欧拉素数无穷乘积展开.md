---
type: example
title: 'spaces-1484: 欧拉素数无穷乘积展开'
article_id: '1484'
article:
- - wiki/sources/spaces-1484-素数无穷两个证明.md
section: 二、欧拉经典
claim: 全体素数等比级数的乘积恰好等于全体自然数倒数构成的调和级数。
notation_mapping:
  p: p
  S(p): S(p)
  K: K
steps:
- step: 1
  description: 建立单个素数 $p$ 的等比累加和，并化简为闭式：$S(p) = 1 + p^{-1} + p^{-2} + \dots = \frac{1}{1-p^{-1}}$。
- step: 2
  description: 构造所有素数 $p \in \{2, 3, 5, 7, \dots\}$ 的乘积项：$K = S(2) \cdot S(3) \cdot
    S(5) \dots = (1+\frac{1}{2}+\frac{1}{4}+\dots)(1+\frac{1}{3}+\frac{1}{9}+\dots)(1+\frac{1}{5}+\dots)\dots$。
- step: 3
  description: 展开所有括号。每一项都具有形式 $\frac{1}{2^a 3^b 5^c \dots}$，对应某一自然数的唯一分解质因数负幂次。
- step: 4
  description: 根据算术基本定理的唯一分解性，这一展开必然产生全体自然数倒数各一次且仅一次：$K = 1 + \frac{1}{2} + \frac{1}{3}
    + \frac{1}{4} + \dots$。
used_concepts:
- - - concept::素数
used_formulas:
- - - wiki/formulas/等比级数求和公式.md
used_methods:
- - - method::基于生成函数的欧拉乘积展开
source_span: ev::1484::欧拉证明
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2011-10-02-欧拉数学-素数有无穷多个的两个证明.md
source_ids:
- '1484'
status: draft
updated: '2026-06-12'
---

# spaces-1484: 欧拉素数无穷乘积展开

本例展示了欧拉基于生成函数技巧与无穷等比数列展开，将所有素数幂次乘积与调和级数相互联系起来，从而借助级数发散的性质反证素数无穷多个的经典推导步骤。

首先，对于任意给定的素数 $p$（满足 $|p| > 1$），可以构造一个无穷等比数列，并利用等比数列的求和公式得到其闭式解：
$$
S(p) = \sum_{n=0}^{\infty} p^{-n} = 1 + p^{-1} + p^{-2} + \dots = \frac{1}{1-p^{-1}} = \frac{p}{p-1}
$$

接着，将所有素数 $p \in \{2, 3, 5, 7, \dots\}$ 对应的等比级数 $S(p)$ 全部相乘，并记这个无穷连乘积为 $K$：
$$
\begin{aligned}
K &= S(2)\cdot S(3)\cdot S(5)\dots \\
  &= \left(1+\frac{1}{2}+\frac{1}{2^2}+\frac{1}{2^3}\dots\right)\left(1+\frac{1}{3}+\frac{1}{3^2}+\frac{1}{3^3}\dots\right)\left(1+\frac{1}{5}+\frac{1}{5^2}+\dots\right)\dots \\
  &= \frac{2}{2-1}\cdot \frac{3}{3-1}\cdot \frac{5}{5-1}\cdot \dots
\end{aligned}
$$

由于在展开这无数个括号的乘积时，每一项都具有 $\frac{1}{p_1^{a_1} p_2^{a_2} \dots}$ 的形式。根据算术基本定理的唯一分解性，任意自然数都可以唯一地分解为若干个素数幂的乘积。这意味着这一展开项完美地再现了自然数的产生过程，恰好构成了全体自然数倒数各一次且仅一次的和，也就是熟知的调和级数：
$$
K = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \dots
$$

微积分的知识告诉我们，调和级数 $1+\frac{1}{2}+\frac{1}{3}+\dots$ 是发散的（即无穷大）。因此，若素数只有有限个，则前面的乘积式 $K = \frac{2}{2-1}\cdot \frac{3}{3-1}\cdot \dots$ 必然是一个有限的确定数值，这就导致了左侧为有限值、右侧为无穷大的矛盾。由此，欧拉严密且极具美感地证明了素数必定有无穷多个。
