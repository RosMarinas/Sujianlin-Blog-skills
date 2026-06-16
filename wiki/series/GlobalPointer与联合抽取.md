---
type: series
title: GlobalPointer与联合抽取
aliases: []
article_ids:
  - "6671"
  - "7161"
  - "8877"
  - "8888"
  - "8926"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-06-03-基于DGCNN和概率图的轻量级信息抽取模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-01-03-用bert4keras做三元组抽取.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-25-Efficient-GlobalPointer-少点参数-多点效果.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-30-GPLinker-基于GlobalPointer的实体关系联合抽取.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-21-GPLinker-基于GlobalPointer的事件联合抽取.md
source_ids:
  - "6671"
  - "7161"
  - "8877"
  - "8888"
  - "8926"
series_goal: 探索监督学习下的实体、关系及事件等联合抽取任务的高效、优雅方案，形成了从概率分解到GlobalPointer与GPLinker的完整技术路线。
entry_roles:
  "6671": 主实体条件分解法开创
  "7161": 基于条件LayerNorm的两步式BERT三元组抽取
  "8877": 提出抽取分类解耦的Efficient GlobalPointer
  "8888": 提出基于五元组分解的GPLinker实体关系联合抽取模型
  "8926": 将GPLinker扩展至事件联合抽取，提出基于完全子图搜索的事件划分
key_concepts:
  - [[GlobalPointer]]
  - [[Efficient GlobalPointer]]
  - [[半指针-半标注]]
  - [[完全子图]]
key_methods:
  - [[基于概率分解的关系抽取]]
  - [[基于完全子图搜索的事件划分]]
  - [[基于条件LayerNorm的实体关系抽取]]
reading_paths:
  - [[GlobalPointer与联合抽取阅读路径]]
status: stable
updated: 2026-06-14
---

# GlobalPointer与联合抽取

本系列记录了作者在实体、关系与事件联合抽取任务上的探索历程与核心技术突破。

系列从2019年百度信息抽取竞赛中基于概率分解的两步法（CasRel baseline模型）出发，确立了将联合抽取解耦为两阶段条件特征提取的思想。随后，在该两阶段因式分解的指导下，模型逐渐演化出基于条件层归一化（Conditional LayerNorm）的bert4keras三元组抽取系统。在2021年提出专门针对命名实体识别的GlobalPointer与二维位置编码（RoPE）后，进一步将这些积木块结合，构筑出了将五元组打分因式分解的GPLinker实体关系联合抽取模型，并融合完全子图搜索成功解决多事件实例的重叠划分，形成了一套工业界极具应用价值的高效、完备的信息联合抽取方案。

## 阅读与检索建议

这条 series 应按“概率分解 -> 条件特征抽取 -> GlobalPointer 打分 -> GPLinker 关系/事件联合抽取”的顺序读。它不是一般 NER 方法清单，而是把结构化抽取任务逐步改写为实体、关系、事件跨度的可打分组合问题。

- 查 CasRel/关系抽取两阶段分解：从 6671、7161 进入。
- 查 Efficient GlobalPointer 的参数效率：从 8877 进入。
- 查 GPLinker 如何统一实体关系五元组：从 8888 进入。
- 查事件抽取多事件实例划分：从 8926 进入。

## 方法递进

1. 6671 将关系抽取拆成主实体识别和条件关系预测，核心是把联合结构抽取转成概率分解。
2. 7161 用条件 LayerNorm 把主体信息注入客体关系抽取，形成更工程化的 BERT 三元组抽取路线。
3. 8877 把实体边界打分改写为 GlobalPointer/Efficient GlobalPointer，降低参数量并统一 span 分类。
4. 8888 将实体关系组合为 GPLinker 五元组打分，减少手工级联带来的误差传播。
5. 8926 把事件联合抽取中的多实例重叠问题转成完全子图搜索，因此它是关系抽取路线向事件抽取的结构升级。

## 与 LLM 相关网络的连接

这条 series 不是架构扩容线，而是 LLM/NLP 下游结构化输出线。它回答“模型已经编码文本之后，如何把实体、关系、事件这些结构稳定读出来”。因此应与 [[基于深度学习的阅读理解问答]] 并列作为信息抽取/问答任务层入口，而不是混入 Transformer 结构页。
