---
type: article_summary
title: 用复数化简二次曲线的尝试
article_id: "1851"
source_url: https://spaces.ac.cn/archives/1851
date: 2013-01-02
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2013-01-02-用复数化简二次曲线的尝试.md
series: []
topics: ['[[topic::矩阵几何]]']
concepts: ['[[复数化简二次曲线]]']
methods: ['[[平面二次曲线的复数坐标代换化简法]]']
problem_patterns: []
evidence_spans: ['ev::1851::复数二次型展开', 'ev::1851::复数坐标代换']
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-01-02-用复数化简二次曲线的尝试.md
source_ids:
  - "1851"
status: draft
updated: 2026-06-11
---

## 文章核心问题
探讨如何以平面复数 $z = x+yi$ 及其共轭为工具，直接通过复数代数变形和旋转变换来化简平面的二次曲线。

## 主要结论
在二维平面上，复数能极其自然地表达旋转与缩放。对于不含一次项的平面二次曲线 $Ax^2+2Bxy+Cy^2=1$，令 $x = 
rac{1}{2}(z+ar{z})$，$y = 
rac{1}{2i}(z-ar{z})$ 可以将其写为复数形式。通过代换 $Z = z\sqrt{A-C+Bi}$，可以直接消去多余的交叉项，得到仅含 $Z^2+ar{Z}^2$ 和 $Zar{Z}$ 的形式，从而非常优雅地给出二次曲线的最简实坐标方程。

## 推导结构
1. **复坐标代换**：代入 $x = 
rac{1}{2}(z+ar{z})$，$y = 
rac{1}{2i}(z-ar{z})$ 至 $Ax^2+2Bxy+Cy^2=1$。
2. **复数方程展开**：展开并合并同类项，得出 $(A-C+Bi)z^2 + (A-C-Bi)ar{z}^2 + 2(A+C)zar{z} = 4$。
3. **构造旋转与缩放**：为使 $z^2$ 的系数变为 $1$，令 $Z = z\sqrt{A-C+Bi}$，其中 $\sqrt{A-C+Bi}$ 代表旋转 $\phi/2$ 与模长缩放。
4. **化简为标准型**：得到 $Z^2 + ar{Z}^2 + 
rac{2(A+C)}{\sqrt{(A-C)^2+B^2}}Zar{Z} = 4$。
5. **还原为实坐标**：令 $Z = X+Yi$，利用 $Z^2+ar{Z}^2=2(X^2-Y^2)$ 和 $Zar{Z}=X^2+Y^2$ 还原出标准坐标下的最简曲线方程。

## 关键公式
- 复数展开二次曲线: $(A-C+Bi)z^2 + (A-C-Bi)ar{z}^2 + 2(A+C)zar{z} = 4$
- 旋转代换: $Z = z\sqrt{A-C+Bi}$
- 化简结果: $(
rac{A+C}{\sqrt{(A-C)^2+B^2}}+1)X^2+(
rac{A+C}{\sqrt{(A-C)^2+B^2}}-1)Y^2=2$

## 体现的方法
- `[[平面二次曲线的复数坐标代换化简法]]`：以复坐标和共轭代换消去二次型交叉项以化简二次曲线的方法。

## 所属系列位置
无。复数工具的应用几何探讨。

## 与其他文章的关系
- 关联 `[[wiki/sources/spaces-1841-矩阵化简二次型-无穷小近似处理抛物型.md]]` 形成了实矩阵对角化与复数代换化简二次曲线的双重对照。

## 原文证据锚点
- `ev::1851::复数二次型展开`：第3段中将 $x,y$ 的实代数式代入得出复二次型形式（公式第2行）的过程。
- `ev::1851::复数坐标代换`：第4段和第5段中令 $Z = z\sqrt{A-C+Bi}$ 代回化简出标准二次形式与实轴方程的过程。
