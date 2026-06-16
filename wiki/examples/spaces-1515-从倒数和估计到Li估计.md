---
type: example
title: 'spaces-1515: 从倒数和估计到Li估计'
article_id: '1515'
article:
- - wiki/sources/spaces-1515-素数定理及加强.md
section: 素数定理及加强
claim: 从素数倒数之和的渐近估计出发，利用差分连续化导数的方法，推导出对数积分表示。
notation_mapping:
  p_n: p_n
  Q_n: Q_n
  Li(N): Li(N)
steps:
- step: 1
  description: 设素数倒数和的良好估计为：$Q_n = \sum_{k=1}^n \frac{1}{p_k} \approx \ln \ln p_n$。
- step: 2
  description: 写出相邻项差分的代数变换：$\frac{1}{p_{n+1}} = Q_{n+1} - Q_n \approx \ln \ln p_{n+1}
    - \ln \ln p_n = \ln \frac{\ln p_{n+1}}{\ln p_n}$。
- step: 3
  description: 设大素数差分为 $\Delta p = p_{n+1} - p_n$，利用泰勒级数展开 $\ln(1+x) \approx x$，将公式变换为：$\ln
    \frac{\ln p_{n+1}}{\ln p_n} = \ln(1 + \frac{\ln p_{n+1} - \ln p_n}{\ln p_n}) \approx
    \frac{\Delta p}{p_n \ln p_n}$。
- step: 4
  description: 联立以上两步：$\frac{1}{p} \approx \frac{\Delta p}{p \ln p} \implies \Delta
    p \approx \ln p$。
- step: 5
  description: 进行连续化代换，令导数 $\frac{dp}{dn} \approx \Delta p$，则微分方程为：$\frac{dp}{dn}
    = \ln p$。
- step: 6
  description: 积分得到 $n = \int_0^p \frac{1}{\ln t} dt$。因为 $n$ 即代表不大于 $p$ 的素数个数 $\pi(p)$，最终得出：$\pi(N)
    \sim Li(N)$。
used_concepts:
- - - concept::素数
used_formulas:
- - - wiki/formulas/对数积分公式.md
used_methods:
- - - method::差分近似导数求解连续极限
source_span: ev::1515::积分推导
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2011-11-19-欧拉数学-素数定理及加强.md
source_ids:
- '1515'
status: draft
updated: '2026-06-12'
---

# spaces-1515: 从倒数和估计到Li估计

本例展示了如何利用差分近似导数的方法，从素数倒数之和的渐近公式出发，将离散的素数序列状态方程转化为连续的常微分方程，从而初等地推导出素数定理的对数积分估计 $Li(N)$。

已知素数倒数和的渐近估计可以写作 $Q_n = \sum_{k=1}^n \frac{1}{p_k} \approx \ln \ln p_n$。考察相邻两项的差分，我们有 $\frac{1}{p_{n+1}} = Q_{n+1} - Q_n \approx \ln \ln p_{n+1} - \ln \ln p_n = \ln \frac{\ln p_{n+1}}{\ln p_n}$。

设相邻素数的差分为 $\Delta p = p_{n+1} - p_n$，在大素数情况下 $\Delta p$ 相对于 $p_n$ 极小。利用一阶泰勒展开式 $\ln(x+\varepsilon) \approx \ln x + \frac{\varepsilon}{x}$，可得 $\ln p_{n+1} \approx \ln p_n + \frac{\Delta p}{p_n}$。进而代入差分公式，并利用近似关系 $\ln(1+x) \approx x$，得到：
$$ \frac{1}{p_{n+1}} \approx \ln \left( 1 + \frac{\Delta p}{p_n \ln p_n} \right) \approx \frac{\Delta p}{p_n \ln p_n} $$

由于 $p_{n+1}$ 与 $p_n$ 差距不大，统一记为 $p$，则有 $\frac{1}{p} \approx \frac{\Delta p}{p \ln p}$，即推导出素数的差分规律 $\Delta p \approx \ln p$。在此基础上进行连续化代换，由于导数 $\frac{dp}{dn}$ 的几何意义近似于区间 $(n, n+1)$ 的平均斜率 $\frac{p_{n+1}-p_n}{(n+1)-n} = \Delta p$，可将差分方程转化为常微分方程 $\frac{dp}{dn} = \ln p$。

对方程进行分离变量并积分，得到 $n = \int \frac{1}{\ln p} dp$。因为 $n$ 恰好代表了不大于 $p$ 的素数个数 $\pi(p)$，最终可以得出素数个数的对数积分表示式 $\pi(N) \sim Li(N) = \int_0^N \frac{1}{\ln t} dt$。相比于经典的素数定理结果 $\pi(N) \sim \frac{N}{\ln N}$，这种基于微积分差分近似的 $Li(N)$ 估计大幅度提升了逼近精度（例如在 $10^{12}$ 的计算范围内，其相对误差从约 $4\%$ 断崖式降低至 $0.0001\%$）。
