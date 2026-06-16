---
type: article_summary
title: "[欧拉数学]素数有无穷多个的两个证明"
article_id: "1484"
source_url: https://spaces.ac.cn/archives/1484
date: 2011-10-02
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2011-10-02-欧拉数学-素数有无穷多个的两个证明.md
series:
  - [[wiki/series/欧拉数学.md]]
concepts:
  - [[concept::素数]]
methods:
  - [[method::素数积加一构造法]]
  - [[method::基于生成函数的欧拉乘积展开]]
evidence_spans:
  - ev::1484::欧几里得证明
  - ev::1484::欧拉证明
  - ev::1484::素数定理联系
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2011-10-02-欧拉数学-素数有无穷多个的两个证明.md
source_ids:
  - "1484"
status: draft
updated: 2026-06-11
---

# [欧拉数学]素数有无穷多个的两个证明

本文介绍了两个关于素数无穷性的经典证明：一个是欧几里得的初等构造法，另一个是欧拉基于等比级数和生成函数的解析证明。最后探讨了欧拉证明与素数定理之间的启发性初等联系。

## 核心内容

- **欧几里得证明**：采用反证法。假设素数有限，记为 $p_1, \dots, p_n$。构造 $P = p_1 \dots p_n + 1$。若 $P$ 为素数，则产生新素数；若 $P$ 为合数，其必有不属于已知列表的新素数因子。均导出矛盾。
- **欧拉乘积证明**：利用等比级数求和公式，对每个素数 $p$ 展开 $S(p) = \sum_{k=0}^{\infty} p^{-k} = \frac{1}{1-p^{-1}}$。将所有素数的项相乘，根据算术基本定理，乘积 $K = \prod_p S(p)$ 等于调和级数 $\sum_{n=1}^{\infty} \frac{1}{n}$。由于调和级数发散，若素数只有有限个，则乘积 $K$ 必定有限，从而导致矛盾。
- **素数定理的初等联系**：利用级数近似 $1 + 1/2 + \dots + 1/n \approx \ln n$，将欧拉乘积倒过来得出 $\prod_{p \le n} (1 - 1/p) \approx \frac{1}{\ln n}$。在此基础上，通过粗糙的整除筛法估计 $\pi(n) \approx n \prod_{p \le n} (1 - 1/p) \approx \frac{n}{\ln n}$，这与素数定理的形式高度一致。
