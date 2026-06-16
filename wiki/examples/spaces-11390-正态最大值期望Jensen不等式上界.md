---
type: example
title: 正态最大值期望Jensen不等式上界
article_id: 11390
article: '[[spaces-11390-n个正态随机数的最大值的渐近估计]]'
section: 快速上界
claim: 使用Jensen不等式与exp函数的代数展开，推导最大值期望的不等式上界
notation_mapping:
  standard_E: E[z_max]
  source_E: E[z_max]
steps:
- 1. 对任何t > 0，写出指数化等式 exp(t * E[z_max])
- 2. 应用Jensen不等式得到极小上界 exp(t * E[z_max]) <= E[exp(t * z_max)]
- 3. 将最大值放大为求和，利用独立性 sum_i E[exp(t * z_i)] = n * exp(t^2/2)
- 4. 两边取对数并选择最优参数 t = sqrt(2 log n)，解得 E[z_max] <= sqrt(2 log n)
used_concepts:
- - - 正态随机变量最大值
used_formulas:
- - - 正态随机数最大值期望渐近估计公式
used_methods:
- - - Jensen不等式放缩
source_span: ev::11390::快速上界
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-11-06-n个正态随机数的最大值的渐近估计.md
source_ids:
- 11390
status: draft
updated: '2026-06-12'
---

# 正态随机值期望Jensen不等式上界

这是概率期望估计中非常巧妙地利用凸函数和最大值放缩的经典推导例子，用以证明 $n$ 个独立标准正态随机数最大值的期望渐近上界。

设 $z_1, z_2, \cdots, z_n \sim \mathcal{N}(0,1)$ 为 $n$ 个独立同分布的标准正态随机变量，其最大值记为 $z_{\max} = \max\{z_1, z_2, \cdots, z_n\}$。我们希望求出其数学期望 $\mathbb{E}[z_{\max}]$ 的严格上界。

该证明过程巧妙地引入了任意正数 $t > 0$，并利用了指数函数 $\exp(x)$ 的凸性。具体而言，可以连续进行以下放缩：

首先，利用 Jensen 不等式，对于凸函数 $\exp$，可以将期望提出到指数函数内部：
$$ \exp(t\mathbb{E}[z_{\max}]) \leq \mathbb{E}[\exp(t z_{\max})] $$

其次，由于 $\exp(x)$ 是严格单调递增函数，最大值的指数等于各分量指数的最大值：
$$ \mathbb{E}[\exp(t z_{\max})] = \mathbb{E}[\max_i \exp(t z_i)] $$

接着，因为对于任意 $t$ 和 $z_i$，$\exp(t z_i) > 0$ 恒成立，若干个非负随机变量的最大值必然小于或等于它们的求和：
$$ \mathbb{E}[\max_i \exp(t z_i)] \leq \sum_{i=1}^n\mathbb{E}[\exp(t z_i)] $$

最后，根据标准正态分布的矩生成函数（Moment Generating Function）性质，我们已知 $\mathbb{E}[\exp(t z_i)] = \exp(t^2 / 2)$。因此上述求和可以化简为：
$$ \sum_{i=1}^n\mathbb{E}[\exp(t z_i)] = n \exp(t^2 / 2) $$

将以上几步不等式链条首尾结合，我们得到：
$$ \exp(t\mathbb{E}[z_{\max}]) \leq n \exp(t^2 / 2) $$

此时，对不等式两端同时取自然对数，并除以正数 $t$ 整理得到：
$$ \mathbb{E}[z_{\max}] \leq \frac{\log n}{t} + \frac{t}{2} $$

需要注意，该结论对任意 $t > 0$ 均成立。为了得到最紧致（最准确）的上界，我们可以寻找能够使得不等式右端最小的 $t$。根据均值不等式（基本不等式），当且仅当 $\frac{\log n}{t} = \frac{t}{2}$ 时右端取得极小值，解得最优参数 $t = \sqrt{2\log n}$。

将此最优参数 $t$ 代回上式，即可得出正态随机数最大值期望的渐近上界：
$$ \mathbb{E}[z_{\max}] \leq \sqrt{2\log n} $$

该推导仅利用了初等不等式放缩与简单的动差计算，不仅过程极其快捷，不需要借助于复杂的概率密度函数积分，且得到的理论上界在渐近意义上出乎意料地准确。
