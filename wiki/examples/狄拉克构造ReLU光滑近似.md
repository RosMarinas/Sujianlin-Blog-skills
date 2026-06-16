---
type: example
title: 狄拉克构造ReLU光滑近似
article_id: "8718"
article: "article::用狄拉克函数来构造非光滑函数的光滑近似"
section: ReLU激活
claim: 利用狄拉克函数的光滑近似，通过卷积推导出ReLU的各种常见光滑激活函数。
notation_mapping:
  - "$\max(x,0)$": ReLU激活函数
  - "$\varphi(x)$": 狄拉克函数的光滑近似核
  - "$t$": sigmoid导数核的温度参数
  - "$\sigma$": 高斯核的宽度参数
steps:
  - "用sigmoid导数核 $\varphi_t(x) = e^{tx}t/(1+e^{tx})^2$ 代入卷积 $g(x) = \int f(y)\varphi(x-y)dy$"
  - "积分得到 $g(x) = \log(1+e^{tx})/t$，即SoftPlus（$t=1$）"
  - "用高斯核 $\varphi_\sigma(x)$ 代入，积分得到含erf的GELU型近似"
  - "利用 $\max(x,0) = x\theta(x)$，用sigmoid近似阶跃函数得到Swish $x\sigma(tx)$"
used_concepts:
  - "concept::狄拉克函数光滑近似"
  - "concept::函数光滑化"
used_formulas:
  - "formula::GELU双曲正切近似公式"
used_methods:
  - "method::基于狄拉克函数的光滑近似构造法"
problem_pattern: "problem_pattern::非光滑函数可导化"
source_span: ev::8718::ReLU激活
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-10-10-用狄拉克函数来构造非光滑函数的光滑近似.md
source_ids:
  - "8718"
status: draft
updated: 2026-06-12
---

## 示例说明

本示例展示了如何从统一的狄拉克函数卷积框架下统一推导SoftPlus、GELU、Swish等常见光滑激活函数，验证了此方法的通用性。三种激活函数的推导路径分别为：(1) 用sigmoid导数核卷积 $\max(y,0)$ 得SoftPlus $\log(1+e^{tx})/t$；(2) 用高斯核卷积得GELU型近似 $\frac{1}{2}[x + x\,\text{erf}(x/(\sqrt{2}\sigma))]$；(3) 利用 $\max(x,0)=x\theta(x)$ 结合sigmoid近似阶跃函数，得Swish $x\sigma(tx)$。这一统一视角揭示了看似不相关的激活函数之间的深层数学联系。
