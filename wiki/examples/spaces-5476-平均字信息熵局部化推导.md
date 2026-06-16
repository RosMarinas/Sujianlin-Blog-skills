---
type: example
title: spaces-5476-平均字信息熵局部化推导
aliases:
- 合并判据推导
article_id: '5476'
article:
- - spaces-5476-最小熵原理-二-当机立断-之词库构建
section: 套路之行，始于局部
claim: 合并相邻元素 $a,b$ 后平均字信息熵 $\mathcal{L}$ 的变化量 $\Delta\mathcal{L} = -\mathcal{F}_{ab}/l$，其中
  $\mathcal{F}_{ab}$ 可近似为 $p_{ab}(PMI(a,b)-1)$。
notation_mapping:
  p_i: 元素i的频率
  l_i: 元素i的字数
  \mathcal{H}: 未合并时的平均元素信息量
  l: 未合并时的平均元素字数
  \mathcal{L}: 平均字信息熵 = \mathcal{H}/l
steps:
- 定义当前平均字信息熵 $\mathcal{L} = \mathcal{H}/l = (-\sum_i p_i\log p_i)/(\sum_i p_i l_i)$
- 合并相邻元素 $a,b$ 后，总频数变为 $\tilde{N} = N - N_{ab}$
- 重新估计合并后的概率 $\tilde{p}_{ab}, \tilde{p}_a, \tilde{p}_b$
- 计算合并后的 $\tilde{\mathcal{H}}$ 和 $\tilde{l}$，发现 $\tilde{l} = l/(1-p_{ab})$
- 计算 $\tilde{\mathcal{H}}/\tilde{l} - \mathcal{H}/l = -\mathcal{F}_{ab}/l$
- 对 $\mathcal{F}_{ab}$ 在 $p_{ab} \ll p_a, p_b$ 下泰勒展开
- 得到近似 $F_{ab}^* = p_{ab}(\ln(p_{ab}/(p_a p_b)) - 1)$
used_concepts:
- - - 信息熵
- - - 最小熵原理
- - - 点互信息PMI
used_formulas:
- - - 最小熵原理公式
- - - 互信息词边界发现公式
used_methods:
- - - 用互信息发现词语边界
problem_pattern:
- - 用互信息发现词语边界
source_span: ev::5476::互信息近似
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-04-24-最小熵原理-二-当机立断-之词库构建.md
source_ids:
- '5476'
status: draft
updated: '2026-06-12'
---

# 平均字信息熵局部化推导

该推导是文章2的核心技术贡献：展示了如何从全局熵目标 $\mathcal{L}$ 出发，通过局部化分析导出可计算的合并判据。

## 详细推导过程

