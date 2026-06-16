---
type: article_summary
title: "【外微分浅谈】3. 正交标架"
article_id: "4058"
source_url: https://spaces.ac.cn/archives/4058
date: 2016-11-05
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-11-05-外微分浅谈-3-正交标架.md
series:
  - "[[外微分浅谈]]"
concepts:
  - "[[活动正交标架]]"
methods:
  - "[[活动正交标架度规分解法]]"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-11-05-外微分浅谈-3-正交标架.md
source_ids:
  - "4058"
status: draft
updated: 2026-06-11
---

## 概述
本文展示了如何通过建立（活动）正交标架（Orthonormal Frame）来简化黎曼几何中的度规表示。分量语言下的度规矩阵可能包含极其繁琐的函数元素，而通过对称度规的矩阵分解 $\boldsymbol{g} = \boldsymbol{h}^T \boldsymbol{\eta} \boldsymbol{h}$，可以将度规变换为对角元素仅为 1 或 -1 的常数度规 $\boldsymbol{\eta}$。这种坐标变换不仅简化了度规的复杂性，也为后文引入 Cartan 活动标架法和外微分计算曲率打下了基础。

## 关键内容
1. **活动正交标架的引入动机**：在一般坐标基底 $\{\boldsymbol{e}_\mu\}$ 下的度规分量 $g_{\mu\nu} = \langle \boldsymbol{e}_\mu, \boldsymbol{e}_\nu \rangle$ 往往很复杂。在标准正交标架 $\{\hat{\boldsymbol{e}}_\mu\}$ 下，计算和表达能够得到极大的简化。
2. **度规矩阵的对角化分解**：
   - 将黎曼度规写为矩阵形式：$ds^2 = d\boldsymbol{x}^T \boldsymbol{g} d\boldsymbol{x}$。
   - 进行分解：$\boldsymbol{g} = \boldsymbol{h}^T \boldsymbol{\eta} \boldsymbol{h}$，其中 $\boldsymbol{\eta}$ 是对角线元素为 $\pm 1$ 的常数矩阵（在广义相对论中通常对应闵氏度规或欧氏度规）。
3. **标架与共标架的变换**：
   - 定义 1-形式基底：$\omega^\mu = h^\mu_\alpha dx^\alpha$。
   - 标架变换：$\hat{\boldsymbol{e}}_\mu = \boldsymbol{e}_\alpha (h^{-1})^\alpha_\mu$，满足 $\eta_{\mu\nu} = \langle \hat{\boldsymbol{e}}_\mu, \hat{\boldsymbol{e}}_\nu \rangle$。
   - 此时位置微元可表达为：$d\boldsymbol{r} = \hat{\boldsymbol{e}}_\mu \omega^\mu$，而黎曼度规形式极度简化为 $ds^2 = \eta_{\mu\nu} \omega^\mu \omega^\nu$。
