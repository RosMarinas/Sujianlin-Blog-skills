---
type: article_summary
title: "【理解黎曼几何】2. 从勾股定理到黎曼度量"
article_id: "3969"
source_url: https://spaces.ac.cn/archives/3969
date: 2016-10-14
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-10-14-理解黎曼几何-2-从勾股定理到黎曼度量.md
series:
  - "[[理解黎曼几何]]"
concepts:
  - "[[黎曼度量]]"
  - "[[等温度量]]"
methods:
  - "[[活动正交标架度规分解法]]"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-10-14-理解黎曼几何-2-从勾股定理到黎曼度量.md
source_ids:
  - "3969"
status: draft
updated: 2026-06-11
---

## 概述
本文展示了如何从平直空间的勾股定理逐步推广到任意维弯曲空间中的黎曼度量。作者首先展示了直角坐标与曲线坐标（如极坐标）在度规上的差异，指出最一般的测量形式为 $ds^2 = g_{\mu\nu} dx^\mu dx^\nu$。此外，文章探讨了局部直角坐标系的矩阵分解 $\boldsymbol{g} = \boldsymbol{h}^T \boldsymbol{h}$，并利用该变换矩阵定义了向量模长、夹角、平行多面体积等几何实体，将平直空间中熟悉的物理量平滑扩展至弯曲空间。

## 关键内容
1. **黎曼度量的引入**：度规 $g_{\mu\nu}$ 描述了流形上每个点处的“当地勾股定理”。
2. **等温度量（等温坐标系）**：以 Feynman 物理学讲义中“热膨胀尺子”为例，建立了 $ds^2 = f(x,y,z)(dx^2 + dy^2 + dz^2)$ 的物理直观，说明弯曲空间可以等价于不均匀的测量基准。
3. **局部直角坐标变换**：对称度规矩阵分解为 $\boldsymbol{g} = \boldsymbol{h}^T \boldsymbol{h}$，其中 $\boldsymbol{h}$ 描述了从弯曲坐标系到局部直角坐标系的变换。由此导出弯曲空间中的内积、夹角、体积元（$\sqrt{g}d\Omega$）及超体积公式。
