---
type: concept
title: Gumbel分布
aliases:
- Gumbel distribution
definition: 极值分布的一种，累积分布函数 Phi(epsilon)=e^{-e^{-epsilon}}，用于Gumbel Max离散采样
standard_notation: Phi(epsilon)=e^{-e^{-epsilon}}
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2019-06-10-漫谈重参数-从正态分布到Gumbel-Softmax.md
- Data/Spaces_ac_cn/markdown/Mathematics/2022-05-25-从重参数的角度看离散概率分布的构建.md
source_ids:
- '6705'
- '9085'
related_methods:
- - Gumbel Softmax离散重参数
evidence_spans: []
series: []
status: draft
updated: '2026-06-12'
---

## 定义

Gumbel噪声是$u\sim U[0,1]$通过$\varepsilon = -\log(-\log u)$变换而来，由于$u$的分布正好是$U[0,1]$，所以解出来$u=e^{-e^{-\varepsilon}}$正好就是Gumbel分布的累积分布函数，即$\Phi(\varepsilon)=e^{-e^{-\varepsilon}}$，而$p(\varepsilon)$就是$\Phi(\varepsilon)$的导数，即$p(\varepsilon)=\Phi'(\varepsilon)=e^{-\varepsilon-e^{-\varepsilon}}$。

## 标准符号

累积分布函数：$\Phi(\varepsilon)=e^{-e^{-\varepsilon}}$
概率密度函数：$p(\varepsilon)=\Phi'(\varepsilon)=e^{-\varepsilon-e^{-\varepsilon}}$

## 核心性质与Gumbel Max采样

Gumbel分布被广泛用于离散概率分布的重参数化采样中。假设每个类别的概率是$p_1,p_2,\dots,p_k$，那么下述过程提供了一种依概率采样类别的方案，称为Gumbel Max：

$$
\mathop{\text{argmax}}_i \Big(\log p_i - \log(-\log \varepsilon_i)\Big)_{i=1}^k,\quad \varepsilon_i\sim U[0, 1]
$$

也就是说，先算出各个概率的对数$\log p_i$，然后从均匀分布$U[0,1]$中采样$k$个随机数$\varepsilon_1,\dots,\varepsilon_k$，把$-\log(-\log \varepsilon_i)$加到$\log p_i$上去，最后把最大值对应的类别抽取出来就行了。这样的过程精确等价于依概率$p_1,p_2,\dots,p_k$采样一个类别，换句话说，在Gumbel Max中，输出$i$的概率正好是$p_i$。

## 与其他概念的关系

**与Gumbel Softmax的关系：**
注意，Gumbel Softmax不是类别采样的等价形式，Gumbel Max才是。而Gumbel Max可以看成是Gumbel Softmax在$\tau \to 0$时的极限。所以在应用Gumbel Softmax时，开始可以选择较大的$\tau$（比如1），然后慢慢退火到一个接近于0的数（比如0.01），这样才能得到比较好的结果。

**与常规Softmax的关系：**
从重参数的视角，当我们设 $\boldsymbol{\varepsilon}=[\varepsilon_1,\cdots,\varepsilon_n]$ 是从分布 $p(\varepsilon)$ 独立重复采样 $n$ 次得到的向量，并通过 $p_i = P[\mathop{\text{argmax}}(\boldsymbol{\mu}+\boldsymbol{\varepsilon})=i]$ 来定义变换 $\mathcal{T}$ 时，当噪声分布取 Gumbel 分布 时：

$$
\begin{aligned}
p_i =&\, \int_{-\infty}^{\infty} e^{-\varepsilon_i-e^{-\varepsilon_i}} e^{-\sum\limits_{j\neq i}e^{-\varepsilon_i + \mu_j - \mu_i}} d\varepsilon_i \\
=&\, \int_{-\infty}^0 e^{-e^{-\varepsilon_i}\left(1+\sum\limits_{j\neq i}e^{\mu_j - \mu_i}\right)} d(-e^{-\varepsilon_i}) \\
=&\, \int_{-\infty}^0 e^{t\left(1+\sum\limits_{j\neq i}e^{\mu_j - \mu_i}\right)} dt\\
=&\, \frac{1}{1+\sum\limits_{j\neq i}e^{\mu_j - \mu_i}} = \frac{e^{\mu_i}}{\sum\limits_j e^{\mu_j }}
\end{aligned}
$$

这正好是Softmax。于是我们再次验证了Gumbel Max与Softmax的对应关系。
