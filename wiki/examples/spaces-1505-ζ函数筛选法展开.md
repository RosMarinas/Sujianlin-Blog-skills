---
type: example
title: 'spaces-1505: ζ函数筛选法展开'
article_id: '1505'
article:
- - wiki/sources/spaces-1505-黎曼ζ函数.md
section: 黎曼ζ函数
claim: 采用类似埃氏筛法的方法，通过在黎曼ζ级数中逐步消去素数倍数项，能够导出无穷乘积乘项与级数的恒等关系。
notation_mapping:
  \xi(s): \xi(s)
  s: s
steps:
- step: 1
  description: 写出 $\zeta(s)$ 的狄利克雷级数求和展开式（此处源码中记为 $\xi(s)$）：$\xi(s) = 1 + \frac{1}{2^s}
    + \frac{1}{3^s} + \frac{1}{4^s} + \dots$。
- step: 2
  description: 两边乘以第一个素数项 $2^{-s}$，得到 $\frac{1}{2^s}\xi(s) = \frac{1}{2^s} + \frac{1}{4^s}
    + \frac{1}{6^s} + \dots$。
- step: 3
  description: 将第一步与第二步的式子相减，削去分母为 2 的倍数项：$(1 - \frac{1}{2^s})\xi(s) = 1 + \frac{1}{3^s}
    + \frac{1}{5^s} + \frac{1}{7^s} + \dots$。
- step: 4
  description: 两边乘以第二个素数项的负幂次 $3^{-s}$，得到 $\frac{1}{3^s}(1 - \frac{1}{2^s})\xi(s)
    = \frac{1}{3^s} + \frac{1}{9^s} + \frac{1}{15^s} + \dots$。
- step: 5
  description: 再次相减以消去分母为 3 的倍数项：$(1 - \frac{1}{3^s})(1 - \frac{1}{2^s})\xi(s) = 1
    + \frac{1}{5^s} + \frac{1}{7^s} + \dots$。
- step: 6
  description: 依次遍历对所有质数执行上述消去操作。由于 $s>1$ 使得级数项在大质数处收敛，最终右端仅剩余首项 1，即 $\lim_{p \to
    \infty} \prod_{q \le p} (1 - q^{-s})\xi(s) = 1$。
- step: 7
  description: 移项整理即得到欧拉乘积公式：$\xi(s) = \prod_{p} (1 - p^{-s})^{-1}$。
used_concepts:
- - - concept::黎曼ζ函数
used_formulas:
- - - wiki/formulas/黎曼ζ函数公式.md
- - - wiki/formulas/欧拉乘积公式.md
used_methods:
- - - method::基于生成函数的欧拉乘积展开
source_span: ev::1505::埃氏筛法推导
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2011-11-18-欧拉数学-黎曼ζ函数.md
source_ids:
- '1505'
status: draft
updated: '2026-06-12'
---

# spaces-1505: ζ函数筛选法展开

本例利用了类比数论中埃拉托色尼筛法的代数消去过程，展示了如何从黎曼ζ函数基础的狄利克雷级数求和逐步推导至欧拉无穷乘积表达式（即欧拉积公式，在数论中常被称为“金钥匙”）。

对于黎曼ζ函数的狄利克雷级数形式 $\xi(s) = 1 + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \dots$，首先在等式两边乘以 $\frac{1}{2^s}$，得到 $\frac{1}{2^s} \xi(s) = \frac{1}{2^s} + \frac{1}{4^s} + \frac{1}{6^s} + \dots$。将两式相减后，右侧所有分母为2的倍数的项均被消除，得到 $(1-\frac{1}{2^s})\xi(s) = 1 + \frac{1}{3^s} + \frac{1}{5^s} + \frac{1}{7^s} + \dots$。

接着，在所得等式两边再乘以 $\frac{1}{3^s}$ 并相减，即可进一步消除所有分母为3的倍数的项，得到 $(1-\frac{1}{3^s})(1-\frac{1}{2^s})\xi(s) = 1 + \frac{1}{5^s} + \frac{1}{7^s} + \frac{1}{11^s} + \dots$。通过持续对所有素数 $p$ 重复此筛除过程，右侧的级数项不断向后推移。例如，当处理到素数 $997$ 时，右侧剩余的第一部分将会变为 $1 + \frac{1}{1009^s} + \frac{1}{1013^s} + \dots$。

由于当 $s > 1$ 时原级数是收敛的，随着消去过程涉及的素数趋于无穷大，等式右侧除首项 $1$ 外的其余项之和将逐渐趋近于零。最终我们可以得出恒等式 $\dots(1-\frac{1}{p^s})\dots(1-\frac{1}{3^s})(1-\frac{1}{2^s})\xi(s) = 1$。将其移项整理，便导出了著名的欧拉积公式：$\xi(s) = \prod_p (1-p^{-s})^{-1}$。这一公式深刻揭示了自然数与素数之间的内在联系，为计算所有素数倒数之和发散、任意两个自然数互质的概率等经典数论问题提供了关键性工具。
