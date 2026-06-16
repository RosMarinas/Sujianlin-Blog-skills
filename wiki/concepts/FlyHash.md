---
type: concept
title: FlyHash
definition: 仿生随机二值映射算法，采用高维稀疏投影矩阵结合赢者通吃实现高维低激活二值哈希表征。
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"]
source_ids: ["8159"]
aliases: ["果蝇哈希", "FlyHash-WTA"]
status: stable
updated: 2026-06-12
---

# FlyHash

## 定义
FlyHash 是一种由果蝇嗅觉回路启发的随机向量二值化哈希算法，由 Science 上的工作提出。

## 机制
其最大特色是“高维 + 低激活”：
1. **升维**：利用随机稀疏二值投影核将原始输入投影到更宽的特征空间 $K > D$；
2. **赢者通吃**：投影后使用 WTA（Winner Take All）机制，仅将前 $k$ 个最大响应特征激活设为 1，其他分量设为 0。
该特征实现了超低碰撞率和快速倒排查询，是高效仿生神经哈希的典型方法。