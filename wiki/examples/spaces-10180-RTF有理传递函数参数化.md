---
type: example
title: RTF有理传递函数参数化
aliases: []
article_id: '10180'
article:
- - 重温SSM（四）：有理生成函数的新视角
section: 惊喜突现
claim: 展示 RTF 如何把 DFT(K) 写为两个 padded 系数向量 DFT 的比值。
notation_mapping:
  same_as_standard: true
steps:
- 证明生成函数是有理函数
- 在单位根上求值
- 把分子分母识别为 padded a,b 的 DFT
- IDFT 得到卷积核
used_concepts:
- - - S4卷积核生成函数
- - - 有理传递函数
used_formulas:
- - - 有理传递函数公式
used_methods:
- - - 有理传递函数参数化
problem_pattern:
- - 将矩阵幂卷积转为生成函数求值
source_span: ev::10180::惊喜突现::fft_ratio
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-06-27-重温SSM-四-有理生成函数的新视角.md
source_ids:
- '10180'
status: stable
updated: '2026-06-12'
---
## 问题

源文“惊喜突现”讨论 RTF 如何高效计算线性系统卷积核 $\bar{K}_{<L}$。训练时输入 $u_{<L}$ 可以通过 DFT 做卷积，剩下的瓶颈是如何避免显式计算 $\bar{A}^k$。

## 推导

源文先把卷积核的生成函数写成有理函数，即分子、分母都是有限阶多项式。对长度 $L$ 的单位根取值后，可以把这些多项式取值识别为 padded 系数向量的 DFT：
$$
DFT(\bar{K}_{<L})=
\frac{DFT(b_1,b_2,\ldots,b_d,0,\ldots,0)}
{DFT(1,a_1,a_2,\ldots,a_d,0,\ldots,0)}.
$$
随后对这个比值做 IDFT 即可恢复 $\bar{K}_{<L}$。由于 DFT/IDFT 复杂度为 $\mathcal{O}(L\log L)$，且只要求 $d<L$，核心计算不再随 state size $d$ 线性增长。

## 方法与证据

本例体现“把状态空间卷积核转到有理生成函数空间，再用频域除法求核”的方法。证据锚点为 `ev::10180::惊喜突现::fft_ratio`，源文还说明可直接把 $a,b$ 作为训练参数，从 $d^2+2d$ 参数降到 $2d$ 参数。
