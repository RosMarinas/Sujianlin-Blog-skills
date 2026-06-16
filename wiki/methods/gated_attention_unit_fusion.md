---
type: method
title: 门控注意力与FFN的融合方法 (GAU)
operation_types:
  primary: Rewrite / identity transform
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-11-门控注意力单元-GAU-还需要Warmup吗.md
source_ids:
  - "8934"
  - "8990"
method_summary: 通过将注意力机制的 token 信息交互直接作为乘性因子注入到门控线性单元（GLU）中，把 Transformer 架构中原本分立的自注意力层（Attention）和前馈网络层（FFN）深度融合成单个门控注意力单元（GAU），实现了注意力头的单头化（Single Head），大幅降低了注意力多头得分矩阵的显存与计算时间。
typical_structure: |
  1. 对于隐层特征 $X \in \mathbb{R}^{n \times d}$，通过投影矩阵得到门控通道：$U = \phi_u(X W_u)$，$V = \phi_v(X W_v) \in \mathbb{R}^{n \times e}$（通常设定 $e = 2d$）
  2. 获取单头注意力计算投影：$Z = \phi_z(X W_z) \in \mathbb{R}^{n \times s}$，其中 $s = 128$
  3. 用简单的仿射变换获取单头 Query 和 Key，计算非概率注意力得分：$A = \frac{1}{ns}\text{relu}^2(\mathcal{Q}(Z)\mathcal{K}(Z)^\top)$
  4. 将注意力信息作为权重加权到 $V$ 分支：$\hat{V} = A V$
  5. 与 $U$ 分支进行门控 Hadamard 积，并通过输出矩阵映射回原本特征维度：$O = (U \odot \hat{V}) W_o$
applicability: 在设计高效 Transformer 模型架构时，当需要削减多头注意力冗余、减少模型中多头矩阵的空间开销（从 $bhn^2$ 降为 $bn^2$），并且希望融合 Attention 和 FFN 以简化计算层时激活。
tools:
  - 门控线性单元 (GLU)
  - 单头注意力
related_methods:
  - [[分块混合注意力自注意力线性化 (MCA)]]
  - [[Synthesizer静态注意力生成]]
  - [[l2 注意力归一化方法]]
examples:
  - [[article::8934]]
  - [[article::8990]]
status: draft
updated: 2026-06-14
---

## 适用问题

标准 Transformer 将自注意力（Attention）和前馈网络（FFN）作为分立的两层交替堆叠。这种设计存在两个冗余：一是 Attention 的多头机制需要存储 $bhn^2$ 量的得分矩阵，内存开销大；二是 Attention 和 FFN 各自有独立的投影矩阵，整体参数量和计算量高。GAU 旨在将二者融合为单一层，通过门控机制替代多头冗余，实现简化架构、加速训练的目标。

## 核心变换

**输入**：隐层特征 $X \in \mathbb{R}^{n \times d}$
**输出**：经门控注意力融合后的特征 $O \in \mathbb{R}^{n \times d}$
**参数**：投影矩阵 $W_u, W_v, W_z, W_o$，单头注意力映射 $\mathcal{Q}, \mathcal{K}$

GLU 形式的 FFN 基线：
$$
O = (U \odot V)W_o
$$

将注意力作为门控因子注入：
$$
O = (U \odot AV)W_o
$$

其中注意力得分为：
$$
A = \frac{1}{ns}\text{relu}^2(\mathcal{Q}(Z)\mathcal{K}(Z)^\top), \quad Z = \phi_z(XW_z)
$$

与标准注意力的关键区别：
- 单头设计（$s = 128$ 固定），无需多头拼接
- 使用 $\text{relu}^2$ 替代 Softmax，除以 $ns$ 实现归一化
- 注意力直接作为乘性门控，而非加性偏置

## 典型步骤

1. **门控通道投影**：对输入 $X$ 分别投影得到 $U = \phi_u(XW_u)$ 和 $V = \phi_v(XW_v)$，$U, V \in \mathbb{R}^{n \times e}$
2. **注意力投影**：计算 $Z = \phi_z(XW_z) \in \mathbb{R}^{n \times s}$，$s$ 固定为 128
3. **单头注意力得分**：$A = \frac{1}{ns}\text{relu}^2(\mathcal{Q}(Z)\mathcal{K}(Z)^\top)$
4. **门控融合**：注意力加权 $V$ 后与 $U$ 做 Hadamard 积：$\hat{V} = AV$，$O = (U \odot \hat{V})W_o$

## 直觉

核心思想：**FFN 负责"说什么"，Attention 负责"听谁说"，二者合二为一**。

GLU 形式的 FFN 已经具备了门控选择能力：$U \odot V$ 中 $U$ 是门控、$V$ 是内容。GAU 在此基础上将注意力作为额外的门控因子注入 $V$ 分支，让每个 token 在"产生内容"之前先通过注意力机制汇聚其他位置的信息。

多头注意力之所以必要，是因为标准注意力中每个头的表达容量有限。但在 GAU 中，GLU 的门控机制承担了大部分特征筛选工作，注意力只需提供 token 交互信息——单头 128 维的投影足以胜任。

## 边界

- 单头注意力去除了多头得分矩阵的内存需求，将空间复杂度从 $bhn^2$ 降至 $bn^2$
- $s = 128$ 是固定超参数，无需随模型大小调整
- 由于使用 $\text{relu}^2/n$ 归一化而非 Softmax，注意力分布的行和不再为 1，这在[[相对位置编码Transformer的一个理论缺陷与对策]]中被证明能避开全同输入的空间对称性缺陷
- GAU 在低算力场景下效果显著，但在超大模型上的表现需进一步验证

## 例子

- FLASH-Quad 使用 GAU 替代标准 Transformer 层，速度和吞吐全面超越基线
- GAU 单头消融实验：Head=1 与 GAU-GLU 配合效果媲美 Head=12 的多头注意力
- GAU 在 FLASH 框架中作为基础层，配合[[分块混合注意力自注意力线性化 (MCA)]]实现线性复杂度

## 证据

- ev::8934::GAU 计算框架：$(U \odot AV)W_o$ 公式，注意力单头化
- ev::8934::单头消融实验：消融图表证实 Head=1 与 GAU-GLU 配合足以媲美 Head=12
- ev::8990::GAU 不需要 Warmup 的训练稳定性分析
