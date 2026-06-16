---
type: concept
definition: Nyströmformer通过选取Q,K的聚类中心，把完整Attention矩阵近似为三个小矩阵乘积，并用伪逆处理中间矩阵。
title: Nyströmformer
aliases:
- Nystromformer
- Nyström Attention
source_ids:
- '8180'
evidence_spans:
- ev::8180::三矩阵近似
- ev::8180::伪逆近似
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
---

# Nyströmformer

Nyströmformer 是一种基于矩阵分解的线性化 Attention 方案，它借鉴了 Nyström 方法的思想来构建一个能逼近标准 Attention 的线性 Attention。它通过选取 $\boldsymbol{Q},\boldsymbol{K}$ 的聚类中心，把完整 Attention 矩阵近似为三个小矩阵乘积，并用伪逆处理中间矩阵，从而将标准 Attention 的 $\mathcal{O}(n^2)$ 复杂度降为线性复杂度。

## 数学定义与核心公式

Nyströmformer 先分别将 $\boldsymbol{Q},\boldsymbol{K}$ 视为 $n$ 个 $d$ 维向量，然后聚成 $m$ 类来得到 $m$ 个聚类中心构成的矩阵 $\tilde{\boldsymbol{Q}},\tilde{\boldsymbol{K}}\in\mathbb{R}^{m\times d}$。

为了确保当 $m=n$ 时完全等价于标准Attention，Nyströmformer 最终的 Attention 矩阵形式定义为：
$$
softmax\left(\boldsymbol{Q}\tilde{\boldsymbol{K}} ^{\top}\right) \, \left(softmax\left(\tilde{\boldsymbol{Q}}\tilde{\boldsymbol{K}}^{\top}\right)\right)^{\dagger} \, softmax\left(\tilde{\boldsymbol{Q}}\boldsymbol{K}^{\top}\right)
$$
由于它变成了三个小矩阵的乘积，可以通过矩阵乘法的结合律转化为线性 Attention计算。公式中的 $\dagger$ 表示伪逆（Moore-Penrose逆），因为 $softmax\left(\tilde{\boldsymbol{Q}}\tilde{\boldsymbol{K}}^{\top}\right)$ 未必可逆。

## 关键属性与边界条件

*   **迭代近似求逆 (pINV)**：
    标准的 SVD 求伪逆计算量大且不容易求梯度，Nyströmformer 采用 Chebyshev 类型的迭代格式来逼近伪逆 $\boldsymbol{A}^{\dagger}$：
    $$
    \boldsymbol{V}_{n+1} = \frac{1}{4} \boldsymbol{V}_n (13 \boldsymbol{I} − \boldsymbol{A} \boldsymbol{V}_n (15 \boldsymbol{I} − \boldsymbol{A} \boldsymbol{V}_n (7 \boldsymbol{I} − \boldsymbol{A} \boldsymbol{V}_n)))
    $$
    原论文中只用上述格式迭代 6 次的结果来代替 $\boldsymbol{A}^{\dagger}$。因为所选的 $m$ 较小（原论文选择 $m=64$），迭代过程仅涉及矩阵乘法，梯度易于求解且计算量可控。
*   **Segment-Means 自适应平均池化**：
    为了解决标准 K-Means 中 $\mathop{\text{argmin}}$ 操作无法求梯度的问题，Nyströmformer 使用了非常简单的自适应平均池化（Adaptive Average Pooling / Segment-Means）来替代聚类：将 $\boldsymbol{Q},\boldsymbol{K}$ 的每 $n/m$ 个向量求平均作为 $\tilde{\boldsymbol{Q}}, \tilde{\boldsymbol{K}}$ 的每个向量。
*   **自回归限制（边界案例）**：
    由于自适应池化会“糅合”每一个区间的信息，导致它不能防止未来信息泄漏，从而**不能做自回归生成**（例如无法用于语言模型或 Seq2Seq 的解码器）。

## 与其他概念及方法的关系

*   **与 Performer 的对比**：
    与 Performer 模型类似，都是通过某种方式将 Attention 的复杂度线性化。但 Performer 是通过随机投影来达到线性化的，必然会带来随机性；而 Nyströmformer 去除了线性化过程中的随机性，是一个确定性的近似方案。
*   **与矩阵 CUR 分解及 Nyström 方法的关系**：
    Nyströmformer 借鉴了 CUR 分解及 Nyström 方法的降维思想。CUR 分解的形式为 $\boldsymbol{A} \approx \boldsymbol{C}\boldsymbol{U}\boldsymbol{R}$；而 Nyström 矩阵分解形式为：
    $$
    \begin{pmatrix}\boldsymbol{A} & \boldsymbol{B} \\ \boldsymbol{C} & \boldsymbol{D}\end{pmatrix} \approx \begin{pmatrix}\boldsymbol{A} \\ \boldsymbol{C}\end{pmatrix} \boldsymbol{A}^{\dagger} \begin{pmatrix}\boldsymbol{A} & \boldsymbol{B}\end{pmatrix}
    $$
    通过提取原矩阵部分行列进行近似。Nyströmformer 巧妙结合此思想构建了带伪逆的小矩阵乘法结构。

## 具体示例与效果

在预训练任务中，使用 Segment-Means 选取聚类且设 $m=64$ 时，Nyströmformer 展现出极强竞争力：在 MLM（Masked Language Modeling）任务上的效果甚至比标准 Attention（如 Small 和 Base 版本的 BERT）还要优异。