假设目前$i$的频数为$N_i$，总频数为$N$，那么可以估算$p_i=N_i/N$，假设$i$的字数为$l_i$，那么就可以算出当前的
$$
\mathcal{L}=\frac{\mathcal{H}}{l}=\frac{-\sum\limits_i p_i\log p_i}{\sum\limits_i p_i l_i}\tag{2.8}
$$
如果将两个相邻的$a,b$合并成一项呢？假设$(a,b)$的频数为$N_{ab}$，那么在合并前可以估计$p_{ab}=N_{ab}/N$。如果将它们合并为一个“词”来看待，那么总频数实际上是下降了，变为$\tilde{N}=N-N_{ab}$，而$\tilde{N}_a=N_a-N_{ab}$，$\tilde{N}_b = N_b-N_{ab}$，其他频数不变，因此我们就可以重新估计各个频率
$$
\begin{aligned}\tilde{p}_{ab}=&\frac{N_{ab}}{\tilde{N}}=\frac{p_{ab}}{1-p_{ab}}\\
\tilde{p}_{a}=&\frac{\tilde{N}_{a}}{\tilde{N}}=\frac{p_a - p_{ab}}{1-p_{ab}},\,\tilde{p}_{b}=\frac{\tilde{N}_{b}}{\tilde{N}}=\frac{p_b - p_{ab}}{1-p_{ab}}\\
\tilde{p}_{i}=&\frac{N_{i}}{\tilde{N}}=\frac{p_i}{1-p_{ab}},\, (i\neq a,b)
\end{aligned}\tag{2.9}
$$
于是
$$
\begin{aligned}\tilde{\mathcal{H}}=&-\frac{1}{1-p_{ab}}\Bigg\{p_{ab}\log\Big(\frac{p_{ab}}{1-p_{ab}}\Big) + \\
&\qquad \sum_{i=a,b}(p_i - p_{ab})\log\Big(\frac{p_i - p_{ab}}{1-p_{ab}}\Big)+\sum_{i\neq a,b} p_i\log \Big(\frac{p_i}{1-p_{ab}}\Big)\Bigg\}\\
=&\frac{1}{1-p_{ab}}(\mathcal{H}-\mathcal{F}_{ab})\end{aligned}\tag{2.10}
$$
其中
$$
\begin{aligned}\mathcal{F}_{ab}= &p_{ab}\log \frac{p_{ab}}{p_a p_b} -(1-p_{ab})\log(1-p_{ab}) \\
&+ \sum_{i=a,b}(p_i-p_{ab})\log\Big(1-\frac{p_{ab}}{p_i}\Big)\end{aligned}\tag{2.11}
$$
而
$$
\begin{aligned}\tilde{l}=&\frac{p_{ab}}{1-p_{ab}}(l_a + l_b) + \sum_{i=a,b}\frac{p_i - p_{ab}}{1-p_{ab}}l_i + \sum_{i\neq a,b} \frac{p_i}{1-p_{ab}} l_i\\
=&\frac{l}{1-p_{ab}}
\end{aligned}\tag{2.12}
$$
因此
$$
\frac{\tilde{\mathcal{H}}}{\tilde{l}}-\frac{\mathcal{H}}{l}=-\frac{\mathcal{F}_{ab}}{l}\tag{2.13}
$$
我们的目的是让$\tilde{\mathcal{H}}/\tilde{l}$变小，所以很明显，一个好的“套路”应该要使得$\mathcal{F}_{ab} \gg 0$。

### 简明优美的近似

$\mathcal{F}_{ab}$的表达式过于复杂，以至于难以发现出规律来，我们可以做一些近似。$p_{ab} \leq p_a, p_b$总是成立的，而很多时候甚至可以认为$p_{ab}\ll p_a,p_b$，这样一来在使用自然对数时就有
$$
\begin{aligned}&\ln(1-p_{ab})\approx -p_{ab}\\
&\ln\Big(1-\frac{p_{ab}}{p_i}\Big)\approx -\frac{p_{ab}}{p_i}\end{aligned}\tag{2.14}
$$
因为这个近似的条件是要使用自然对数（$\ln(1+x)\approx x$），所以我们将下面的$\log$全部改为自然对数$\ln$。代入$\mathcal{F}_{ab}$的表达式并去掉$p_{ab}$的二次以上的项，得到
$$
\mathcal{F}_{ab}\approx F_{ab}^*=p_{ab} \left(\ln \frac{p_{ab}}{p_{a} p_{b}}-1\right)\tag{2.15}
$$
这个指标就比较简明漂亮了，其中$PMI(a, b)=\ln\frac{p_{ab}}{p_{a} p_{b}}$我们称之为点互信息。

> 利用泰勒级数，可以得到更一般的展开式为
> 
> $$
> \mathcal{F}_{ab} = p_{ab} \left(\ln \frac{p_{ab}}{p_{a} p_{b}}-1\right)+\frac{1}{2}\left(\frac{1}{p_a}+\frac{1}{p_b}-1\right)p_{ab}^2+\dots
> $$
> 
> 可见（也可以严格证明）$F_{ab}^*$的近似总是小于$\mathcal{F}_{ab}$的真实值，因此$F_{ab}^* = p_{ab} \left(\ln \frac{p_{ab}}{p_{a} p_{b}}-1\right)\gg 0$其实是$\mathcal{F}_{ab}\gg 0$的一个充分条件。
