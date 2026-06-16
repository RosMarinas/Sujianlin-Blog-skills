---
type: example
title: 二维球面黎曼度量
article_id: '3969'
article: '[[spaces-3969-理解黎曼几何-2-从勾股定理到黎曼度量]]'
section: 一些例子
claim: 通过球面参数方程，推导半径为 1 的二维球面的对称度规线元。
notation_mapping:
  g_{\mu\nu}: g_{\mu\nu}
  ds^2: ds^2
  \theta: \theta
  \varphi: \varphi
steps:
- "1. 设定单位球面的欧氏坐标参数方程：\n   x = \\sin\\theta \\cos\\varphi\n   y = \\sin\\theta \\\
  sin\\varphi\n   z = \\cos\\theta"
- "2. 计算各坐标的微分项：\n   dx = \\cos\\theta \\cos\\varphi d\\theta - \\sin\\theta \\sin\\\
  varphi d\\varphi\n   dy = \\cos\\theta \\sin\\varphi d\\theta + \\sin\\theta \\\
  cos\\varphi d\\varphi\n   dz = -\\sin\\theta d\\theta"
- "3. 代入欧氏平面直角坐标系下的度规公式：\n   ds^2 = dx^2 + dy^2 + dz^2"
- "4. 展开并合并 $d\\theta^2$ 和 $d\\varphi^2$ 以及交叉项的系数：\n   - $d\\theta^2$ 项系数为：$\\cos^2\\\
  theta \\cos^2\\varphi + \\cos^2\\theta \\sin^2\\varphi + \\sin^2\\theta = \\cos^2\\\
  theta + \\sin^2\\theta = 1$\n   - $d\\varphi^2$ 项系数为：$\\sin^2\\theta \\sin^2\\varphi\
  \ + \\sin^2\\theta \\cos^2\\varphi = \\sin^2\\theta$\n   - 交叉项 $d\\theta d\\varphi$\
  \ 的系数为：$-2\\sin\\theta \\cos\\theta \\sin\\varphi \\cos\\varphi + 2\\sin\\theta\
  \ \\cos\\theta \\sin\\varphi \\cos\\varphi = 0$"
- "5. 合并得出二维球面度规二次型：\n   ds^2 = d\\theta^2 + \\sin^2\\theta d\\varphi^2"
used_concepts:
- '[[concept::黎曼度量]]'
used_formulas:
- '[[formula::黎曼度量二次型]]'
source_span: ev::3969::二维球面度规
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2016-10-14-理解黎曼几何-2-从勾股定理到黎曼度量.md
source_ids:
- '3969'
status: draft
updated: '2026-06-12'
---

## 概述
这是一个最经典的弯曲流形度规例子。它展示了如何通过外在的嵌入映射式，计算内蕴的黎曼度规二次型。在黎曼几何中，弯曲空间的黎曼度量一定是非常数的，而半径为 1 的二维球面（需要注意区别于三维空间中的球坐标系）就是理解非常数黎曼度量最生动具体的特例之一。

## 二维球面度规推导
我们在平直的三维欧氏空间中，通过直角坐标系来考察相邻两点间的距离平方（即勾股定理的微小形式）：
$$ ds^2 = dx^2 + dy^2 + dz^2 $$

根据几何设定，建立半径为 1 的单位二维球面的坐标参数方程：
$$
\left\{\begin{aligned}&x=\sin\theta\cos\varphi\\
&y=\sin\theta\sin\varphi\\
&z=\cos\theta\end{aligned}\right.
$$
这里，$\theta$ 代表极角，$\varphi$ 代表方位角。由于度量刻画的是坐标点间的微小位移 $ds$，我们需要对各个坐标分量取全微分，得到微分项：
$$ dx = \cos\theta\cos\varphi d\theta - \sin\theta\sin\varphi d\varphi $$
$$ dy = \cos\theta\sin\varphi d\theta + \sin\theta\cos\varphi d\varphi $$
$$ dz = -\sin\theta d\theta $$

接下来，将这组微分表达式直接代入三维欧氏平面的度规公式 $ds^2 = dx^2 + dy^2 + dz^2$ 中并展开。在此过程中我们需要分别合并 $d\theta^2$、$d\varphi^2$ 以及交叉项 $d\theta d\varphi$ 的系数：

1. **$d\theta^2$ 的系数化简：**
   该项由 $dx^2$ 贡献 $\cos^2\theta\cos^2\varphi$，$dy^2$ 贡献 $\cos^2\theta\sin^2\varphi$，以及 $dz^2$ 贡献 $\sin^2\theta$。合并可得：
   $$ \cos^2\theta\cos^2\varphi + \cos^2\theta\sin^2\varphi + \sin^2\theta = \cos^2\theta(\cos^2\varphi + \sin^2\varphi) + \sin^2\theta = \cos^2\theta + \sin^2\theta = 1 $$

2. **$d\varphi^2$ 的系数化简：**
   该项由 $dx^2$ 贡献 $\sin^2\theta\sin^2\varphi$，$dy^2$ 贡献 $\sin^2\theta\cos^2\varphi$。合并可得：
   $$ \sin^2\theta\sin^2\varphi + \sin^2\theta\cos^2\varphi = \sin^2\theta(\sin^2\varphi + \cos^2\varphi) = \sin^2\theta $$

3. **交叉项 $d\theta d\varphi$ 的系数化简：**
   该项在 $dx^2$ 展开中为 $-2\sin\theta\cos\theta\sin\varphi\cos\varphi$，在 $dy^2$ 展开中为 $2\sin\theta\cos\theta\sin\varphi\cos\varphi$。两项正好互为相反数，相互抵消：
   $$ -2\sin\theta\cos\theta\sin\varphi\cos\varphi + 2\sin\theta\cos\theta\sin\varphi\cos\varphi = 0 $$

综上所述，所有交叉项消失，最终我们可以合并得出这个单位二维球面上的对称度规二次型：
$$ ds^2 = d\theta^2 + \sin^2\theta d\varphi^2 $$

从最终的结果可以看出，这个黎曼度量的形式为 $ds^2 = g_{\mu\nu} dx^{\mu} dx^{\nu}$，其矩阵是对角阵，且分量 $g_{\varphi\varphi} = \sin^2\theta$ 并不是常数。这种非常数的度规性质，正是该二维曲面发生“弯曲”的数学根源。
