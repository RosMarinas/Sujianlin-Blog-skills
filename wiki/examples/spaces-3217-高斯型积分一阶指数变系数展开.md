---
type: example
title: 高斯型积分一阶指数变系数展开
article_id: 3217
article: '[[spaces-3217-高斯型积分的微扰展开-一]]'
section: 在指数中展开：一个封闭的解
claim: 通过引入代定系数A重写积分指数，令一阶展开项积分为0解出A，求得封闭解析解
notation_mapping:
  standard_A: A
  source_A: A
steps:
- 1. 将被积项改写为 e^{-Ax^2 - [(a-A)x^2 + eps * x^4]}
- 2. 将扰动中括号项泰勒展开，积分得到 sqrt(pi/A) * [1 - (2A(a-A) + 3*eps)/(4A^2)]
- 3. 令修正分子为零 2A(a-A) + 3*eps = 0
- 4. 解出变分A值 A = (a + sqrt(a^2 + 6*eps)) / 2，求得极高精度的一阶封闭解
used_concepts:
- - - 高斯型积分
- - - 微扰展开
used_formulas: []
used_methods:
- - - 指数系数变易摄动法
source_span: ev::3217::在指数中展开：一个封闭的解
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2015-02-14-高斯型积分的微扰展开-一.md
source_ids:
- 3217
status: draft
updated: '2026-06-12'
---

# 高斯型积分一阶指数变系数展开

在研究费曼的路径积分理论时，通常使用小参数微扰展开的方式逐步逼近传播子。对于含有四次方微扰项的高斯型积分 $\int_{-\infty}^{+\infty} e^{-ax^2-\varepsilon x^4} dx$（更一般地可以写为 $\int_{-\infty}^{+\infty} e^{-ax^2-\varepsilon V(x)} dx$），最简单直接的方法是对微扰项 $e^{-\varepsilon V(x)}$ 进行泰勒级数展开。当 $V(x)=x^4$ 时，直接展开积分后会得到：
$$
\int_{-\infty}^{+\infty} e^{-ax^2-\varepsilon x^4} dx=\sqrt{\frac{\pi}{a}}\left(1-\frac{3\varepsilon}{4a^2}+\frac{105\varepsilon^2}{32a^4}-\frac{3465\varepsilon^3}{128a^6}+\dots\right)
$$
这实际上是一个渐近级数。该级数的严格收敛半径实际上为零，在 $\varepsilon=a^2$ 时便完全失效；且渐近级数的特性决定了取的项越多，有效收敛半径越小。当 $\varepsilon$ 较大或者 $a=0$ 时，这种简单展开法会彻底发散。

为了解决大微扰参数下的发散问题，可以借鉴微分方程摄动展开中对周期进行展开的技巧（即将原来的系数作参数展开）。在积分指数中引入一个待定系数 $A$，将原积分恒等变形为：
$$
\int_{-\infty}^{+\infty} e^{-Ax^2-[(a-A)x^2+\varepsilon x^4]} dx
$$
随后，将方括号中的部分 $[(a-A)x^2+\varepsilon x^4]$ 当作微扰项进行一阶泰勒展开，可以得到近似积分表达式：
$$
\int_{-\infty}^{+\infty} e^{-Ax^2} \left\{1-[(a-A)x^2+\varepsilon x^4]\right\}dx
$$
分别对展开后的各项计算积分，其中修正项的积分为 $\sqrt{\frac{\pi}{A}}\frac{2 A (a-A)+3 \varepsilon}{4 A^2}$。接下来是关键的一步：为了使得该一阶修正项严格为零，只需选取适当的 $A$ 令其分子 $2 A (a-A)+3 \varepsilon = 0$。求解这个一元二次方程，取使得 $A > 0$ 的根，得到变分系数 $A$ 的解析解：
$$
A = \frac{1}{2} \left(a+\sqrt{a^2+6 \varepsilon}\right)
$$
因此，原积分的一阶封闭解析近似解可以表示为 $\sqrt{\frac{\pi}{A}} = \sqrt{\frac{2\pi}{a+\sqrt{a^2+6 \varepsilon}}}$。这种“指数系数变易”摄动法构建的封闭解具有极高的精度。

即使在最极端的无高斯主导项情况 $a=0$ 下，该近似不仅能够正常计算，且算出的尺度 $\sqrt{\frac{2\pi}{\sqrt{6\varepsilon}}}$ 也准确反映了精确解随 $\varepsilon$ 呈现 $\varepsilon^{-1/4}$ 衰减的正确物理行为（精确值就是一个常数乘上 $1/\varepsilon^{1/4}$ 的形式）。在 $\varepsilon \to +\infty$ 时，近似解也能正确给出积分值为 $0$ 的极限，而直接展开的渐近级数此时再次完全失效。

数值比较进一步证实了这种方法的优异表现。例如在 $\varepsilon=1, a=10$ 时，精确值为 $0.556466$；而在 $\varepsilon=0.1, a=1$（精确值 $1.67409$）、$\varepsilon=1, a=1$（精确值 $1.36843$）以及 $\varepsilon=1, a=0$（精确值 $1.8128$）等情况下，该封闭解算出的值在所有场合都显著优于简单展开的一阶近似 $\sqrt{\frac{\pi}{a}}\left(1-\frac{3\varepsilon}{4a^2}\right)$，有时甚至比简单展开的高阶近似还要好，彻底克服了简单展开法的发散缺陷。
