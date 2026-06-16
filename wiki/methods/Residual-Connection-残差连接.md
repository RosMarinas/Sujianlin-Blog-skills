---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: 残差连接 (Residual Connection)
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-19-为什么需要残差-一个来自DeepNet的视角.md
  - Data/wiki/sources/spaces-8994-为什么需要残差.md
source_ids:
  - 8994
method_summary: 要使梯度缩放至 $\mathcal{O}(1/\sqrt{N})$（$N$ 为总层数），设置： $$ \varepsilon = \frac{1}{\sqrt{N}} $$
typical_structure: |
  1. 定义残差分支的非线性变换函数 $F(x)$。
  2. 选定残差分支相对于深度的放缩系数 $\varepsilon$（如 $1/\sqrt{N}$）。
  3. 将残差分支计算输出 $\varepsilon F(x)$ 并同原始输入相加得到 $y = x + \varepsilon F(x)$。
  4. 将合并后的输出进行层归一化或激活传递至更深的网络层。
applicability: 构建极深神经网络（数百、千层）且避免因层数增加产生的“增量爆炸”、梯度消失及梯度爆炸，实现稳定前反向传播。
examples:
  - [[article::8994]]
status: stable
updated: 2026-06-12
tags: 
belongs_to: 
layering: 
formula_standard_notation: true
related_concepts: 
problem_patterns: 
evidence_spans: 
  - ev::8994::"残差结构是可以同时稳定前向传播和反向传播、并且可以缩放参数梯度以解决增量爆炸的一种设计...要想梯度缩放到$1/\sqrt{N}$，那么让$\varepsilon=1/\sqrt{N}$即可"
---

# 残差连接 (Residual Connection)

## 适用问题

在网络层数极其庞大（百层以上）时，普通的深层前馈网络随着优化步数会面临“参数微小变化诱发巨大输出变动”的增量爆炸困境，且初始化策略难以单独抵消随深度放大的梯度影响，直接制约超深层 Transformer 乃至 DeepNet 的规模化训练收敛性。

## 核心变换

将非线性的序列复合函数映射重构为“线性直通（恒等映射） + 非线性增量扰动”形式，并通过控制非线性扰动量级的标量系数将梯度与层深相解耦。

## 典型步骤

1. **获取输入**：得到当前层 $l$ 的隐含输入向量 $x$。
2. **分支计算**：将该向量送入该层的主要非线性处理分支 $F(x)$ 中处理（如全连接加上非线性激活，或注意力汇聚模块）。
3. **调节比例**：基于系统总层深 $N$ 动态约束非线性量级，应用标量因子 $\varepsilon$ （当 $N \to \infty$ 时，设为 $1/\sqrt{N}$）对支路进行缩放得到 $\varepsilon F(x)$。
4. **恒等聚合**：将未修改的输入 $x$ 本身和缩放后的分支信号通过矩阵逐元素加和合并：$y = x + \varepsilon F(x)$。

## 直觉

如果你想从 1 加到 1000 并且每一步都不失控，最好保证起初传递信息的“主干道”根本不发生大变形（它就是原本的自己）。每一层仅仅在它身上微调一小撮改变。由于大部分输入直接畅通无阻地溜到了下一层，微小的修正即使迭代1000次也只能逐步积累，前向和反向传播的稳定性都不会被深度层层吞噬。

## 边界

- **缩放系数 $\varepsilon$ 依赖**：如果 $\varepsilon$ 不能有效根据层数 $N$ 在初始化阶段加以控制，依然会出现深层梯度膨胀的状况。
- **架构依赖性**：对输入和输出必须强制使用相同特征维度，否则只能辅以投影矩阵转换。且往往强绑定于特定的 Normalization 位置配合（如 Pre-LN 结构）来保障极致的稳定。

## 例子

- **千层 Transformer (DeepNet)**：通过巧妙控制残差分支初始化量级（等效于 $\varepsilon \approx 1/\sqrt{N}$）以及增加恒等路径的权重，使得 1000 层以上的 Transformer 免除了极容易诱发失败的 “增量爆炸”问题，成功得到训练收敛。

## 证据

- ev::8994::"残差结构是可以同时稳定前向传播和反向传播、并且可以缩放参数梯度以解决增量爆炸的一种设计，它能帮助我们训练更深层的模型。"
- ev::8994::"所以也可以看出，只要$\varepsilon$足够小，那么反向传播也是稳定的。至于参数的梯度...这说明我们可以通过控制$\varepsilon$来实现层数相关的梯度缩放！比如要想梯度缩放到$1/\sqrt{N}$，那么让$\varepsilon=1/\sqrt{N}$即可。"
