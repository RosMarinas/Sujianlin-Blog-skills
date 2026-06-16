---
type: example
title: 对角微扰化简抛物型二次曲线
article_id: '1841'
article:
- - wiki/sources/spaces-1841-矩阵化简二次型-无穷小近似处理抛物型.md
section: 2、抛物型
claim: 通过引入小参数对角微扰 \bar{A} = A + \varepsilon I 统一化简奇异的二次曲线矩阵
notation_mapping:
  A: 二次型对称系数矩阵
  \varepsilon: 引入的对角正则化微扰小参数
  \bar{A}: 微扰后的正则化可逆矩阵
  x_0: 依赖微扰参数的带参平移中心
steps:
- 1. 给定二次曲线 x^2-4xy+4y^2+2x-2y-1=0，提取系数矩阵 A=[ [1, -2], [-2, 4] ]，一次项 b=[1, -1]^T，常数
  c=-1。
- 2. 求解 A 的特征值为 0 和 5。因为包含零特征值，矩阵不可逆，无法直接用常规中心公式。
- 3. 引入对角微扰矩阵 \bar{A} = A + \varepsilon I = [ [1+\varepsilon, -2], [-2, 4+\varepsilon]
  ]。
- 4. 求解微扰矩阵的逆：\bar{A}^{-1} \approx \frac{1}{5\varepsilon}[ [4, 2], [2, 1] ] （保留至 1/\varepsilon
  阶）。
- 5. 计算带参平移中心：x_0 = \bar{A}^{-1}b = \frac{1}{5\varepsilon}[2, 1]^T。
- 6. 计算带参标准常数：k = x_0^T b - c = \frac{1}{5\varepsilon} + 1。
- 7. 写出对角化变形等效方程：\varepsilon Y^2 + 5X^2 - (\frac{1}{5\varepsilon} + 1) = 0。
- 8. 对微扰平方项进行配方并取 \varepsilon \to 0$极限，消去发散项，还原为标准抛物线方程 5X^2 \pm 2\sqrt{1/5}Y = 0。
used_concepts:
- '[[二次型化简]]'
used_formulas:
- '[[平面二次型保距平移最简形式公式]]'
used_methods:
- '[[用相似矩阵表达同一线性变换]]'
- '[[奇异矩阵的对角微扰化简法]]'
source_span: ev::1841::对角微扰
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2012-12-25-矩阵化简二次型-无穷小近似处理抛物型.md
source_ids:
- '1841'
status: stable
updated: '2026-06-12'
---

# 对角微扰化简抛物型二次曲线

## 问题

源文在处理二次型
$$
x^T A x+2b^T x+c=0
$$
时，先给出可逆情形的平移量 $x_0=A^{-1}b$。难点是抛物型对应矩阵 $A$ 有零特征根，不能直接求逆。

## 推导

源文把抛物线看作双曲线或椭圆的极限。例如 $2py+x^2=0$ 可看作
$$
2py+x^2+\varepsilon y^2=0,
$$
配方后得到
$$
x^2+\varepsilon\left(y+\frac{p}{\varepsilon}\right)^2-\frac{p^2}{\varepsilon}=0.
$$
一般情况下，做法是在 $A$ 的对角线上加入小偏离，得到可逆矩阵 $\bar{A}$。然后按原步骤计算 $x_0=(\bar{A})^{-1}b$ 和常数项，保留一阶无穷小，再令偏离趋于 0。若有 $k$ 个零根，源文按对角元素依次加入 $\varepsilon_1,\ldots,\varepsilon_k$ 来统一处理高维情形。

## 方法与证据

本例体现“用对角微扰把奇异二次型纳入可逆流程，再取极限恢复抛物项”的方法。证据锚点为 `ev::1841::对角微扰`，源文明确说明这种方式把不可逆的抛物型重新变回原来的对角化步骤。
