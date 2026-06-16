---


type: method
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
title: MCMC
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-01-14-搜出来的文本-二-从MCMC到模拟退火.md
source_ids:
  - 8084
method_summary: MCMC（Markov Chain Monte Carlo）将马尔可夫链和蒙特卡洛方法结合起来，通过构建以目标分布 p(x) 为平稳分布的马尔可夫链，采用“微调/转移”的方式渐进式采样来逼近高维目标分布。
typical_structure: |
  1. 定义难以直接采样的目标分布 $p(x)$ 的形式（通常只需知道未归一化的势函数 $\rho(x)$）。
  2. 构造一个易于采样的邻域参考转移分布 $q(y \leftarrow x)$。
  3. 通过引入并计算接受率（如 Metropolis-Hastings 的 $\mathcal{A}(y \leftarrow x)$）以满足细致平稳条件。
  4. 从初始状态开始，使用随机采样生成候选并使用 $\varepsilon \sim U[0,1]$ 判断是否接受，接受则跳转，否则状态不变，反复迭代生成马尔可夫链。
applicability: 直接计算期望、积分或配分函数不可行，尤其是高维空间中单纯拒绝采样效率极低，而需要通过构建邻域游走马尔可夫链来进行渐进近似采样的场景。
examples:
  - [[article::8084]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::8084::文章指出 MCMC 的本质是化难为易：“MCMC 方法根本就没有去归一化 $\tilde{q}$，而是将剩余部分的概率全部转移到自身去了...也就是将‘直接生成 x’转换为了‘从 x0 出发反复对它微调润色’”。
---






# MCMC

## 适用问题
在机器学习、物理或受限文本生成任务中，需要从极高维、复杂的且难以解析求解归一化常数（配分函数）的目标概率分布 $p(\boldsymbol{x})$ 中提取随机样本计算期望。

## 核心变换
将“寻找在全域空间中独立投掷骰子生成服从 $p(\boldsymbol{x})$ 的样本”这件不可能的事，**重写转换**为“在空间中搭建一张随机漫游网（马尔可夫链），通过限制游走者向大概率区域靠拢（细致平稳条件保证），使得漫游者留下来的长长轨迹脚印整体上恰好服从目标分布”。

## 典型步骤
以 Metropolis-Hastings (MH) 采样为例：
1. 设定马尔可夫链初始状态为 $\boldsymbol{x}_0$。
2. 在第 $t$ 步时（当前处在 $\boldsymbol{x}_t$），从一个简单设计的参考分布 $q(\boldsymbol{y} \leftarrow \boldsymbol{x}_t)$ 中生成一个相邻的候选新状态 $\boldsymbol{y}$。
3. 从均匀分布 $U[0,1]$ 中采样随机标量 $\varepsilon$。
4. 计算基于细致平稳条件推导出的接受概率 $\mathcal{A}(\boldsymbol{y}\leftarrow\boldsymbol{x}_t) = \min\left(1, \frac{q(\boldsymbol{x}_t\leftarrow\boldsymbol{y})p(\boldsymbol{y})}{q(\boldsymbol{y}\leftarrow\boldsymbol{x}_t)p(\boldsymbol{x}_t)}\right)$。注意这里由于是比值，目标分布 $p$ 的归一化常数恰好被完全消掉。
5. 若 $\varepsilon \leq \mathcal{A}$，则接受这步修改，进入状态 $\boldsymbol{x}_{t+1} = \boldsymbol{y}$。
6. 否则拒绝修改，原地踏步维持 $\boldsymbol{x}_{t+1} = \boldsymbol{x}_t$。
7. 迭代无限次（Burn-in 后），收集得到的序列即为近似的蒙特卡洛样本。

## 直觉
普通的拒绝采样就像大海捞针：在一个长得像正方体的盒子里狂撒针，指望其中几只能恰好掉在盒子中央复杂的苹果形状里。一旦苹果的维度到达上百维，这几乎不可能。
MCMC 则像是个被蒙住眼睛的摸象人：你把他随机扔到盒子里，他沿着附近摸一摸，如果感觉前面更有可能是苹果（概率变大），他就走过去；如果感觉像空气，他也有小概率走过去（容错）。只要给他足够多的时间，他逗留在这个苹果里各个位置的时间分布，就精妙地等价于苹果本身的形状。这就是微调与渐进式的魔力。

## 边界
MCMC 的两个致命伤。第一，高度依赖提议分布（Proposal Distribution）$q$ 的质量：步子迈得太大，导致接受率暴跌，模型只会在原地打转不前进；步子迈得太小，它只能在这个山头转悠，跨不过深沟去另一个高概率的山头（难以探索多峰分布全貌）。第二，样本在时间维度上是自相关（非独立）的，需要丢弃初始的大量步骤（Burn-in 期），其本质是“用海量时间算力换取空间求解的可行性”。

## 例子
Gibbs 采样就是 MCMC 的一个特例。如果要为一个 10 维变量采样，它不去同时摇 10 个维度的候选骰子，而是每次死死固定 9 个变量，只按概率更新第 10 个变量。因为每次只动一点，它完全不偏离当前状态太多，这神奇地导致了每次尝试必定 100% 成功（接受率恒为 1）。再如基于受限生成的文本修改，MCMC 每次只在句中换掉一两个字，慢慢就能让原句游走到具有特定情绪风格的“高概率”句子上。

## 证据
- ev::8084::揭示了马尔可夫链转移操作背后的补全真理：“将剩余部分的概率概率全部转移到自身去了...代表了只能转移到自身（永远不变）的转移概率”。
- ev::8084::阐述了MH采样的核心优势公式：“$\mathcal{A}$ 只依赖于 $p(y)$ 的相对值，所以我们可以不用算出它的归一化因子了”。
