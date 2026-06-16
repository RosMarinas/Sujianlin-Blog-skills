---
type: concept
title: Fokker-Planck方程
aliases:
- Fokker-Planck Equation
- FP方程
definition: Fokker-Planck方程是描述随机过程边际概率密度$p_t(\boldsymbol{x})$随时间演化的偏微分方程，由SDE的漂移系数$\boldsymbol{f}_t$和扩散系数$g_t$决定，形式为$\partial_t
  p_t = -\nabla\cdot[\boldsymbol{f}_t p_t] + \frac{1}{2}g_t^2\nabla^2 p_t$。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-08-08-生成扩散模型漫谈-六-一般框架之ODE篇.md
source_ids:
- '9228'
prerequisites: []
equivalent_forms: []
direct_consequences:
- '[[前向过程等价性]]'
related_formulas: []
related_methods:
- '[[Fokker-Planck方程推导法]]'
series:
- '[[生成扩散模型漫谈]]'
evidence_spans:
- ev::9228::F-P方程
status: draft
updated: '2026-06-12'
---

在扩散模型的语境中，Fokker-Planck方程被用作等价变换的桥梁。给定前向SDE $d\boldsymbol{x} = \boldsymbol{f}_t(\boldsymbol{x})dt + g_t d\boldsymbol{w}$，其F-P方程为$\frac{\partial}{\partial t} p_t(\boldsymbol{x}) = -\nabla_{\boldsymbol{x}}\cdot[\boldsymbol{f}_t(\boldsymbol{x})p_t(\boldsymbol{x})] + \frac{1}{2}g_t^2 \nabla_{\boldsymbol{x}}\cdot\nabla_{\boldsymbol{x}}p_t(\boldsymbol{x})$。文章通过Dirac delta函数方法推导该方程：将概率密度表达为期望形式的Dirac函数，进行泰勒展开后取期望并取极限。F-P方程的关键作用是：通过将扩散项拆分为不同方式，可以证明不同SDE具有相同的边际分布，从而导出概率流ODE。