---
type: article_summary
title: 动手做个DialoGPT：基于LM的生成式多轮对话模型
article_id: "7718"
source_url: https://spaces.ac.cn/archives/7718
date: 2020-09-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-09-07-动手做个DialoGPT-基于LM的生成式多轮对话模型.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-09-07-动手做个DialoGPT-基于LM的生成式多轮对话模型.md
source_ids:
  - "7718"
status: draft
updated: 2026-06-12
---

## 文章核心问题
基于LCCC中文闲聊语料库，使用语言模型（GPT）架构训练多轮对话模型DialoGPT。

## 主要结论
使用NEZHA（相对位置编码）+语言模型Mask可以有效地建模多轮对话，在LCCC数据集上训练得到了可用的聊天模型。

## 推导结构
1. LCCC语料库介绍
2. 模型设计：单向LM（GPT）+ NEZHA + Segment Id区分角色
3. 训练细节：单卡RTX 22G + 梯度累积
4. 测试效果展示
5. 与CDial-GPT的对比分析

## 关键公式
（无核心数学公式；以模型架构和训练配置为主）

## 体现的方法
基于LM的多轮对话建模方法、相对位置编码对话模型方法、梯度累积训练方法

## 所属系列位置
独立文章，属于生成式对话模型系列

## 与其他文章的关系
使用[6933]的Mask方法；基于[6915]的bert4keras；与[7912]共享GPT应用主题

## 原文证据锚点
语料统计数据、模型架构图、对话效果示例