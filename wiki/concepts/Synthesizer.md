---
type: concept
title: "Synthesizer"
definition: "Synthesizer是Google提出的重新思考自注意力机制的模型，将Attention矩阵直接设为可训练的参数矩阵。"
aliases: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "8431"
status: draft
updated: 2026-06-13
---

Synthesizer是Google提出的重新思考自注意力机制的模型。其核心发现是将Attention矩阵直接设为可训练的参数矩阵（Random模式），去掉与输入Q和K的相关性，仍能取得不错的效果。这证明Attention中QK交互并非绝对必要。MLP-Mixer、FNet等工作都是这一思想的延伸。 Synthesizer的实验包括机器翻译、自动摘要、对话生成等丰富场景，其Random模式证明即使没有基于内容的注意力交互，模型仍能有效工作。
