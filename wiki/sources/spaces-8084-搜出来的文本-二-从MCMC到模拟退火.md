---
type: article_summary
title: "【搜出来的文本】⋅（二）从MCMC到模拟退火"
article_id: "8084"
source_url: https://spaces.ac.cn/archives/8084
date: 2021-01-14
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-01-14-搜出来的文本-二-从MCMC到模拟退火.md
series: [搜出来的文本]
topics: [MCMC, 采样算法, 受限文本生成]
concepts: [马尔可夫链, 细致平稳条件, MCMC, MH采样, Gibbs采样, 模拟退火]
methods: [MCMC, MH采样, Gibbs采样, 模拟退火]
problem_patterns: [高维分布采样困难]
evidence_spans:
  - 8084-马尔可夫链
  - 8084-细致平稳
  - 8084-转移概率
  - 8084-MCMC方法
  - 8084-MH采样
  - 8084-分析思考
  - 8084-Gibbs采样
  - 8084-模拟退火
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-01-14-搜出来的文本-二-从MCMC到模拟退火.md
source_ids:
  - "8084"
status: draft
updated: 2026-06-10
---

## 文章核心问题

MCMC方法如何解决高维分布的采样问题？相比普通拒绝采样，MCMC为什么实用？

## 主要结论

1. MCMC的核心思想是构建以目标分布为平稳分布的马尔可夫链，通过迭代采样逼近目标分布。
2. 细致平稳条件提供了为任意分布构建转移概率的便利工具。
3. 真正的MCMC转移概率将未归一化的概率部分转移到"自身转移"（δ函数），保证归一化和细致平稳条件同时成立。
4. MH采样使用改进的接受率 A = min(1, q(x←y)p(y) / q(y←x)p(x))，只依赖于p的相对值，不需要归一化因子。
5. MCMC相比普通拒绝采样实用的原因：每次只对当前样本微调（而非整体重新生成），接受率更高。
6. Gibbs采样：每次只调整序列中的一个元素，以条件概率p(y|x_{-i})为转移概率，接受率恒为1。
7. 模拟退火（Simulated Annealing）：构造Boltzmann分布p_τ(x) ∝ e^{f(x)/τ}，通过缓慢退火（τ→0）逼近最大值点。

## 推导结构

- 马尔可夫链与平稳分布
- 细致平稳条件
- 转移概率构造（归一化技巧 + δ函数）
- Metropolis算法 → MH采样改进
- MCMC实用原因分析
- Gibbs采样特例
- 模拟退火搜索策略
