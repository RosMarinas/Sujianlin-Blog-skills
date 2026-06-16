---
type: article_summary
title: 细水长flow之f-VAEs：Glow与VAEs的联姻
article_id: "5977"
source_url: https://spaces.ac.cn/archives/5977
date: 2018-09-21
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-09-21-细水长flow之f-VAEs-Glow与VAEs的联姻.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-09-21-细水长flow之f-VAEs-Glow与VAEs的联姻.md
source_ids:
  - "5977"
status: draft
updated: 2026-06-12
---

# 细水长flow之f-VAEs：Glow与VAEs的联姻

## 文章核心问题

如何整合变分自编码器（VAEs）和常规流模型（Normalizing Flows），利用流模型增强 VAEs 简单的后验分布表达能力以消除图像生成模糊问题，同时利用自编码器的强非线性减少流模型对大量耦合层的依赖以缩小网络规模。

## 主要结论

1. **图像模糊的本质**：传统的 VAEs 假设其后验分布 $p(z|x)$ 为简单的高斯分布，这极大限制了模型的拟合表达能力。自编码器低维重构原始图像的固有方式也是造成生成图像模糊的主因。
2. **f-VAEs 框架**：提出基于流的变分自编码器（f-VAEs）。f-VAEs 中不采用对低维隐空间进行降维，而是使隐变量与输入具有相同大小以避免重构模糊，并引入“条件流”（Conditional Flow）来对极具表现力的非高斯后验分布 $p(z|x)$ 进行参数化建模。
3. **两类特例的数学包容性**：
   - 当条件流退化为一般的缩放平移时，f-VAEs 损失函数完全还原为标准的 VAE 损失函数（含重参数化步骤）。
   - 当条件流的参数与 $x$ 无关且似然方差 $\sigma^2 \to 0$ 时，f-VAEs 损失函数完全还原为标准的无条件流模型（例如加入了高斯噪声的 Glow）。
4. **计算量降低与非线性提升**：在 f-VAEs 中，普通的卷积编码器负责主要的强非线性特征映射，且该映射不需要计算雅可比行列式；无条件流仅需处理简单的变量对齐，使得网络可以使用相比 Glow 浅得多的深度达到相同的采样拟合效果。

## 推导结构

1. **基于条件流的 VAE 损失函数推导**：
   设后验分布 $p(z|x) = \int \delta(z - F_x(u)) q(u) du$（其中 $F_x(u)$ 关于 $u$ 可逆且为条件流，先验 $q(u)$ 是标准高斯分布）。代入 VAEs 联合分布 KL 损失：
   $$KL(\tilde{p}(x)p(z|x) \| q(z)q(x|z)) = \iint \tilde{p}(x) p(z|x) \log \frac{\tilde{p}(x) p(z|x)}{q(x|z)q(z)} dz dx$$
   通过狄拉克 $\delta$ 函数和雅可比行列式变量替换，最终约化得到：
   $$Loss = \iint \tilde{p}(x)q(u)\log \frac{\tilde{p}(x) q(u)}{q(x| F_x(u))q(F_x(u))\left|\det \left[\frac{\partial F_x (u)}{\partial u}\right]\right|} dudx$$
2. **模型简化损失设计**：
   选择 $F_x(u) = F(\sigma_1 u + E(x))$，其中 $F$ 为无条件流，$E(x)$ 为编码器，$q(x|z) = \mathcal{N}(x; G(F^{-1}(z)), \sigma_2^2)$。等效优化损失：
   $$Loss \propto \iint \tilde{p}(x)q(u)\left[ \frac{1}{2\sigma_2^2}\| G(\sigma_1 u + E(x))-x\|^2 + \frac{1}{2}\| F(\sigma_1 u + E(x))\|^2 - \log \left|\det \left[\frac{\partial F(\sigma_1 u + E(x))}{\partial u}\right]\right|\right] dudx$$

## 关键公式

- 条件流后验定义式：
  $$p(z|x) = \int \delta(z - F_x(u))q(u)du$$
- f-VAEs 统一框架损失函数：
  $$\iint \tilde{p}(x)q(u)\log \frac{\tilde{p}(x) q(u)}{q(x| F_x(u))q(F_x(u))\left|\det \left[\frac{\partial F_x (u)}{\partial u}\right]\right|} dudx$$
- 采样生成链：
  $$u \sim q(u), \quad z = F^{-1}(u),\quad x = G(z)$$

## 体现的方法

- **基于条件流的变分后验推断**：用条件可逆映射 $F_x(u)$ 代替普通高斯分布，参数化描述更一般、非对称的隐空间后验概率。
- **不降维流式自编码建模**：规定编码隐空间维度等于输入维度，通过条件方差调节避免传统降维自编码的边界坍缩与模糊，大幅减小网络耦合层的堆叠需求。

## 所属系列位置

本篇为“细水长flow”系列的第 3 篇，是流模型与变分自编码器（VAE）的结合体，首次在大图像拟合上将自编码的非线性优势和流的精确似然优势相结合。

## 与其他文章的关系

- **变分自编码器系列**：f-VAEs 利用条件流扩展了传统变分自编码器的后验分布建模，是 `wiki/series/变分自编码器.md` 的前沿探索。
- **RealNVP & Glow**：f-VAEs 内部将普通的 CNN 作为编解码器，并将 Glow 的简化版作为无条件流变换核心。

## 原文证据锚点

- **f-VAEs 损失函数的严谨证明**：参见原文 `### 推导过程` 下方大段数学代换推导（公式 (75) 到 (87)）。
- **特例退火等价性**：参见原文 `### 两个特例` 公式 (107)-(137)，推导了如何分别退化为标准 VAE 和输入加高斯噪声的流模型。
- **实验与网络拓扑结构对比**：参见原文 `### 实验流程`，给出了 VAEs、流模型和 f-VAEs 在 celeba 上的生成效果与收敛速度比对，并附带了隐变量线性插值图像。
