---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: TTT框架构建RNN
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-03-18-时空之章-将Attention视为平方复杂度的RNN.md
source_ids:
  - 10017
  - 11320
method_summary: TTT（Test Time Training）将序列模型构建视为在线学习问题，通过优化器在推理阶段更新模型隐状态来记忆历史上下文。
typical_structure: |
  1. 将序列的历史输入转换为键值对 $(\boldsymbol{k}_t, \boldsymbol{v}_t)$，并将其视作在线学习（Online Learning）的训练样本。
  2. 初始化一个映射模型 $\boldsymbol{f}$ 及其权重参数 $\boldsymbol{S}_0$。
  3. 在每一步 $t$，使用优化器（如 SGD）沿梯度方向更新参数矩阵：$\boldsymbol{S}_t = \boldsymbol{S}_{t-1} - \eta_t\nabla_{\boldsymbol{S}_{t-1}}\mathcal{L}$，使得模型拟合历史键值对。
  4. 对于当前查询 $\boldsymbol{q}_t$，通过前向传播 $\boldsymbol{o}_t = \boldsymbol{f}(\boldsymbol{S}_t; \boldsymbol{q}_t)$ 获取输出，从而实现 RNN 般的常数空间复杂度推理。
applicability: 在序列建模中，当面临传统注意力机制的平方复杂度且难以缩放，希望通过常数空间复杂度的 RNN 架构实现长期记忆（长文本或复杂序列）时。
evidence_spans:
  - ev::11320::"TTT基于优化器更新与RNN迭代的相似性，通过优化器来构建（不一定是线性的）RNN模型，诸如DeltaNet、GDN、Comba等线性Attention都可以看成它的特例"
  - ev::11320::"核心任务是利用“训练模型”约等于“背诵训练集”这件事情，来实现$\boldsymbol{K},\boldsymbol{V}$的压缩"
  - ev::10017::"Attention可以重写成RNN的形式，并且它的每一步生成理论上也能够以$\mathcal{O}(1)$的空间复杂度进行"
examples:
  - [[article::10017]]
  - [[article::11320]]
status: stable
updated: 2026-06-13
---

# TTT框架构建RNN

## 适用问题

序列建模中需要以常数空间复杂度处理长文本，同时希望模型能够充分记住历史上下文，从而避免普通 RNN 的记忆瓶颈以及传统 Softmax Attention 的平方级显存增长。

## 核心变换

将普通的键值对 $\boldsymbol{K}, \boldsymbol{V}$ 缓存机制（KV Cache），变换为利用这些历史语料对训练一个隐含模型的“在线学习（Online Learning）”过程。即把“提取特征”变换为“Test Time Training (TTT)”，将历史信息压缩为固定大小的模型参数状态 $\boldsymbol{S}_t$，由当前查询 $\boldsymbol{q}_t$ 读取。

## 典型步骤

1. **构造语料对**：将序列的历史输入转换为一系列键值对 $(\boldsymbol{k}_t, \boldsymbol{v}_t)$，视作在线学习任务的监督训练集。为避免键值同源造成的平凡解，可通过在 $\boldsymbol{K}$ 加入 Short Conv 使任务变为“根据上一时刻预测当前时刻”（Next Token Prediction，NTP）。
2. **初始化模型**：定义一个以 $\boldsymbol{S}_0$ 为状态参数的内部函数 $\boldsymbol{v} = \boldsymbol{f}(\boldsymbol{S}_t; \boldsymbol{k})$。
3. **在线更新记忆**：随着时间步 $t$ 推移，使用优化器（如 SGD 或 Muon）计算损失函数 $\mathcal{L}$ 对参数 $\boldsymbol{S}_{t-1}$ 的梯度，更新得到当前时间步的状态矩阵：$\boldsymbol{S}_t = \boldsymbol{S}_{t-1} - \eta_t\nabla_{\boldsymbol{S}_{t-1}}\mathcal{L}(\boldsymbol{f}(\boldsymbol{S}_{t-1};\boldsymbol{k}_t), \boldsymbol{v}_t)$。
4. **提取信息**：利用当前时间步的查询向量 $\boldsymbol{q}_t$，代入更新后的状态模型计算输出 $\boldsymbol{o}_t = \boldsymbol{f}(\boldsymbol{S}_t; \boldsymbol{q}_t)$，用于最终解码。

## 直觉

“训练模型”本质上等同于“背诵训练集”。既然注意力机制的核心是利用 KV 字典提取和压缩历史序列的知识，我们不如直接在推理时（Test Time）的每一步，内部做一次“训练任务”。通过让状态矩阵 $\boldsymbol{S}_t$ 持续且增量地拟合之前的 $(\boldsymbol{k}_i, \boldsymbol{v}_i)$ 数据分布，它自然就“背下”了过去的上下文，以此将序列压缩进常数大小的权重参数里。

## 边界

- **键值同源的退化**：若 $\boldsymbol{K}$ 和 $\boldsymbol{V}$ 来源于同一个特征映射的完全相同拷贝，可能导致模型只学到平凡的恒等变换。这要求引入一定的局部扰动（如 Short Conv）打破这种“自己预测自己”的设定。
- **时间效率损耗**：由于在每一步前向计算中嵌套了梯度下降等优化步骤，其实际时间计算量远大于普通 RNN 单元。常数空间复杂度的优势只有在需要处理极长序列从而遭遇严重内存瓶颈时，收益才会大于其计算开销。

## 例子

在诸如 DeltaNet 的线性注意力架构中，就是 TTT 框架下模型选择了简单的线性回归模型 $\boldsymbol{v} = \boldsymbol{S}_t\boldsymbol{k}$，损失函数采用最简单的平方误差。通过标准的随机梯度下降 SGD 更新：$\boldsymbol{S}_t = \boldsymbol{S}_{t-1} - \eta_t\nabla\mathcal{L}$ 形成时序动力学。当为 $\boldsymbol{K}$ 增加 Short-Conv 时，实质上是让模型混合过去的词进行未来的预测（n-gram 模型），有效增强了信息的压缩与表达能力。

## 证据

- ev::11320::"TTT基于优化器更新与RNN迭代的相似性，通过优化器来构建（不一定是线性的）RNN模型，诸如DeltaNet、GDN、Comba等线性Attention都可以看成它的特例。"
- ev::11320::"TTT将$\boldsymbol{K},\boldsymbol{V}$视为成对的语料...核心任务是利用“训练模型”约等于“背诵训练集”这件事情，来实现$\boldsymbol{K},\boldsymbol{V}$的压缩。"
- ev::10017::"Attention可以重写成RNN的形式，并且它的每一步生成理论上也能够以$\mathcal{O}(1)$的空间复杂度进行（代价是时间复杂度非常高，远超平方级）。"
