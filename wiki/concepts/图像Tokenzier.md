---
type: concept
definition: 图像Tokenizer是指将图像从连续的像素空间压缩为离散的编码序列的模型，类似于文本的Tokenizer角色。主流方案包括VQ-VAE、VQ-GAN以及最新的FSQ（Finite
  Scalar Quantization）。
title: 图像Tokenzier
aliases:
- Image Tokenizer
- VQ-VAE Tokenizer
- VQ-GAN Tokenizer
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2024-02-21-闭门造车-之多模态思路浅谈-一-无损输入.md
source_ids:
- '9984'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred.
status: draft
updated: '2026-06-12'
---


# 图像Tokenzier

## Definition

图像Tokenizer是指将图像从连续的像素空间压缩为离散的编码序列的模型，类似于文本的Tokenizer角色。主流方案包括VQ-VAE、VQ-GAN以及最新的FSQ（Finite Scalar Quantization）。

## Purpose

核心目的是"先压缩，后生成"——通过另外的模型压缩序列长度（如256×256→32×32），然后在压缩后的离散空间进行自回归生成，生成后再通过Decoder恢复为图像。

## Information Loss Problem

图像Tokenizer为了明显提高生成速度而做高度压缩，导致了严重的信息损失。信息熵分析表明：
- ImageNet-64平均信息熵约3比特/字节
- 64×64图像总信息熵 = 64×64×3×3 = 36864比特
- 如果压缩到1024个token（32×32），需要V≥2^36的codebook
- 如果压缩到256个token（16×16），需要V≥2^144的codebook
- 当前实际codebook大小远未达到这个量级

这意味着当前图像Tokenizer必然存在严重的信息损失，难以支持需要精细细节的任务（如OCR）。

## Related Pages
- [[连续型概率建模困难]]
- [[压缩损失 (多模态)]]
- [[Patch输入]]