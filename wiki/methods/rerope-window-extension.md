---


type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: ReRoPE窗口外推方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-31-Transformer升级之路-11-将β进制位置进行到底.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-07-Transformer升级之路-12-无限外推的ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-24-Transformer升级之路-14-当HWFA遇见ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-20-Transformer升级之路-15-Key归一化助力长度外推.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-01-26-Transformer升级之路-16-复盘-长度外推技术.md
source_ids:
  - 9706
  - 9708
  - 9728
  - 9731
  - 9859
  - 9948
method_summary: ReRoPE窗口外推方法是一种免微调的长度外推技术，通过在推理阶段将相对位置矩阵截断到窗口w以内，实现理论上无限的长度外推。
typical_structure: |
  1. 设定一个局域相对位置窗口大小 $w$（通常小于训练长度）。
  2. 对于相对距离在窗口内（$< w$）的注意力连接，使用未经修改的原始 RoPE 矩阵进行计算。
  3. 对于相对距离在窗口外（$\ge w$）的注意力连接，强制将其相对位置全部截断为常数 $w$（或者按倒数步长等效缩小），计算出受限的注意力分数。
  4. 利用分块掩蔽（Mask）组合二者的结果完成自注意力归约。
applicability: 在已训完的纯 RoPE Transformer 模型上，直接免微调且理论无限地扩大外推文本长度的应用环境。
examples:
  - [[article::9708]]
  - [[article::9731]]
  - [[article::9948]]
status: stable
updated: 2026-06-12
created: 2026-06-09
tags: 
related_articles: 
related_concepts: 
problem_patterns: 
evidence_spans: 
  - ev::9708::"通过在推理阶段将相对位置矩阵截断到窗口w以内，实现理论上无限的长度外推"
proposes: ""
---

# ReRoPE窗口外推方法

## 适用问题

经过在受限序列长度下使用旋转位置编码（RoPE）预训练完毕的模型，推理遇到超长文本外推时，由于绝对及相对距离超过训练所见范围而发生急剧失效。希望能在此基础上完全“免微调”地支持极长推理。

## 核心变换

抛弃长距离绝对顺序依赖，将“随距离无限增加的衰减矩阵”变换为“局域保持精确坐标，远距强行截断为统一常量坐标”的逻辑矩阵拼接。

## 典型步骤

1. **选择阈值**：选取一个局部特征有效捕获的窗口尺寸 $w$，一般为模型预训练窗口长度的 $1/4$ 到 $1/2$。
2. **标准矩阵计算**：根据传统 RoPE 计算全局 Attention logits（负责处理近距离特征）。
3. **常量矩阵计算**：假定所有跨距超出的长程节点相对距离全部截断为 $w$（这导致所有超出这范围的 Token 之间相当于只共用同一个“远距离”表征，类似于 Leaky RoPE 取 $k\to\infty$），计算第二层 Attention Logits。
4. **拼接判断**：在计算 $o_t$ 向量归一化聚合时，对相对距离 $i-j < w$ 的组合调用第一个矩阵值，对 $i-j \ge w$ 的组合调用第二个矩阵值。
5. **正常聚合输出**。

## 直觉

既然模型只在训练长度之内才懂相对距离是怎么分配的，跑到训练长度外头就会发疯，那我就立个规矩：所有超出一个固定距离窗口的标记，统统一视同仁当作最远合法位置处理。虽然这损失了超远距离的相对顺序细节，但远距离关联本身就是一团不需要极高时序分辨率的统计背景（词袋效果）。只要近处的关联（窗口内）保真，大段文本堆叠也不会让位置网络由于越界计算而崩盘。

## 边界

- **计算负担**：由于矩阵计算时包含条件判断和两套矩阵混用，很难无缝兼容现成的 FlashAttention 硬件级融合优化，常常导致推断时间严重减慢。必须借助如 HWFA 等分解策略来进行联合加速。
- **窗口依赖**：若 $w$ 定得太小，无法获取哪怕中距离的基础顺序信息；若定得太大，等于丧失外推防崩功能。

## 例子

- **免微调扩展 LLAMA 上下文**：对于原本只能推理有限长度的 LLAMA 系列，通过加入 ReRoPE 设定截断窗口为 256，可以使得语言模型跨到上万乃至极长的 Tokens 测试中，Loss 仍维持稳定平滑衰退而不暴增。

## 证据

- ev::9708::"ReRoPE窗口外推方法是一种免微调的长度外推技术，通过在推理阶段将相对位置矩阵截断到窗口w以内，实现理论上无限的长度外推。"
- ev::9708::"w约为训练长度的1/4到1/2（如训练长度512则w取128-256）...根据条件 i - j < w 选择矩阵1（窗口内）或矩阵2（窗口外）"
