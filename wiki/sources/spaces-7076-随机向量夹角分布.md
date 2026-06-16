---
type: article_summary
title: n维空间下两个随机向量的夹角分布
article_id: "7076"
source_url: https://spaces.ac.cn/archives/7076
date: 2019-11-13
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2019-11-13-n维空间下两个随机向量的夹角分布.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[顺序统计量]]
  - [[超球坐标]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-11-13-n维空间下两个随机向量的夹角分布.md
source_ids:
  - "7076"
status: draft
updated: 2026-06-11
---

## 文章核心问题

n维空间中两个随机向量夹角θ的概率分布，以及高维空间中随机向量几乎垂直的反直觉现象。

## 主要结论

夹角θ的概率密度：$p_n(\theta) = \frac{\Gamma(n/2)}{\Gamma((n-1)/2)\sqrt{\pi}} \sin^{n-2}\theta$。当n增大时，方差趋近于0，均值$\pi/2$，即高维空间中随机向量几乎正交。

## 推导结构

1. 超球坐标变换，固定一个向量为$(1,0,\ldots,0)$
2. 夹角$\theta$ = 超球坐标第一角$\varphi_1$
3. 超球面积分计算概率密度

## 关键公式

$p_n(\theta) = \frac{\Gamma(n/2)}{\Gamma((n-1)/2)\sqrt{\pi}} \sin^{n-2}\theta$

方差近似：$Var(\theta) \approx \frac{1}{n-2}$（n较大时）

## 体现的方法

超球坐标积分、拉普拉斯近似

## 所属系列位置

独立单篇。

## 与其他文章的关系

几何概率主题，与9324（圆内随机点）同属几何概率类别。

## 原文证据锚点

- 超球坐标变换
- 概率密度推导
- 方差数值表
