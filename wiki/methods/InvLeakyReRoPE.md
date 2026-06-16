---

type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: InvLeaky ReRoPE逆用长度外推
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-06-02-我们可以无损放大一个Transformer模型吗-一.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2022-03-09-训练1000层的Transformer究竟有什么困难.md
source_ids:
  - 9728
method_summary: InvLeaky ReRoPE是Leaky ReRoPE的逆向应用。在训练阶段使用外推惩罚形式（更小步长），从而在推理时可以退回常规无惩罚形式（正常步长），将额外计算开销从推理转移到训练。
typical_structure: |
  1. 在模型训练阶段，修改相对位置矩阵为带窗口外的衰减步长（即 Leaky ReRoPE，步长 > 1）。
  2. 训练模型时设置参数 $k$（建议为扩展倍数的倒数的两倍）和窗口 $w$（建议为训练长度的 1/4）。
  3. 模型训练完成后进行推理。
  4. 推理阶段退化为使用常规的标准 RoPE 相对位置编码（步长 = 1）。
applicability: 需要获取长度外推能力，且希望不增加推理阶段的计算负担或需要兼容现有注意力加速技术时。
examples:
  - [[article::9728]]
status: stable
updated: 2026-06-13
created: 2026-06-10
tags: 
related_articles: 
related_concepts: 
evidence_spans: 
  - ev::9728::原文提出“能否让训练阶段变慢，让推理阶段变为常规的RoPE...在训练阶段使用Leaky ReRoPE，并让它窗口外的步长大于1”。
---




## 适用问题
需要在基于旋转位置编码（RoPE）的大语言模型中实现长度外推，但又不能接受像 ReRoPE 或 Leaky ReRoPE 在推理时因重算注意力矩阵造成的延迟（例如需兼容 Flash Attention 加速技术）。

## 核心变换
将 ReRoPE 解决外推的“惩罚设计”反向操作：不再是“训练用标准 RoPE，推理用 Leaky ReRoPE”，而是**“训练阶段使用窗口外步长大于1的 Leaky ReRoPE，推理阶段反而退回标准 RoPE（步长等于1）”**。

## 典型步骤
1. 定义窗口大小 $w$（通常取训练上下文长度的 1/4 到 1/2）和比例因子 $k$。
2. 训练阶段：对超出一个局部窗口 $w$ 的相对距离施加修正步长（$1/k > 1$），强制模型在训练时就学会在压缩的高密度相对位置下工作。
3. 训练过程可能因相对位置矩阵计算变复杂而略微变慢（如速度下降 10%~50%），但属于一次性成本。
4. 推理阶段：去掉窗口限制与惩罚，直接退化回标准 RoPE，由于步长变成 $1 < 1/k$，等同于拉伸了分辨率，从而顺利支持处理更长的序列。

## 直觉
由于目标是“Train Short, Test Long”，也就是训练的代价是一次性的、短期可控的，而推理的负担是长期的。通过对训练阶段的相对位置施加“压缩惩罚”（大步长），那么当测试时恢复正常步长，模型就感觉外推的距离仍然在它训练过的压缩距离视野内。这就相当于在训练期间戴着沙袋负重练习，比赛（推理）时卸下沙袋，反而更游刃有余。

## 边界
实验显示，“Leaky ReRoPE → RoPE”的组合在性能上不如顺向的“RoPE → ReRoPE/Leaky ReRoPE”，不过依然胜过了单纯的局部窗口注意力（HWFA）或直接插值方案，属于折衷手段。

## 例子
对于一个 1 亿参数语言模型，训练长度 512，将步长参数 $k$ 设置为 1/16，$w=128$。此时训练每 1000 步的时间仅增加了约 6%，而在 4096 长度的测试中，保持了 48.32% 的外推准确率，而且推理速度保持不变。

## 证据
- ev::9728::提出核心反转：“能否让训练阶段变慢，让推理阶段变为常规的RoPE？...在训练阶段使用Leaky ReRoPE，并让它窗口外的步长大于1”。
- ev::9728::说明了为什么这样设计：“训练速度的变慢是短期的、可控的，推理速度的变慢才是长期的、难顶的，所以相较之下...我们更愿意将变慢的部分放到训练阶段”。
