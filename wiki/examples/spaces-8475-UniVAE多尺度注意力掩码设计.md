---
type: example
title: UniVAE多尺度注意力掩码设计
article_id: "8475"
article: "[[spaces-8475-UniVAE-基于Transformer的单模型-多尺度的VAE模型]]"
section: 解耦能力
claim: 在基于 Transformer 的单模型自编码器中，前 k 层用独立掩码而后续 L-k 层用 UniAE 掩码可以得到层次化多尺度解耦控制的潜随机特征
notation_mapping:
  split_threshold_layer: k
  attention_mask_matrix: M
  layer_index: l
  layer_cls_representation: h_l
  latent_space_dimension_reduced: z_l
steps:
  - 1. **单模型拼接输入**：输入序列 `[CLS] + Input + [CLS] + Output` 传入 L 层共享权重的自注意力层中。
  - 2. **前 k 层施加隔离独立遮蔽**：在层 1 到层 k 的自注意力子层中，设定 Attention Mask 使得解码部分无法检索到任何编码部分的信息。该隔离为编码器提供了多层自注意力深度以抽取高度抽象的复杂文本表示。
  - 3. **后 L-k 层施加 UniAE 式遮蔽**：在层 k+1 到层 L 的自注意力子层中，重构 Attention Mask，允许解码通道的所有 Token 在每一步仅能检索编码通道的 `[CLS]` 位置特征 and 解码通道的前序特征。
  - 4. **层级全连接双向降维**：对任意 l > k 层的词表征特征，提取 `[CLS]` 的输出 h_l，使用一个 Dense 降维层压缩为 z_l，做 vMF 或高斯重参数随机处理后，由另一个 Dense 升维层投影回 $d$ 维，并替换下一层输入的 `[CLS]` 标记。
  - 5. **隐表征拼接组合控制**：将层 k+1 到层 L 的全部低维隐向量 $z_{k+1}, \dots, z_L$ 拼接作为 VAE 的潜特征向量，用于生成重构和文本句式/概念的层级解耦编辑。
used_concepts:
  - "[[变分自编码器]]"
  - "[[多尺度变分自编码]]"
used_methods:
  - "[[多尺度注意力掩码自编码]]"
  - "[[重参数技巧]]"
source_span: ev::8475::layer_split_mask_decoupling
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-06-29-UniVAE-基于Transformer的单模型-多尺度的VAE模型.md
source_ids:
  - "8475"
status: draft
updated: 2026-06-12
---

本例详细演示了 UniVAE 在单模型 Transformer 架构上，如何利用 Attention Mask 的巧妙分层组合设计（浅层独立掩码，深层 UniAE 掩码）和层级 CLS 降维重参数技巧，实现具备多尺度解耦特性的文本变分自编码生成。

本例设计的精妙之处在于它在同一个共享权重的网络内同时充当了 Encoder 和 Decoder 的双重角色。如果在自注意力的浅层就引入 UniAE 遮蔽，由于此时 `[CLS]` 仅仅经过了寥寥数次自注意力计算，其语义抽象程度远远不够，无法承载整句文本的多样化压缩语义，从而导致隐空间无法提取解耦的高质量表征。通过对前 $k$ 层（如前 8 层）应用隔离独立掩码，编码网络获得了足够的“净空层级”来抽取深层非线性文本特征；当计算流进入 $k+1$ 层后，UniAE 掩码与多尺度 `[CLS]` 双向全连接降维升维映射联合被激活，构筑了严密的信息瓶颈。这一独特的层级掩码过渡与降维设计，在保证生成文本极佳重构率的与此同时，成功使前半部维度的主题控制与后半部维度的句式控制实现高度解耦，为自然语言生成领域的隐特征层次化操控给出了创新的技术示范。
