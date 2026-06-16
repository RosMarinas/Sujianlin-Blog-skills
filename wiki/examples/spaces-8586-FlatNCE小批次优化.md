---
type: example
title: FlatNCE小批次优化
article_id: 8586
article: FlatNCE：小批次对比学习效果差的原因竟是浮点误差？
section: 变微为著
claim: 通过FlatNCE一阶展开和 stop_gradient 等效公式去除正对得分以改善小批次训练精度的计算步骤。
steps: 1. 计算正样本得分 $s_t$ 与其他负样本得分 $s_i$；\n2. 估计对比项 $\xi = \sum_{i \neq t} e^{s_i - s_t}$。在微调快收敛时 $\xi \to 0$；\n3. 为避免浮点下溢，引入 FlatNCE 缩放形式：$\frac{\xi}{\text{sg}(\xi)}$；\n4. 梯度链求偏导发现：$\nabla_{\theta}(\frac{\xi}{\text{sg}(\xi)}) = \frac{\nabla_{\theta}\xi}{\xi} = \nabla_{\theta} \log \xi$；\n5. 将对数负得分和做展开：$\log \xi = \log(\sum_{i \neq t} e^{s_i}) - s_t$；\n6. 采用该损失更新参数，消除对超大 batch 的绝对约束。
used_concepts: ["[[FlatNCE]]"]
notation_mapping: {"s_t": "正对打分表示", "\\xi": "负样本相对相似度指数求和"}
source_span: ev::8586::FlatNCE等效
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-07-26-FlatNCE-小批次对比学习效果差的原因竟是浮点误差.md"]
source_ids: ["8586"]
status: stable
updated: 2026-06-12
---

# FlatNCE小批次优化

## 演示过程
本例展示如何通过 FlatNCE 数学公式变形，在不携带 stop_gradient 算子下消除交叉熵的下溢梯度噪声。

考虑对数损失公式为 $\mathcal{L} = \log(1+\xi)$。
求梯度：
$$
\nabla_{\theta} \mathcal{L} = \frac{\nabla_{\theta} \xi}{1+\xi} \approx \nabla_{\theta} \xi \quad (\xi \to 0)
$$
由于自适应优化器如 Adam，其更新大小正比于 $\text{sgn}(\nabla_{\theta} \mathcal{L})$，而 $\xi$ 本身下溢造成的舍入误差会主导该梯度符号。
设计 FlatNCE 对比函数：
$$
\mathcal{L}_{\text{Flat}} = \frac{\xi}{\text{sg}(\xi)}
$$
其关于参数 $\theta$ 的梯度流完全等于对数求和：
$$
\nabla_{\theta} \mathcal{L}_{\text{Flat}} = \frac{\nabla_{\theta} \xi}{\xi} = \nabla_{\theta} \log \xi
$$
因为：
$$
\log \xi = \log \left(\sum_{i \neq t} e^{s_i - s_t}\right) = \log\left(\sum_{i\neq t} e^{s_i}\right) - s_t
$$
以该式为损失直接计算，由于 LogSumExp 可被稳定并行估计，从而彻底消除了浮点误差的舍入干扰。