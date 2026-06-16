---
type: concept
title: AdaX优化器
aliases:
- AdaX
- Adaptive Gradient Descent with Exponential Long Term Memory
definition: 通过将二阶矩更新从滑动平均改为指数长期记忆形式(v_t=(1+β2)v_{t-1}+β2 g_t^2)的优化器，其等效Beta2衰减满足β̂_{2,1}=0,
  β̂_{2,∞}=1。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-05-11-AdaX优化器浅析-附开源实现.md
source_ids:
- '7387'
prerequisites:
- '[[Adam优化器]]'
related_formulas: []
related_methods: []
evidence_spans:
- ev::7387::AdaX格式
- ev::7387::等价形式变换
- ev::7387::衰减策略比较
status: draft
updated: '2026-06-12'
---

# AdaX优化器

## 核心定义与数学形式

AdaX（Adaptive Gradient Descent with Exponential Long Term Memory）是对Adam优化器的一种改进。其完整的更新格式为：
$$
\left\{\begin{aligned}&g_t = \nabla_{\theta} L(\theta_t)\\
&m_t = \beta_1 m_{t-1} + \left(1 - \beta_1\right) g_t\\
&v_t = (1 + \beta_2) v_{t-1} + \beta_2 g_t^2\\
&\hat{v}_t = v_t\left/\left(\left(1 + \beta_2\right)^t - 1\right)\right.\\
&\theta_t = \theta_{t-1} - \alpha_t m_t\left/\sqrt{\hat{v}_t + \epsilon}\right.
\end{aligned}\right.
$$
其中$\beta_2$的默认值是$0.0001$。

与Adam相比，AdaX的两个主要区别在于：
1. **去除了动量的偏置校正**：即没有了 $\hat{m}_t = m_t\left/\left(1 - \beta_1^t\right)\right.$ 这一步，但这其实影响不大。
2. **二阶矩更新方式**：本来Adam中 $v_t = \beta_2 v_{t-1} + \left(1 - \beta_2\right) g_t^2$ 是滑动平均格式，而AdaX的 $v_t = (1 + \beta_2) v_{t-1} + \beta_2 g_t^2$ 由于 $1 + \beta_2 > 1$，导致历史累积梯度的比重不会越来越小，反而会越来越大，这就是它的“长期记忆性（Exponential Long Term Memory）”。

## 等价形式变换与理论分析

事实上，学习率校正用的是 $\hat{v}_t$，所以究竟有没有爆炸，我们要观察的是 $\hat{v}_t$。不管是Adam还是AdaX，从真正用来校正梯度的 $\hat{v}_t$ 来看，其更新公式都是滑动平均的格式：
$$
\hat{v}_t =\hat{\beta}_{2,t}\hat{v}_{t-1} + \left(1 - \hat{\beta}_{2,t}\right)g_t^2
$$

对于AdaX，如果设：
$$
\hat{\beta}_{2,t}=1 - \frac{\beta_2}{(1 + \beta_2)^t - 1}
$$
那么AdaX的 $\hat{v}_t$ 的更新公式也可以写成上述的滑动平均格式。

## 衰减策略比较与理想性质

通过分析等效衰减系数 $\hat{\beta}_{2,t}$，可以明确AdaX相较于Adam的理论优势：

* **Adam的缺陷**：对于Adam来说，当 $t \to \infty$ 时，$\hat{\beta}_{2,t} \to \beta_2$。这意味着当前梯度的权重 $1 - \beta_2$ 不为0，这可能导致训练不稳定，因为训练后期梯度变小，训练本身趋于稳定，校正学习率的意义就不大了。
* **AdaX的理想性质**：对于AdaX来说，当 $t=1$ 时 $\hat{\beta}_{2,t}=0$，这时候 $\hat{v}_t$ 就是 $g_t^2$，也就是用实时梯度来校正学习率，这时候校正力度最大；当 $t \to \infty$，$\hat{\beta}_{2,t} \to 1$，满足学习率的校正力度应该变小，并且 $t \to \infty$，学习率最好恒定为常数（这时候相当于退化为SGD）的理想性质。

这一性质印证了优化器改进的一个基本条件：$\hat{\beta}_{2,t}$ 应当满足条件 “$\hat{\beta}_{2,1}=0, \hat{\beta}_{2,\infty}=1$”。（注：在AdaFactor中使用的 $\hat{\beta}_{2,t} =1 - \frac{1}{t^c}$ 也是从这个角度设计的）。
