---
type: example
title: 求解三次方程微扰近似
article_id: '1878'
article:
- - wiki/sources/spaces-1878-轻微的扰动-摄动法简介-1.md
section: 一、求解方程：\varepsilon x^3+x^2=p^2
claim: 利用一阶/二阶摄动法求解包含小参数的三次代数方程并提供极高精度的解析逼近
notation_mapping:
  \varepsilon: 摄动小参数
  x: 代数方程的真实解
  p: 零阶方程的正实数根基准值
  a_1: 一阶摄动修正系数
  a_2: 二阶摄动修正系数
steps:
- 1. 给定代数方程 \varepsilon x^3+x^2=p^2，令 \varepsilon=0 求得基准精确解为 x=\pm p，取正根 x_0 = p。
- 2. 设定真实解的摄动级数假设为 x = p + a_1 \varepsilon + a_2 \varepsilon^2 + \dots。
- 3. 将级数代回原方程，对 \varepsilon 的各项幂次展开并合并同类项。
- 4. 提取对齐 \varepsilon 阶项系数：(p^3 + 2a_1 p)\varepsilon + (3a_1 p^2 + a_1^2 + 2a_2 p)\varepsilon^2
  = 0。
- 5. 令各阶系数为零，联立方程组求得 a_1 = -p^2/2, a_2 = 5p^3/8。
- 6. 组合得出二阶级数近似解 x = p - \frac{p^2}{2}\varepsilon + \frac{5p^3}{8}\varepsilon^2。
used_concepts:
- '[[摄动法]]'
used_formulas: []
used_methods:
- '[[摄动级数展开法]]'
source_span: ev::1878::代数方程
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2013-01-16-轻微的扰动-摄动法简介-1.md
source_ids:
- '1878'
status: stable
updated: '2026-06-12'
---

# 求解三次方程微扰近似

## 问题

源文用代数方程
$$
\varepsilon x^3+x^2=p^2
$$
介绍摄动法。虽然三次方程有精确求根公式，但源文强调在实用计算中，当 $\varepsilon$ 是小量时，从可精确求解的零阶模型出发更直接。

## 推导

令 $\varepsilon=0$，得到 $x^2=p^2$。以正根 $x=p$ 为基础，设
$$
x=p+a_1\varepsilon+a_2\varepsilon^2+a_3\varepsilon^3+\cdots.
$$
代回原方程并展开到 $\varepsilon^2$，得到系数方程
$$
p^3+2a_1p=0,\qquad 3a_1p^2+a_1^2+2a_2p=0.
$$
解得
$$
a_1=-\frac{p^2}{2},\qquad a_2=\frac{5p^3}{8},
$$
所以近似解为
$$
x=p-\frac{p^2}{2}\varepsilon+\frac{5p^3}{8}\varepsilon^2.
$$

## 方法与证据

本例体现“忽略小参数求零阶解，再按小参数幂级数逐阶配平系数”的摄动流程。证据锚点为 `ev::1878::代数方程`；源文以 $0.1x^3+x^2=1$ 验证，近似值 $0.95625$ 接近精确解 $0.9554\ldots$。
