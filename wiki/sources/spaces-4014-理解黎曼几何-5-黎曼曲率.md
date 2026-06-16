---
type: article_summary
title: "【理解黎曼几何】5. 黎曼曲率"
article_id: "4014"
source_url: https://spaces.ac.cn/archives/4014
date: 2016-10-18
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-10-18-理解黎曼几何-5-黎曼曲率.md
series:
  - "[[理解黎曼几何]]"
concepts:
  - "[[黎曼曲率]]"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-10-18-理解黎曼几何-5-黎曼曲率.md
source_ids:
  - "4014"
status: draft
updated: 2026-06-11
---

## 概述
本文系统探讨了内蕴刻画空间弯曲的核心物理量——黎曼曲率张量（Riemann Curvature Tensor）。作者对比了三种不同的黎曼曲率导出路径，深入阐述了其各自对应的几何和物理背景。这三种途径分别是：二阶协变导数不可交换性、测地线偏离（Jacobi场）以及向量沿闭合回路平行移动产生的偏差，均从不同角度揭示了弯曲空间与平直空间的本质差异。

## 关键内容
1. **三种曲率导出方式的几何直观**：
   - **二阶协变导数顺序的可交换性**：平直空间下求导顺序可交换，而弯曲空间则有偏差，二者之差分离出曲率张量：
     $$A^{\mu}_{;\alpha;\beta}-A^{\mu}_{;\beta;\alpha}=-R^{\mu}_{\nu\alpha\beta}A^{\nu}$$
   - **测地线偏离（Geodesic Deviation）**：邻近的两条测地线 $\delta x^\mu$ 沿弧长演化时满足：
     $$\frac{D^2 \delta x^{\mu}}{Ds^2}=-R^{\mu}_{\nu\alpha\beta}\delta x^{\alpha}\frac{dx^{\nu}}{ds}\frac{dx^{\beta}}{ds}$$
     表明曲率张量非零对应着测地线的 converge 或 diverge（相当于广义相对论中的潮汐力）。
   - **闭合回路平行移动（Holonomy）**：将向量沿着无穷小平行四边形回路平行平移一圈回到起点后，向量会发生改变，二阶近似偏差为：
     $$\Delta A^{\mu} = -R^{\mu}_{\alpha\beta\gamma} A^{\alpha} dx^{\beta}\delta x^{\gamma}$$
2. **黎曼曲率张量的定义式**：
   $$R^{\mu}_{\alpha\beta\gamma}=\frac{\partial \Gamma^{\mu}_{\alpha\gamma}}{\partial x^{\beta}}-\frac{\partial \Gamma^{\mu}_{\alpha\beta}}{\partial x^{\gamma}}+\Gamma^{\mu}_{\nu\beta}\Gamma^{\nu}_{\alpha\gamma}-\Gamma^{\mu}_{\nu\gamma}\Gamma^{\nu}_{\alpha\beta}$$
3. **弯曲与平直空间的根本区别**：平直空间中，求导可交换、测地线呈线性均匀分布、闭回路平移后向量保持不变；而在弯曲空间中，上述三点均不再成立。
