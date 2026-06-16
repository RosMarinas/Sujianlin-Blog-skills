---
type: concept
title: von Mises-Fisher分布
aliases:
- vMF Distribution
- von Mises-Fisher分布
- Fisher-von Mises分布
definition: 定义在 $(d-1)$ 维超球面 $S^{d-1}$ 上的概率分布，概率密度 $p(x) = C_{d,\kappa} e^{\kappa\langle\mu,x\rangle}$，其中
  $\mu$ 是均值方向，$\kappa$ 是浓度参数（$\kappa=0$ 为球面均匀分布），以余弦相似度作为度量。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-05-17-变分自编码器-七-球面上的VAE-vMF-VAE.md
source_ids:
- '8404'
prerequisites:
- '[[超球面]]'
- '[[余弦相似度]]'
- '[[指数族分布]]'
equivalent_forms: []
direct_consequences:
- '[[球面VAE构造法]]'
- '[[vMF采样]]'
related_formulas:
- '[[vMF概率密度函数]]'
- '[[vMF一阶矩]]'
related_methods:
- '[[球面VAE构造法]]'
series:
- '[[变分自编码器]]'
evidence_spans:
- ev::8404::vMF分布
- ev::8404::从vMF采样
status: draft
updated: '2026-06-12'
---

## 定义

vMF分布是定义在 $(d-1)$ 维超球面 $S^{d-1} = \{x \in \mathbb{R}^d : \|x\| = 1\}$ 上的概率分布。其概率密度函数为：

$$p(x) = C_{d,\kappa} e^{\kappa\langle\mu,x\rangle},\quad x \in S^{d-1}$$

其中 $\mu \in S^{d-1}$ 是均值方向，$\kappa \ge 0$ 是浓度参数（concentration parameter），$C_{d,\kappa}$ 是归一化常数。

## 关键性质

- **浓度参数 $\kappa$**：$\kappa$ 越大，分布越集中在 $\mu$ 方向附近；$\kappa=0$ 时退化为球面上的均匀分布。类比：$\tau = 1/\kappa$ 是温度参数。
- **余弦相似度度量**：$\langle\mu,x\rangle$ 即 $\mu$ 和 $x$ 的夹角余弦。因此vMF分布天然适用于以余弦相似度为度量的场景。
- **各向同性**：归一化常数 $C_{d,\kappa}$ 仅依赖于 $d$ 和 $\kappa$，不依赖于 $\mu$ 的方向。
- **一阶矩**：$\mathbb{E}_{x\sim p(x)}[x] = \frac{d\log Z_{d,\|\xi\|}}{d\|\xi\|} \cdot \frac{\xi}{\|\xi\|}$，方向与 $\xi$ 一致，模长仅依赖 $d$ 和 $\kappa$。

## 在VAE中的应用

在vMF-VAE中：
- 先验取 $\kappa=0$（球面均匀分布）
- 后验取 $p(z|x) = C_{d,\kappa} e^{\kappa\langle\mu(x),z\rangle}$
- KL散度 $KL(p(z|x) \| q(z))$ 仅依赖于 $d$ 和 $\kappa$，为常数，不自变量数据或编码器参数
- 解决了KL散度消失问题