---
type: example
title: spaces-5655-SGD到SDE噪声近似
aliases: []
article_id: '5655'
article:
- - 从动力学角度看优化算法（一）：从SGD到动量加速
section: 从SGD到SDE
claim: SGD 可通过引入随机噪声从 ODE 近似为 SDE。
notation_mapping:
  theta_t: boldsymbol{theta}
  sigma: source-local noise coefficient
  B_t: Gaussian noise limit
steps:
- 把小批量梯度看成全量梯度加误差
- 用高斯噪声近似误差
- 在连续时间极限中写成 SDE
- 用平衡分布解释学习率与 Batch Size 启发
used_concepts:
- - - SGD-SDE近似
- - - 优化动力学视角
used_formulas:
- - - SGD-SDE近似公式
used_methods:
- - - 把优化算法解释为动力系统离散化
problem_pattern:
- - 把优化器经验现象改写为动力系统问题
source_span: ev::5655::从SGD到SDE
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
source_ids:
- '5655'
status: stable
updated: '2026-06-12'
---

# spaces-5655-SGD到SDE噪声近似

## 所在文章

[[从动力学角度看优化算法（一）：从SGD到动量加速]]

## 原始问题

SGD 可通过引入随机噪声从 ODE 近似为 SDE。

## 推导步骤

1. 把小批量梯度看成全量梯度加误差
2. 用高斯噪声近似误差
3. 在连续时间极限中写成 SDE
4. 用平衡分布解释学习率与 Batch Size 启发

## 证据锚点

- `ev::5655::从SGD到SDE`