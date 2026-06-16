---
type: method
title: KL散度交替最小化EM法
aliases:
  - KL Alternating Minimization EM
operation_types:
  primary: Align / calibrate by invariance
  secondary:
    - Estimate / sample instead of compute
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-03-15-从最大似然到EM算法-一致的理解方式.md
source_ids:
  - "5239"
method_summary: 通过交替固定隐变量后验分布和模型参数，最小化联合分布KL散度来求解含隐变量的最大似然问题。
typical_structure:
  - 1. E步：固定当前参数θ^(r-1)，计算隐变量后验 p^(r-1)(Y|X) = p_θ(Y|X)。
  - 2. M步：固定后验分布，优化参数 θ^(r) = argmax_θ E_X[Σ_Y p^(r-1)(Y|X) log p_θ(Y)p_θ(X|Y)]。
  - 3. 重复E步和M步直至收敛。
applicability: 适用于含隐变量的概率模型参数估计，如GMM、pLSA、隐马尔可夫模型等。
related_methods:
  - "[[近似曲线迭代法]]"
examples:
  - "[[spaces-4277-pLSA的EM算法推导]]"
  - "[[spaces-4277-KMeans的EM推导]]"
evidence_spans:
  - "ev::5239::em_alternating_minimization"
status: draft
updated: 2026-06-13
---

## 适用问题

含隐变量的概率模型参数估计问题，如高斯混合模型（GMM）、pLSA、隐马尔可夫模型（HMM）等。当观测数据$X$背后存在未观测的隐变量$Y$时，直接最大化边际似然$p_\theta(X)$通常不可行。

## 核心变换

**输入**：观测数据$X$、含隐变量$Y$的概率模型$p_\theta(X,Y)$
**输出**：参数$\theta$的最大似然估计

从联合分布KL散度出发：
$$
KL(\tilde{p}(X,Y) \| p_\theta(X,Y)) = \iint \tilde{p}(X,Y) \log \frac{\tilde{p}(X,Y)}{p_\theta(X,Y)} dXdY
$$
其中$\tilde{p}(X,Y) = \tilde{p}(X)\tilde{p}(Y|X)$。展开后得到交替优化形式：
- **E步**：固定$\theta^{(r-1)}$，最小化KL得后验$\tilde{p}(Y|X) = p_{\theta^{(r-1)}}(Y|X)$
- **M步**：固定后验，最大化完整数据对数似然的期望：$\theta^{(r)} = \arg\max_\theta \mathbb{E}_{X}[\sum_Y p^{(r-1)}(Y|X) \log p_\theta(Y)p_\theta(X|Y)]$

## 典型步骤

1. **初始化参数**：随机初始化$\theta^{(0)}$
2. **E步**：利用当前参数$\theta^{(r-1)}$计算隐变量后验分布$p_{\theta^{(r-1)}}(Y|X)$
3. **构造Q函数**：$Q(\theta, \theta^{(r-1)}) = \mathbb{E}_{Y|X,\theta^{(r-1)}}[\log p_\theta(X,Y)]$
4. **M步**：最大化$Q$函数更新参数$\theta^{(r)} = \arg\max_\theta Q(\theta, \theta^{(r-1)})$
5. **收敛判断**：检查参数或似然变化是否小于阈值；否则返回步骤2

## 直觉

EM算法的本质是"用已知替代未知"：观测数据$X$的似然$p_\theta(X)$难以直接优化，但完整数据$(X,Y)$的似然$p_\theta(X,Y)$通常有简单形式。E步用当前参数估计隐变量的分布（填空）；M步基于填充后的完整数据估计参数。从KL散度视角看，EM就是交替固定$\theta$和后验$\tilde{p}(Y|X)$，一步步降低联合分布KL散度。

K-Means是EM的一个特例：E步等价于将每个点分配给最近的聚类中心（硬分配），M步更新聚类中心为类内均值。

## 边界

- EM收敛到局部最优，对初始值敏感，需要多次随机重启
- E步需要后验$p(Y|X)$可计算，对于复杂模型需近似（如变分EM）
- 假设数据独立同分布，不适用于序列依赖过强的场景（需HMM等变体）
- M步的Q函数最大化需解析可解，否则需数值优化

## 例子

- GMM参数估计：E步计算每个样本属于各高斯分量的责任度，M步更新均值、协方差和混合系数
- pLSA主题模型：E步计算文档-主题和词-主题分布，M步更新主题-词分布
- HMM训练（Baum-Welch）：E步计算前向后向概率，M步更新转移矩阵和发射矩阵

## 证据

- ev::5239::em_alternating_minimization：从$KL(\tilde{p}(X,Y)\|p_\theta(X,Y))$出发的交替优化推导
- ev::5239::K-Means作为EM特例：硬分配对应E步，中心更新对应M步
