---
type: article_summary
title: Muon优化器指南：快速上手与关键细节
article_id: "11416"
source_url: https://spaces.ac.cn/archives/11416
date: 2025-11-19
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-11-19-Muon优化器指南-快速上手与关键细节.md
source_html: null
series: []
topics:
  - "[[矩阵优化]]"
concepts:
  - "[[矩阵符号函数(msign)]]"
  - "[[Embedding输出头稳定性]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
problem_patterns: []
evidence_spans:
  - ev::11416::简要介绍
  - ev::11416::四个版本
  - ev::11416::两个维度
  - ev::11416::超参设置
  - ev::11416::其他参数
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-11-19-Muon优化器指南-快速上手与关键细节.md
source_ids:
  - "11416"
status: draft
updated: 2026-06-10
---

## 文章核心问题

如何从Adam优化器快速切换到Muon？Muon的多个版本有何区别？不同框架（Keras/Torch）下如何正确设置超参数？

## 主要结论

1. Muon已有四个版本（朴素版/KellerJordan版/MuP版/Moonlight版），区别仅在msign前的缩放因子。
2. d_in/d_out的顺序敏感：Keras实现`xW`时W的第一个维度是d_in，Torch的Linear实现`xW^T`时W的第二个维度是d_in。错误排序会导致缩放因子错误。
3. Moonlight版通过对齐Adam的Update RMS，可直接复用Adam的学习率和权重衰减，迁移成本最低。
4. KellerJordan版和MuP版的学习率需放大约$0.2\sqrt{d}$倍（d=hidden_size）才能对齐Adam更新幅度。
5. Embedding层和输出分类层的矩阵参数不能用Muon（需用Adam），卷积层可将参数reshape为矩阵间接使用Muon。

## 推导结构

简要介绍（Muon的发展历程与业界采用情况）→ 四个版本（更新公式对比，朴素/KellerJordan/MuP/Moonlight）→ 两个维度（框架实现的d_in/d_out顺序差异与Keras的bug）→ 超参设置（各版本学习率迁移策略，Magic Number 0.2的来源）→ 其他参数（Bias/Norm/Embedding/Conv的处理方式）→ 期望结果。

## 关键公式

- 四个版本更新公式的统一形式：$W_t = W_{t-1} - \eta_t (c \cdot \text{msign}(M_t) + \lambda W_{t-1})$，其中c分别为1、$\sqrt{\max(1,d_{out}/d_{in})}$、$\sqrt{d_{out}/d_{in}}$、$0.2\sqrt{\max(d_{out},d_{in})}$。

## 体现的方法

- **用稳定性指标约束优化器缩放**：四个版本的缩放因子差异本质上来自对齐不同稳定性指标（Update RMS对齐 vs 学习率跨尺度可迁移），Moonlight版对齐Adam的Update RMS，MuP版对齐宽度不变性。

## 所属系列位置

独立文章。与[[series::基于流式幂迭代的Muon实现]]使用层共享msign算子并关注实现细节；与[[series::MuP之上]]在方法层共享缩放因子设计原则。

## 与其他文章的关系

- 直接引用[[spaces-10592-Muon优化器赏析-从向量到矩阵的本质跨越]]作为理论基础。
- 是[[spaces-11772-为什么官方版Muon比MuP版多出一个max-1]]的前置背景（后者解释了KellerJordan版max截断的原因）。
- 与系列[[series::基于流式幂迭代的Muon实现]]互补：本文侧重使用指南，后者侧重计算优化。
- 在实践层面补充了MuP理论（10770）中未展开的实现细节和框架差异。

## 原文证据锚点

- `ev::11416::简要介绍`：Muon发展历程，Torch/Keras/Megatron均内置支持，Moonlight/K2/GLM-4.5验证。
- `ev::11416::四个版本`：四个版本更新公式及缩放因子差异，Nesterov动量选项。
- `ev::11416::两个维度`：Keras的Dense和Torch的Linear在d_in/d_out顺序上的差异，Keras 3.12的bug。
- `ev::11416::超参设置`：Moonlight版可直接复用Adam超参；其他版本需放大$\approx 0.2\sqrt{d}$倍学习率。
- `ev::11416::其他参数`：Embedding和输出头不能用Muon；卷积可reshape后使用；RMSNorm Gamma可视为对角矩阵处理。
