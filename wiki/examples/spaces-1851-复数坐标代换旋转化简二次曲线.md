---
type: example
title: 复数坐标代换旋转化简二次曲线
article_id: '1851'
article:
- - wiki/sources/spaces-1851-用复数化简二次曲线的尝试.md
section: 用复数化简二次曲线的尝试
claim: 通过复坐标及共轭代换直接消去平面二次曲线中的交叉项得出标准型
notation_mapping:
  z: 平面复数坐标
  \bar{z}: z 的共轭复数
  Z: 旋转并归一化后的复数坐标
  X: 变换后的实直角坐标轴X
  Y: 变换后的实直角坐标轴Y
steps:
- 1. 给定平面曲线 Ax^2+2Bxy+Cy^2=1，引入复坐标 z = x+yi。
- 2. 代换 x = \frac{1}{2}(z+\bar{z}) 和 y = \frac{1}{2i}(z-\bar{z}) 进曲线方程。
- 3. 展开并整理成复数表达式：(A-C+Bi)z^2 + (A-C-Bi)\bar{z}^2 + 2(A+C)z\bar{z} = 4。
- 4. 构造旋转缩放复数代换 Z = z\sqrt{A-C+Bi} 以消去 z^2,\bar{z}^2 的复系数。
- 5. 变形为标准形式：Z^2 + \bar{Z}^2 + \frac{2(A+C)}{\sqrt{(A-C)^2+B^2}}Z\bar{Z} = 4。
- 6. 设 Z = X+Yi，代回实坐标关系，得出标准实直角方程：(\frac{A+C}{\sqrt{(A-C)^2+B^2}}+1)X^2+(\frac{A+C}{\sqrt{(A-C)^2+B^2}}-1)Y^2=2。
used_concepts:
- '[[复数化简二次曲线]]'
used_formulas:
- '[[平面二次曲线复数最简形式公式]]'
used_methods:
- '[[平面二次曲线的复数坐标代换化简法]]'
source_span: ev::1851::复数坐标代换
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2013-01-02-用复数化简二次曲线的尝试.md
source_ids:
- '1851'
status: stable
updated: '2026-06-12'
---

# 复数坐标代换旋转化简二次曲线

## 问题

源文只考虑不含抛物线的二次曲线
$$
Ax^2+2Bxy+Cy^2=1,
$$
目的是用复数坐标把平移、旋转相关的化简写得更直接。

## 推导

令 $z=x+yi$，则
$$
x=\frac{1}{2}(z+\bar{z}),\qquad y=\frac{1}{2i}(z-\bar{z}).
$$
代入后，二次曲线变为
$$
(A-C+Bi)z^2+(A-C-Bi)\bar{z}^2+2(A+C)z\bar{z}=4.
$$
为了把它改写成 $z\bar{z}$ 与 $z^2+\bar{z}^2$ 的组合，源文取
$$
Z=z\sqrt{A-C+Bi}.
$$
于是得到
$$
Z^2+\bar{Z}^2+\frac{2(A+C)}{\sqrt{(A-C)^2+B^2}}Z\bar{Z}=4,
$$
再写回实部虚部 $X,Y$，交叉项被消去，曲线化为标准平方项形式。

## 方法与证据

本例的方法是“复坐标代换加复数缩放旋转”，证据锚点为 `ev::1851::复数坐标代换`。源文特别指出，矩阵化简时旋转变换具体形式较难给出，而复数直接给出 $Z=z\sqrt{A-C+Bi}$。
