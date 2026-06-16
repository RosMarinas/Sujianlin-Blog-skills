---
type: article_summary
title: 配置不同的学习率，LoRA还能再涨一点？
article_id: "10001"
source_url: https://spaces.ac.cn/archives/10001
date: 2024-02-27
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-02-27-配置不同的学习率-LoRA还能再涨一点.md
source_html: Data/Spaces_ac_cn/raw/articles/10001/page.html
series: []
topics:
  - "[[topic::LoRA微调]]"
concepts:
  - "[[concept::LoRA]]"
  - "[[concept::LoRA+]]"
methods:
  - "[[method::用数值稳定性分析推导非对称学习率]]"
problem_patterns: []
evidence_spans:
  - ev::10001::结论简析
  - ev::10001::数值稳定
  - ev::10001::快速推导
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-02-27-配置不同的学习率-LoRA还能再涨一点.md
source_ids:
  - "10001"
status: draft
updated: 2026-06-11
---

## 文章核心问题

LoRA的两个低秩矩阵A和B是否需要设置不同的学习率？如果需，理论依据是什么？

## 主要结论

1. LoRA的A,B矩阵存在固有的不对称性：为了使前向传播数值稳定，A用1/n方差初始化，B用1/r方差初始化，导致A分量绝对值远小于B。
2. 基于"贡献相当"假设，推导出B的学习率应大于A，比例η_B/η_A ≈ O(√n)（当m=n时）。
3. 该结论与A,B哪个全零初始化无关——不对称性源于矩阵形状差异而非初始化方式。
4. 实验验证推荐学习率比例为16（对应n=768~4096, r=8），符合O(√(n/r))估计。

## 推导结构

结论简析（LoRA参数化+核心结论）→ 数值稳定（XA, XAB都应O(1)）→ 贡献相当（每步更新A,B贡献应相当）→ 快速推导（SignSGD近似下的定量分析）。

## 关键公式

- 数值稳定要求：A用方差1/n，B用方差1/r初始化
- SignSGD下：ΔA = -η_A sign(∂L/∂A), ΔB = -η_B sign(∂L/∂B)
- 贡献相当条件：η_A × nr × √(1/r) ≈ η_B × mr × √(1/n)
- 学习率比例：η_B/η_A ≈ (n/m)√(n/r) → m=n时 O(√n)

## 体现的方法

- **用数值稳定性分析推导非对称学习率**：通过前向传播数值稳定性和贡献相当假设，从理论上推导LoRA+非对称学习率的必要性。

## 所属系列位置

独立文章，与[[series::LoRA改进系列]]共享LoRA方法论基础。

## 与其他文章的关系

- 被[[article::10226]]引用说明LoRA的非对称性。
- 基于[[article::9590]]的LoRA梯度分析。
- 与[[method::用梯度SVD初始化LoRA]]和[[method::用伪逆投影优化LoRA更新]]共同构成LoRA改进的三大理论主线。

## 原文证据锚点

- `ev::10001::结论简析`：LoRA+的核心结论和两点假设。
- `ev::10001::数值稳定`：数值稳定性条件引出A,B不对称性。
- `ev::10001::快速推导`：SignSGD近似下推导学习率比例。
