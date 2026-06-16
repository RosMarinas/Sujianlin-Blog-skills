---
type: concept
title: 一般ODE构建框架
aliases:
- General ODE Construction Framework
- ODE扩散模型生产车间
definition: 一个系统性地构造ODE扩散模型的数学框架，核心是将连续方程改写为 $d+1$ 维无散度条件，然后通过格林函数方法（第14篇）或特征线法（第15篇）来求解。该框架可将PFGM引力解和高斯扩散解统一为不同对称性假设下的特例，并支持构造新的ODE扩散模型。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-12-15-生成扩散模型漫谈-十四-构建ODE的一般步骤-上.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-12-22-生成扩散模型漫谈-十五-构建ODE的一般步骤-中.md
source_ids:
- '9370'
- '9379'
prerequisites:
- '[[连续方程]]'
- '[[无散度条件]]'
- '[[格林函数方法]]'
- '[[特征线法]]'
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods:
- '[[万有引力类比构造法]]'
- '[[特征线ODE构造法]]'
series:
- '[[生成扩散模型漫谈]]'
evidence_spans:
- ev::9370::简化方程
- ev::9370::格林函数
- ev::9379::特征线法
status: draft
updated: '2026-06-12'
---

# 一般ODE构建框架

## 一句话总结

一个名副其实的"ODE扩散模型生产车间"，通过系统运用连续方程、无散度条件、格林函数和特征线法等数学工具，为构造各式各样的ODE扩散模型提供了统一而通用的方法论。

## 核心要点

1. **核心方程**：以连续方程 $\frac{\partial p_t}{\partial t} = -\nabla\cdot(\boldsymbol{f}_t p_t)$ 为出发点。由于1个方程对 $d$ 个未知数，存在无穷多解。
2. **两大求解方法**：
   - 格林函数方法（第14篇）：假设对称性（各向同性/时空分离），先解点源再积分。
   - 特征线法（第15篇）：直接设计轨迹，沿特征线同时满足初值和终值条件。
3. **统一解释力**：
   - 全 $d+1$ 维各向同性假设 → PFGM引力解。
   - 空间各向同性假设 + 高斯条件概率 → 标准高斯扩散ODE。
   - 直线轨迹 + 任意先验分布 → Flow Matching框架。
4. **逆向构造**：通过设计累积概率函数 $\psi_t(r)$，可避开复杂积分直接构造新模型。
5. **实践启示**：数学等价的框架在实际效果上仍有差异（引力ODE优于高斯ODE），"什么样的设计才是更好的扩散模型"仍然是有意义的研究问题。

## 来源

- 文章 14（9370）：全文
- 文章 15（9379）：全文