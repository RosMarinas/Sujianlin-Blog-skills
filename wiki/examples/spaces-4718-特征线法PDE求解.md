---
type: example
title: 特征线法PDE求解
aliases: []
article_id: "4718"
article: article::4718
section: 拟线性情形
claim: "特征线法将一阶PDE转化为常微分方程组求解，以ut + x*ux = u^2为例展示"
notation_mapping:
  u: 待求解函数
  x: 空间变量
  t: 时间变量
  f(x): 初值函数
steps:
  - "写出特征线方程：dt = dx/x = du/u^2"
  - "求解常微分方程得到参数解 x=C_1 e^t, u=1/(C_2-t)"
  - "代入初始条件 t=0时 u=f(x)，确定常数关系 C_2=1/f(C_1)"
  - "消去常数得到显式解 u = f(xe^{-t})/(1-t f(xe^{-t}))"
used_concepts:
  - "[[特征线法]]"
  - "[[一阶偏微分方程]]"
source_span:
  start: 58
  end: 76
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-12-07-一阶偏微分方程的特征线法.md
source_ids:
  - "4718"
method: "[[特征线法]]"
status: draft
updated: 2026-06-13
---

对于方程 $\partial u/\partial t + x \partial u/\partial x = u^2$ 和初值 $u(x,0)=f(x)$，特征线方程为 $dt = dx/x = du/u^2$，解得 $x=C_1 e^t, u=1/(C_2-t)$。代入初值得 $u = f(xe^{-t})/(1-t f(xe^{-t}))$。这个例子展示了特征线法的完整解题流程：化PDE为ODE，求解代入初值消去参数。
