---
type: article_summary
title: "【理解黎曼几何】4. 联络和协变导数"
article_id: "3998"
source_url: https://spaces.ac.cn/archives/3998
date: 2016-10-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-10-16-理解黎曼几何-4-联络和协变导数.md
series:
  - "[[理解黎曼几何]]"
concepts:
  - "[[联络]]"
  - "[[协变导数]]"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-10-16-理解黎曼几何-4-联络和协变导数.md
source_ids:
  - "3998"
status: draft
updated: 2026-06-11
---

## 概述
本文展示了如何通过物理直观和几何移动（平行移动）导出联络和协变导数。作者指出，直接对不同位置处的向量进行相减是没有几何意义的，因为局部坐标系的方向和尺度不同。为了解决这一问题，需要使用测地线作为最自然的参照物，将一个位置的向量坐标变换到另一相邻位置。这就导出了联络系数，并基于此定义了能够在弯曲空间中保持几何意义的协变导数（Covariant Derivative）和协变微分（Covariant Differential）。

## 关键内容
1. **向量差的几何障碍**：不同位置对应的局部标架不同，不能直接对向量的分量进行数值相减（类比不同货币不能直接相减）。
2. **联络作为坐标变换**：借用测地线方程作为单位切向量平行移动的基准，导出从 $\boldsymbol{x}+d\boldsymbol{x}$ 到 $\boldsymbol{x}$ 的无穷小坐标变换矩阵为 $\delta_{\nu}^{\mu}+\Gamma_{\nu\beta}^{\mu} d x^{\beta}$。$\Gamma_{\nu\beta}^{\mu}$ 起到了联系两个邻近坐标系的作用，故称“联络”。
3. **协变导数与协变微分**：将 $\boldsymbol{x}+d\boldsymbol{x}$ 处的向量平移到 $\boldsymbol{x}$ 处后作差，在极限下导出协变导数：
   $$A^{\mu}_{;\beta}=\frac{\partial A^{\mu}}{\partial x^{\beta}}+\Gamma_{\nu\beta}^{\mu} A^{\nu}$$
   以及协变微分：
   $$D A^{\mu}=dA^{\mu}+\Gamma_{\nu\beta}^{\mu} A^{\nu}dx^{\beta}$$
4. **与传统导出的对比**：传统教材常基于平直空间直角坐标的转换导出协变导数，隐含了平直空间的假设。而这里的平行移动推导方式更加内在且具备明显的几何直观。
