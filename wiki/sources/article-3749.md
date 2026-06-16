---
type: article_summary
article_id: "3749"
source_url: https://spaces.ac.cn/archives/3749
date: 2016-05-30
category: Mathematics
series: [[路径积分系列]]
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-05-30-路径积分系列-1-我的毕业论文.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-05-30-路径积分系列-1-我的毕业论文.md
source_ids:
  - "3749"
status: draft
updated: 2026-06-10
---

# article-3749: 路径积分系列：1.我的毕业论文

## 文章核心问题

介绍毕业论文《随机游走、随机微分方程与偏微分方程的路径积分方法》的整体框架和目标：从随机游走模型出发，引出路径积分方法，实现随机游走、随机微分方程与抛物型偏微分方程的相互转化。

## 主要结论

1. 路径积分方法可抽象为一个通用的数学工具，不限于量子力学领域。
2. 随机游走、随机微分方程和抛物型偏微分方程三者可通过路径积分方法相互转化。
3. 不对称随机游走是对称随机游走的重要推广，现有文献对此研究不足。
4. 在国内推广路径积分方法具有重要的学术价值。

## 推导结构

本文为整篇毕业论文的总纲，列出五章结构：
- 第1章：随机游走（对称与非对称模型、简化形式、计算机模拟）
- 第2章：路径积分（从点的概率到路径的概率、对路径进行求和、抛物方程的路径积分、从路径积分到偏微分方程、算例）
- 第3章：随机微分方程（概念、线性SDE、雅可比行列式计算、路径积分方法）
- 第4章：例子（股票价格模型）
- 第5章：论文综述

## 关键公式

- 随机游走的概率分布：正态分布形式
- 路径积分的泛函积分形式
- SDE与随机游走的等价关系

## 体现的方法

- **path integral formulation** → discrete ↔ continuous bridge: 通过离散化路径再取连续极限构造路径积分
- **random walk → diffusion limit** → discrete ↔ continuous bridge: 从离散随机游走到连续扩散方程
- **SDE path integral method** → discrete ↔ continuous bridge: 从SDE的离散化构造路径积分

## 所属系列位置

路径积分系列第1篇，提纲挈领式导言，介绍毕业论文整体结构。

## 与其他文章的关系

- [[article-3750]]（第2篇）详述随机游走模型
- [[article-3757]]（第3篇）详述路径积分形式
- [[article-3762]]（第4篇）建立SDE与路径积分的联系
- [[article-3766]]（第5篇）给出具体案例和综述

## 原文证据锚点

- ev::3749::论文摘要：文章摘要中明确指出"实现了随机游走、随机微分方程与抛物型微分方程的相互转化"
- ev::3749::目录结构：展示了全文五章的组织框架
- ev::3749::推广目的：强调"在国内推广路径积分方法"的学术价值

## 参考文献

- [1] Hagen Kleinert, "Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets" (第5版)
- [5] Feynman, "量子力学与路径积分"
- [8] Carson C. Chow, Michael A. Buice, "Path Integral Methods for Stochastic Differential Equations"
- [10] Belal E. Baaquie, "Quantum Finance: Path Integrals and Hamiltonians for Options and Interest Rates"
