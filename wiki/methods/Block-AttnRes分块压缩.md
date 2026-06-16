---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: Block AttnRes分块压缩层间注意力
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-03-19-Attention-Residuals-回忆录.md
source_ids:
  - 11664
method_summary: "将 Full AttnRes 的层间注意力按层块压缩为块内求和、块间 Attention，在保留大部分层间汇聚收益的同时降低训练和推理开销。"
typical_structure: |
  1. 将 Embedding 层单独作为一个 Block。
  2. 将剩余的每 $m$ 层作为一个 Block。
  3. 在 Block 内部，通过直接将各层的输出 $\boldsymbol{y}_s$ 等权求和来进行状态压缩。
  4. 以各 Block 的求和结果作为注意力计算的 Keys 和 Values。
  5. 各层维护自身的静态查询向量 $\boldsymbol{w}_t$，与前面各 Block 的压缩结果计算层间注意力得分。
applicability: "在大规模 Transformer 模型中，想要使用层间注意力（Depth/Layer Attention）替代传统的残差连接以提升效果，但全量层间注意力（Full AttnRes）会导致不可接受的计算、通信开销和显存占用时。"
examples:
  - "[[article::11664]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::11664::Block AttnRes的想法大致是这样的：首先Embedding层单独作为一个Block...剩下的每m层作为一个Block，Block内通过求和做压缩，以求和结果为单位算Block间Attention。"
---

# Block AttnRes分块压缩层间注意力

## 适用问题
如何在大规模模型中引入层间注意力（Layer Attention）替代残差连接，同时避免全量层间注意力（Full AttnRes）随层数平方增长带来的巨大显存和通信开销？

## 核心变换
将全量层间注意力的精确键值对存储转化为分块（Block）求和压缩的键值对。即将相邻 $m$ 层的输出相加 $\boldsymbol{y}_{s:t} = \sum_{i=s}^t \boldsymbol{y}_i$，以这个压缩后的结果去与查询向量 $\boldsymbol{w}$ 进行基于 RMSNorm 的缩放点积注意力计算：
$$ \phi(\boldsymbol{w}, \boldsymbol{y}_{s:t}) = \exp(\boldsymbol{w} \cdot \text{RMSNorm}(\boldsymbol{y}_{s:t})) $$

## 典型步骤
1. 将 Embedding 层单独作为一个 Block（因为其总是获得极高的注意力权重）。
2. 将剩余的网络层每 $m$ 层划分为一个 Block。
3. 在 Block 内部，直接将本 Block 内各层的输出 $\boldsymbol{y}_i$ 进行求和，得到压缩后的状态向量。
4. 将当前层 $t$ 之前的各个 Block 的求和结果作为 Keys 和 Values。
5. 当前层使用其独有的静态可学习向量 $\boldsymbol{w}_t$ 作为 Query，与前面的各个 Block 计算 Attention 权重并加权求和，作为下一层的输入。

## 直觉
朴素的残差连接本质上是前面所有层状态的“等权求和”。如果引入高效注意力机制（比如滑动窗口注意力 SWA）反而丢弃了部分状态，其表现往往还不如残差连接这一强基线。既然等权求和已经足够好，那么“压缩”就比“稀疏”更有效。将相邻层的输出简单加和作为代表，既保留了覆盖所有历史状态的能力，又把层间注意力的时间空间复杂度降到了完全可接受的程度。

## 边界
Block 的划分粒度 $m$ 需要仔细权衡。如果 $m$ 过大，层间注意力的灵活性将丧失，退化为接近残差连接的表现；实验发现划分为大约 8 个 Block 即可获得全量版本的大部分收益。此外，虽然计算量和显存显著降低，但仍有少许额外开销（约5%以内）。

## 例子
一个 32 层的 Transformer，如果用 Full AttnRes，最后一层需要与前面的 32 个状态进行注意力计算。使用 Block AttnRes（设 $m=4$），Embedding 是第1个块，后面32层分为8个块，每块内部将4层的输出相加。这样第 32 层只需要与前面大约 9 个压缩状态计算注意力，大大减少了上下文长度和缓存压力。

## 证据
- 11664 记载：“首先Embedding层单独作为一个Block...剩下的每 $m$ 层作为一个Block，Block内通过求和做压缩，以求和结果为单位算Block间Attention”，并且指出“固定分8个Block左右，就可以获得AttnRes大部分收益”。
