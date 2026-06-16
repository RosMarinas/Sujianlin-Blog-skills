---
type: article_summary
title: "生成扩散模型漫谈（十一）：统一扩散模型（应用篇）"
article_id: "9271"
source_url: "https://spaces.ac.cn/archives/9271"
date: "2022-09-21"
category: "Big-Data"
source_markdown: "Data/Spaces_ac_cn/markdown/Big-Data/2022-09-21-生成扩散模型漫谈-十一-统一扩散模型-应用篇.md"
series:
  - "[[生成扩散模型漫谈]]"
topics: []
concepts:
  - "[[统一扩散模型UDM]]"
  - "[[热扩散与冷扩散]]"
  - "[[离散扩散模型]]"
  - "[[掩码语言模型生成]]"
methods: []
problem_patterns: []
evidence_spans:
  - "ev::9271::框架回顾"
  - "ev::9271::热之扩散"
  - "ev::9271::冷之扩散"
  - "ev::9271::编辑模型"
  - "ev::9271::掩码模型"
  - "ev::9271::编码模型"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2022-09-21-生成扩散模型漫谈-十一-统一扩散模型-应用篇.md"
source_ids:
  - "9271"
status: draft
updated: "2026-06-09"
---

# 生成扩散模型漫谈（十一）：统一扩散模型（应用篇）

## 文章核心问题

将上一篇文章构建的统一扩散模型（UDM）理论框架应用于具体模型，验证其能否涵盖主流扩散模型（DDPM、DDIM）、Cold Diffusion、文本编辑生成、MLM掩码生成及编码模型等多种生成模型。

## 主要结论

1. UDM框架能够统一表达所有上述模型：通过选择不同的前向变换 $\boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon})$ 和噪声分布 $q(\boldsymbol{\varepsilon})$，可以分别恢复DDPM/DDIM（热扩散）、Cold Diffusion（冷扩散）、文本编辑模型、MLM掩码模型以及编码模型。
2. Cold Diffusion 强调"无噪声"的前向过程，但其确定性变换导致不可逆的信息损失（如将 $3w^2$ 维图片压缩到 $3$ 维），限制了生成清晰度。引入噪声（$\sigma>0$）可以缓解该问题。
3. 噪声在扩散模型中扮演"一对多"映射的关键角色，使得"多对一"的前向信息损失过程不会损害反向生成质量。
4. 对于离散数据（文本），前向变换关于噪声的可逆性是实现渐进式稳定生成的关键——"替换为不同token"的约束使生成过程能保留已预测的有效部分。

## 推导结构

1. 回顾UDM框架：前向过程 $\boldsymbol{x}_t = \boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon})$，反向过程分解为 $\hat{\boldsymbol{x}}_0$ 估计和 $\boldsymbol{x}_{t-1}$ 条件采样两步。
2. 热扩散作为UDM：代入 $\boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon}) = \bar{\alpha}_t \boldsymbol{x}_0 + \bar{\beta}_t \boldsymbol{\varepsilon}$，恢复标准噪声预测训练目标；反向过程通过 $\sigma_t$ 的选择关联DDPM、DDIM和Analytical-DPM。
3. 冷扩散作为UDM：代入 $\boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon}) = \boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0) + \sigma\boldsymbol{\varepsilon}$，恢复 Naive Sampling 和 Improved Sampling 两种采样方案。
4. 编辑模型和掩码模型作为UDM：定义随机替换或随机掩码的前向过程，通过可逆性条件改进生成质量。
5. 编码模型：将DDPM扩展为 $\boldsymbol{x}_t = \bar{\alpha}_t \boldsymbol{\mathcal{F}}(\boldsymbol{x}_0) + \bar{\beta}_t \boldsymbol{\varepsilon}$，引入可学习编码器。

## 关键公式

- **UDM前向过程**: $\boldsymbol{x}_t = \boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon}),\quad \boldsymbol{\varepsilon}\sim q(\boldsymbol{\varepsilon})$
- **基准反向选择**: $\boldsymbol{x}_{t-1}=\boldsymbol{\mathcal{F}}_{t-1}(\boldsymbol{x}_0,\boldsymbol{\varepsilon})$
- **确定性采样（可逆时）**: $\boldsymbol{x}_{t-1} = \boldsymbol{\mathcal{F}}_{t-1}(\boldsymbol{x}_0,\boldsymbol{\mathcal{F}}_t^{-1}(\boldsymbol{x}_0,\boldsymbol{x}_t))$
- **热扩散前向**: $\boldsymbol{x}_t = \bar{\alpha}_t \boldsymbol{x}_0 + \bar{\beta}_t \boldsymbol{\varepsilon}$
- **冷扩散Improved Sampling**: $\hat{\boldsymbol{x}}_0=\boldsymbol{\mathcal{G}}_t(\boldsymbol{x}_t),\quad \boldsymbol{x}_{t-1} = \boldsymbol{x}_t + \boldsymbol{\mathcal{F}}_{t-1}(\hat{\boldsymbol{x}}_0) - \boldsymbol{\mathcal{F}}_t(\hat{\boldsymbol{x}}_0)$

## 实验或案例

本文为纯理论推导，未提供新实验。文章引用了Cold Diffusion论文中的实验发现：往 $3$ 维向量中加入 $3w^2$ 维轻微随机噪声可以提高生成效果，验证了噪声在生成过程中的必要性。

## 所属系列位置

本文是"生成扩散模型漫谈"系列第11篇，是第10篇（UDM理论篇）的直接应用续篇，通过实例验证UDM框架的一般性。后续文章将在不同方向上扩展扩散模型的理解（ODE直接推导、PFGM、一般ODE构建框架）。

## 与其他文章的关系

- continues: [[生成扩散模型漫谈（十）：统一扩散模型（理论篇）]]
- builds_on: DDPM（文章4）、DDIM（文章3）
- belongs_to: [[生成扩散模型漫谈]]
- references: Cold Diffusion论文（arXiv:2208.09392）

## 原文证据锚点

- `ev::9271::框架回顾`
- `ev::9271::热之扩散`
- `ev::9271::冷之扩散`
- `ev::9271::编辑模型`
- `ev::9271::掩码模型`
- `ev::9271::编码模型`
