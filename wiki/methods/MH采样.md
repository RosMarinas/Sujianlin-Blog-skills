---
type: method
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
title: MH采样
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-01-14-搜出来的文本-二-从MCMC到模拟退火.md
source_ids:
  - 8084
method_summary: MH采样（Metropolis-Hastings Sampling）是MCMC方法的核心变体，使用改进的接受率使其只依赖于p(x)的相对值（从而不需要归一化因子），且接受率更高。
typical_structure: |
  1. 采样 y ∼ q(y←xt)
  2. 采样 ε ∼ U[0,1]
  3. 计算接受率 A(y←xt) = min(1, q(xt←y)p(y) / (q(y←xt)p(xt)))
  4. 若 ε ≤ A(y←xt)，则 x_{t+1} = y，否则 x_{t+1} = xt
applicability: 直接计算期望、积分或配分函数不可行，需要通过采样或估计近似时，特别是目标分布的精确形式未知但相对概率可计算时。
examples:
  - [[article::8084]]
evidence_spans:
  - ev::8084::提出了通过令恒等式两边的接受率都除以max(alpha(y<-x), alpha(x<-y))，使得接受率A(y<-x_t)放大的方法，从而推导出了只依赖相对值的接受率。
status: stable
updated: 2026-06-12
belongs_to: null
---

# MH采样

## 适用问题
直接计算期望、积分或配分函数不可行，需要通过采样或估计近似时，特别是目标分布的精确形式未知但相对概率可计算时。传统Metropolis算法需要知道目标分布精确表达式且接受率往往过小。

## 核心变换
通过将恒等式两边的接受率同时除以一个最大化常数，放大实际的接受率，从而将复杂的接受计算转换为仅依赖分布相对比例的比值（去除归一化因子的需求）。

## 典型步骤
1. 采样 y ∼ q(y←xt)
2. 采样 ε ∼ U[0,1]
3. 计算接受率 A(y←xt) = min(1, q(xt←y)p(y) / (q(y←xt)p(xt)))
4. 若 ε ≤ A(y←xt)，则 x_{t+1} = y，否则 x_{t+1} = xt

## 直觉
既然MCMC是微调润色的过程，并且只要满足细致平稳条件的转移概率就可以使用。为提高接受率并避免归一化，我们可以让原来的接受比两端都除以最大的那个值，把一端强行变为1，另一端变为比值。

## 边界
如果提议分布(proposal distribution) $q$ 过于宽泛或与目标分布相差极大，会导致接受率依旧很低；虽然只依赖相对概率，但马尔可夫链仍需跑足够多步才能达到平稳。

## 例子
Gibbs采样就是MH采样的一个特例，它通过只在一维变动使得提议分布与后验完全匹配，从而使得计算得到的接受率恒为1。

## 证据
- ev::8084::提出了通过令恒等式两边的接受率都除以max(alpha(y<-x), alpha(x<-y))，使得接受率A(y<-x_t)放大的方法。
