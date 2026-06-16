---
type: example
title: NVAE双向相对参数化残差结构
article_id: "7574"
article: "[[spaces-7574-强大的NVAE-以后再也不能说VAE生成的图像模糊了]]"
section: 自回归分布
claim: 在 NVAE 中通过相对残差均值方差公式更新层级后验高斯分布，可以使深度自回归潜随机层网络稳定收敛
notation_mapping:
  absolute_prior_mean: \mu_{\text{prior}}
  absolute_prior_variance: \sigma^2_{\text{prior}}
  relative_posterior_mean_offset: \Delta\mu
  relative_posterior_variance_scale: \Delta\sigma^2
  final_posterior_mean: \mu_{\text{post}}
  final_posterior_variance: \sigma^2_{\text{post}}
steps:
  - 1. **先验网络特征输出**：根据前续已采样的条件潜表征 $z_{<l}$，由先验深度生成网络计算出当前潜随机层 $l$ 的绝对均值 $\mu_{\text{prior}}$ 及绝对方差 $\sigma^2_{\text{prior}}$。
  - 2. **编码分支预测残差**：后验编码器接收图像 $x$ 并融合 $z_{<l}$，输出相对于先验的残差分布微调量：均值偏置 $\Delta\mu$ 以及方差比例因子 $\Delta\sigma^2$。
  - 3. **融合计算条件后验**：计算求得当前层后验高斯分布的最终均值与方差：$\mu_{\text{post}} = \mu_{\text{prior}} + \Delta\mu$ 以及 $\sigma^2_{\text{post}} = \sigma^2_{\text{prior}} \otimes \Delta\sigma^2$。
  - 4. **重参数化采样潜表征**：引入高斯独立白噪声 $\epsilon \sim \mathcal{N}(0, I)$，采样出当前层级的隐随机状态：$z_l = \mu_{\text{post}} + \sigma_{\text{post}} \odot \epsilon$。
  - 5. **动态计算相对条件损失**：计算层级相对 KL 散度并将其求和，作为多随机层自回归对齐损失叠加到总优化目标：
       `loss_kl_l = 0.5 * K.sum(K.square(Delta_mu) / sigma^2_prior + Delta_sigma^2 - K.log(Delta_sigma^2) - 1)`。
used_concepts:
  - "[[分层变分自编码器]]"
  - "[[多尺度变分自编码]]"
used_formulas:
  - "[[相对参数化均值方差公式]]"
used_methods:
  - "[[分层变分自编码相对参数化]]"
  - "[[重参数技巧]]"
source_span: ev::7574::relative_parameterization_dist
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-10-强大的NVAE-以后再也不能说VAE生成的图像模糊了.md
source_ids:
  - "7574"
status: draft
updated: 2026-06-12
---

本例展示了 NVAE 自回归高斯潜表征空间中，如何利用“相对参数化”残差思想稳定深层变分自动编码网络训练的过程，该相对式参数化能防止训练早期的条件 KL 散度数值爆炸。

在构建极深层级的自回归随机层级网络（如 NVAE 中包含多达 36 组不同空间分辨率与感受野的潜随机层）时，如果继续采用传统的绝对值均值建模，后验分支和先验分支在优化初始阶段的估计失配往往会产生巨大的 KL 散度波动，进而将巨大的发散梯度向深层后向传播，导致整个神经网络在训练首个 Epoch 时便发生数值下溢或上溢。通过使用本例给出的相对均值方差参数化形式，我们成功把绝对尺度的度量改造为了“基于先验均值方差的局部微调”。在网络初始权重下，偏移修正项 $\Delta\mu$ 自然趋近于 0 且比例因子 $\Delta\sigma^2$ 趋近于 1，使得后验分布与先验分布天生处于高度重合咬合状态。这既保证了初始 KL 损失项接近于零，为系统提供了安全的初始梯度流，又极大地稳定了全局潜表征在多尺度层级生成流中的自适应梯度交互。
