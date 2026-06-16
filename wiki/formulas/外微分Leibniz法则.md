---
type: formula
title: 外微分Leibniz法则
aliases:
- 外微分乘积法则
latex: d(\alpha\land \beta)=d\alpha\land \beta + (-1)^p \alpha\land d\beta
symbol_meanings:
  \alpha, \beta: 微分形式
  d: 外微分算符
standard_notation:
- 'd: 外微分算符'
- '\alpha, \beta: 微分形式'
conditions: "$\alpha$ 为流形上的可微 $p$-形式，$\beta$ 为流形上的可微微分形式。"
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2016-11-05-外微分浅谈-4-微分不微.md
source_ids:
- '4059'
derived_from:
- '[[外微分]]'
appears_in:
- '[[spaces-4059-外微分浅谈-4-微分不微]]'
null_evidence_reason: Staged as draft during compilation.
status: draft
updated: "2026-06-14"
---

## 概述
这是微分形式外积的求导乘积法则（Leibniz 法则）。若 $\alpha$ 是一个微分 $p$ 形式，$\beta$ 是一个微分 $q$ 形式，那么它们的外积 $\alpha \land \beta$ 会构成一个微分 $p+q$ 形式。对其作用外微分算符 $d$，结果不仅包含 $d\alpha \land \beta$ 和 $\alpha \land d\beta$ 两项，还需要考虑到外代数的严格反对称性。

根据外微分的定义，算符 $d$ 形式上与普通的微分算符一致，它允许我们从一个微分 $p$ 形式产生一个微分 $p+1$ 形式（本质上是对系数求偏导后附加一个新的基 $dx^{\mu_{p+1}}$ 并与原形式做外积）。当外微分算符 $d$ 作用在乘积 $\alpha \land \beta$ 的第二部分 $\beta$ 上时，相当于微分算符带来的新的基元跨越了 $p$-形式 $\alpha$ 中的 $p$ 个基元。由于外积基底满足反对称关系（如 $dx^\mu \land dx^\nu = - dx^\nu \land dx^\mu$），每次交换都会引入一个负号。因此，跨越 $\alpha$ 的 $p$ 个基必然会产生一个 $(-1)^p$ 的正负号因子，从而得到完整的恒等式 $d(\alpha\land \beta)=d\alpha\land \beta + (-1)^p \alpha\land d\beta$。此外，结合此反对称性质，外微分算符还满足幂零性，即对于任意微分形式 $\omega$，均有 $d^2 \omega = 0$。
