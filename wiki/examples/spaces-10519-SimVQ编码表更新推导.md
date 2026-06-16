---
type: example
title: spaces-10519-SimVQ编码表更新推导
article_id: 10519
article:
- - spaces-10519-给编码表加线性变换
section: 分析
claim: 通过将编码表向量 e_i 参数化为 q_i * W，在 SGD 更新下，即使编码没有被当前 batch 选中，其也会通过共享矩阵 W 获得梯度协同更新
notation_mapping:
  e_i: e_i (传统编码表向量)
  q_i: q_i (SimVQ 的固定随机初始向量)
  W: W (可学习的共享基底变换矩阵)
steps:
- 在时间步 t，设置当前的 VQ 编码表示为 e_i^(t) = q_i^(t) * W^(t)
- 写出关于 W 和 q_i 的一阶偏导关系： dL/dq_i = dL/de_i * W^T, dL/dW = sum_i q_i^T * dL/de_i
- 在 SGD 更新下写出权重 W 的时间步演化： W^(t+1) = W^(t) - eta * sum_i q_i^T * dL/de_i
- 将 W^(t+1) 代回编码向量的表示式中进行展开化简： e_i^(t+1) approx e_i^(t) - eta * (dL/de_i * W^T * W
  + q_i * sum_j q_j^T * dL/de_j)
- 观察更新项，第一部分为当前特征的传统梯度投影；第二部分为全体被选中编码梯度的加和投影，从而实现了编码的梯度联动更新
used_concepts:
- - - 过参数化
- - - SimVQ
used_methods:
- - - 编码表线性变换过参数化法
source_span: ev::10519::分析
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-11-06-VQ的又一技巧-给编码表加一个线性变换.md
source_ids:
- 10519
status: stable
updated: '2026-06-12'
---

## 问题

源文“分析”一节解释 SimVQ 为什么只在编码表后乘一个线性变换 $W$，就能改变 VQ 编码表的优化动力学，并提高编码利用率。

## 推导

普通 VQ 中，若编码 $e_i$ 当前批次没有被选中，则 $\partial\mathcal{L}/\partial e_i^{(t)}=0$，它在 SGD 下不更新。SimVQ 把编码参数化为 $e_i=q_iW$，于是
$$
q_i^{(t+1)}=q_i^{(t)}-\eta\frac{\partial\mathcal{L}}{\partial e_i^{(t)}}W^{(t)\top},
$$
$$
W^{(t+1)}=W^{(t)}-\eta\sum_iq_i^{(t)\top}\frac{\partial\mathcal{L}}{\partial e_i^{(t)}}.
$$
展开 $e_i^{(t+1)}=q_i^{(t+1)}W^{(t+1)}$ 后，源文指出其中含有
$$
q_i^{(t)}\sum_iq_i^{(t)\top}\frac{\partial\mathcal{L}}{\partial e_i^{(t)}},
$$
所以即使某个 $i$ 没被当前 batch 选中，它仍会因共享矩阵 $W$ 的更新获得近似非零的联动更新。

## 方法与证据

本例体现“过参数化不改变表达能力，但改变梯度耦合结构”的方法。证据锚点为 `ev::10519::分析`，源文还说明 SimVQ 默认只更新 $W$、冻结随机初始化的 $q$，以降低编码表坍缩风险。
