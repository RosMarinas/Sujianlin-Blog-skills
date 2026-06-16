---
type: concept
title: EMA等效批量放大
aliases: null
definition: 动量 EMA 通过时间平均降低梯度噪声方差，可在尺度律中表现为把 Batch Size 放大到一个有效批量。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md
source_ids:
- '11301'
related_formulas:
- '[[二阶近似最优学习率公式]]'
related_methods:
- '[[用平均场近似替代复杂期望计算]]'
series:
- '[[重新思考学习率与Batch Size]]'
evidence_spans:
- ev::11301::放大批量
- ev::11301::符号动量
status: draft
updated: '2026-06-14'
---

# EMA等效批量放大

## 定义

动量 EMA（Exponential Moving Average）通过时间平均降低梯度噪声方差，可在尺度律中表现为把 Batch Size 放大到一个有效批量。按照其数学机制，动量就是通过对优化轨迹上的梯度做EMA来低成本地消除梯度噪声。具体而言，动量机制的引入，相当于把 SGD 的 Batch Size 放大到了 $\frac{1 + \beta_1}{1 - \beta_1}$ 倍。

## 关键性质与条件

1. **对SGDM的作用**：动量的引入相当于把 SGD 的最优学习率公式中的 $B$ 替换为放大后的批量。具体近似如下：
   $$
   \eta^* \approx \frac{\eta_{\max}}{1 + \frac{1 - \beta_1}{1 + \beta_1}\mathcal{B}_{\text{noise}}/B}
   $$
   其中 $\eta_{\max} = \frac{\boldsymbol{g}^{\top}\boldsymbol{g}}{\boldsymbol{g}^{\top}\boldsymbol{H}\boldsymbol{g}}$，$\mathcal{B}_{\text{noise}} = \frac{\mathop{\text{tr}}(\boldsymbol{\Sigma}\boldsymbol{H})}{\boldsymbol{g}^{\top}\boldsymbol{H}\boldsymbol{g}}$。

2. **对SignSGD类算法（含Lion和Muon）的作用**：跟SGDM一样，动量相当于把SignSGD的Batch Size放大到了 $\frac{1 + \beta_1}{1 - \beta_1}$ 倍。对SignSGDM，结合平均场近似有：
   $$
   \mathbb{E}[\tilde{\boldsymbol{\varphi}}_B] \approx \frac{\mathop{\text{sign}}(\boldsymbol{g}_t)}{\sqrt{1 + \frac{1 - \beta_1}{1 + \beta_1} \mathcal{B}_{\text{simple}}/B}}
   $$
   此外，动量在 Muon 中的作用跟 SignSGDM 一样，都约等于将 Batch Size 放大成 $\frac{1 + \beta_1}{1 - \beta_1}$ 倍。

3. **加速“Surge现象”**：Surge现象指当 Batch Size 超过某个阈值后，最优学习率随着 Batch Size 的增大而减少。因为动量的引入约等于将 Batch Size 扩大到 $\frac{1 + \beta_1}{1 - \beta_1} > 1$ 倍，这自然增加了超过阈值的可能性。因此，随着 $\beta_1$ 的增大，“Surge现象”将更容易出现。

## 与其他概念的关系

该概念用于把优化器更新规则、采样噪声和 Batch Size 关系连接起来，避免只停留在经验调参描述。主要关联以下概念与优化器：

* **SGDM / SignSGDM / Muon**：在这些优化算法中，“动量机制约等于放大Batch Size”这一点始终是成立的，增大Batch Size（或提高动量系数）能够降低噪声方差。
* **Adam**：Adam 包含双重EMA（同时滑动平均一阶矩 $\boldsymbol{m}_t$ 和二阶矩 $\boldsymbol{v}_t$）。虽然从一阶矩看，SignSGD作为Adam的近似是合理的，但在二阶期望计算 $\mathbb{E}[\tilde{\boldsymbol{\varphi}}_B^2]$ 时，Adam 受到动量 $\beta_1$ 的影响呈现出与 SignSGD 不同的特性：即使在对角 Hessian 假设下，当 $\beta_1 > 1/3$ 时依然会出现 Surge 现象。这解释了为什么 Adam 在常用设置（如 $\beta_1=0.9$）下，Batch Size超过一定值后学习效率会下降，而 Muon 在同样假设下不会出现。
* **平均场近似**：计算EMA统计量的期望时，必须依赖协方差矩阵和梯度的缓变性假设（模型训练进入“正轨”后），并通过平均场近似得出 EMA 等效于减小随机噪声（方差变小 $\frac{1-\beta_1}{1+\beta_1}$ 倍）从而放大有效批量的结论。

## 证据

- `ev::11301::放大批量`
- `ev::11301::符号动量`
