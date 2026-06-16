---
type: example
title: 三球交会定位计算流程
article_id: 10684
article: '[[spaces-10684-三个球的交点坐标-三球交会定位]]'
section: 总的流程
claim: 在一般情形下通过构建三轴正交向量u,v,w，计算投影常数并最终得出精确坐标
notation_mapping:
  standard_u: u
  source_u: u
  standard_v: v
  source_v: v
steps:
- 1. 以o_1为新坐标原点，定义正交基向量 u = o12 / ||o12||
- 2. 提取o13正交余量方向归一化为 v = (o13 - (o13.u)u)/||o13 - (o13.u)u||, w = u x v
- 3. 计算特殊坐标系下投影常数 a = o12.u, b = o13.u, c = o13.v
- 4. 计算代数分量 x = (r1^2 - r2^2 + a^2)/(2a), y = (r1^2 - r3^2 + b^2 - 2bx + c^2)/(2c),
  z = +-sqrt(r1^2 - x^2 - y^2)
- 5. 通过局部坐标反投影得到最终三维坐标 x_glob = x*u + y*v + z*w + o_1
used_concepts:
- - - 三球交会定位
used_formulas:
- - - 三球交会一般坐标系转换公式
used_methods:
- - - 建立局部正交基简化几何问题
source_span: ev::10684::一般情形
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-01-28-三个球的交点坐标-三球交会定位.md
source_ids:
- 10684
status: draft
updated: '2026-06-12'
---

# 三球交会定位计算流程

该实例提供了一个具有高可读性和可复现性的三球交会定位（如GPS定位中的True-range multilateration过程）解析解计算过程。

在一般情形下，求解三个给定球心 $\boldsymbol{o}_1, \boldsymbol{o}_2, \boldsymbol{o}_3$ 及其对应半径 $r_1, r_2, r_3$ 的相交点，若直接联立三维二次方程较为困难。通过平移原点与重构局部正交基，可以将其转化为简单的代数运算。具体计算流程如下：

1. **构建局部正交基**
首先将坐标原点平移至 $\boldsymbol{o}_1$。记球心之间的相对位置向量为 $\boldsymbol{o}_{ij} = \boldsymbol{o}_j - \boldsymbol{o}_i$。利用这些相对位置构建一组新的标准正交基：
- 定义 $x$ 轴方向向量：$\boldsymbol{u}=\frac{\boldsymbol{o}_{12}}{\Vert\boldsymbol{o}_{12}\Vert}$，这使得 $\boldsymbol{o}_2$ 落在局部 $x$ 轴上。
- 定义 $y$ 轴方向向量：提取 $\boldsymbol{o}_{13}$ 垂直于 $\boldsymbol{u}$ 的正交余量方向并归一化，即 $\boldsymbol{v}=\frac{\boldsymbol{o}_{13} - (\boldsymbol{o}_{13}\cdot \boldsymbol{u})\boldsymbol{u}}{\Vert\boldsymbol{o}_{13} - (\boldsymbol{o}_{13}\cdot \boldsymbol{u})\boldsymbol{u}\Vert}$。这使得 $\boldsymbol{o}_3$ 落在局部的 $x,y$ 平面上。
- 定义 $z$ 轴方向向量：利用叉积补全第三个维度，即 $\boldsymbol{w}=\boldsymbol{u}\times \boldsymbol{v}$。

2. **计算投影常数与代数分量**
根据构建的局部坐标系，计算相对距离在各轴上的投影参数：
令 $a = \boldsymbol{o}_{12}\cdot\boldsymbol{u}$（实际上 $a=\Vert\boldsymbol{o}_{12}\Vert$），$b = \boldsymbol{o}_{13}\cdot \boldsymbol{u}$，以及 $c = \boldsymbol{o}_{13}\cdot \boldsymbol{v}$。
在此特殊坐标系下，三个球体的交点坐标 $(x, y, z)$ 可通过如下简化的方程组求解：
$$x = \frac{r_1^2 - r_2^2 + a^2}{2a}$$
$$y = \frac{r_1^2 - r_3^2 + b^2 - 2bx + c^2}{2c}$$
$$z = \pm \sqrt{r_1^2 - x^2 - y^2}$$
这里的 $\pm$ 表明，在一般相交的情形下，交点会存在两个对称解。

3. **反投影恢复全局三维坐标**
最终计算得到的代数分量 $(x, y, z)$ 是在局部坐标系 $(\boldsymbol{u},\boldsymbol{v},\boldsymbol{w})$ 中的坐标。为了获得真实的全局坐标，需要使用该坐标轴和原先的球心 $\boldsymbol{o}_1$ 偏移量进行反向映射：
$$\boldsymbol{x}=x \boldsymbol{u} + y\boldsymbol{v} + z \boldsymbol{w} + \boldsymbol{o}_1$$
这样即可精准求出原坐标系下三个球的交点位置。
