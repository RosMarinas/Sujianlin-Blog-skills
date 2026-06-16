---
type: method
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
title: BERT MLM Gibbs采样
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-01-22-搜出来的文本-三-基于BERT的文本采样.md
source_ids:
  - 8119
method_summary: "把 BERT 的 MLM 条件预测视为 Gibbs 采样中的条件分布，反复随机 mask 一个位置并采样替换 token 来生成固定长度文本。"
typical_structure: |
  1. 设定一个初始状态句子 x_0 = (x_{0,1}, x_{0,2}, ..., x_{0,l})。
  2. 均匀地从 1 到 l 中随机采样一个位置 i。
  3. 将第 i 个位置的 token 替换为 [MASK]，得到序列 x_{t,-i}。
  4. 将带有 [MASK] 的序列输入到 BERT MLM 模型中，计算第 i 个位置的概率分布 p_{t+1}。
  5. 从概率分布 p_{t+1} 中随机采样出一个新的 token y。
  6. 将原来序列第 i 个位置替换为 y，作为下一个时刻的句子 x_{t+1}。
  7. 重复步骤 2-6，直到满足采样需求。
applicability: "在需要利用现有的双向掩码语言模型（如 BERT）进行自然语言句子的随机采样和生成，而无法直接进行自回归采样时。"
examples:
  - "[[article::8119]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8119::均匀地从1,2,\\cdots,l中采样一个i，将第i的位置的token替换为[MASK]...算概率分布，采样一个token y...将第i个token替换成y来作为新句子。"
---

# BERT MLM Gibbs采样

## 适用问题
如何利用双向掩码语言模型（如 BERT）实现文本的随机采样，打破“随机文本采样是单向自回归模型专有功能”的限制？

## 核心变换
将 BERT 的 MLM (Masked Language Model) 作为 Gibbs 采样中计算条件概率 $p(y|\boldsymbol{x}_{-i})$ 的引擎。通过 MLM “给定上下文其余词预测当前词”的能力来执行标准的 Gibbs 采样步骤。

## 典型步骤
1. 设定一个初始状态句子 x_0 = (x_{0,1}, x_{0,2}, ..., x_{0,l})。
2. 均匀地从 1 到 l 中随机采样一个位置 i。
3. 将第 i 个位置的 token 替换为 [MASK]，得到序列 x_{t,-i}。
4. 将带有 [MASK] 的序列输入到 BERT MLM 模型中，计算第 i 个位置的概率分布 p_{t+1}。
5. 从概率分布 p_{t+1} 中随机采样出一个新的 token y。
6. 将原来序列第 i 个位置替换为 y，作为下一个时刻的句子 x_{t+1}。
7. 重复步骤 2-6，直到满足采样需求。

## 直觉
Gibbs 采样的核心是每次根据除去当前元素外其余所有元素的条件概率 $p(y|\boldsymbol{x}_{-i})$ 来采样当前元素。BERT 的 MLM 任务正是被训练来根据上下文（其余词）去预测被 MASK 掉的那个词。两者在数学和机制上完美契合，可以直接利用预训练好的 MLM 进行马尔可夫链蒙特卡洛（MCMC）采样。

## 边界
这种基于 Gibbs 采样的生成过程仅能处理固定长度的序列，即采样过程中不会改变句子的长度。为了得到不同长度的句子，必须提前随机采样一个长度，并构建一个全 [MASK] 的初始序列。此外，虽然理论上 MLM 和 Gibbs 采样结合是有效的，但 MLM 实际上并不能严谨地对应到一个全局的马尔可夫随机场（MRF）联合概率分布上，只能算作一种局部条件分布的近似。

## 例子
想要生成长度为 9 的句子：初始设定 9 个 `[MASK]` 的序列，循环多次进行：随机选取其中 1 个位置，通过 MLM 算出分布，采样 1 个真实的汉字填进去，再重新选一个位置……随着迭代的进行，文本会逐渐变得连贯，例如“你每天学你妈妈啊！”。

## 证据
- 8119 提到，MLM 模型随机采样将第 i 个位置的 token 替换为 [MASK]，送入 MLM 模型算出概率分布，从中采样一个 token $y$ 替换回去。虽然这无法对应准确的 MRF，但在实践中成功生成了具备可读性的中文甚至夹杂日语的句子。
