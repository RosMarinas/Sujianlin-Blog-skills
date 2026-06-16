---
type: example
title: 中心引力场角动量守恒
article_id: '4054'
article: '[[spaces-4054-外微分浅谈-2-反对称的威力]]'
section: 反对称的威力
claim: 利用外积的反对称性质，在无分量表示下直接推导质点在中心力场运动时的角动量守恒律。
notation_mapping:
  \boldsymbol{x}: \boldsymbol{x}
  \dot{\boldsymbol{x}}: \dot{\boldsymbol{x}}
  \ddot{\boldsymbol{x}}: \ddot{\boldsymbol{x}}
  \land: \land
steps:
- "1. 设定质点在固定引力中心中的运动方程：\n   \\ddot{\\boldsymbol{x}} = -\\frac{\\mu \\boldsymbol{x}}{|\\\
  boldsymbol{x}|^3}"
- "2. 方程两边与位置向量 $\\boldsymbol{x}$ 进行外积运算：\n   \\boldsymbol{x} \\land \\ddot{\\boldsymbol{x}}\
  \ = -\\boldsymbol{x} \\land \\frac{\\mu \\boldsymbol{x}}{|\\boldsymbol{x}|^3}"
- "3. 利用外积的自身零幂性（因反对称性，$\\boldsymbol{x} \\land \\boldsymbol{x} = 0$）消去方程右侧项，得到：\n\
  \   \\boldsymbol{x} \\land \\ddot{\\boldsymbol{x}} = 0"
- "4. 根据 Leibniz 导数求导乘积法则，展开位置与速度外积的导数：\n   \\frac{d}{dt}(\\boldsymbol{x} \\land \\\
  dot{\\boldsymbol{x}}) = \\dot{\\boldsymbol{x}} \\land \\dot{\\boldsymbol{x}} + \\\
  boldsymbol{x} \\land \\ddot{\\boldsymbol{x}}"
- "5. 再次应用反对称性（速度向量自身的叉积 $\\dot{\\boldsymbol{x}} \\land \\dot{\\boldsymbol{x}} = 0$），将公式化简为：\n\
  \   \\frac{d}{dt}(\\boldsymbol{x} \\land \\dot{\\boldsymbol{x}}) = \\boldsymbol{x}\
  \ \\land \\ddot{\\boldsymbol{x}}"
- "6. 联立步骤 3 和步骤 5，得到微分方程：\n   \\frac{d}{dt}(\\boldsymbol{x} \\land \\dot{\\boldsymbol{x}})\
  \ = 0"
- "7. 两边积分，导出角动量守恒律：\n   \\boldsymbol{x} \\land \\dot{\\boldsymbol{x}} = \\boldsymbol{C}"
used_concepts:
- '[[concept::外微分]]'
used_methods:
- '[[method::外积反对称积分法]]'
source_span: ev::4054::角动量守恒
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2016-11-04-外微分浅谈-2-反对称的威力.md
source_ids:
- '4054'
status: draft
updated: '2026-06-12'
---

## 概述

这是一个利用代数反对称性质简化动力学第一积分推导的极佳物理实例。它不仅说明了外积在守恒量寻找中的天然结构优势，也回避了采用常规笛卡尔分量或极坐标下错综复杂的方程积分。

在外微分和向量代数中，外积（通常用 $\land$ 或 $\times$ 表示）被定义为满足分配律的反对称运算。若将向量写为基底展开形式 $\boldsymbol{A}=\boldsymbol{e}_{\mu}A^{\mu}$ 和 $\boldsymbol{B}=\boldsymbol{e}_{\nu}B^{\nu}$，其外积可表示为 $\boldsymbol{A}\land \boldsymbol{B}=\boldsymbol{e}_{\mu}\land\boldsymbol{e}_{\nu} A^{\mu}B^{\nu}$。由于其反对称的代数性质，任何向量与其自身的外积均为零，即对于基向量有 $\boldsymbol{e}_1\land\boldsymbol{e}_1=\boldsymbol{e}_2\land\boldsymbol{e}_2=0$，推广到任意向量则有 $\boldsymbol{x}\land\boldsymbol{x}=0$ 且 $\dot{\boldsymbol{x}}\land\dot{\boldsymbol{x}}=0$。在二维空间中外积得到的是张成平行四边形面积的标量（如 $\boldsymbol{e}_1\land\boldsymbol{e}_2=1$ 且 $\boldsymbol{e}_2\land\boldsymbol{e}_1=-1$），而在三维空间中通过定义 $\boldsymbol{e}_1\land\boldsymbol{e}_2=\boldsymbol{e}_3$ 等，外积可产生与原平面垂直的新向量。

具体到物理动力学中，质点在固定引力中心运动的运动方程为 $\ddot{\boldsymbol{x}}=-\frac{\mu\boldsymbol{x}}{|\boldsymbol{x}|^3}$。在寻找系统的守恒量时，当在运动方程两边同时左乘位置向量 $\boldsymbol{x}$ 进行外积运算时，方程右侧变为 $-\boldsymbol{x}\land \frac{\mu\boldsymbol{x}}{|\boldsymbol{x}|^3}$。因为该项本质上包含了共线向量的外积 $\boldsymbol{x}\land\boldsymbol{x}$，根据反对称运算的特点，它必然等于 $0$，从而我们得到 $\boldsymbol{x}\land \ddot{\boldsymbol{x}}=0$。

同时，根据导数的乘积法则（Leibniz 法则），对 $\boldsymbol{x}\land \dot{\boldsymbol{x}}$ 求关于时间的微商可展开为：
$$
\frac{d}{dt}(\boldsymbol{x}\land \dot{\boldsymbol{x}}) = \dot{\boldsymbol{x}}\land \dot{\boldsymbol{x}}+\boldsymbol{x}\land \ddot{\boldsymbol{x}}
$$
由于速度向量与其自身的外积恒为零（$\dot{\boldsymbol{x}}\land \dot{\boldsymbol{x}}=0$），等式被进一步化简为 $\frac{d}{dt}(\boldsymbol{x}\land \dot{\boldsymbol{x}})=\boldsymbol{x}\land \ddot{\boldsymbol{x}}$。结合前述得到的 $\boldsymbol{x}\land \ddot{\boldsymbol{x}}=0$，这直接给出了微分方程 $\frac{d}{dt}(\boldsymbol{x}\land \dot{\boldsymbol{x}})=0$。

对其进行时间积分，可以直接证明角动量 $\boldsymbol{x}\land \dot{\boldsymbol{x}}$ 为一常数向量 $\boldsymbol{C}$。相较于在直角坐标系或极坐标系中展开庞杂的分量（如算得 $\boldsymbol{A}\land \boldsymbol{B}=A^1 B^2 - A^2 B^1$）进行暴力积分计算，这种纯粹利用代数定义和反对称性质推导角动量守恒律的方法，极大地体现了不可交换的反对称运算在消去动力学对称项、简化物理推导中的强大威力。
