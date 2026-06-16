---

type: formula
title: mclip via msign公式
aliases:
- mclip through msign
standard_notation:
  M: input matrix
  I: identity matrix
  alpha: lower singular-value clipping bound
  beta: upper singular-value clipping bound
  msign: matrix sign function
  mclip: singular-value clipping operator
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-07-通过msign来计算奇异值裁剪mclip-上.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-23-通过msign来计算奇异值裁剪mclip-下.md
source_ids:
- '11006'
- '11059'
related_concepts:
- '[[矩阵符号函数(msign)]]'
- '[[奇异值裁剪(mclip)]]'
evidence_spans:
- ev::11006::msign表示mclip推导
- ev::11059::mclip通解
- ev::11059::去嵌套技巧
- ev::11059::奇函数误差抵消
status: draft
updated: "2026-06-14"
latex: \text{mclip}_{[\alpha,\beta]}(M) = \frac{1}{2}[(\alpha+\beta)\text{msign}(M)
  + (\alpha I - M\text{msign}(M)^\top)\text{msign}(\alpha\text{msign}(M)-M) - (\beta
  I - M\text{msign}(M)^\top)\text{msign}(\beta\text{msign}(M)-M)]
symbol_meanings:
  I: identity matrix
  M: input matrix
  alpha: lower singular-value clipping bound
  beta: upper singular-value clipping bound
  mclip: singular-value clipping operator
  msign: matrix sign function
conditions: （待从源文章提取）
appears_in:
- '11006'
- '11059'
---

# mclip via msign公式


## 概述

（待补充）

## 通解 ($[\alpha,\beta]$)

$$\text{mclip}_{[\alpha,\beta]}(M) = \frac{1}{2}[(\alpha+\beta)\text{msign}(M) + (\alpha I - M\text{msign}(M)^\top)\text{msign}(\alpha\text{msign}(M)-M) - (\beta I - M\text{msign}(M)^\top)\text{msign}(\beta\text{msign}(M)-M)]$$

## v1: 嵌套版 ($\alpha=0,\beta=1$)

$$2\text{mclip}(M) = M + \text{msign}(M) + (I - M\text{msign}(M)^\top)\text{msign}(M - \text{msign}(M))$$

## v2: 去嵌套版

$$2\text{mclip}(M) = M + \text{msign}(M) + (\text{msign}(M)-M)\text{msign}(M^\top M - I)$$

## v3: 奇函数误差抵消版 ($\alpha=-1,\beta=1$)

$$2\text{mclip}(M) = (\text{msign}(M)+M)\text{msign}(M^\top M + I) + (\text{msign}(M)-M)\text{msign}(M^\top M - I)$$

## mstep

$$\text{mstep}(M) = \frac{1}{2}[\text{msign}(M) + \text{msign}(M - \text{msign}(M))]$$

## 任意次奇异值多项式

$$U\Sigma^{2n}V^\top = \text{msign}(M)(M^\top M)^n,\quad U\Sigma^{2n+1}V^\top = M(M^\top M)^n$$