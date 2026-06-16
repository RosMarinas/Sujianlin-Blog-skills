---
type: formula
title: Fokker-Planck方程和连续性方程公式
aliases:
- FP equation
- Continuity equation
standard_notation: Fokker-Planck方程和连续性方程公式
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2023-02-11-测试函数法推导连续性方程和Fokker-Planck方程.md
source_ids:
- '9461'
evidence_spans: []
latex: \frac{\partial p_t(\boldsymbol{x})}{\partial t} = -\nabla_{\boldsymbol{x}}\cdot\big(p_t(\boldsymbol{x})\boldsymbol{f}_t(\boldsymbol{x})\big)
symbol_meanings:
  p_t(\boldsymbol{x}): 时刻 $t$ 的概率密度函数
  \boldsymbol{x}: 空间变量
  t: 时间变量
  \boldsymbol{f}_t(\boldsymbol{x}): SDE/ODE 在时刻 $t$ 的漂移项
  \nabla_{\boldsymbol{x}} \cdot: 关于 $\boldsymbol{x}$ 的散度算子
conditions: （待从源文章提取）
appears_in:
- '9461'
---
## 概述

（待补充）



## 连续性方程（ODE）

$$
\frac{\partial p_t(\boldsymbol{x})}{\partial t} = -\nabla_{\boldsymbol{x}}\cdot\big(p_t(\boldsymbol{x})\boldsymbol{f}_t(\boldsymbol{x})\big)
$$

## Fokker-Planck方程（SDE）

$$
\frac{\partial p_t(\boldsymbol{x})}{\partial t} = -\nabla_{\boldsymbol{x}}\cdot\big(p_t(\boldsymbol{x})\boldsymbol{f}_t(\boldsymbol{x})\big)+\frac{1}{2}g_t^2 \nabla^2 p_t(\boldsymbol{x})
$$

## 高维分部积分

$$
\int_{\Omega}\boldsymbol{v}\cdot\nabla u\, d\boldsymbol{x} = \int_{\partial\Omega}u\boldsymbol{v}\cdot\hat{\boldsymbol{n}}\,dS - \int_{\Omega}u\nabla\cdot\boldsymbol{v}\, d\boldsymbol{x}
$$

无穷远边界消失时：$\int \boldsymbol{v}\cdot\nabla p\, d\boldsymbol{x} = -\int p\nabla\cdot\boldsymbol{v}\, d\boldsymbol{x}$

## 所属系列

[[随机过程]] — [[偏微分方程]]