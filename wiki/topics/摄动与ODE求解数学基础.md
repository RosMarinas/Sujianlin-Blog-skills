---
type: topic
title: 摄动与ODE求解数学基础
aliases:
  - Perturbation Theory and ODE Fundamentals
  - 微扰与微分方程基础
scope: 摄动法（微扰理论）的基本原理和操作步骤，高斯型积分的微扰展开技巧，线性常微分方程的算子求解方法，拟齐次微分方程的特殊解法，以及利用李对称性求解微分方程的系统方法。
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-01-16-轻微的扰动-摄动法简介-1.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-02-06-轻微的扰动-摄动法简介-2.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-03-07-轻微的扰动-摄动法简介-3.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2015-02-14-高斯型积分的微扰展开-一.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2015-03-07-高斯型积分的微扰展开-二.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2015-04-26-高斯型积分的微扰展开-三.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-11-30-算子与线性常微分方程-上.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-11-30-算子与线性常微分方程-下.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-09-26-数学基本技艺之23-24-上.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-09-27-数学基本技艺之23-24-下.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-10-29-求解微分方程的李对称方法-一.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-11-26-求解微分方程的李对称方法-二.md
source_ids:
  - 1791
  - 1794
  - 1878
  - 1909
  - 1929
  - 2083
  - 2096
  - 2107
  - 2185
  - 3217
  - 3241
  - 3280
series:
  - [[摄动法简介系列]]
  - [[高斯型积分微扰展开系列]]
  - [[算子与线性常微分方程系列]]
  - [[数学基本技艺之23-24系列]]
  - [[李对称方法求解微分方程系列]]
concepts:
  - [[摄动法]]
  - [[渐近级数]]
  - [[高斯型积分微扰技巧]]
  - [[算子法求解线性常微分方程]]
  - [[拟齐次微分方程]]
  - [[李对称方法]]
  - [[对易子]]
  - [[长期项]]
formulas:
  - x = p + a₁ε + a₂ε² + ... (摄动级数一般形式)
  - ∫exp(-ax²-εx⁴)dx ≈ √(2π/(a+√(a²+6ε))) (封闭近似)
  - y = (D-rₙ)⁻¹...(D-r₁)⁻¹f(x) (算子反演通解)
  - (y-c₁x^{m+1})^{α}(y-c₂x^{m+1})^{β}=C (拟齐次通解)
propositions: []
methods:
  - [[摄动级数展开法]]
  - [[指数变系数展开法]]
  - [[参数变换微扰法]]
  - [[算子分解法]]
  - [[拟齐次变量代换法]]
  - [[李对称降阶法]]
open_questions:
  - 摄动法中长期项的精确消除技巧（PL、多尺度、PLK方法等）未在本文集中深入展开
status: draft
updated: 2026-06-11
---

# 摄动与ODE求解数学基础

本专题汇集苏剑林关于摄动法（微扰理论）和线性/非线性常微分方程求解方法的系列文章，涵盖从小参数展开到算子分解再到李对称方法的完整数学工具链。

## 子专题

- **摄动法**：小参数级数展开的核心思想（代数方程 + 微分方程）
- **高斯型积分微扰**：渐近级数展开 vs 变系数技巧 vs 参数变换优化
- **线性ODE算子法**：微分算子的分解与逆算子逐次积分
- **拟齐次方程**：特殊变量代换技巧和通解结构发现
- **李对称方法**：利用对称群简化/求解微分方程的通用框架
