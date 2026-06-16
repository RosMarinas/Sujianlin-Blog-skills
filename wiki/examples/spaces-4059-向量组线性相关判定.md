---
type: example
title: 向量组线性相关判定
article_id: '4059'
article: '[[spaces-4059-外微分浅谈-4-微分不微]]'
section: 立竿见影的应用
claim: 利用微分形式的外积，判定一组多维空间切空间内向量的线性相关性。
notation_mapping:
  \alpha^i: \alpha^i
  dx^\mu: dx^\mu
  \land: \land
steps:
- 1. 给定 $k$ 个 $n$ 维向量，记其分量为 $\alpha^1_\mu, \alpha^2_\mu, \dots, \alpha^k_\mu$。
- "2. 对应构造 1-形式：\n   \\omega^1 = \\alpha^1_\\mu dx^\\mu\n   \\omega^2 = \\alpha^2_\\mu dx^\\mu\n   ...\n   \\omega^k = \\alpha^k_\\mu dx^\\mu"
- "3. 实施微分形式的连环外积运算：\n   I = \\omega^1 \\land \\omega^2 \\land \\dots \\land \\omega^k"
- 4. 进行代数展开与合并。根据外积的性质，若发现任何向量存在线性表出关系（如第一个 1-形式写为其他形式的组合 $\omega^1 = \sum_{i=2}^k
  b_i \omega^i$），则因自身外积零幂性 $\omega^i \land \omega^i = 0$ 导致全部项归零。
- "5. 判定标准：\n   - 若最终外积结果 $I = 0$，则该向量组必线性相关；\n   - 若最终外积结果 $I \\neq 0$，则该向量组必线性无关。"
used_concepts:
- '[[concept::微分形式]]'
- '[[concept::外微分]]'
used_propositions:
- '[[proposition::向量线性相关外积判定]]'
source_span: ev::4059::线性相关判定
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2016-11-05-外微分浅谈-4-微分不微.md
source_ids:
- '4059'
status: draft
updated: '2026-06-12'
---

## 概述
这是一个利用反对称外积判断线性相关性的典型应用。它在形式上将经典的 $n$ 阶行列式判别法（只能针对 $n$ 个 $n$ 维向量）推广到任意 $k$ 个向量，体现了反对称形式代数的简练性与丰富内涵。

## 理论基础：微分形式与外积
在 $n$ 维空间中，任意函数的微分可以写成 $dx^{\mu}$ 的线性组合，这里 $dx^{\mu}$ 扮演了一组基的角色。诸如 $\omega = \alpha_{\mu}dx^{\mu}$ 的式子被称为**微分 1-形式**。

在这组基底 $dx^{\mu}$ 之上，引入具有反对称性的外积运算 $\land$。例如，$dx^{\mu}\land dx^{\nu}$ 是一个新空间的基（即微分 2-形式），并且由于反对称性，对于相同的基必然有 $dx^{\mu} \land dx^{\mu} = 0$，进而推导至对于任意微分 1-形式 $\omega$ 均满足 $\omega \land \omega = 0$。允许 $\land$ 重复执行，我们便可以以此构造出更高阶的微分形式。

## 代数判定原理
常规的行列式法则可以判断 $n$ 个 $n$ 维向量是否线性相关，但如果我们要判断任意 $k$ 个向量 $\alpha_{\mu}^1, \alpha_{\mu}^2, \dots, \alpha_{\mu}^k$ 呢？此时即可借助微分形式的连环外积。

首先，利用基底 $dx^{\mu}$ 依次构造出相应的 $k$ 个微分 1-形式：
$$
\omega^1 = \alpha_{\mu}^1 dx^{\mu}, \quad \omega^2 = \alpha_{\mu}^2 dx^{\mu}, \quad \dots, \quad \omega^k = \alpha_{\mu}^k dx^{\mu}
$$

随后，考察这 $k$ 个 1-形式的连环外积：
$$
I = (\alpha_{\mu}^1 dx^{\mu}) \land (\alpha_{\mu}^2 dx^{\mu}) \land \dots \land (\alpha_{\mu}^k dx^{\mu})
$$

如果这 $k$ 个向量线性相关，意味着其中至少有一个向量能够表示为其余 $k-1$ 个向量的线性组合。不失一般性地，假设第一个向量 $\alpha_{\mu}^1$ 可以写为其余向量的线性组合，即存在常数 $b_i$ 使得：
$$
\alpha_{\mu}^1 = \sum_{i=2}^{k} b_i \alpha_{\mu}^i
$$

在这样的条件下，代入基底，第一个微分 1-形式同样满足完全相同的线性表出关系：
$$
\alpha_{\mu}^1 dx^{\mu} = \sum_{i=2}^{k} b_i \alpha_{\mu}^i dx^{\mu}
$$

将此线性组合代入原连环外积表达式 $I$ 中进行展开。依据外积运算的线性特性与分配律，该式化为多个子项的求和。因为在这个求和表达式中，每一项必定包含形式为 $(\alpha_{\mu}^i dx^{\mu}) \land \dots \land (\alpha_{\mu}^i dx^{\mu})$ 的重复元素。由于外积的反对称性（相同微分形式的外积为 0），展开后的所有子项无可避免地全部归于 0。其逆命题在代数结构上同样成立。

**结论判定：**
因此，我们可以得到一个极其简洁且具有普适性的充要判定条件：$k$ 个向量线性相关，当且仅当它们构造的 1-形式的连环外积等于 0，即：
$$
(\alpha_{\mu}^1 dx^{\mu}) \land (\alpha_{\mu}^2 dx^{\mu}) \land \dots \land (\alpha_{\mu}^k dx^{\mu}) = 0
$$
