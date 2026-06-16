---
title: Dropout视角下的MLM和MAE：一些新的启发
source_id: 8770
type: source
url: https://spaces.ac.cn/archives/8770
author: 苏剑林
date: 2021-11-29
category: 信息时代
tags: [dropout, mlm, mae, pre-training]
license: CC BY-NC-SA
abstract: 从Dropout视角重新审视MLM和MAE模型。MLM可视为特殊Dropout，揭示了其预训练-微调不一致性根源；MAE等价于Attention Dropout，具有更好的一致性。提出Embedding修正和DropToken正则化方法。
key_contributions:
  - MLM作为特殊Dropout的数学建模（伯努利分布视角）
  - 预训练后Embedding修正公式（实验结论：无显著提升）
  - MAE作为Attention Dropout的等价形式
  - MAE取消Dropout后与原始模型一致的数学证明
  - DropToken正则化方法（随机丢弃token，保留位置）
  - CLUE分类任务上DropToken的实验对比
