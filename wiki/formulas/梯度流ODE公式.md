---

type: formula
title: 梯度流ODE公式
aliases: []
latex: \dot{\boldsymbol{\theta}}=-\nabla_{\boldsymbol{\theta}}L(\boldsymbol{\theta})
symbol_meanings:
  L: 损失函数
  t: 连续时间
  theta: 参数向量
standard_notation:
  theta: 参数向量
  L: 损失函数
  t: 连续时间
conditions:
- 连续时间近似下的一阶梯度下降动力学。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
- Data/Spaces_ac_cn/markdown/Mathematics/2018-12-20-从动力学角度看优化算法-二-自适应学习率算法.md
- Data/Spaces_ac_cn/markdown/Big-Data/2019-05-03-从动力学角度看优化算法-四-GAN的第三个阶段.md
source_ids:
- '5655'
- '6234'
- '6583'
derived_from: []
implies: []
appears_in:
- - - 从动力学角度看优化算法（一）：从SGD到动量加速
- - - 从动力学角度看优化算法（二）：自适应学习率算法
- - - 从动力学角度看优化算法（四）：GAN的第三个阶段
evidence_spans:
- ev::5655::GD与ODE
- ev::6234::极小值点和ODE
- ev::6583::动力系统
status: draft
updated: "2026-06-14"
---

# 梯度流ODE公式


## 概述

（待补充）

## 公式

```tex
\dot{\boldsymbol{\theta}}=-\nabla_{\boldsymbol{\theta}}L(\boldsymbol{\theta})
```

## 条件

- 连续时间近似下的一阶梯度下降动力学。

## 证据

- `ev::5655::GD与ODE`
- `ev::6234::极小值点和ODE`
- `ev::6583::动力系统`