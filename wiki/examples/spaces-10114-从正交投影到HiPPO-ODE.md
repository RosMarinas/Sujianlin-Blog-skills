---
type: example
title: 从正交投影到HiPPO ODE
aliases: []
article_id: '10114'
article:
- - 重温SSM（一）：线性系统和HiPPO矩阵
section: 一般框架
claim: 展示如何从 L2 正交投影系数对时间求导，得到有限维线性状态动力学。
notation_mapping:
  same_as_standard: true
steps:
- 选择正交基并写出最优投影系数
- 对动态区间映射后的系数求导
- 用分部积分将结果闭合为系数线性组合
used_concepts:
- - - 线性状态空间ODE
- - - HiPPO矩阵
used_formulas:
- - - 线性状态空间ODE公式
used_methods:
- - - 正交基投影推导状态动力学
problem_pattern:
- - 将在线记忆转为有限维系数动力学
source_span: ev::10114::一般框架::projection_coefficients
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
source_ids:
- '10114'
status: stable
updated: '2026-06-12'
---
## 问题

源文“一般框架”把 HiPPO 的在线函数逼近问题抽象成：在区间 $[a,b]$ 上用正交基 $\{g_n(t)\}_{n=0}^N$ 逼近目标函数 $u(t)$，并在观察窗口 $[0,T]$ 随时间扩张时更新有限维系数。

## 推导

对标准正交基，最小化
$$
\int_a^b\left[u(t)-\sum_{n=0}^Nc_ng_n(t)\right]^2dt
$$
给出投影系数
$$
c_n^*=\int_a^bu(t)g_n(t)dt.
$$
当历史区间由映射 $s\mapsto t_{\leq T}(s)$ 拉回到固定区间时，系数变为
$$
c_n(T)=\int_a^bu(t_{\leq T}(s))g_n(s)ds.
$$
源文随后对 $T$ 求导，并用分部积分把 $u'(t_{\leq T}(s))$ 的项转成边界项与基函数导数项。选择具体的多项式正交基后，这些导数项可闭合成有限个系数的线性组合，从而得到线性状态 ODE。

## 方法与证据

本例体现“正交投影系数随窗口变化求导，分部积分闭合为有限维动力学”的方法。证据锚点为 `ev::10114::一般框架::projection_coefficients`，源文随后用 Legendre 多项式继续推出 HiPPO 矩阵。
