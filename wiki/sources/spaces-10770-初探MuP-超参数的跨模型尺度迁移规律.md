---
type: article_summary
title: 初探MuP：超参数的跨模型尺度迁移规律
article_id: "10770"
source_url: https://spaces.ac.cn/archives/10770
date: 2025-03-13
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-03-13-初探MuP-超参数的跨模型尺度迁移规律.md
source_html: null
series: []
topics:
  - "[[矩阵优化]]"
concepts:
  - "[[MuP稳定性三条件]]"
  - "[[RMS尺度]]"
  - "[[Embedding输出头稳定性]]"
  - "[[矩阵符号函数(msign)]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
problem_patterns: []
evidence_spans:
  - ev::10770::前向传播
  - ev::10770::反向传播
  - ev::10770::损失增量
  - ev::10770::组装结果
  - ev::10770::特征变化
  - ev::10770::Adam版本
  - ev::10770::Muon版本
  - ev::10770::结论汇总
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-03-13-初探MuP-超参数的跨模型尺度迁移规律.md
source_ids:
  - "10770"
status: draft
updated: 2026-06-10
---

## 文章核心问题

当模型宽度 d 增大时，超参数（学习率、初始化方差）该如何缩放才能保持训练行为和效果不变？MuP（Maximal Update Parametrization）提供了这个问题的系统答案。

## 主要结论

1. MuP给出SGD/Adam/Muon三种优化器下学习率随宽度 d 的缩放规律，不同参数层（W_in, W_k, W_out）需要不同的缩放因子。
2. 缩放规律通过四类稳定性条件推导：前向传播RMS稳定、反向传播RMS稳定、损失增量$\Delta\mathcal{L}=\Theta(1)$、特征变化$\Delta Y_k=\Theta(1)$。
3. SGD下：$\eta_{in}\propto d,\ \eta_k\propto 1,\ \eta_{out}\propto 1/d$；Adam下：$\eta_{in}\propto 1,\ \eta_k\propto 1/d,\ \eta_{out}\propto 1/d$；Muon下：$\eta_{in}\propto \sqrt{d},\ \eta_k\propto 1,\ \eta_{out}\propto 1/\sqrt{d}$。
4. Initialization方差设置：W_in用fan_in初始化($1/d_{in}$)，W_k用fan_in($1/d$)，W_out需特设$\propto 1/d^2$以保证特征变化稳定。

## 推导结构

方法大意（明确目标：超参数跨宽度转移）→ 前向传播（fan_in初始化维持RMS稳定）→ 反向传播（梯度规模分析，fan_in/fan_out冲突）→ 损失增量（$\Delta\mathcal{L}$的尺度分析，揭示直接迁移学习率会爆炸的原因）→ 模型假设（三层结构：W_in→NN(方阵)→W_out）→ 组装结果（对各参数层分别做尺度分析）→ 特征变化（增加$\Delta Y_k=\Theta(1)$约束，反推出W_out初始化$\propto 1/d^2$）→ Adam版本（SignSGD近似下的分析）→ Muon版本（MSignSGD近似，Nuclear范数的分析）→ 结论汇总表。

## 关键公式

- RMS定义：$\text{RMS}(W) = \sqrt{\frac{1}{d_{in}d_{out}}\sum W_{ij}^2}$
- 对线性层$Y=XW$，前向RMS稳定需要fan_in初始化：方差$\propto 1/d_{in}$
- 损失增量近似：$\Delta\mathcal{L} \approx -\eta \|\partial\mathcal{L}/\partial W\|_F^2$
- MuP尺度汇总表：SGD/Adam/Muon三种参数化下各层初始化方差与学习率的缩放规律

## 体现的方法

- **用稳定性指标约束优化器缩放**：本文是该方法的核心演示——从前向、反向、损失增量、特征变化四类稳定性指标反推出初始化方差和学习率的缩放规则。

## 所属系列位置

独立文章（非系列内文章），但作为[[series::MuP之上]]系列的前置知识。MuP之上系列在前向/反向/更新稳定性的基础上增加了方法层面的推导和扩展。

## 与其他文章的关系

- 引用[[spaces-10592-Muon优化器赏析-从向量到矩阵的本质跨越]]作为Muon版本分析的背景理论。
- 引用[[spaces-10542-当Batch-Size增大时学习率该如何随之变化]]介绍的SignSGD近似用于Adam分析。
- 直接连接[[series::MuP之上]]系列：本文的损失增量分析和特征变化要求是该系列稳定性三条件的前身。
- 在操作类型上与[[用稳定性指标约束优化器缩放]]方法一致，本文是该方法在宽度转移场景下的实例。

## 原文证据锚点

- `ev::10770::前向传播`：线性层前向RMS稳定要求fan_in初始化，激活函数不影响尺度关系。
- `ev::10770::反向传播`：反向传播的RMS稳定要求fan_out初始化，与fan_in在非方阵时冲突。
- `ev::10770::损失增量`：$\Delta\mathcal{L}$的规模正比于$d_{in}d_{out}$，直接迁移学习率会导致爆炸。
- `ev::10770::组装结果`：三层模型（W_in, NN方阵, W_out）下各参数梯度F-范数的尺度分析。
- `ev::10770::特征变化`：引入$\Delta Y_k=\Theta(1)$约束，反推出W_out初始化方差$\propto 1/d^2$。
- `ev::10770::Adam版本`：用SignSGD近似分析Adam，得$\eta_k\propto 1/d,\eta_{in}\propto 1$。
- `ev::10770::Muon版本`：用MSignSGD近似分析Muon，Nuclear范数近似，得$\eta_{in}\propto \sqrt{d},\eta_{out}\propto 1/\sqrt{d}$。
- `ev::10770::结论汇总`：三种参数化下的完整缩放表格，并讨论了Muon+Adjust LR的实际修正。
