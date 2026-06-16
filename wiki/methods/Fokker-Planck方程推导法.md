---

type: method
operation_types:
  primary: Discrete ↔ continuous bridge
  secondary: []
title: Fokker-Planck方程推导法
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-05-03-从动力学角度看优化算法-四-GAN的第三个阶段.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-10-10-从动力学角度看优化算法-五-为什么学习率不宜过小.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-12-11-从动力学角度看优化算法-六-为什么SimSiam不退化.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-12-21-从动力学角度看优化算法-七-SGD-SVM.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-08-08-生成扩散模型漫谈-六-一般框架之ODE篇.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-05-30-路径积分系列-2-随机游走模型.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-06-02-路径积分系列-3-路径积分.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-06-09-路径积分系列-4-随机微分方程.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-12-20-从动力学角度看优化算法-二-自适应学习率算法.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-01-08-从动力学角度看优化算法-三-一个更整体的视角.md
source_ids:
  - 9228
method_summary: 通过Dirac delta函数将概率密度转化为期望形式，利用泰勒展开和期望运算推导随机过程的Fokker-Planck方程，再通过重写F-P方程构建等价的前向SDE。
typical_structure: |
  1. 写出原前向 SDE 对应的离散更新方程。
  2. 将边际概率密度 $p_t(x)$ 表达为狄拉克函数对真实路径的期望。
  3. 对增量 $\delta(x - x_{t+\Delta t})$ 进行泰勒展开保留至 $\Delta t$ 一阶项。
  4. 取期望消去高阶项与随机鞅项，导出对应的 F-P 偏微分方程。
  5. 拆分 F-P 方程的二阶导数方差项，将其余量通过得分函数并入一阶漂移项。
  6. 根据新组装的 F-P 方程逆向对应出具有不同扩散系数和漂移项的新 SDE。
applicability: 生成扩散模型的理论推导中，需要在保持边际分布不变的前提下改变 SDE 的方差系数（如将 SDE 降级为 ODE，或推导概率流模型）。
examples:
  - 扩散模型中通过设新方差为0推导出概率流 ODE (Probability Flow ODE)，作为 DDIM 采样的连续时间理论基础。
status: stable
updated: 2026-06-12
evidence_spans:
  - ev::9228::原文"等价变换"节详细描述了基于 F-P 偏微分方程的代数重写使得方程保持一致，进而导出具有不同方差但是等价边际分布的新 SDE。
---



## 适用问题
在生成扩散模型的理论推导中，往往需要从前向随机微分方程 (SDE) 的扩散过程推导出其在某个时刻的边际分布演化方程。同时，为了构建更灵活的采样算法（例如方差调整或确定性 ODE 采样），需要证明存在一系列不同的前向 SDE，它们对应的边际分布完全等同。直接在 SDE 层面证明边际概率密度的等价性极其困难。

## 核心变换
将 SDE 中难以操作的路径积分问题转化为偏微分方程（Fokker-Planck方程，F-P方程）中的代数变换。利用狄拉克 Delta 函数 $\delta(x-x_t)$ 将概率密度写作期望形式，对 Delta 函数进行泰勒展开并取期望，推导出描述边际分布演化的 F-P 偏微分方程。随后直接在偏微分方程上重写方差项 $\sigma_t^2$ 和漂移项，使得方程在等式意义上完全成立，最后反向写出重写后等效的 SDE。

## 典型步骤
1. 写出原前向 SDE 对应的离散更新方程。
2. 将边际概率密度 $p_t(x)$ 表达为狄拉克函数对真实路径分布的期望 $p_t(x) = \mathbb{E}[\delta(x - x_t)]$。
3. 利用 SDE 的增量关系，将 $\delta(x - x_{t+\Delta t})$ 进行泰勒展开，保留到 $\Delta t$ 的一阶项和随机项增量的二阶项。
4. 两边取期望，利用独立增量消去一阶随机项，得到时间导数的极限形式，即原 SDE 对应的 F-P 方程。
5. 在 F-P 方程的偏导项中拆分和重组，将原方差 $g_t^2$ 替换为目标方差 $\sigma_t^2$，多出的部分通过得分函数 $\nabla_x \log p_t(x)$ 吸收到漂移项 $f_t(x)$ 中。
6. 根据重写后的新 F-P 方程结构，逆向写出它对应的新 SDE。

## 直觉
SDE 描述的是“个体的微观随机轨迹”，而 F-P 方程描述的是“群体的宏观密度分布演化”。就如同研究大量气体分子的运动，追踪每个分子的布朗运动很难，但研究全体气体密度的扩散偏微分方程很容易。在偏微分方程中，“方差扩散项”和“得分函数带来的漂移项”是可以互相转换的。我们在数学上挪用一部分的扩散项去充当漂移项，保持总和不变，就意味着可以找到一个噪音更小（甚至没有噪音变为常微分方程 ODE）、但宏观分布结果完全相同的替代演化路径。

## 边界
- 必须满足重写后的方差非负且不超过原扩散界限的条件，即新的方差项 $\sigma_t^2 \leq g_t^2$。
- 推导过程依赖能够精确计算或用神经网络估计得分函数（Score Function） $\nabla_x \log p_t(x)$。
- 处理过程只是保证宏观边际分布等价的，微观上的单条样本路径已经被彻底改变。

## 例子
在生成扩散模型中推导概率流 ODE (Probability Flow ODE)：通过 F-P 方程推导法，选取极端情况 $\sigma_t = 0$，将原 SDE 的所有随机扩散项通过得分函数转移到漂移项中，得到纯确定性的逆向 ODE。这使得我们在生成样本时不再需要注入随机噪声，DDIM 可视作该 ODE 的线性特例，从而可以借助诸多数值 ODE 求解器实现快速采样。

## 证据
- 原文 9228 "等价变换"节展示："形式上该F-P方程又相当于原来的F-P的$f_t(x)$换成了$f_t(x) - \frac{1}{2}(g_t^2 - \sigma_t^2)\nabla_x\log p_t(x)$、$g_t$换成了$\sigma_t$ ... 别忘了式跟式是完全等价的，所以这意味着这两个随机微分方程所对应的边际分布是完全等价的！这个结果告诉我们存在不同方差的前向过程，它们产生的边际分布是一样的。"
