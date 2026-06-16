---
type: example
title: TARFLOW自回归流采样与去噪
article_id: 10667
article: '[[spaces-10667-细水长flow之TARFLOW-流模型满血归来]]'
section: 加噪去噪
claim: 生成流程中，采自标准高斯的z通过g_theta映射后，用其概率梯度加上一步最优去噪
notation_mapping:
  standard_q: q_theta(y)
  source_q: q(x)
steps:
- 1. 从标准高斯噪声中采样 z ~ N(0, I)
- 2. 输入可逆Causal Transformer架构得到带噪生成结果 y = g_theta(z)
- 3. 计算对数似然度在y点的梯度 ∇_y log q_theta(y)
- 4. 执行最终去噪采样：x = y + sigma^2 * ∇_y log q_theta(y)
used_concepts:
- - - TARFLOW
used_formulas:
- - - 流模型最优去噪估计公式
- - - 多块自回归耦合层公式
used_methods:
- - - 流模型去噪采样
source_span: ev::10667::加噪去噪
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-01-17-细水长flow之TARFLOW-流模型满血归来.md
source_ids:
- 10667
status: draft
updated: '2026-06-12'
---

# TARFLOW自回归流采样与去噪

TARFLOW（Normalizing Flows are Capable Generative Models）结合了去噪自编码器的思想，在生成采样中实现了基于对数似然梯度的一步去噪过程，有效提升了流模型的生成质量，并逼近了基于扩散模型或GAN的SOTA效果。

根据前向映射与去噪估计理论，TARFLOW的具体加噪与去噪采样步骤如下：

1. **初始噪声采样**：首先从标准高斯分布中抽取随机噪声，即 $z \sim \mathcal{N}(0, I)$。
2. **前向映射生成带噪结果**：将采样得到的噪声 $z$ 输入到确定性函数（例如基于可逆Causal Transformer架构的流模型网络）中，得到初步的带噪生成结果 $y = g_\theta(z)$。该生成过程的理论分布可表示为 $q_\theta(y) = \int \delta(y - g_\theta(z))q(z)dz$。
3. **计算对数似然梯度**：基于当前流模型建模的概率密度函数 $q_\theta(y)$，计算带噪点 $y$ 处的对数似然度梯度 $\nabla_y \log q_\theta(y)$。
4. **执行最终去噪采样**：利用流模型的最优去噪估计公式，结合设定的噪声方差参数 $\sigma^2$，将对数概率梯度叠加到初步带噪结果上，从而得到最终的高质量目标分布样本：
   $$ x = y + \sigma^2 \nabla_y \log q_\theta(y) $$

这种在生成流程中将由标准高斯映射得来的结果利用概率梯度进行一步最优去噪的机制，使得流模型在保持单步生成与精确似然计算（无须对抗训练）独特优势的同时，大幅改善了旧有流模型（如Glow）在复杂自然图像生成中广泛存在的视觉瑕疵。
