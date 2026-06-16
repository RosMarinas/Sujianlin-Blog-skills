---
type: concept
title: SGD-SDE近似
aliases: []
definition: 把 SGD 中的小批量随机误差近似为扩散噪声，从而得到随机微分方程。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
source_ids:
- '5655'
related_methods:
- - - 把优化算法解释为动力系统离散化
series:
- - - 从动力学角度看优化算法
evidence_spans:
- ev::5655::从SGD到SDE
status: draft
updated: '2026-06-12'
---

# SGD-SDE近似

## 定义

把 SGD 中的小批量随机误差近似为扩散噪声，从而得到随机微分方程。

## 激活场景

该概念在需要解释 batch size、随机梯度噪声和优化轨迹时被激活。源文先把全量梯度下降视为 ODE 的欧拉解法，再把 mini-batch 梯度看作全量梯度的随机估计，由估计误差引入噪声项。

## 关键关系

源文记 $L_R(\boldsymbol{\theta})$ 为随机子集上的损失，并假设
$$
\nabla_{\boldsymbol{\theta}}L(\boldsymbol{\theta}_n)-\nabla_{\boldsymbol{\theta}}L_R(\boldsymbol{\theta}_n)=\boldsymbol{\xi}_n
$$
近似服从方差为 $\sigma^2$ 的正态分布。于是 SGD 可被半定性地写为
$$
\dot{\boldsymbol{\theta}}=-\nabla_{\boldsymbol{\theta}}L(\boldsymbol{\theta})+\sigma\boldsymbol{\xi},
$$
即朗之万型 SDE。源文据此解释：batch size 越大，梯度方差越小；噪声越大，参数分布越平缓，更可能在不同区域间游走。

## 证据

- `ev::5655::从SGD到SDE`
