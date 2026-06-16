---
type: method
title: Synthesizer静态注意力生成
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-05-25-Google新作Synthesizer-我们还不够了解自注意力.md
source_ids:
  - "7430"
method_summary: 通过使用基于单位置输入的前馈层预测，或者完全与输入无关的随机初始化常数矩阵，来代替自注意力中传统的双向 Query-Key 动态内积计算，从而省去了大维度的内积相乘，达到简化注意力和提升运算效率的目的。
typical_structure: |
  1. **Dense 模式**：通过两层前馈网络，根据当前输入预测对序列所有位置的注意力：$B = relu(XW_1 + b_1)W_2 + b_2$，随后应用 $A = softmax(B)$
  2. **Random 模式**：直接初始化一个与输入无关的常数矩阵 $R \in \mathbb{R}^{n \times n}$ 作为自注意力权重评分矩阵
  3. **低秩分解加速**：将常数矩阵分解为两个低秩矩阵的乘积 $R_1 R_2^\top$ 以大幅节省参数
  4. **特征汇聚**：将得到的自注意力矩阵 $A$ 乘以 Value 的投影向量：$O = A (XW_v)$
applicability: 在特定的单一领域生成式任务（如摘要、翻译、特定对话）中，当需要省去 $QK^\top$ 动态乘法以显著加快模型的前向运行速度，或在大规模长文本的定制场景下，可采用此方法。
tools:
  - Dense 注意力生成
  - Random 注意力
  - 低秩分解
related_methods:
  - [[T-TA结构与共享键值防泄漏法]]
  - [[增大key_size解除注意力低秩瓶颈]]
examples:
  - [[article::7430]]
status: draft
updated: 2026-06-14
---

## 适用问题

标准自注意力中 $QK^\top$ 的 token 对 token 动态交互计算是否是必需的？Synthesizer 通过实验证明：在许多单任务场景中，完全可以用更简单的映射替代复杂的动态交互。该方法适用于对推理速度有高要求、且不需要跨任务迁移能力的特定领域生成任务。

## 核心变换

**输入**：序列 $X \in \mathbb{R}^{n \times d}$
**输出**：经静态注意力汇聚的表示 $O \in \mathbb{R}^{n \times d}$
**核心**：用静态/简化的注意力得分生成替代 $QK^\top$ 动态计算

统一注意力框架：
$$
O = A(X) \cdot (XW_v), \quad A = softmax(B)
$$

标准注意力中 $B = \frac{XW_q W_k^\top X^\top}{\sqrt{d_k}}$。

### Dense 模式

使用前馈网络直接从输入预测注意力得分：
$$
B = relu(XW_1 + b_1)W_2 + b_2
$$
每行 $B_{i,:}$ 表示位置 $i$ 对所有位置（包括自身）的注意力强度，由位置 $i$ 的输入特征 $X_{i,:}$ 独立预测。

### Random 模式

使用与输入无关的可训练常数矩阵：
$$
B = R \in \mathbb{R}^{n \times n}
$$
$R$ 在训练期间可更新或固定，相当于学习了一个全局的位置先验注意力模式。

### 低秩分解

为减少参数量，将 $R$ 分解为低秩乘积：
$$
B = R_1 R_2^\top, \quad R_1, R_2 \in \mathbb{R}^{n \times k}
$$

### 混合模式

可学习权重 $\alpha_i$ 将多种注意力得分叠加：
$$
B = \sum_i \alpha_i B_i
$$

## 典型步骤

1. **选择模式**：根据任务需求选择 Dense、Random 或混合模式
2. **生成注意力得分**：按所选模式计算 $B$ 矩阵
3. **Softmax 归一化**：$A = softmax(B)$
4. **值汇聚**：$O = A (XW_v)$

## 直觉

核心思想：**token 间的动态交互并非注意力的本质**。

标准自注意力的 $QK^\top$ 操作看似不可或缺，但 Synthesizer 揭示了一个反直觉的事实：$QK^\top$ 只是生成 $n \times n$ 注意力矩阵的一种方式，而非唯一方式。

- **Dense 模式**：每个位置根据自身特征直接"宣告"自己应该关注哪些位置。这等价于一种隐式的注意力先验——位置 $i$ 的注意力模式是位置 $i$ 特征的可学习函数。
- **Random 模式**：注意力模式完全不依赖于输入，就像卷积网络中的固定卷积核。这种方法能有效说明很多任务中的注意力模式实际上是位置相关的、任务特定的，而非内容相关的。

## 边界

- Dense 和 Random 模式在单任务场景（翻译、摘要、对话）中表现与标准注意力相当甚至更好
- **迁移学习能力弱**：在 T5 预训练微调范式下，标准注意力显著优于 Synthesizer 变体，说明动态 token 交互对通用表示学习至关重要
- Random 模式低秩分解中 $k$ 的选取需要在参数效率和表达力之间权衡
- 矩阵 $B \in \mathbb{R}^{n \times n}$ 显式存储，在极长序列下需配合低秩分解使用

## 例子

- **机器翻译**：Dense 和 Random 模式效果媲美标准注意力
- **对话生成**：Random 模式表现最好，标准注意力反而最差
- **摘要任务**：Dense 模式接近标准注意力
- **T5 预训练**：标准注意力最优，Synthesizer 变体在迁移上受限

## 证据

- ev::7430::Dense 模式公式：$B = relu(XW_1 + b_1)W_2 + b_2$
- ev::7430::Random 模式公式：$B = R$
- ev::7430::Factorized 低秩分解：$B = R_1 R_2^\top$
- ev::7430::实验结论：对话中标准注意力表现最差，Random 最优；迁移学习中标准注意力最优
