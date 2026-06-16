---
type: proposition
title: RTF将SSM卷积核参数化为有理生成函数
aliases:
  []
statement: RTF 观察到 SSM 卷积核生成函数是有理函数，并直接训练分子、分母多项式系数来简化参数化与计算。
assumptions:
  - 源文对应章节的建模假设成立。
requires:
  - [[S4卷积核生成函数]]
  - [[有理传递函数]]
  - [[友矩阵]]
proof_route: 用伴随矩阵和行列式把生成函数写成分式多项式，再在单位根上将 DFT(K) 写成两个 padded 系数向量 DFT 的比。
methods:
  []
limits:
  - 不自动推广到未在源文推导的后续模型。
examples:
  []
evidence_spans:
  - ev::10180::有理函数::rational
  - ev::10180::惊喜突现::fft_ratio
  - ev::10180::另起炉灶::ab_params
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-27-重温SSM-四-有理生成函数的新视角.md
source_ids:
  - "10180"
status: stable
updated: 2026-06-09
---
## 命题

RTF 观察到 SSM 卷积核生成函数是有理函数，并直接训练分子、分母多项式系数来简化参数化与计算。

## 证明路线

用伴随矩阵和行列式把生成函数写成分式多项式，再在单位根上将 DFT(K) 写成两个 padded 系数向量 DFT 的比。

## 适用边界

不把背景提到的 Mamba/S5 结论并入本 stable 命题。
