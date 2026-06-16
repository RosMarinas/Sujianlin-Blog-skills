---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: AdamW最优LR/WD调度法
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-12-05-滑动平均视角下的权重衰减和学习率.md
source_ids:
  - 11459
method_summary: "从滑动平均记忆视角重写 AdamW 的权重衰减与学习率，令各训练 batch 的记忆权重近似均等，反解出 LR/WD 的联合衰减调度。"
typical_structure: |
  1. 将优化器的更新过程重写为对初始权重和梯度信息的滑动平均（EMA）加权形式。
  2. 确定模型的“记忆周期”，使之与训练总步数成正比，以平衡“防止遗忘早期数据”与“遗忘初始化/防止参数爆炸”之间的矛盾。
  3. 假定每一个 Batch 的数据同等重要，反解出动态 Learning Rate (LR) 和 Weight Decay (WD) 的最佳联合调度策略。
  4. 根据解出的方程 $\lambda_s \eta_s + \dot{\eta}_s / \eta_s \approx 0$ 以及 $\lambda_s = \alpha \eta_s$ 设定每步的 LR 和 WD 参数。
applicability: "所有需要预训练并且具有单轮（Single-Epoch）特性、追求权重最优衰减与学习率调度的自适应学习率优化器场景。"
examples:
  - "[[article::11459]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::11459::这便是常数Weight Decay下的最佳LR Schedule...为了解决这个问题，我们可以考虑让 \\lambda_s = \\alpha\\eta_s，此时可以解得 \\eta_s \\approx \\frac{\\eta_{\\max}}{\\sqrt{2\\lambda_{\\max}\\eta_{\\max} s + 1}}。"
---

# AdamW最优LR/WD调度法

## 适用问题
在 LLM 的预训练过程中，如何科学地设定自适应优化器（如 AdamW）的 Weight Decay 和 Learning Rate 调度，使得训练过程不遗忘早期的 Batch，同时避免模型权重的发散或坍缩？

## 核心变换
通过将 Weight Decay 和 Learning Rate 参数化为一个滑动平均记忆衰减系统，并将每一 Batch 的梯度贡献设定为同等重要，通过平均场近似推导出一个最优的倒数/平方根衰减调度曲线 $\eta_s \approx \eta_{\max}/\sqrt{2\lambda_{\max}\eta_{\max} s + 1}$。

## 典型步骤
1. 将优化器的更新过程重写为对初始权重和梯度信息的滑动平均（EMA）加权形式。
2. 确定模型的“记忆周期”，使之与训练总步数成正比，以平衡“防止遗忘早期数据”与“遗忘初始化/防止参数爆炸”之间的矛盾。
3. 假定每一个 Batch 的数据同等重要，反解出动态 Learning Rate (LR) 和 Weight Decay (WD) 的最佳联合调度策略。
4. 根据解出的方程 $\lambda_s \eta_s + \dot{\eta}_s / \eta_s \approx 0$ 以及 $\lambda_s = \alpha \eta_s$ 设定每步的 LR 和 WD 参数。

## 直觉
Weight Decay 的本质是参数与优化器更新量的一个加权滑动平均。如果不加 WD，模型容易权重爆炸，并且记忆周期无穷大但保留了过多初始化的不良影响。若希望在 Single-Epoch 的预训练中不遗忘所有早期训练数据，每一 Batch 对应的加权系数应尽量相等。当这个期望常数被代入到微积分方程中时，反解出来的最优学习率就是与时间步长的平方根成反比的函数。

## 边界
这种最优调度的推导基于“平均场近似”以及“每一步梯度包含当前 Batch 的增量信息同等重要”的假设。在课程学习（Curriculum Learning）这种后期数据明显比前期数据重要的情况，或当更新并非齐次类型且梯度模长严重影响 Weight RMS 动态时，直接采用该理论结果可能会导致次优表现。

## 例子
设定 $\lambda_s = \alpha\eta_s$，通过初始的最大学习率和权重衰减值计算每一步的调整：$\eta_s = \eta_{\max}/\sqrt{2\lambda_{\max}\eta_{\max} s + 1}$，将其应用于 AdamW 的参数更新调度器中取代传统的 Cosine Decay。

## 证据
- 11459 通过 EMA 的视角反解指出，在要求每个 Batch 权重一致的前提下，当 $\lambda_s = \alpha\eta_s$ 时可得最优调度为 $\eta_s \approx \frac{\eta_{\max}}{\sqrt{2\lambda_{\max}\eta_{\max} s + 1}}$。
