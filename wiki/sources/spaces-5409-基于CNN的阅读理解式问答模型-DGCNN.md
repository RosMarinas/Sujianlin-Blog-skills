---
type: article_summary
title: 基于CNN的阅读理解式问答模型：DGCNN
article_id: "5409"
source_url: https://spaces.ac.cn/archives/5409
date: 2018-04-15
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-04-15-基于CNN的阅读理解式问答模型-DGCNN.md
series:
  - [[基于深度学习的阅读理解问答]]
concepts:
  - [[DGCNN]]
  - [[门卷积]]
  - [[膨胀卷积]]
  - [[加性注意力]]
  - [[双标注输出]]
methods:
  - [[平方加权投票解码算法]]
formulas:
  - [[残差门卷积公式]]
  - [[平方加权投票打分公式]]
examples:
  - [[spaces-5409-白云山海拔问答]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-04-15-基于CNN的阅读理解式问答模型-DGCNN.md
source_ids:
  - "5409"
status: draft
updated: 2026-06-11
---

# 基于CNN的阅读理解式问答模型：DGCNN

## 内容概要
文章介绍了一个专为 WebQA 事实类问答定制的轻量级纯 CNN 阅读理解模型 —— DGCNN（膨胀门卷积神经网络）。模型不含 RNN 结构，在搜狗 CIPS-SOGOU 问答比赛中表现优异，具备训练速度极快和工业落地可行的特点。

## 关键内容
1. **模型架构与特点**：
   - 抛弃了主流模型（如 AoA、R-Net）使用的复杂 RNN 和繁琐的注意力交互机制。
   - 核心模块为一维门卷积（GCNN）与膨胀卷积（Dilated Convolution）的残差组合。
   - 将预测任务转化为序列双标注，通过 “半指针半标注” 预测答案起止位置。
2. **门卷积与膨胀卷积机制**：
   - **门控线性单元 (GLU)**：$\boldsymbol{Y}=\text{Conv1D}_1(\boldsymbol{X}) \otimes \sigma(\text{Conv1D}_2(\boldsymbol{X}))$。通过门控制信息流，减轻梯度消失并提高表现。残差版本在数学上等价于类 GRU 的门控传输结构。
   - **膨胀卷积**：按 1, 2, 4, 8... 几何级数增大膨胀率，在不增加参数和计算复杂度的情况下呈指数级扩大感受野。
3. **加性注意力与位置嵌入**：
   - 使用 R-Net 风格的加性注意力代替简单池化，将句子序列压缩为向量。
   - 拼接正弦位置嵌入（Transformer 方案）以增强 CNN 对文本位置的感知。
4. **输出设计与大局观得分**：
   - 针对 WebQA 检索场景下多段材料可能无答案或有多个答案的特点，使用 Sigmoid 预测每个词是起止点的概率。
   - 提取全局篇章向量，接 Dense 层计算 `p_global`。最终起止概率分别乘以该全局得分，用以自动筛除无答案材料。
5. **八大人工特征**：
   - Q-E 全匹配、E-E 共现率。
   - Q-E 软匹配：以问题长度为窗口，计算窗口内材料与问题的 Jaccard 相似度和相对编辑距离。
   - 字符特征：在字级别上重复计算前述 4 种特征并平均到词级别。人工特征可带来约 2% 的绝对性能提升。
6. **解码与平方加权投票**：
   - 同一段材料中的同名候选答案只取最大打分。
   - 多篇章投票使用“专家加权”与“小样本惩罚”相结合的平方加权公式融合得分：
     $$s_a = \frac{\sum_{i=1}^n s_{a,i}^2}{1+\sum_{i=1}^n s_{a,i}}$$
7. **数据扩增与训练**：
   - 将 Sogou 语料与 WebQA 语料以 2:1 混合；采用随机置零词 ID（无尺度缩放的 Dropout）等扩增手段。
   - 采用 Focal Loss 损失函数缓解起止点类别不均衡问题。
