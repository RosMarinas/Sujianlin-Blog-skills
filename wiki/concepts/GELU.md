---
type: concept
definition: GELU(x) = xΦ(x)，其中 Φ(x) 是标准正态分布的累积分布函数。
title: GELU
aliases:
- Gaussian Error Linear Unit
- GELU激活函数
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
- Data/Spaces_ac_cn/markdown/Mathematics/2021-10-10-用狄拉克函数来构造非光滑函数的光滑近似.md
source_ids:
- '7309'
- '8718'
evidence_spans: []
---


## 定义

GELU(x) = xΦ(x)，其中 Φ(x) 是标准正态分布的累积分布函数。

## 精确形式

$\text{GELU}(x)=x\Phi(x)=\frac12 x\left[1+\text{erf}\left(\frac{x}{\sqrt{2}}\right)\right]$

## 初等函数近似

1. **Sigmoid近似**：$\text{GELU}(x)\approx x\sigma(1.702x)$ — Logistic函数全局逼近累积正态分布的结果
2. **Tanh近似**：$\text{GELU}(x)\approx\frac12 x\left[1+\tanh\left(\sqrt{\frac{2}{\pi}}(x+0.044715x^3)\right)\right]$ — 局部泰勒展开+全局min-max优化的混合结果

## 性质

GELU是ReLU的光滑近似（可由Dirac delta方法推导），在BERT/GPT等预训练语言模型中被广泛使用。

## 所属系列

[[激活函数理论]] — [[函数逼近论]]