---
type: concept
title: DGCNN
aliases:
- Dilate Gated Convolutional Neural Network
- 膨胀门卷积神经网络
definition: 一种融合了膨胀卷积与门控卷积(GLU)的轻量高效一维卷积序列建模网络，常用于不依赖RNN的NLP任务。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-04-15-基于CNN的阅读理解式问答模型-DGCNN.md
source_ids:
- '5409'
prerequisites:
- '[[膨胀卷积]]'
- '[[门卷积]]'
evidence_spans:
- ev::5409::残差门卷积
status: stable
updated: '2026-06-13'
---

# DGCNN

## 定义

DGCNN（Dilate Gated Convolutional Neural Network）是源文为 WebQA 阅读理解任务设计的一维卷积序列模型。它不用 RNN，而是在 Conv1D Block 中结合门卷积、残差通道和膨胀卷积，再配合注意力、位置向量、人工特征和双标注输出完成答案片段预测。

## 激活场景

该概念出现在需要轻量、快速处理问答材料序列的 NLP 场景。源文明确将 DGCNN 与 AoA、R-Net 等带 RNN 和复杂注意力交互的模型对比，强调其针对 WebQA 式任务定制，目标是在较低结构复杂度下保留长距离建模与并行计算能力。

## 关键关系

DGCNN 的核心构件是门卷积 GLU 与残差结构：一个 Conv1D 输出线性变换，另一个 Conv1D 经 sigmoid 后作为阀门逐位相乘；当输入输出维度一致时，残差项让信息能在直接通道和变换通道之间流动。膨胀卷积则通过 `1,2,4,8,...` 的膨胀率扩大感受野，使第三层可看到更远输入而不增加参数量和速度成本。

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2018-04-15-基于CNN的阅读理解式问答模型-DGCNN.md`
- `ev::5409::残差门卷积`
