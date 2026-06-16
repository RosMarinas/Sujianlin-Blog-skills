---
title: FID梯度与流式近似公式
type: formula
standard_notation: FID梯度与流式近似公式
tags:
- FID
- 梯度
- 流式训练
- 矩阵平方根
status: draft
updated: '2026-06-14'
source_ids:
- '11738'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-05-08-直接以FID为Loss-从梯度计算到流式训练.md
latex: \mathcal{F} \triangleq \mathcal{W}_2^2[p,q] = \|\boldsymbol{\mu}_p - \boldsymbol{\mu}_q\|^2 + \mathop{\text{tr}}(\boldsymbol{\Sigma}_p + \boldsymbol{\Sigma}_q - 2(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{1/2})
symbol_meanings:
  \mathcal{F}: FID（Fréchet Inception Distance）值
  \boldsymbol{\mu}_p: 真实分布均值向量
  \boldsymbol{\mu}_q: 生成分布均值向量
  \boldsymbol{\Sigma}_p: 真实分布协方差矩阵
  \boldsymbol{\Sigma}_q: 生成分布协方差矩阵
  p: 真实数据分布
  q: 生成数据分布
conditions: （待从源文章提取）
appears_in:
- '11738'
---
# FID梯度与流式近似公式


## 概述

（待补充）

## FID定义
F = W_2^2[p,q] = ||mu_p - mu_q||^2 + tr(Sigma_p + Sigma_q - 2(Sigma_p^{1/2} Sigma_q Sigma_p^{1/2})^{1/2})

## 梯度公式
- nabla_{mu_q} F = 2(mu_q - mu_p)
- nabla_{Sigma_q} F = I - Sigma_p^{1/2} (Sigma_p^{1/2} Sigma_q Sigma_p^{1/2})^{-1/2} Sigma_p^{1/2}

## EMA流式更新
- mu_q^{(t)} = beta mu_q^{(t-1)} + (1-beta) tilde{mu}_q^{(t)}
- V_q^{(t)} = beta V_q^{(t-1)} + (1-beta) tilde{V}_q^{(t)}