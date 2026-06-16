---
type: method
title: Talking-Heads Attention 混合注意力分布
operation_types:
  primary: Structure-expose by factorization
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
source_ids:
  - "7325"
method_summary: 通过在自注意力的 Softmax 计算之前和之后引入可训练的线性映射参数矩阵，将各个相互孤立的多头自注意力矩阵（得分矩阵与混合概率矩阵）进行加权求和（混合），实现头信息的充分流转与协同表示，极大地增强了自注意力的概率分布拟合能力。
typical_structure: |
  1. 计算各个头独立的自注意力得分矩阵：$\hat{J}^{(i)} = Q^{(i)} {K^{(i)}}^\top$
  2. 在 Softmax 之前，乘上可训练投影矩阵 $\lambda$ 混合头得分：$J^{(i)} = \sum_{j} \lambda_{ij} \hat{J}^{(j)}$
  3. 对混合得分矩阵进行 Softmax 归一化：$P^{(i)} = softmax(J^{(i)})$
  4. 对各头特征进行 Value 融合：$O^{(i)} = P^{(i)} V^{(i)}$，最后拼接并映射输出
applicability: 当需要增强多头注意力的拟合表征能力，或者希望在缩减单个头维度（head_size）的同时通过头间联合分布保留模型表示容量时采用此方法。
tools:
  - 头间混合投影
  - 注意力分布混合
related_methods:
  - [[增大key_size解除注意力低秩瓶颈]]
  - [[Synthesizer静态注意力生成]]
examples:
  - [[article::7325]]
status: draft
updated: 2026-06-14
---

## 适用问题

标准多头自注意力中各头独立计算注意力分布，头与头之间没有信息交互。这种"各扫门前雪"的设计意味着每个头只能依赖自己有限的投影维度 $head\_size$ 来拟合注意力模式，无法通过头间协同来表达更复杂的联合分布。当 $head\_size$ 较小时，这一问题尤为突出。

## 核心变换

**输入**：各头的独立注意力得分矩阵 $\hat{J}^{(i)} \in \mathbb{R}^{n \times n}$
**输出**：头间混合后的注意力概率矩阵 $P^{(i)} \in \mathbb{R}^{n \times n}$
**参数**：可训练的混合投影矩阵 $\lambda \in \mathbb{R}^{h \times h}$（和可选的后 Softmax 混合矩阵）

### Softmax 之前的头间混合

设第 $i$ 个头的注意力得分为 $\hat{J}^{(i)} = Q^{(i)}{K^{(i)}}^\top$。引入可训练混合矩阵 $\lambda$，将各头得分线性组合：

$$
J^{(i)} = \sum_{j=1}^{h} \lambda_{ij} \hat{J}^{(j)}
$$

对混合后的得分应用 Softmax：
$$
P^{(i)} = softmax(J^{(i)})
$$

### Softmax 之后的可选二次混合

可进一步引入第二个混合矩阵，对注意力概率分布再次线性组合。

## 典型步骤

1. **计算各头得分**：对每个头独立计算 $Q^{(i)}{K^{(i)}}^\top$
2. **前 Softmax 混合**：使用可训练矩阵 $\lambda$ 对各头得分加权求和
3. **Softmax 归一化**：对混合得分应用 Softmax 得到注意力概率
4. **后 Softmax 混合（可选）**：再次引入投影矩阵对概率分布进行二次线性混合
5. **值汇聚**：每个头用得到的混合分布加权值向量 $V^{(i)}$，拼接后映射输出

## 直觉

核心思想：**多头的力量在于联合，而非独立**。

标准多头注意力类似于 $h$ 个独立专家各自投票然后简单拼接。Talking-Heads 则允许专家们在形成最终意见前相互交流——在 Softmax 之前混合得分矩阵，相当于让各头在"打分阶段"共享信息；在 Softmax 之后混合概率分布，则相当于让各头在"决策阶段"再次协商。

从分布拟合的角度看，Talking-Heads 等价于混合高斯模型（GMM）：每个头产生一个注意力分布，通过线性混合得到更复杂的多模态分布。这打破了单个注意力分布的单调性限制，使模型能够表达"关注位置 A 同时忽略位置 B"这类复杂的注意力模式。

## 边界

- 引入两个 $h \times h$ 的混合矩阵，额外参数量极小（$2h^2$），计算开销可忽略
- 前 Softmax 混合改变的是得分（logits）空间，后 Softmax 混合改变的是概率空间，二者作用不同，可根据需求选择
- 与[[增大key_size解除注意力低秩瓶颈]]互补：Talking-Heads 通过头间协同增强表达，增大 key_size 通过增大单个头的表达空间增强表达
- 混合矩阵 $\lambda$ 的初始化为单位矩阵较合理，确保初始状态下各头保持独立

## 例子

- 在 $head\_size$ 较小的 Transformer 中，Talking-Heads 可显著提升注意力分布的拟合能力
- 与 key_size 增大技术结合使用时，可在更小的 key_size 下达到与大幅增大 key_size 相当的效果
- 实验证明，混合分布能使小 key_size 在多头叠加下表现出与标准注意力匹敌甚至更优的性能

## 证据

- ev::7325::Talking-Heads 公式推导：公式 (86) 到 (94) 的混合变换
- ev::7325::前 Softmax 混合公式：$J^{(i)} = \sum_j \lambda_{ij} \hat{J}^{(j)}$
- ev::7325::实验结论：混合分布能使小 key_size 在多头叠加下表现强劲
