---
type: article_summary
title: 貌离神合的RNN与ODE：花式RNN简介
article_id: "5643"
source_url: https://spaces.ac.cn/archives/5643
date: 2018-06-23
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2018-06-23-貌离神合的RNN与ODE-花式RNN简介.md
concepts:
  - [[ODE-RNN等价性]]
methods:
  - [[用RNN反向传播估计常微分方程参数]]
examples:
  - [[spaces-5643-生物种群竞争模型参数估计]]
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-06-23-貌离神合的RNN与ODE-花式RNN简介.md
source_ids:
  - "5643"
status: stable
updated: 2026-06-12
---

# 貌离神合的RNN与ODE：花式RNN简介

## 摘要
本文探讨了循环神经网络（RNN）与常微分方程（ODE）数值解法之间的深层数学联系。作者指出，RNN的递归计算本质上可以对应于常微分方程组在欧拉折线法（Euler's method）下的数值迭代离散形式。在此基础上，本文展示了两个主要应用：首先是直接利用Keras搭建前向传播模型，在无需训练的情形下数值求解生物种群竞争方程组；其次是利用已知的部分实验观测数据，将ODE的参数作为神经网络的可训练权重，通过反向传播（梯度下降/Adam）来反推和估计动力系统的参数。文章最后指出在将RNN应用于物理ODE系统时面临的梯度消失与爆炸挑战，强调了精心初始化和截断处理的重要性。
