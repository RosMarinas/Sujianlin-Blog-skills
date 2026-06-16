---
type: example
title: 'spaces-1510: 素数倒数和发散积分放缩'
article_id: '1510'
article:
- - wiki/sources/spaces-1510-素数倒数之和.md
section: '[欧拉数学]素数倒数之和'
claim: 利用级数与无穷乘积收敛性一致引理 $T < e^S$ 对截断素数乘积进行放缩，推导出素数倒数之和的双对数下界估计。
notation_mapping:
  p: p
  q: q
  Q: Q
steps:
- step: 1
  description: 截取不大于 $p$ 的有限素数集，利用等比展开得出其欧拉乘积下界被调和级数截断和控制：$\prod_{q \le p} \frac{q}{q-1}
    > 1 + \frac{1}{2} + \dots + \frac{1}{p} > \ln(p+1)$。
- step: 2
  description: 利用不等式 $\frac{q}{q-1} < 1 + \frac{1}{q-1}$，由于对于素数 $p_n$ 有 $p_n - 1 >
    p_{n-1}$，可将乘积放大为两部分：$\prod_{q \le p} \frac{q}{q-1} < 2 \prod_{q \le p} (1 + \frac{1}{q})$。
- step: 3
  description: 应用级数乘积引理 $T < e^S$，令 $T = \prod_{q \le p} (1+\frac{1}{q})$，$S = Q =
    \sum_{q \le p} \frac{1}{q}$，得到：$\prod_{q \le p} (1+\frac{1}{q}) < e^Q$。
- step: 4
  description: 联立不等式：$\ln(p+1) < 2 \prod_{q \le p} (1+\frac{1}{q}) < 2 e^Q$。
- step: 5
  description: 对两边取自然对数：$\ln \ln (p+1) < \ln 2 + Q \implies Q > \ln \ln (p+1) - \ln
    2$。
used_concepts:
- - - concept::素数
used_formulas:
- - - wiki/formulas/欧拉乘积公式.md
- - - wiki/formulas/素数倒数之和双对数估计.md
used_methods:
- - - method::基于生成函数的欧拉乘积展开
source_span: ev::1510::倒数和发散证明
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2011-11-19-欧拉数学-素数倒数之和.md
source_ids:
- '1510'
status: draft
updated: '2026-06-12'
---

# spaces-1510: 素数倒数和发散积分放缩

本例通过不等式放缩与级数-乘积不等式引理，详细呈现了素数倒数之和发散的双对数估计推导步骤。具体而言，证明过程巧妙结合了黎曼 $\zeta$ 函数在 $s=1$ 时的欧拉乘积公式（“金钥匙”）与基础极限不等式，其核心推导逻辑如下：

首先，引入级数与无穷乘积的收敛性一致引理：对于各项均大于0的无限数列 $a_n$，$\sum_{n=1}^{\infty} a_n$ 与 $\prod_{n=1}^{\infty} (1+a_n)$ 的敛散性互为充分必要条件。记部分和 $S=\sum_{i=1}^n a_i$，部分乘积 $T=\prod_{i=1}^n (1+a_i)$。
一方面，由于代数展开 $(1+a_1)(1+a_2) = 1+a_1+a_2+a_1a_2 > 1+(a_1+a_2)$，依此递推可严谨确立下界 $T > 1+S$。
另一方面，借助平均不等式（AM-GM）$\frac{x_1+x_2+...+x_n}{n} \geq \sqrt[n]{x_1 x_2...x_n}$，可对乘积项提供上限放缩：
$$ T = (1+a_1)(1+a_2)...(1+a_n) \leq \left(\frac{n+a_1+a_2+...+a_n}{n}\right)^n = \left(1+\frac{S}{n}\right)^n $$
根据自然对数底 $e$ 的定义，$\left(1+\frac{S}{n}\right)^n < e^S$。由此构筑了关于 $T$ 的双侧严格限制：
$$ 1+S < T < e^S $$

其次，运用黎曼 $\zeta$ 函数的欧拉乘积展开 $\xi(s)=\prod_p (1-p^{-s})^{-1}$，提取 $s=1$ 时的情形，将其截断至不大于 $p$ 的素数，利用几何级数（等比数列）展开：
$$ \prod_{q \le p} \frac{q}{q-1} = \left(1+\frac{1}{2}+\frac{1}{2^2}+...\right)\left(1+\frac{1}{3}+\frac{1}{3^2}+...\right)...\left(1+\frac{1}{p}+\frac{1}{p^2}+...\right) $$
这一无穷乘积的展开结果包含了所有素因子不大于 $p$ 的正整数倒数，因而在项集上必然覆盖前 $p$ 个自然数的倒数之和：
$$ = 1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+...+\frac{1}{p}+... > 1+\frac{1}{2}+\frac{1}{3}+...+\frac{1}{p} $$
通过调和级数放缩，这部分和严格大于 $\ln(p+1)$。

接着，为了使乘积项符合 $\prod (1+a_n)$ 格式以应用前述引理，引入素数序列的性质：设第 $n$ 个素数为 $p_n$，通过素数间距的递增性可证 $\frac{p_n}{p_n-1} < 1+\frac{1}{p_{n-1}}$。利用此不等式对截断的欧拉乘积放缩并提出 $p_1=2$ 的常数因子项（即 $\frac{2}{2-1}=2$）：
$$ \prod_{q \le p} \frac{q}{q-1} < 2\left(1+\frac{1}{2}\right)\left(1+\frac{1}{3}\right)\left(1+\frac{1}{5}\right)...\left(1+\frac{1}{p}\right) $$

最后，将收敛性引理的结论代入其中。令倒数之和 $Q = \frac{1}{2}+\frac{1}{3}+\frac{1}{5}+...+\frac{1}{p}$（对应 $S$），由引理可知乘积部分必小于 $e^Q$。将所有推导所得的不等关系合体连结：
$$ \ln(p+1) < \prod_{q \le p} \frac{q}{q-1} < 2\prod_{q \le p} \left(1+\frac{1}{q}\right) < 2e^Q $$
两端取自然对数运算，即分离出素数倒数和 $Q$ 的下界：
$$ Q > \ln \ln(p+1) - \ln 2 $$
鉴于素数个数不仅无穷且单调递增，随着界限 $p \to \infty$，对数复合项 $\ln\ln(p+1)$ 同样发散至无穷大，这严格地证实了素数倒数和发散的结论。而且根据文中结论，$e^S$ 作为 $T$ 的优良近似，从本质上反映出 $\ln \ln p$ 是目标和 $Q$ 的高度契合的渐近近似估计。
