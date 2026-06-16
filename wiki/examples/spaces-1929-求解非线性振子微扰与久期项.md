---
type: example
title: 求解非线性振子微扰与久期项
article_id: '1929'
article:
- - wiki/sources/spaces-1929-轻微的扰动-摄动法简介-3.md
section: E.g.2 小参数的展开
claim: 通过小参数摄动法将非线性二阶常微分方程线性化，并展示解中产生的长期项（久期项）现象
notation_mapping:
  \varepsilon: 扰动小参数
  x: 振子的位移函数
  t: 时间自变量
  x_0: 无微扰零阶谐振子解
  x_1: 一阶微扰位移修正函数
  x_2: 二阶微扰位移修正函数，包含久期项
steps:
- 1. 给定非线性振子方程 x'' + x = \varepsilon x^2 且满足初始值条件 x(0)=1, x'(0)=0。
- 2. 假设摄动级数解形式为 x(t) = x_0(t) + \varepsilon x_1(t) + \varepsilon^2 x_2(t) + \dots。
- 3. 代入微分方程并合并同类项，得到递推线性方程序列。
- 4. 解无摄动方程 x_0'' + x_0 = 0, x_0(0)=1, x_0'(0)=0，求得 x_0(t) = \cos t。
- 5. 解一阶修正方程 x_1'' + x_1 - x_0^2 = 0 \implies x_1'' + x_1 = \cos^2 t，且 x_1(0)=x_1'(0)=0，解得
  x_1(t) = \frac{1}{6}(3 - 2\cos t - \cos 2t)。
- 6. 解二阶修正方程 x_2'' + x_2 - 2x_0 x_1 = 0，初始值全为 0。代入已解项展开，解得 x_2(t) = \frac{1}{144}(-48
  + 29\cos t + 16\cos 2t + 3\cos 3t + 60t\sin t)。
- 7. 识别其中的长期项（久期项）为 60t\sin t，当 t \to \infty 时发散，表明级数解在此发散。
used_concepts:
- '[[摄动法]]'
- '[[长期项]]'
used_formulas: []
used_methods:
- '[[摄动级数展开法]]'
source_span: ev::1929::小参数展开
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2013-03-07-轻微的扰动-摄动法简介-3.md
source_ids:
- '1929'
status: stable
updated: '2026-06-12'
---

# 求解非线性振子微扰与久期项

## 问题

源文“E.g.2 小参数的展开”求解非线性振子
$$
x''+x=\varepsilon x^2,\qquad x(0)=1,\quad x'(0)=0.
$$
目标是把非线性方程转成按小参数 $\varepsilon$ 分层的线性方程。

## 推导

当 $\varepsilon=0$ 时，零阶解为 $x_0(t)=\cos t$。源文设
$$
x(t)=x_0(t)+\varepsilon x_1(t)+\varepsilon^2x_2(t)+\cdots,
$$
代回原方程并按 $\varepsilon$ 幂次收集，得到
$$
x_0''+x_0=0,\quad x_1''+x_1-x_0^2=0,\quad x_2''+x_2-2x_0x_1=0,\ldots
$$
在初值 $x_i(0)=x_i'(0)=0$ 下依次求解：
$$
x_1(t)=\frac{1}{6}(3-2\cos t-\cos2t),
$$
$$
x_2(t)=\frac{1}{144}(-48+29\cos t+16\cos2t+3\cos3t+60t\sin t).
$$

## 方法与证据

本例体现“按小参数展开，把非线性微分方程化为无穷多个线性微分方程”的摄动方法。证据锚点为 `ev::1929::小参数展开`；源文特别指出 $t\sin t$ 是长期项/久期项，说明常规摄动解在长时间尺度上会暴露缺陷。
