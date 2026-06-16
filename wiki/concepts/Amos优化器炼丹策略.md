---
title: 基于Amos优化器思想推导出来的一些"炼丹策略"
definition: 借鉴Amos优化器思想，从权重衰减不应喧宾夺主的条件出发，系统推导学习率和权重衰减率的变化规律，得到平方反比衰减和逆时间衰减两种策略。
type: concept
source_url: https://spaces.ac.cn/archives/9344
date: '2022-11-22'
author: 苏剑林
tags:
- Amos
- 权重衰减
- 学习率
- 优化器
- 参数化
status: draft
updated: '2026-06-12'
source_ids:
- '9344'
sources:
- （待从源文章提取）
---

# 基于Amos优化器思想推导出来的一些"炼丹策略"

## 概述
借鉴Amos优化器思想，从权重衰减不应喧宾夺主的条件出发，系统推导学习率和权重衰减率的变化规律，得到平方反比衰减和逆时间衰减两种策略。

## 核心思想
1. 权重衰减更新量应比目标相关更新量高一阶(O(alpha^2) = O(rho))。
2. 从距离收缩条件导出alpha_t和rho_t的耦合关系。
3. 参数尺度分离：更新量正比于参数估计的变化尺度||epsilon_0||，自动适应不同初始化。
4. 平方案反比衰减(固定收敛速度) vs 逆时间衰减(递减收敛速度)。

## 关键公式
平方反比衰减: alpha_t ~ (alpha_0*||epsilon_0||/||u_t||) * 1/(alpha_0*p*t+1)^2
逆时间衰减: alpha_t ~ (alpha_0*||epsilon_0||/||u_t||) * 1/(2*alpha_0*p_0*t+1)

## 与LAMB的关系
将||epsilon_0||换成||theta_t||即得LAMB优化器的规则。