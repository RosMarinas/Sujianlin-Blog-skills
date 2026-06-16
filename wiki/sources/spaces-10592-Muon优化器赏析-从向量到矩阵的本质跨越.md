---
type: article_summary
title: Muon优化器赏析：从向量到矩阵的本质跨越
article_id: "10592"
source_url: https://spaces.ac.cn/archives/10592
date: 2024-12-10
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-12-10-Muon优化器赏析-从向量到矩阵的本质跨越.md
source_html: null
series: []
topics:
  - "[[矩阵优化]]"
concepts:
  - "[[矩阵符号函数(msign)]]"
  - "[[Newton-Schulz迭代]]"
  - "[[谱范数]]"
  - "[[RMS尺度]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
  - "[[用迭代逼近替代矩阵分解]]"
problem_patterns: []
evidence_spans:
  - ev::10592::算法初探
  - ev::10592::符号函数
  - ev::10592::迭代求解
  - ev::10592::收敛加速
  - ev::10592::范数视角
  - ev::10592::矩阵范数
  - ev::10592::追根溯源
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-12-10-Muon优化器赏析-从向量到矩阵的本质跨越.md
source_ids:
  - "10592"
status: draft
updated: 2026-06-10
---

## 文章核心问题

Muon优化器如何利用矩阵参数的结构特性（而非Element-wise方式）实现更本质的优化，以及它与SGD、Adam等传统优化器的数学联系。

## 主要结论

1. Muon是为矩阵参数定制的优化器，其核心是将动量矩阵的SVD奇异值全部置1（msign操作），相当于在谱范数约束下做最速梯度下降。
2. msign可以通过Newton-Schulz迭代高效近似，迭代系数可通过优化奇异值收敛速度确定，且与矩阵大小和迭代步数有关。
3. 当 beta=0 时，Muon与Shampoo优化器在理论上等价；msign退化为对动量取 sign 时，Muon退化为SignSGD/Signum/Tiger。
4. 谱范数（2-范数）比F-范数更紧凑，前者惩罚下的最速下降给出msign方向，后者则退化为SGD。

## 推导结构

算法初探（给出Muon更新公式）→ 符号函数性质（msign的SVD形式、恒等式、最优正交近似）→ 迭代求解（Newton-Schulz泰勒展开近似msign）→ 收敛加速（将系数选择建模为奇异值收敛优化问题）→ 范数视角（最速梯度下降的范数-方向解耦框架）→ 矩阵范数（谱范数下最速下降等价于Muon）→ 追根溯源（与Shampoo的关系）。

## 关键公式

- Muon更新规则：$M_t = \beta M_{t-1} + G_t,\ W_t = W_{t-1} - \eta_t[\text{msign}(M_t) + \lambda W_{t-1}]$
- msign的SVD形式：$\text{msign}(M) = U_{[:,:r]} V_{[:,:r]}^\top$
- msign恒等式：$\text{msign}(M) = (M M^\top)^{-1/2} M = M(M^\top M)^{-1/2}$
- 最优正交近似：$\text{msign}(M) = \argmin_{O^\top O = I} \|M - O\|_F^2$
- Newton-Schulz迭代：$X_{t+1} = a X_t + b X_t(X_t^\top X_t) + c X_t(X_t^\top X_t)^2$
- 2-范数下最速下降方向：$\Phi^* = \sum_{i=1}^r u_i v_i^\top = \text{msign}(G)$

## 体现的方法

- **用稳定性指标约束优化器缩放**：将Muon视为谱范数（2-范数）约束下的最速梯度下降，从范数约束反推更新方向。
- **用迭代逼近替代矩阵分解**：Newton-Schulz迭代绕过昂贵的SVD，用低阶多项式近似逼近msign。
- **将系数优化问题参数化为可导优化问题**：将NS迭代系数选择转化为奇异值收敛速度的优化目标。

## 所属系列位置

独立文章。与[[series::基于流式幂迭代的Muon实现]]直接相关（该系列改进msign的计算路径）；与[[series::MuP之上]]方法层共享稳定性指标约束的推导框架。

## 与其他文章的关系

- 被[[spaces-10770-初探MuP-超参数的跨模型尺度迁移规律]]引用作为Muon版本分析的背景。
- 被[[spaces-11416-Muon优化器指南-快速上手与关键细节]]引用作为理论基础。
- 在操作类型上与[[series::流形上的最速下降]]共享"在范数约束下求最速下降方向"的生成动作。
- 与系列[[series::msign算子的Newton-Schulz迭代]]互补（本文着重Muon视角，后者着重msign算子本身）。

## 原文证据锚点

- `ev::10592::算法初探`：Muon更新公式定义，动量、msign、学习率、权重衰减的关系。
- `ev::10592::符号函数`：msign的SVD形式、恒等式$(\cdot)^{-1/2}$形式、最优正交近似。
- `ev::10592::迭代求解`：Newton-Schulz迭代的泰勒展开源头，官方代码与展开系数的不一致。
- `ev::10592::收敛加速`：将NS系数选择转化为奇异值收敛优化问题，表格给出不同矩阵大小的最优系数。
- `ev::10592::范数视角`：最速梯度下降的范数-方向解耦框架，p-范数下导出SignSGD。
- `ev::10592::矩阵范数`：谱范数下最速下降方向恰好是msign(G)，证明Muon是2-范数约束下的梯度下降。
- `ev::10592::追根溯源`：Shampoo在beta=0时与Muon等价，Shampoo传承Adagrad外积缓存思想。
