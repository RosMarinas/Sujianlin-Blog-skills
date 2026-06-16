---
type: method
title: "BERT MLM小样本学习"
aliases:
  - "MLM Few-shot"
  - "PET"
operation_types:
  primary: "Construct auxiliary sequence"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-09-27-必须要GPT3吗-不-BERT的MLM模型也能小样本学习.md
source_ids:
  - "7764"
method_summary: "通过Pattern模板将分类任务转换为完形填空，利用BERT的MLM模型做小样本/零样本学习。"
typical_structure: |
  1. 设计Pattern将输入转为完形填空
  2. 定义Verbalizer映射预测词到类别
  3. 用MLM模型预测mask位置
  4. 多个Pattern集成+自训练
applicability: "小样本文本分类，零样本学习"
tools:
  - Pattern模板
  - Verbalizer
  - MLM模型
related_methods: []
examples:
  - [[article::7764]]
status: draft
updated: 2026-06-13
---

## 适用问题

小样本/零样本文本分类，尤其是候选类别有限的分类任务（情感分类、主题分类、自然语言推理等）。当标注数据极少（几十到几百条）或完全无标注时，利用BERT的MLM能力完成分类。

## 核心变换

**输入**：原始文本 + 模式模板（Pattern）+ 候选词映射表（Verbalizer）
**输出**：类别预测

将标准分类任务转换为完形填空（Cloze）任务。例如情感分类：
> "____满意。这趟北京之旅我感觉很不错。"

模型预测Mask位置最可能的词，通过Verbalizer将预测词映射到类别标签（如"很"$\to$正面，"不"$\to$负面）。数学上等价于：
$$
y^* = \mathop{\text{argmax}}_{v \in \mathcal{V}} p_{\text{MLM}}(\text{mask} = v \;|\; \text{Pattern}(x))
$$
其中$\mathcal{V}$是Verbalizer定义的候选词集合。

## 典型步骤

1. **设计Pattern**：为任务构造自然语言模板，将输入包装为完形填空形式（前缀/后缀均可，实验表明前缀效果更优）
2. **定义Verbalizer**：建立预测词到类别标签的映射（可多对一）
3. **零样本预测**：直接使用预训练MLM模型预测Mask位置token，通过Verbalizer得到分类结果
4. **小样本微调**：用少量标注数据+Pattern微调MLM模型，同时随机Mask额外Token增强正则化
5. **多Pattern集成**：训练多个Pattern的MLM模型后集成，用集成模型对无标签数据预测伪标签
6. **自训练**：用伪标签数据Finetune常规分类模型（非MLM）

## 直觉

预训练MLM模型已经在海量文本上学会了完形填空能力——即根据上下文预测被Mask的词。分类任务本质上是"根据上下文判断类别"，两者高度相似。通过精心设计的Pattern，可以将"判断类别"转化为"预测某个位置最自然的词"，从而直接调用MLM的预训练知识。

多Pattern集成类似于数据增强：不同的Pattern从不同角度"询问"同一个样本，集成后获得更鲁棒的预测。

## 边界

- 仅适用于**候选空间有限的任务**（本质上只能做选择题），无法处理生成式任务或答案不定长的场景
- MLM的独立假设限制了其对更长文本的预测能力（Mask位置不能过长）
- Pattern设计对效果影响显著，需要一定的人工经验
- 不同预训练模型（BERT Base vs Large、RoBERTa等）和不同Pattern的组合效果差异较大
- 该方法依赖MLM预训练权重，使用未保留MLM权重的模型（如某些RoBERTa版本）无法复现

## 例子

- 情感二分类零样本：使用RoBERTa-wwm-ext + P1模式（"____满意。{text}"），零样本准确率达85.17%（验证集）
- 继续无监督MLM预训练后：零样本准确率提升至88.05%
- 200个小样本+Pattern微调：准确率达89.29%，接近常规微调效果
- 半监督（1:99标注比例）：准确率达90.09%，媲美VAT半监督方法
- 在SuperGLUE小样本任务上，PET方法超过GPT3（论文报告结果）

## 证据

- ev::7764::Pattern模板设计：多种Pattern（P1-P5）对零样本效果的影响
- ev::7764::Verbalizer映射：候选词到类别标签的多对一映射机制
- ev::7764::零样本/小样本/半监督实验：M2模型下各Pattern的准确率对比表
- ev::7764::PET多Pattern集成+自训练流程：Pattern-Exploiting Training的完整训练管线
