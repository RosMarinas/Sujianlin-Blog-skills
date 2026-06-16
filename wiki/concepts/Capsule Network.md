---
type: concept
title: "Capsule Network"
aliases:
  - "胶囊网络"
  - "CapsNet"
definition: "Hinton提出的以向量（胶囊）为基本计算单元的神经网络，通过动态路由实现特征的聚类组合表达。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "4819"
  - "5112"
related_methods:
  - [[method::Capsule动态路由]]
  - [[method::EM路由算法]]
status: draft
updated: 2026-06-13
---

Capsule Network是Hinton提出的以向量（胶囊）为基本计算单位的创新神经网络架构。每个胶囊的模长表示特征存在的概率，方向表示特征的实例化参数。通过动态路由算法迭代更新底层到高层胶囊的连接权重，实现特征的聚类组合表达。相比于传统标量神经元，胶囊网络具有更好的可解释性和特征层次表达能力。 与CNN、RNN等传统架构相比，Capsule的vector in vector out设计使其能更好地保持特征的空间层次关系，具有更好的可解释性和泛化能力。
