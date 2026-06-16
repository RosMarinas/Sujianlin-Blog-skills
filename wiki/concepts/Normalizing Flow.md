---
type: concept
title: Normalizing Flow
aliases:
- 流模型
- 可逆流模型
definition: 一种模型架构具有可逆特点、以最大似然为训练目标、能实现单步生成的可逆生成式概率模型。
standard_notation: "\boldsymbol{x}=\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z})"
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-01-17-细水长flow之TARFLOW-流模型满血归来.md
source_ids:
- 10667
status: draft
updated: '2026-06-12'
---

# Normalizing Flow

## 定义

Normalizing Flow 在源文中特指“模型架构具有可逆特点、以最大似然为训练目标、能实现一步生成”的生成式概率模型。它用确定性函数 $\boldsymbol{x}=\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z})$ 将简单噪声分布（如标准高斯）映射到目标数据分布，同时要求存在逆函数 $\boldsymbol{z}=\boldsymbol{f}_{\boldsymbol{\theta}}(\boldsymbol{x})$。

## 激活场景

当 Method 页讨论 TARFLOW、仿射耦合层、去噪采样或可逆生成模型时，本页提供共同背景。源文强调，流模型与 GAN 的分歧在于训练目标的处理：GAN 用判别器间接近似概率差异，而流模型通过可逆变换和变量替换直接计算 $q_{\boldsymbol{\theta}}(\boldsymbol{x})$，因此可用最大似然训练。

## 关键关系

流模型可训练的关键条件有两个：一是变换必须可逆，二是雅可比行列式必须可计算。源文由变量替换得到
$$
q_{\boldsymbol{\theta}}(\boldsymbol{x})=q(\boldsymbol{f}_{\boldsymbol{\theta}}(\boldsymbol{x}))\left|\det \frac{\partial \boldsymbol{f}_{\boldsymbol{\theta}}(\boldsymbol{x})}{\partial \boldsymbol{x}}\right|,
$$
对应负对数似然包含先验密度项和雅可比行列式项。仿射耦合层正是为了同时满足可逆性和行列式易算性而设计；TARFLOW 则是在这一框架下引入多块划分和 Transformer 自回归结构。

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2025-01-17-细水长flow之TARFLOW-流模型满血归来.md`
