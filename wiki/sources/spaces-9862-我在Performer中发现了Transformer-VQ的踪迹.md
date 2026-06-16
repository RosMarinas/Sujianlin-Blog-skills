---
type: article_summary
title: 我在Performer中发现了Transformer-VQ的踪迹
article_id: "9862"
source_url: https://spaces.ac.cn/archives/9862
date: 2023-11-29
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-11-29-我在Performer中发现了Transformer-VQ的踪迹.md
series: []
topics:
  - "[[向量量化优化]]"
concepts:
  - "[[Transformer-VQ]]"
  - "[[向量量化]]"
  - "[[Performer]]"
methods:
  - "[[狄拉克函数光滑近似法]]"
problem_patterns: []
evidence_spans:
  - ev::9862::Transformer-VQ近似
  - ev::9862::Performer与Transformer-VQ类比
  - ev::9862::狄拉克函数恒等式
  - ev::9862::GMM近似与onehot
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-29-我在Performer中发现了Transformer-VQ的踪迹.md
source_ids:
  - "9862"
status: draft
updated: 2026-06-12
---

# 我在Performer中发现了Transformer-VQ的踪迹

## 文章核心问题

如何通过理解 Performer 这一线性 Attention 架构与 Transformer-VQ（对 Key 序列做 VQ）的内在数学联系，基于狄拉克 $\delta$ 函数与高斯混合模型（GMM）重新推导出 Transformer-VQ，以寻求克服其硬 VQ 带来的梯度估计瓶颈。

## 主要结论

- **Performer是Soft版的Transformer-VQ**：通过将 Performer 展开，发现其投影特征 $\tilde{\boldsymbol{k}}$ 以 $-\|\boldsymbol{k}-\boldsymbol{\omega}_i\|^2/2$ 为 Logits 做 Softmax。当 $\boldsymbol{\omega}_i$ 视为 Codebook 中心，Softmax 在极限状态下收敛为 One-hot 指派，即退化为 Transformer-VQ 中的 $\Delta$ 指派矩阵。
- **硬VQ梯度次优问题**：硬 VQ 采用直通估计器（STE）容易导致梯度不准；且 Transformer-VQ 为了训练线性化采取了梯度截断，这是潜在的效果瓶颈。
- **基于狄拉克函数的新推导**：利用狄拉克 $\delta$ 函数定义，可以将标准 Self-Attention 精确重写为无限维的线性 Attention 格式。
- **GMM离散化通道**：使用高斯混合模型（GMM）对狄拉克条件概率 $p(\boldsymbol{\omega}|\boldsymbol{k}_j)$ 进行多中心逼近，并在高斯方差 $\sigma \to 0$ 时求极限，可以直接导出有限维的线性 Attention（对齐 one-hot 之后即得到 Transformer-VQ）。

## 推导结构

1. **回顾 Transformer-VQ**：介绍以离散矩阵 $\Delta$ 与编码矩阵 $C$ 对 Key 进行逼近的方法，展示其计算复杂度如何下降至线性。
2. **连接 Performer**：展开 Performer 随机投影的高斯指数公式，提取出以 $-\|\boldsymbol{k}-\boldsymbol{\omega}_i\|^2/2$ 为自变量的 Softmax 指派格式。
3. **建立无限维等价**：使用狄拉克 $\delta(\boldsymbol{\omega} - \boldsymbol{k})$ 算子，写出关于 $\exp(\boldsymbol{q}\cdot\boldsymbol{k})$ 的积分恒等式，形式上重写为线性形式。
4. **实施 GMM 离散近似**：将条件概率用 $m$ 个高斯分量混合近似，在零方差极限下收敛，完成硬分类到软概率通道的过渡。

## 关键公式

- **Transformer-VQ 线性变换形式**：
  $$
  \exp\left(Q\hat{K}{}^{\top}\right)V = \exp\left(QC^{\top}\right)(\Delta^{\top}V)
  $$
- **Performer 等效变换形式**：
  $$
  \tilde{\boldsymbol{k}} \propto softmax\begin{pmatrix}e^{-\Vert \boldsymbol{k}-\boldsymbol{\omega}_1\Vert^2 / 2} \\
  e^{-\Vert \boldsymbol{k} - \boldsymbol{\omega}_2\Vert^2 / 2}\\
  \vdots\\
  e^{-\Vert \boldsymbol{k} - \boldsymbol{\omega}_m\Vert^2 / 2} \end{pmatrix}
  $$
- **狄拉克积分恒等式**：
  $$
  e^{\boldsymbol{q}\cdot \boldsymbol{k}} = \int e^{\boldsymbol{q}\cdot \boldsymbol{\omega}}\delta(\boldsymbol{\omega} - \boldsymbol{k})d\boldsymbol{\omega}
  $$
- **条件分布 GMM 近似**：
  $$
  p(\boldsymbol{\omega}|\boldsymbol{k}_j) \approx \sum_{y=1}^m \mathcal{N}(\boldsymbol{\omega};\boldsymbol{c}_y,\sigma^2\boldsymbol{I}) \,p(y|\boldsymbol{k}_j)
  $$

## 体现的方法

- **狄拉克函数光滑近似法**（即 `method::狄拉克函数光滑近似法`）：利用狄拉克 $\delta$ 分布的条件极限，配合高斯混合模型实现积分动力系统的离散化投影计算。

## 所属系列位置

独立研究文章，属于 Transformer 线性 Attention 升级和向量量化优化的交汇领域。

## 与其他文章的关系

- 前置的线性 Attention 理论来源于 [Performer](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/performer.md) (8338, 8601)。
- 离散直通估计（STE）缺陷和量化瓶颈在 [FSQ](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/有限标量量化.md) (9826) 中有所论述。

## 原文证据锚点

- **ev::9862::Transformer-VQ近似**: 第22-38行，展示了利用 $\Delta C$ 近似 $K$ 之后注意力方程变为线性的推导步骤。
- **ev::9862::Performer与Transformer-VQ类比**: 第43-80行，将 Performer 的投影分量等价改写，提取出 Logits 指派结构，说明其与 Transformer-VQ 的对应。
- **ev::9862::狄拉克函数恒等式**: 第86-94行，引入狄拉克分布，将标准 Self-Attention 变换为无限维度的积分线性 Attention 方程。
- **ev::9862::GMM近似与onehot**: 第96-104行，通过 GMM 建模以及高斯极限消去连续积分，推导获得基于 GMM 中心映射的有限维线性 Attention 结果。
