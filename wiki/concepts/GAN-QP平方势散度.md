---
type: concept
definition: GAN-QP平方势散度在WGAN式判别器差值上加入距离归一化的二次势能项，使判别器目标本身形成散度，并使最优解自动呈现类似L约束的性质。
title: GAN-QP平方势散度
aliases:
- QP-div
- Quadratic Potential Divergence
source_ids:
- '6163'
- '6214'
evidence_spans:
- ev::6163::平方势散度
- ev::6163::GAN-QP目标
- ev::6214::BiGAN-QP目标
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-11-20-不用L约束又不会梯度消失的GAN-了解一下.md
- Data/Spaces_ac_cn/markdown/Big-Data/2018-12-10-BiGAN-QP-简单清晰的编码-生成模型.md
---

# GAN-QP平方势散度

GAN-QP平方势散度（QP-div, Quadratic Potential Divergence）通过在WGAN式判别器差值的基础上加入距离归一化的二次势能项，直接在对偶空间定义了一种概率散度。它不仅克服了SGAN的梯度消失问题，同时使得判别器的最优解自动满足类似Lipschitz（L）的约束，无需像WGAN那样使用额外的梯度惩罚或谱归一化。

## 数学定义

平方势散度的具体定义如下：

$$
\begin{aligned}&\mathcal{L}[p(x),q(x)] \\
=& \max_{T}\, \mathbb{E}_{(x_r,x_f)\sim p(x_r)q(x_f)}\left[T(x_r,x_f)-T(x_f,x_r) - \frac{(T(x_r,x_f)-T(x_f,x_r))^2}{2\lambda d(x_r,x_f)}\right]\end{aligned}
$$

其中 $\lambda > 0$ 是一个超参数，$d$ 可以是任意一种现成的距离度量（如欧氏距离）。由于该形式在WGAN目标的基础上增加了一个平方形式的势能项 $-\frac{(T(x_r,x_f)-T(x_f,x_r))^2}{2\lambda d(x_r,x_f)}$，因此被称为平方势散度。

## 关键性质与分析

### 1. 免疫梯度消失（极端分布分析）

为了验证其在无交集分布下的表现，考察极端情形的单点分布 $p(x)=\delta(x-\alpha), q(x)=\delta(x-\beta)$，代入散度公式后有：

$$
\mathcal{L}[p(x),q(x)] = \max_{T}\, T(\alpha,\beta)-T(\beta,\alpha) - \frac{(T(\alpha,\beta)-T(\beta,\alpha))^2}{2\lambda d(\alpha,\beta)}
$$

若令 $z = T(\alpha,\beta)-T(\beta,\alpha)$，问题转化为求二次函数 $z - \frac{z^2}{2\lambda d(\alpha,\beta)}$ 的最大值，该最大值为 $\frac{1}{2}\lambda d(\alpha,\beta)$。因此：

$$
\mathcal{L}[p(x),q(x)] = \frac{1}{2}\lambda d(\alpha,\beta)
$$

这表明即使两个分布完全没有交集，度量结果依然与真实样本和生成样本之间的距离 $d(\alpha,\beta)$ 成正比，而不是像SGAN那样收敛到常数 $\log 2$。因此，在极端情况下模型依然能够提供拉近分布距离的梯度，避免了梯度消失的风险。

### 2. 自适应L约束（最优解特性）

通过变分法可以证明该形式下判别器的最优解为：

$$
\frac{p(x_r)q(x_f) - p(x_f)q(x_r)}{p(x_r)q(x_f) + p(x_f)q(x_r)} = \frac{T(x_r,x_f)-T(x_f,x_r)}{\lambda d(x_r, x_f)}
$$

从该等式左侧的值域中容易得出最优解满足：

$$
-1 \leq \frac{T(x_r,x_f)-T(x_f,x_r)}{\lambda d(x_r, x_f)}\leq 1
$$

这意味着最优解自动满足L约束（Lipschitz约束性质）。GAN-QP因此可被视为一种**自适应L约束**的方案。同时可以看到，超参数 $\lambda$ 只是一个缩放因子，模型对 $\lambda$ 的取值是鲁棒的，不会明显影响生成效果。

## 与GAN目标的结合（GAN-QP与BiGAN-QP）

**标准GAN-QP**：基于平方势散度，对抗网络（GAN-QP）的目标转化为：
$$
\begin{aligned}&T= \mathop{\text{argmax}}_T\, \mathbb{E}_{(x_r,x_f)\sim p(x_r)q(x_f)}\left[T(x_r,x_f)-T(x_f,x_r) - \frac{(T(x_r,x_f)-T(x_f,x_r))^2}{2\lambda d(x_r,x_f)}\right] \\
&G = \mathop{\text{argmin}}_G\,\mathbb{E}_{(x_r,x_f)\sim p(x_r)q(x_f)}\left[T(x_r,x_f)-T(x_f,x_r)\right]
\end{aligned}
$$
需要注意的是，二次势能项只用于训练判别器 $T$ 以形成散度约束，绝对不能加入生成器 $G$ 的损失中。如果生成器最小化该二次项，等价于直接最小化度量 $d(x_r,x_f)$ 本身，这是不科学的。实际应用中，尽管 $T$ 理论上是二元函数，简化为一元差值 $T(x_r) - T(x_f)$ 足以取得优秀的生成结果。

**BiGAN-QP扩展**：在同时包含编码器 $E$ 和生成器 $G$ 的BiGAN任务中，GAN-QP的目标可进行平行扩展。通过将判别器的单输入替换为联合分布 $(x, E(x))$ 与 $(G(z), z)$，即令 $\Delta T = T(x,E(x))-T(G(z),z)$，并引入针对隐变量和显变量的均方误差（MSE）重构引导项（同时切断一半的梯度传递以避免强耦合导致的模糊），BiGAN-QP 能够成功训练出一个同时具备清晰编码和生成能力的双向映射模型。
