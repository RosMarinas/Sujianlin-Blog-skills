---
type: example
title: 对比学习梯度累积
article_id: 8471
article: 对比学习可以使用梯度累积吗？
section: 内积
claim: 利用偏导数重写公式，将InfoNCE的多样本耦合损失导数解调为单样本与辅助特征向量内积偏导累加的步骤。
steps: 1. 读入大 batch $nb$ 个样本的内积打分 $s_{i,j}=\langle h_i, h_j \rangle$；\n2. 在不追踪梯度的图（`stop_gradient`）下，计算前向概率矩阵项 $p_{i,j} = e^{s_{i,j}}/\sum_m e^{s_{i,m}}$；\n3. 根据对称内积导数性质，求出偏导线性加权和并缓存常数辅助向量标签 $\tilde{h}_i$；\n4. 将导数表达式转化为对无多体交互损失 $\sum_i \langle h_i, \tilde{h}_i \rangle$ 的求导；\n5. 将样本 $\{h_i\}$ 划分为 $n$ 批，分步前向求出对参数 $\theta$ 的小批偏导，执行梯度累加，最后在步终更新参数。
used_concepts: ["[[FlatNCE]]"]
notation_mapping: {"\\tilde{h}_i": "第 i 样本在当前大批次下拟合的目标均值表示", "p_{i,j}": "内积的 softmax 预测概率"}
source_span: ev::8471::梯度累积
sources: ["Data/Spaces_ac_cn/markdown/Mathematics/2021-06-17-对比学习可以使用梯度累积吗.md"]
source_ids: ["8471"]
status: stable
updated: 2026-06-12
---

# 对比学习梯度累积

## 演示过程
本例展示如何通过将 InfoNCE 对比损失求导，转化为对单样本内积求和梯度进行精确累积。

对比交叉熵损失为：
$$
\mathcal{L} = -\sum_{i,j} t_{i,j} \log p_{i,j}
$$
其关于特征内积 $s_{i,j} = \langle h_i, h_j \rangle$ 的导数为：
$$
\frac{\partial \mathcal{L}}{\partial s_{i,j}} = p_{i,j} - t_{i,j}
$$
损失的梯度为：
$$
\nabla_{\theta} \mathcal{L} = \sum_{i,j} (p_{i,j} - t_{i,j}) \nabla_{\theta} s_{i,j}
$$
因为 $s_{i,j}$ 对 $\theta$ 的梯度满足：
$$
\nabla_{\theta} s_{i,j} = \langle \nabla h_i, h_j \rangle + \langle h_i, \nabla h_j \rangle
$$
代入上式，并利用求和下标对称性，有：
$$
\nabla_{\theta} \mathcal{L} = \sum_{i} \left\langle \nabla h_i, 2\sum_{j} (\overline{p_{i,j}} - t_{i,j}) h_j \right\rangle
$$
其中 $2\overline{p_{i,j}} = p_{i,j} + p_{j,i}$。
若把辅助组合向量定义为常数标量：
$$
\tilde{h}_i = 2\sum_{j} (\overline{p_{i,j}^{(sg)}} - t_{i,j}) h_j^{(sg)}
$$
则梯度完全等价于单样本目标：
$$
\nabla_{\theta} \mathcal{L} = \nabla_{\theta} \sum_{i} \langle h_i, \tilde{h}_i \rangle
$$
此结构使得多样本完全解耦，支持了常规的分步梯度累加。