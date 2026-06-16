---
type: article_summary
title: 线性注意力简史：从模仿、创新到反哺
article_id: 11033
source_url: "https://spaces.ac.cn/archives/11033"
date: 2025-06-20
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
series: []
topics:
  - [[Transformer架构]]
  - [[状态空间模型数学基础]]
concepts:
  - [[线性注意力]]
  - [[TTT框架]]
  - [[DeltaNet]]
  - [[MesaNet]]
  - [[Gated DeltaNet]]
  - [[PaTH Attention]]
methods:
  - [[DeltaRule序列建模]]
  - [[MesaNet解析解序列建模方法]]
  - [[线性Attention遗忘门方法]]
evidence_spans:
  - ev::11033::最初的模样
  - ev::11033::花式遗忘门
  - ev::11033::测试时训练
  - ev::11033::除旧而迎新
  - ev::11033::求逆与推广
  - ev::11033::反哺进行时
  - ev::11033::硬核编码术
  - ev::11033::化简乐无穷
  - ev::11033::剑走偏锋法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
  - 11033
status: draft
updated: 2026-06-11
---

# 线性注意力简史：从模仿、创新到反哺

## 文章核心问题

线性注意力（Linear Attention）的发展脉络：从最初模仿Softmax Attention、引入静态/动态遗忘门，到用在线学习/TTT框架构建并用Delta Rule除旧迎新、RLS解析解等，以及反哺Softmax Attention的研究。

## 主要结论

- **最初的模样**: Causal线性Attention可以写为以S_t为状态的线性RNN形式，实现线性计算复杂度。
- **花式遗忘门**: RetNet等工作给线性Attention引入衰减因子gamma，以就近原则保留最近token的分辨率。
- **测试时训练**: TTT（Test-Time Training）将RNN状态更新视为在线学习过程，通过优化器梯度更新State。
- **除旧而迎新**: DeltaNet使用平方误差作为TTT损失，其更新规则对应LMS Delta Rule，实现除旧迎新。
- **求逆与推广**: DeltaNet的并行形式可表示为下三角方程组的求解，其复杂度可通过低秩结构降为线性。
- **反哺进行时**: 线性Attention可通过核技巧恢复指数关系以反哺Softmax Attention，如ALIBI和FoX。
- **硬核编码术**: PaTH Attention利用Householder镜面反射矩阵表达上下文相关位置编码，属于CoPE的一种。
- **化简乐无穷**: 当Householder基W=K时，PaTH Attention退化为DeltaNet的注意力矩阵。
- **剑走偏锋法**: MesaNet将TTT视为线性回归问题并使用解析解（对应RLS）构建序列模型，在局部最优更新上优于DeltaNet。
