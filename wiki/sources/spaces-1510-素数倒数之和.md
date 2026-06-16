---
type: article_summary
title: "[欧拉数学]素数倒数之和"
article_id: "1510"
source_url: https://spaces.ac.cn/archives/1510
date: 2011-11-19
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2011-11-19-欧拉数学-素数倒数之和.md
series:
  - [[wiki/series/欧拉数学.md]]
concepts:
  - [[concept::素数]]
methods:
  - [[method::基于生成函数的欧拉乘积展开]]
evidence_spans:
  - ev::1510::收敛性引理
  - ev::1510::倒数和发散证明
  - ev::1510::双对数估计
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2011-11-19-欧拉数学-素数倒数之和.md
source_ids:
  - "1510"
status: draft
updated: 2026-06-11
---

# [欧拉数学]素数倒数之和

本文证明了所有素数的倒数之和发散。首先给出了连接级数与无穷乘积收敛性行为一致的重要引理，并利用欧拉乘积“金钥匙”与平均值不等式放缩，完成了对素数倒数和发散性的解析证明。

## 核心内容

- **收敛性一致引理**：若无限正项数列 $a_n > 0$，定义 $S = \sum_{k=1}^n a_k$，$T = \prod_{k=1}^n (1+a_k)$。通过数学归纳法和平均不等式（AM-GM）及极限定义可证明：
  $$1+S < T < e^S$$
  因此，$\sum a_n$ 与 $\prod (1+a_n)$ 的敛散性完全一致，且 $e^S$ 是 $T$ 的优良近似。
- **素数倒数之和发散证明**：
  1. 使用“金钥匙”在 $s=1$ 处的截断形式：
     $$\prod_{q \le p} \frac{q}{q-1} = 1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{p} + \dots > \ln(p+1)$$
  2. 利用不等式关系 $\frac{q}{q-1} < 1 + \frac{1}{q-1}$（对第 $n$ 个素数有 $\frac{p_n}{p_n-1} < 1 + \frac{1}{p_{n-1}}$）将乘积放缩为：
     $$\ln(p+1) < 2 \prod_{q \le p} (1 + 1/q)$$
  3. 套用引理 $T < e^S$，得到：
     $$\ln(p+1) < 2 e^{Q} \quad \text{其中 } Q = \sum_{q \le p} \frac{1}{q}$$
  4. 对两边取对数，得到双对数下界估计：
     $$Q > \ln \ln (p+1) - \ln 2$$
  5. 随着素数上限 $p \to \infty$，$\ln \ln (p+1) \to \infty$，故所有素数倒数之和发散。
- **渐近估计**：由 $T \approx e^S$ 近似，可认为 $\ln \ln p$ 是素数倒数之和 $Q$ 的一个良好渐近估计。
