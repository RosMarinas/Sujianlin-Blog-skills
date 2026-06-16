---
type: article_summary
title: "【理解黎曼几何】3. 测地线"
article_id: "3977"
source_url: https://spaces.ac.cn/archives/3977
date: 2016-10-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-10-15-理解黎曼几何-3-测地线.md
series:
  - "[[理解黎曼几何]]"
concepts:
  - "[[测地线]]"
  - "[[联络]]"
methods:
  - "[[变分求解联络系数法]]"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-10-15-理解黎曼几何-3-测地线.md
source_ids:
  - "3977"
status: draft
updated: 2026-06-11
---

## 概述
本文引入了测地线（Geodesic）这一在坐标变换下保持不变的客观实体，并从变分法（Variational Method）的角度推导了测地线方程。变分推导过程中自然引出了第二类克里斯托费尔（Christoffel）符号，即联络系数 $\Gamma_{\alpha\beta}^\mu$。文章进一步介绍了一种利用 Euler-Lagrange 方程直接计算联络系数的实用变分技巧，避免了通过繁琐定义式进行计算的复杂过程。

## 关键内容
1. **测地线作为客观实体**：它是两点之间距离积分 $s = \int \sqrt{g_{\mu\nu} dx^\mu dx^\nu}$ 取极值所确定的曲线，不依赖于坐标系的选择。
2. **变分推导测地线方程**：对弧长 $s$ 的变分可以转化为对无根号的能量泛函 $S = \frac{1}{2}\int g_{\mu\nu} \frac{dx^\mu}{ds} \frac{dx^\nu}{ds} ds$ 的变分，从而利用欧拉-拉格朗日方程推导出标准测地线方程：
   $$\frac{d^2 x^{\mu}}{ds^2}+\Gamma_{\alpha\beta}^{\mu} \frac{d x^{\alpha}}{ds}\frac{d x^{\beta}}{ds}=0$$
3. **第二类克里斯托费尔符号**：
   $$\Gamma_{\alpha\beta}^{\mu}=\frac{1}{2}g^{\mu\nu}\left(\frac{\partial g_{\alpha\nu}}{\partial x^{\beta}}+\frac{\partial g_{\nu\beta}}{\partial x^{\alpha}}-\frac{\partial g_{\alpha\beta}}{\partial x^{\nu}}\right)$$
4. **变分计算工具**：利用对无根号泛函 $S$ 作用 Euler-Lagrange 方程反推克氏符号的方法，在球坐标系下展示了其高效性和简明性。
