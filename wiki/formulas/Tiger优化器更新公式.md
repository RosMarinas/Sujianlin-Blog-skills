---
type: formula
title: Tiger优化器更新公式
aliases:
  - Tiger更新公式
latex: |
  \begin{aligned}
  \boldsymbol{m}_t &= \beta \boldsymbol{m}_{t-1} + (1 - \beta) \boldsymbol{g}_t \\
  \boldsymbol{\theta}_t &= \boldsymbol{\theta}_{t-1} - \eta_t \left[\text{sign}(\boldsymbol{m}_t) + \lambda_t \boldsymbol{\theta}_{t-1}\right]
  \end{aligned}
symbol_meanings:
  \boldsymbol{\theta}_t: 第 t 步的模型参数权重向量
  \boldsymbol{g}_t: 第 t 步的损失函数梯度向量
  \boldsymbol{m}_t: 第 t 步的一阶滑动动量缓存
  \eta_t: 第 t 步的相对/自适应全局学习率
  \lambda_t: 第 t 步的权重衰减率，偏置与归一化层通常取 0，Kernel层取常数 0.01
  \beta: 动量滑动衰减率，NLP推荐取 0.965，CV推荐取 0.945
  \text{sign}: 符号函数
standard_notation:
  \boldsymbol{\theta}: 模型参数
  \boldsymbol{m}: 动量向量
  \boldsymbol{g}: 梯度向量
  \text{sign}: 符号函数
conditions: 优化器滑动平均常数统一满足 $\beta_1 = \beta_2 = \beta$；学习率 $\eta_t$ 可以根据网络层 Kernel 的 $\text{RMS}(\boldsymbol{\theta})$ 进行块级自适应调节。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-07-Tiger-一个-抠-到极致的优化器.md
source_ids:
  - "9512"
appears_in:
  - "[[spaces-9512-Tiger-一个-抠-到极致的优化器]]"
  - "[[spaces-9736-Lion-Tiger优化器训练下的Embedding异常和对策]]"
evidence_spans:
  - ev::9512::Tiger更新公式
status: draft
updated: 2026-06-12
---

# Tiger优化器更新公式


## 概述

（待补充）

## 物理意义与机制

本公式定义了 **Tiger优化器** 在每一步的状态迭代规则。作为 Lion 的特例与极简版本，Tiger 将动量更新率和更新插值率统一为单个参数 $\beta$，这消除了 Lion 更新量计算中对即时梯度 $\boldsymbol{g}_t$ 的显式交叉混合依赖。

这一简化的直接结果是，Tiger 在执行梯度累积时，动量滑动公式的展开可以天然地嵌入为对 $\beta$ 和学习率的分段缩放，从而完全“无感”地完成梯度累加，**不需要额外分配任何显存来保存累积的梯度**。这在算力与显存资源受限的大模型训练场景中表现出极佳的内存经济性。
