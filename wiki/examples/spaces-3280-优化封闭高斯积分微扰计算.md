---
type: example
title: 优化封闭高斯积分微扰计算
article_id: '3280'
article:
- - wiki/sources/spaces-3280-高斯型积分的微扰展开-三.md
section: 更好的参数
claim: 通过二次参数重构优化高斯型积分的指数微扰级数收敛性并作数值逼近
notation_mapping:
  a: 高斯基轴平方系数
  \varepsilon: 高斯型积分指数微扰参数
  \lambda: 引入的最优重参数化二次变换后的小参数
  a_1: 重参数化后的一阶展开修正系数
  a_2: 重参数化后的二阶展开修正系数，被设定为0以达到最优
steps:
- 1. 给定待求积分 \int_{-\infty}^{+\infty} e^{-ax^2-\varepsilon x^4} dx。
- 2. 引入一般的参数二次代换 \varepsilon = b_2 \lambda^2 + b_1 \lambda。
- 3. 将代换输入指数中，写为对 \lambda 的级数展开形式，其对应前三阶系数为 a_1 = \frac{3b_1}{2a}, a_2 = \frac{3(4a^2
  b_2 - 13b_1^2)}{8a^3}。
- 4. 设定最优化条件 a_2 = 0，选取系数 b_1 = 2a, b_2 = 13，即参数变换为 \varepsilon = 13\lambda^2 + 2a\lambda。
- 5. 求解解析出的新参数值 \lambda = \frac{\sqrt{a^2+13\varepsilon}-a}{13}。
- 6. 忽略 \lambda^2 阶以上指数项，直接得出一阶封闭近似 \int e^{-(a+3\lambda)x^2}dx = \sqrt{\frac{\pi}{a+3\lambda}}，代回得出最优封闭公式。
used_concepts:
- '[[高斯型积分微扰技巧]]'
used_formulas:
- '[[高斯积分优化封闭近似公式]]'
used_methods:
- '[[指数变系数展开法]]'
- '[[参数变换微扰法]]'
source_span: ev::3280::优化封闭近似
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2015-04-26-高斯型积分的微扰展开-三.md
source_ids:
- '3280'
status: stable
updated: '2026-06-12'
---

# 优化封闭高斯积分微扰计算

## 问题

源文“更好的参数”一节改进高斯型积分
$$
\int_{-\infty}^{+\infty}e^{-ax^2-\varepsilon x^4}dx
$$
的微扰近似。普通展开在某些参数下误差较大，因此源文尝试通过二次参数变换改善封闭近似。

## 推导

先设一般变换
$$
\varepsilon=b_2\lambda^2+b_1\lambda.
$$
重复前面的匹配过程后得到系数
$$
a_1=\frac{3b_1}{2a},\qquad
a_2=\frac{3(4a^2b_2-13b_1^2)}{8a^3}.
$$
源文取 $b_1=2a,b_2=13$，使 $a_1=3,a_2=0$，即
$$
\varepsilon=13\lambda^2+2a\lambda,\qquad
\lambda=\frac{\sqrt{a^2+13\varepsilon}-a}{13}.
$$
于是积分近似为
$$
\int e^{-ax^2-\varepsilon x^4}dx\approx
\sqrt{\frac{13\pi}{10a+3\sqrt{a^2+13\varepsilon}}}.
$$

## 方法与证据

本例体现“用可调参数重构小参数，使低阶误差项消失”的微扰优化方法。证据锚点为 `ev::3280::优化封闭近似`，源文表格显示在 $a=1,\varepsilon=1$ 时，该式给出 $1.38715$，比旧式 $1.31279$ 更接近精确值 $1.36843$。
