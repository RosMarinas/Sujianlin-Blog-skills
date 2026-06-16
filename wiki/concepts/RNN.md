---
type: concept
title: "RNN"
aliases:
  - "循环神经网络"
  - "Recurrent Neural Network"
definition: "处理序列数据的神经网络结构，通过循环连接捕获序列中的时序依赖关系。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "4582"
related_methods:
  []
status: draft
updated: 2026-06-13
---

RNN（循环神经网络）通过循环连接捕获序列中的时序依赖关系。在文本分类等任务中，RNN将词向量序列编码为隐藏状态序列，最后一步状态用于分类决策。本文提出通过分析各时间步隐藏状态到最终状态的距离变化来评估每个输入词的重要性，为RNN模型提供可解释性分析。 近年来Transformer逐渐取代RNN成为主流，但RNN在某些序列任务中仍有其独特优势，尤其在长度受限和资源受限的场景下。 虽然近年来Transformer逐渐取代了RNN的主流地位，但RNN在特定序列任务中仍有不可替代的优势。
