---
type: article_summary
title: 【外微分浅谈】7. 有力的计算
article_id: "4076"
source_url: https://spaces.ac.cn/archives/4076
date: 2016-11-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-11-11-外微分浅谈-7-有力的计算.md
series:
  - 外微分浅谈
topics:
  - 微分几何
  - 外微分
concepts:
  - 外微分
  - 黎曼曲率张量
  - 正交标架
  - 史瓦西度规
methods:
  - 外微分计算黎曼曲率
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-11-11-外微分浅谈-7-有力的计算.md
source_ids:
  - "4076"
status: draft
updated: 2026-06-10
---

## 总结

本文展示用外微分方法计算黎曼曲率张量的实操：先以二维球面 $ds^2=d\theta^2+\sin^2\theta d\phi^2$ 热身，再求解四维史瓦西度规的黎曼曲率。外微分方法通过正交标架、联络形式 $\omega_\nu^\mu$ 和曲率形式 $\mathscr{R}_\nu^\mu=d\omega_\nu^\mu+\omega_\alpha^\mu\land\omega_\nu^\alpha$，将繁琐的张量指标计算简化为矩阵乘法和外代数运算。

## 关键思想

- 外微分方法将曲率计算转化为：选择正交标架 → 求解联络形式 → 计算曲率形式 → 读取曲率张量分量
- 正交标架下 $\omega_\nu^\mu$ 的反对称性（$\eta$ 为常数矩阵时）大幅减少待求分量
- 二维空间恒有 $\omega_\alpha^\mu\land\omega_\nu^\alpha=0$
- 史瓦西度规计算展示了外微分处理4维非平凡度规的实际可行性和系统化步骤

## 所属系列

[[外微分浅谈]] — [[微分几何]] — [[广义相对论数学基础]]
