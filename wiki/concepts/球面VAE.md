---
type: concept
title: 球面VAE
aliases:
- Spherical VAE
- vMF-VAE
- Hyperspherical VAE
- 超球面VAE
definition: 使用von Mises-Fisher分布替代高斯分布作为先验和后验的VAE变体，隐变量被约束在超球面 $S^{d-1}$ 上（即 $\|z\|=1$），KL散度项为仅依赖于维度
  $d$ 和浓度 $\kappa$ 的常数，从根本上消除了KL散度消失问题。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-05-17-变分自编码器-七-球面上的VAE-vMF-VAE.md
source_ids:
- '8404'
prerequisites:
- '[[变分自编码器]]'
- '[[von Mises-Fisher分布]]'
- '[[KL散度消失]]'
equivalent_forms:
- '[[vMF-VAE目标函数]]'
direct_consequences: []
related_formulas:
- '[[vMF-VAE训练流程]]'
related_methods:
- '[[球面VAE构造法]]'
series:
- '[[变分自编码器]]'
evidence_spans:
- ev::8404::vMF-VAE
status: draft
updated: '2026-06-12'
---

## 定义

球面VAE（vMF-VAE / Spherical VAE）是一种隐变量被约束在超球面上的VAE架构。与标准VAE（使用各向同性高斯分布）不同，球面VAE使用von Mises-Fisher分布来建模先验和后验：

- **先验 $q(z)$**：球面均匀分布（$\kappa=0$），即 $p(z) = C_{d,0}$（常数）。
- **后验 $p(z|x)$**：$p(z|x) = C_{d,\kappa} e^{\kappa\langle\mu(x),z\rangle}$。
- **隐空间约束**：$\|z\| = 1$，$z \in S^{d-1}$。

## 关键特性

1. **KL散度为常数**：$KL(p(z|x) \| q(z))$ 的计算结果仅依赖于 $d$ 和 $\kappa$，不依赖于 $\mu(x)$。这意味着KL项不参与梯度更新，训练简化为"AE + 重参数化"。
2. **无KL消失**：由于KL是常数且 $\kappa > 0$ 时KL > 0，彻底消除了KL散度消失的可能。
3. **余弦相似度度量**：隐变量之间的相似度由余弦相似度衡量，在许多任务中比欧氏距离更自然。
4. **简化架构**：不需要像标准VAE那样同时输出 $\mu$ 和 $\sigma$，只需要输出 $\mu(x)$（球面上的方向）。

## 采样过程

vMF-VAE的重参数化采样分解为两步：
1. 采样 $w \sim e^{\kappa w}(1-w^2)^{(d-3)/2}$（控制与 $\mu$ 的夹角），使用数值逆CDF方法。
2. 采样 $\nu$ 为与 $\mu$ 正交的超球面均匀方向，使用Gram-Schmidt方法。
3. 组合：$z = w\mu + \sqrt{1-w^2}\nu$。

## 局限

$\kappa$ 作为超参数需人工调参，因为保留 $\kappa$ 在采样过程中的梯度困难。