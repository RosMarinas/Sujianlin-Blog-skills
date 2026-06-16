---
type: method
title: 分块混合注意力自注意力线性化 (MCA)
operation_types:
  primary: Decompose / reduce dimension
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
source_ids:
  - "8934"
method_summary: 将长度为 $n$ 的大序列划分为若干不重叠的、大小为 $c$ 的块（如 $c=256$）。在块内部直接计算常规自注意力（局部二次复杂度），在块之间采用线性注意力算子进行全局特征汇聚，将注意力的整体时间与空间复杂度降为线性阶 $\mathcal{O}(n)$，并保留了 Causal（解码器）下的并行加速能力。
typical_structure: |
  1. **分块划分**：将输入序列 $X$ 划分为 $n/c$ 个非重叠块
  2. **局部注意力计算**：每个块内用独立的 Query 和 Key 做局部二次自注意力：$\hat{\boldsymbol{V}}_g^{\text{quad}} = \frac{1}{cs}\text{relu}^2(\boldsymbol{Q}_g^{\text{quad}}{\boldsymbol{K}_g^{\text{quad}}}^{\top})\boldsymbol{V}_g$
  3. **全局线性自注意力**：使用全局线性注意力将跨块信息汇聚
  4. **融合输出**：$\boldsymbol{O}_g = [\boldsymbol{U}_g \odot (\hat{\boldsymbol{V}}_g^{\text{quad}} + \hat{\boldsymbol{V}}_g^{\text{lin}})]\boldsymbol{W}_o$
applicability: 在处理极长文本序列（如数千甚至上万长度）的 Transformer/FLASH 架构中，为了大幅削减二次复杂度带来的时空负担，并且需要保证 Decoder 模式下的并行训练速度时激活此方法。
tools:
  - 分块混合注意力
  - 线性化自注意力
related_methods:
  - [[门控注意力与FFN的融合方法 (GAU)]]
  - [[线性注意力]]
examples:
  - [[article::8934]]
status: draft
updated: 2026-06-14
---

## 适用问题

标准自注意力的复杂度 $\mathcal{O}(n^2)$ 随序列长度 $n$ 二次增长，在长序列（数千 token 以上）场景中面临显存溢出和计算时间过长的问题。纯线性注意力虽然复杂度为 $\mathcal{O}(n)$，但全局平均池化式的汇聚会丢失局部精细交互。MCA 在局部（块内）保留二次注意力的精细建模，在全局（块间）使用线性注意力汇聚，兼顾效率与效果。

## 核心变换

**输入**：长度为 $n$ 的序列 $X$，块大小 $c$
**输出**：经分块混合注意力处理的表示 $\boldsymbol{O}_g$
**复杂度**：$\mathcal{O}(nc)$（块内二次 $\mathcal{O}(c^2)$，块间线性 $\mathcal{O}(n)$）

将序列划分为 $n/c$ 个不重叠的块，每个块长度为 $c$。对第 $g$ 个块：

**局部注意力（块内二次）**：
$$
\hat{\boldsymbol{V}}_g^{\text{quad}} = \frac{1}{cs}\text{relu}^2\left(\boldsymbol{Q}_g^{\text{quad}}{\boldsymbol{K}_g^{\text{quad}}}^{\top}\right)\boldsymbol{V}_g
$$

**全局注意力（块间线性）**：

双向模式：
$$
\hat{\boldsymbol{V}}_g^{\text{lin}} = \frac{1}{n}\boldsymbol{Q}_g^{\text{lin}}\sum_{h} {\boldsymbol{K}_h^{\text{lin}}}^{\top}\boldsymbol{V}_h
$$

因果模式：
$$
\hat{\boldsymbol{V}}_g^{\text{lin}} = \frac{1}{(g-1)n/c}\boldsymbol{Q}_g^{\text{lin}}\sum_{h=1}^{g-1} {\boldsymbol{K}_h^{\text{lin}}}^{\top}\boldsymbol{V}_h
$$

**融合输出**：
$$
\boldsymbol{O}_g = \left[\boldsymbol{U}_g \odot \left(\hat{\boldsymbol{V}}_g^{\text{quad}} + \hat{\boldsymbol{V}}_g^{\text{lin}}\right)\right]\boldsymbol{W}_o
$$

## 典型步骤

1. **分块**：将输入划分为 $n/c$ 个长度为 $c$ 的不重叠块
2. **局部注意力**：在每个块内使用独立的 $Q^{\text{quad}}, K^{\text{quad}}$ 计算二次注意力
3. **全局注意力**：使用独立的 $Q^{\text{lin}}, K^{\text{lin}}$ 计算块间的线性注意力
   - 双向：对所有块求和后平均
   - 因果：使用 cumsum 对已处理块做前缀和累积
4. **门控融合**：将局部和全局结果相加，与门控通道 $U$ 做 Hadamard 积，通过输出投影

## 直觉

核心思想：**近处精细交互，远处概要汇聚**。

自然语言中，相邻 token 往往有强依赖关系（如语法结构、局部修饰），而远处 token 只需了解话题和语境。MCA 的设计恰好对应了这一直觉：

- **局部块内**（$c=256$）：保留标准二次注意力，可以精细建模短语级别的语法依赖和修饰关系。块内复杂度仅为 $\mathcal{O}(c^2)$，与 $n$ 无关。
- **全局块间**：通过 Key 的累计和进行线性汇聚，相当于为每个块生成一个"摘要向量"，供所有其他块查询。这种方式虽不能建模精细的远距离依赖，但对整体语义理解已足够。

因果模式下，块间线性注意力可使用 cumsum 前缀和算法实现并行计算，避免了 RNN 式的串行递归。

## 边界

- 块大小 $c$ 是关键超参数：$c$ 过小会丢失局部依赖的精细度，$c$ 过大会增加局部二次复杂度
- 推荐块大小 $c = 256$，在大多数序列长度上取得效率和效果的平衡
- 全局注意力使用线性近似，无法建模精细的远程语义对应关系
- 因果模式下的空间复杂度仅为 $b(n/c)se$，显著低于标准因果注意力的 $bn^2$

## 例子

- FLASH 模型使用 MCA 实现线性复杂度 Transformer，在 LRA 基准上超越标准 Transformer
- 序列长度 $n = 8192, c = 256$ 时，局部复杂度为 $\mathcal{O}(256^2)$ 而非 $\mathcal{O}(8192^2)$
- MCA + GAU 架构在速度-效果曲线上占据主导地位

## 证据

- ev::8934::MCA 分块公式：局部 $\hat{\boldsymbol{V}}_g^{\text{quad}}$ + 全局 $\hat{\boldsymbol{V}}_g^{\text{lin}}$ 的融合设计
- ev::8934::因果模式 cumsum 并行推导：线性空间复杂度 $b(n/c)se$
- ev::8934::LRA 实验：FLASH 在线性复杂度模型中取得最优效果
