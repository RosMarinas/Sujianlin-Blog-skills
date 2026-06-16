---
type: problem_pattern
title: 序列模型的TTT构建
aliases: []
pattern_summary: 当需要构建一个固定大小的State来表示序列时，将序列建模视为在线学习问题：用优化器（如SGD）在(K,V)数据对上更新模型参数作为RNN状态。
trigger_questions:
  - 序列模型是否需要固定大小的State表示？
  - State更新能否视为优化器对训练数据的压缩？
  - 不同的模型架构f和损失函数L能否产生不同的序列模型？
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
source_ids:
  - "10017"
  - "11320"
activates_methods:
  - [[TTT框架构建RNN]]
  - [[DeltaRule序列建模]]
  - [[MesaNet解析解序列建模]]
  - [[线性Attention中的遗忘门]]
examples:
  - [[spaces-10017-TTT统一视角下的序列模型推导]]
typical_prerequisites:
  - [[线性注意力]]
  - [[TTT框架]]
failure_modes:
  - K=V时TTT框架退化为恒等变换
  - "预测自己"而非"预测周围"导致可学信息有限
  - 解析解形式缺乏灵活性

---
