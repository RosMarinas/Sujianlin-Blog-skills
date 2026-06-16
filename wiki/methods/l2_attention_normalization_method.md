---
type: method
title: l2 注意力归一化方法
operation_types:
  primary: Rewrite / identity transform
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
source_ids:
  - "9105"
method_summary: 在自注意力计算中，通过将常规的对注意力得分矩阵做 Softmax 变换（基于 $l_1$ 范数归一化）改为基于平方和开方根做 $l_2$ 范数归一化，使得注意力矩阵的行概率和不再恒等于 1，从而在不增加多余参数的前提下打破了自注意力对全同输入的空间对称限制，增强了模型的理论表征容量。
typical_structure: |
  1. 通过 Query 和 Key 的内积计算自注意力得分矩阵：$\boldsymbol{B} = \frac{\boldsymbol{Q}\boldsymbol{K}^{\top}}{\sqrt{d_k}}$
  2. 对得分矩阵的每一行向量进行指数乘方变换：$e^{\boldsymbol{B}}$，计算 $l_2$ 归一化分母：$\boldsymbol{D}_i = \sqrt{\sum_{k} e^{2b_{i,k}}}$
  3. 进行 $l_2$ 归一化得到注意力分布：$a_{i,j} = \frac{e^{b_{i,j}}}{\boldsymbol{D}_i}$
  4. 将注意力权重作用于值向量，汇聚得到输出：$\boldsymbol{o}_i = \sum_{j} a_{i,j} \boldsymbol{v}_j$
applicability: 在使用相对位置编码的 Transformer 或 GAU 架构模型时，当需要提高模型对全同输入的空间位置分辨能力（解决拟合退化问题），或在大模型训练中需要加快收敛速度和轻微提升模型效果时采用此方法。
tools:
  - l2 注意力归一化
  - 非概率注意力
related_methods:
  - [[门控注意力与FFN的融合方法 (GAU)]]
  - [[标记符边界解耦位置法]]
examples:
  - [[article::9105]]
status: draft
updated: 2026-06-14
---

## 适用问题

使用相对位置编码（RoPE、T5、Transformer-XL 等）的 Transformer 存在一个理论缺陷：当输入序列的所有 token 完全相同时（全同输入），由于 Softmax 的行和恒为 1，自注意力的输出在每个位置上完全相同，模型无法区分不同位置的差异，丧失了理论上的万能拟合能力。l2 注意力归一化通过改变归一化方式打破这一对称性。

## 核心变换

**输入**：注意力得分矩阵 $\boldsymbol{B} \in \mathbb{R}^{n \times n}$
**输出**：经 l2 归一化的注意力权重 $a_{i,j}$
**关键性质**：$\sum_j a_{i,j} \neq 1$，行和随得分分布变化

标准 Softmax 归一化（l1 归一化）：
$$
a_{i,j} = \frac{e^{b_{i,j}}}{\sum_k e^{b_{i,k}}}, \quad \sum_j a_{i,j} = 1
$$

l2 注意力归一化：
$$
a_{i,j} = \frac{e^{b_{i,j}}}{\sqrt{\sum_k e^{2b_{i,k}}}}, \quad \sum_j a_{i,j} \neq 1
$$

在全同输入下，所有值向量 $\boldsymbol{v}_j = \boldsymbol{v}$，输出为：
$$
\boldsymbol{o}_i = \sum_j a_{i,j} \boldsymbol{v}_j = \left(\sum_j a_{i,j}\right)\boldsymbol{v}
$$

Softmax 下 $\sum_j a_{i,j} \equiv 1$，导致 $\boldsymbol{o}_i = \boldsymbol{v}$ 与位置 $i$ 无关。l2 归一化下 $\sum_j a_{i,j}$ 随得分分布变化，即使输入全同也可通过位置编码在得分上产生的微小差异来影响输出。

## 典型步骤

1. **计算得分**：$b_{i,j} = \frac{\boldsymbol{q}_i \boldsymbol{k}_j}{\sqrt{d_k}}$
2. **指数变换**：对得分矩阵逐元素求指数 $e^{b_{i,j}}$
3. **l2 归一化**：每行除以 l2 范数 $a_{i,j} = e^{b_{i,j}} / \sqrt{\sum_k e^{2b_{i,k}}}$
4. **值汇聚**：$\boldsymbol{o}_i = \sum_j a_{i,j} \boldsymbol{v}_j$

## 直觉

核心思想：**Softmax 的行和约束是空间对称性的根源**。

当所有输入 token 相同时，注意力得分矩阵 $\boldsymbol{B}$ 各行不同（因位置编码不同），但 Softmax 归一化强制每行之和为 1，相当于对每行施加了"总权重固定"的约束。在全同输入下，所有位置的 $\boldsymbol{v}$ 相同，$\boldsymbol{o}_i = (\sum_j a_{i,j})\boldsymbol{v} = \boldsymbol{v}$，输出与位置无关。

l2 归一化去掉了这个约束：虽然每行的元素经过了指数变换，但总和不固定。位置 $i$ 的注意力分布如果是"尖峰"（集中到少数位置），则 $\sum_j a_{i,j}$ 较大；如果是"平坦"（分散到多个位置），则总和较小。这种差异使得即使值向量相同，不同位置的汇聚结果也不同。

## 边界

- l2 归一化后注意力权重不再具有概率解释性（行和不为 1）
- 在 GAU 架构中（使用 $\text{relu}^2/n$ 归一化），l2 归一化可加速收敛并轻微提升效果
- 与插入 `[CLS]`/`[SEP]` 等边界标记符相比，l2 归一化从数学上修复了缺陷，而非通过工程技巧绕过
- 该方法不增加额外参数，替换成本极低

## 例子

- 全同输入探针实验：输入全 0 序列，要求输出有序位置编号 $[1, 2, \dots, n]$，l2 归一化模型可通过该探针，而 Softmax 模型无法通过
- GAU 模型使用 l2 归一化替代 $\text{relu}^2/n$ 后，训练收敛速度加快，下游任务效果轻微提升

## 证据

- ev::9105::全同输入理论缺陷证明：$\boldsymbol{o}_i = \sum_j a_{i,j}\boldsymbol{v}_j = \boldsymbol{v}$ 的行和恒为 1 推导
- ev::9105::l2 归一化公式：$a_{i,j} = e^{b_{i,j}} / \sqrt{\sum_k e^{2b_{i,k}}}$
- ev::9105::探针实验证明：l2 归一化模型可通过全同输入排序探针
