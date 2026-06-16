---
type: example
title: spaces-6163 GAN-QP平方势散度
source_ids:
- '6163'
evidence_spans:
- ev::6163::平方势散度
- ev::6163::GAN-QP目标
notation_mapping:
  p: p(x)
  q: q(x)
  T: T
  Delta_T: T(x_r,x_f)-T(x_f,x_r)
  d: d(x_r,x_f)
  lambda: lambda
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-11-20-不用L约束又不会梯度消失的GAN-了解一下.md
article_id: '6163'
article: '[[spaces-6163-不用L约束又不会梯度消失的GAN-了解一下]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

# spaces-6163 GAN-QP平方势散度

源文中提出了一种直接在对偶空间分析和构造概率散度的新思路。通常构建GAN框架需要先寻找概率散度，再推导其对偶形式，最后转化为极小-极大游戏（min-max game）。但实际上，第一步并非必要。我们可以直接在对偶空间中构造满足散度基本定义的标量函数（即恒满足 $\mathcal{D}[p, q]\geq 0$ 且 $\mathcal{D}[p, q]=0\Leftrightarrow p=q$），而无需关心其在原空间具体对应的是JS散度还是W距离。

例如，在标准GAN（SGAN）中，判别器损失基于JS散度的对偶形式定义为：
$$
\mathcal{D}[p(x),q(x)] = \max_T\, \frac{1}{2}\mathbb{E}_{x\sim p(x)}[\log \sigma(T(x))] + \frac{1}{2}\mathbb{E}_{x\sim q(x)}[\log (1 - \sigma(T(x)))] + \log 2
$$
源文深入分析了SGAN可能产生梯度消失的根本原因：考虑一个极端情形，即真实分布和生成分布退化为毫无交集的单点分布 $p(x)=\delta(x-\alpha)$ 和 $q(x)=\delta(x-\beta)$（$\alpha\neq\beta$），由于缺乏对判别器 $T$ 的有效约束，为了求得上确界，模型会让 $T(\alpha)\to +\infty$ 且 $T(\beta)\to -\infty$。此时该散度最大值完全退化为一个常数 $\log 2$，导致生成器在训练时梯度消失，无法获得有效的优化信号。

为克服这一缺陷，源文中把判别器差值 $\Delta T$ 和样本距离 $d(x_r,x_f)$ 组合成二次势能项，从而直接在对偶空间定义QP-div并导出GAN-QP训练目标。该方法不需要像WGAN那样引入复杂的L约束（Lipschitz约束），同时彻底避免了SGAN的梯度消失问题，实验表明其具备不逊色于甚至优于WGAN的生成表现。
