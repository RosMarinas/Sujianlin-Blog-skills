---

type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: QK-Clip权重裁剪法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-07-12-QK-Clip-让Muon在Scaleup之路上更进一步.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-02-27-Muon续集-为什么我们选择尝试Muon.md
source_ids:
  - 11126
method_summary: 在多头注意力迭代更新中，按 Head 监控注意力 Logits 的最大值，若超过安全边界，则在事后对 Query/Key 对应的局域映射权重进行成比例缩放裁剪，在零推理开销下压制 MaxLogit 爆炸。
typical_structure: |
  1. 在每次 Attention 的前向/反向传播迭代后，按注意力头（Per-Head）监控 $\boldsymbol{Q}\boldsymbol{K}^{\top}$ 的最大值 $S_{\max}$。
  2. 判断是否有头的 $S_{\max}$ 超过设定的安全阈值 $\tau$（如 100）。
  3. 对于超标的 Head，提取其产生异常 Logit 的查询（Query）和键（Key）投影权重矩阵 $\boldsymbol{W}_q, \boldsymbol{W}_k$。
  4. 将这部分权重直接乘以缩放系数 $\sqrt{\tau / S_{\max}}$。若包含共享权重（如 MLA 的 $\boldsymbol{W}_{qr}, \boldsymbol{W}_{kr}$），需采用防止殃及池鱼的定向裁剪策略。
  5. 继续后续训练更新步骤。
applicability: 在大规模预训练中发生了 MaxLogit 爆炸，且由于使用了 MLA 架构无法直接采用 QK-Norm 以前向约束的场景，尤其是 Muon 等优化器易触发谱范数膨胀时。
tools: 
related_methods: 
examples:
  - [[article::11126]]
status: stable
updated: 2026-06-12
problem_patterns: 
evidence_spans: 
  - ev::11126::"当MaxLogit超过期望阈值$\tau$时，我们直接给$\boldsymbol{Q}\boldsymbol{K}^{\top}$乘上$\gamma = \tau / S_{\max}$，那么新的MaxLogit肯定就不超过$\tau$了。乘$\gamma$的操作，我们可以分别吸收到权重$\boldsymbol{Q}\boldsymbol{K}$的权重上去"
---

# QK-Clip权重裁剪法

## 适用问题

大规模语言模型（万亿参数级别）由于多层线性叠加或使用了特定优化器（如 Muon），在训练中常常遭遇 Attention Logit 最大值线性甚至指数爆炸（MaxLogit爆炸），导致训练不稳定。若使用无法兼容 Decoding 期 QK Materialize 的 MLA 架构，传统的 QK-Norm 将失效。

## 核心变换

将“控制 Attention 计算结果上限”的问题转换为“反手修改局部参数矩阵范数”的过程：以超出预期阈值的 Logit 比例为监控惩罚信号，直接事后缩放 Query 和 Key 的投影权重，截断其线性膨胀趋势。

## 典型步骤

1. **监控记录**：在每一次优化器更新权重后，按头（Per-Head）统计各层的 Attention 计算结果，求出 $\boldsymbol{Q}\boldsymbol{K}^{\top}$ 的全局极大值 $S_{\max}$。
2. **条件判定**：检查每一个 $S_{\max}$ 是否超过预先设置的阈值 $\tau$（如 $\tau=100$）。
3. **定向权重缩放**：对于超出阈值的 Head，将其对应的局部权重 $\boldsymbol{W}_q, \boldsymbol{W}_k$ 直接乘上标量因子 $\sqrt{\tau / S_{\max}}$，这样在前向乘法中其结果就会按比例收敛回 $\tau$ 以内。
4. **共享参数避让**：在 MLA 等含有所有 Head 共享状态的参数中，若某参数属于共享项（如 $kr$），应避免所有头均对同一权重造成“殃及池鱼”的缩放。将乘数完全移至私有成分（如仅在 $qr$ 端乘上完整的 $\tau / S_{\max}$）。

## 直觉

不改变任何网络前向传播的架构或公式，遵循“哪里越界压迫哪里”的极简思路。既然网络在拼命让 Q、K 的乘积变得无穷大（意味着权重的谱范数在失控），那就每次计算完之后，把那些正在起飞的权重矩阵人为地按比例往下按一按，拉回警戒线以下。

## 边界

- **过度裁剪（殃及池鱼）**：必须细化到 Per-Head 的裁剪，否则没爆炸的头也会被不断压平导致权重趋近于零。
- **与 Weight Decay 的拉锯**：该策略仅在训练初期协助平稳，当中后期 Weight Decay 生效、网络学会主动抑制奇异值之后，Clip 即不再触发。因此它的角色是度过起步危险期的“临时护栏”。

## 例子

- **万亿模型 Kimi K2 的 Muon 优化训练**：在使用 Muon 优化器进行万亿规模的模型预训练时，Muon 的满秩更新量导致模型比用 Adam 更易发生 MaxLogit 爆炸。采用按头定制的 QK-Clip 以后，与 Muon 互相拔河，顺利让训练过渡到后期而没有牺牲推理兼容性或降低最终性能。

## 证据

- ev::11126::"当MaxLogit超过期望阈值$\tau$时，我们直接给$\boldsymbol{Q}\boldsymbol{K}^{\top}$乘上$\gamma = \tau / S_{\max}$，那么新的MaxLogit肯定就不超过$\tau$了。乘$\gamma$的操作，我们可以分别吸收到权重$\boldsymbol{Q}\boldsymbol{K}$的权重上去，于是我们得到初版QK-Clip"
- ev::11126::"对于(qr, kr)，我们应该只Clip到qr上去...直接以我们期望的MaxLogit为信号，对$\boldsymbol{Q},\boldsymbol{K}$的权重进行尽可能小的改动"