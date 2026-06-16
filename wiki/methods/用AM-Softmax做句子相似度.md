---
type: method
operation_types:
  primary: Structure-expose by factorization
  secondary: []
title: 用AM-Softmax做句子相似度
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-07-29-基于GRU和AM-Softmax的句子相似度模型.md
source_ids:
  - 5743
method_summary: "把句子相似度训练改写为大规模同义句类别分类，并用 AM-Softmax 的归一化、margin 与缩放约束特征空间中的类内紧凑和类间分离。"
typical_structure: |
  1. 将句子相似度检索问题构建为海量分类问题。
  2. 对提取的句子特征特征和类别权重向量分别做 $L_2$ 归一化，转换为纯夹角（余弦相似度）度量。
  3. 在正样本的余弦相似度上增加 margin $m$，施加比例因子 $s$ 放缩，形成 AM-Softmax。
  4. 利用交叉熵训练，使得类内更紧凑，类间更疏远。
applicability: "大规模句子相似度召回、FAQ问答库检索及特征排序任务。"
examples:
  - "[[article::5743]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::5743::阐述了句子相似度与人脸识别的对应关系，并在模型中引入$L_2$归一化、加性裕度（margin）和缩放比例构建AM-Softmax实现文本相似度分类（Lines 105-131）。"
---

# 用AM-Softmax做句子相似度

## 适用问题

传统的双塔二分类模型（Siamese Network）或 Triplet Loss 模型在处理句子相似度任务时，存在负样本采样困难、效率低下及难以逼近真实海量检索场景等问题。需要利用大规模正负样本同时优化特征。

## 核心变换

$$ \cos\theta_t \xrightarrow{m} \cos\theta_t - m \xrightarrow{s} s(\cos\theta_t - m) \xrightarrow{\text{Softmax}} P(y|x) $$
将普通的内积 Softmax 改造为基于归一化向量余弦值的加性裕度（Additive Margin）Softmax。

## 典型步骤

1. 把 FAQ 语料对中的每一个“簇”（意图相同的所有句子）当成一个独立的类别，将检索问题转化为几万甚至几十万类的大规模多分类问题。
2. 使用编码器（如 GRU）提取句子特征向量 $\boldsymbol{z}$，并对其与最后分类层的权重矩阵列向量 $\boldsymbol{c}_i$ 进行 $L_2$ 归一化。
3. 把目标类别 $t$ 的余弦相似度输出调整为 $\cos\theta_t - m$（增加严格度）。
4. 对所有余弦值进行统一的缩放因子 $s$ 放大，并送入 Softmax 计算交叉熵损失进行训练。

## 直觉

普通的分类就像是考 60 分及格就行，模型一旦把相似的句子分到对应的类，就不再对特征加以聚拢，导致真正使用余弦距离寻找最近邻时效果不佳。加入了 Margin $m$，就像把及格线提高到了 80 分，逼迫模型不断地把相同意图的句子在特征空间中狠狠揉成一团，这样直接比对空间距离检索时就会极其精准。

## 边界

- 只有经过 $L_2$ 归一化并引入比例因子 $s$ 的组合，网络才能成功收敛，缺一不可。
- 类别数极其庞大时，巨大的分类层权重 $\boldsymbol{W}$ 会占用较多显存（可通过 Sparse 优化缓解）。

## 例子

在构建客服系统的 FAQ 自动匹配时，将文本过单层 GRU，最后一层舍弃 Bias 并进行权重归一化，训练时针对 target 加上 `margin=0.35` 和 `scale=30` 的 AM-Softmax Loss，能非常有效地召回意图相近的未见疑问句。

## 证据

- ev::5743::阐述了句子相似度与人脸识别的对应关系，并在模型中引入$L_2$归一化、加性裕度（margin）和缩放比例构建AM-Softmax实现文本相似度分类（Lines 105-131）。
