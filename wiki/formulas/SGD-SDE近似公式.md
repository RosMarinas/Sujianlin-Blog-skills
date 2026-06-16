---

type: formula
title: SGD-SDE近似公式
aliases: []
latex: d\boldsymbol{\theta}_t=-\nabla L(\boldsymbol{\theta}_t)dt+\sigma(\boldsymbol{\theta}_t)d\boldsymbol{B}_t
symbol_meanings:
  \boldsymbol{\theta}_t: 连续时间参数轨迹
  L(\boldsymbol{\theta}_t): 全量损失函数
  \sigma(\boldsymbol{\theta}_t): 小批量梯度噪声尺度
  \boldsymbol{B}_t: 布朗运动噪声项
standard_notation:
  theta_t: 随机参数轨迹
  sigma: 噪声强度
  B_t: 布朗运动
conditions:
- 把小批量梯度噪声近似为高斯扩散项。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
source_ids:
- '5655'
derived_from: []
implies: []
appears_in:
- - - 从动力学角度看优化算法（一）：从SGD到动量加速
evidence_spans:
- ev::5655::从SGD到SDE
status: draft
updated: '2026-06-14'
---


# SGD-SDE近似公式


## 概述

（待补充）

## 公式

```tex
d\boldsymbol{\theta}_t=-\nabla L(\boldsymbol{\theta}_t)dt+\sigma(\boldsymbol{\theta}_t)d\boldsymbol{B}_t
```

## 条件

- 把小批量梯度噪声近似为高斯扩散项。

## 符号与条件

$\boldsymbol{\theta}_t$ 是连续时间参数轨迹，$L$ 是全量损失，$\boldsymbol{B}_t$ 表示布朗运动噪声项，$\sigma(\boldsymbol{\theta}_t)$ 表示噪声尺度。frontmatter 中的公式是源文半定性 SDE 写法的标准化版本；源文原式先假设小批量梯度与全量梯度的差 $\boldsymbol{\xi}_n$ 服从方差为 $\sigma^2$ 的正态分布，再把确定性 ODE 改写为
$$
\dot{\boldsymbol{\theta}}=-\nabla_{\boldsymbol{\theta}}L(\boldsymbol{\theta})+\sigma\boldsymbol{\xi}.
$$

## 用途

该近似用于解释 SGD 相比 GD 多出的随机性。源文指出原来的 ODE 解是一条确定轨线，加入高斯噪声后变为 SDE，平衡态概率近似满足 $P(\boldsymbol{\theta})\sim\exp(-L(\boldsymbol{\theta})/\sigma^2)$。因此它服务于从动力学角度理解 SGD 的收敛与噪声效应。

## 证据

- `ev::5655::从SGD到SDE`
