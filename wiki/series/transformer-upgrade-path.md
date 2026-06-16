---
type: series
title: Transformer升级之路
aliases:
  - Transformer Upgrade Path
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-03-08-Transformer升级之路-1-Sinusoidal位置编码追根溯源.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-23-Transformer升级之路-2-博采众长的旋转式位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-22-Transformer升级之路-3-从Performer到线性Attention.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-05-10-Transformer升级之路-4-二维位置的旋转式位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-12-28-Transformer升级之路-6-旋转位置编码的完备性分析.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-31-Transformer升级之路-8-长度外推性与位置鲁棒性.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-12-Transformer升级之路-9-一种全局长度外推的新思路.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-06-Transformer升级之路-10-RoPE是一种β进制编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-31-Transformer升级之路-11-将β进制位置进行到底.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-07-Transformer升级之路-12-无限外推的ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-24-Transformer升级之路-14-当HWFA遇见ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-20-Transformer升级之路-15-Key归一化助力长度外推.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-01-26-Transformer升级之路-16-复盘-长度外推技术.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-03-29-Transformer升级之路-17-多模态位置编码的简单思考.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-05-29-Transformer升级之路-18-RoPE的底数选择原则.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-04-18-Transformer升级之路-19-第二类旋转位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-05-04-Transformer升级之路-20-MLA好在哪里-上.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-07-10-Transformer升级之路-21-MLA好在哪里-下.md
article_ids:
  - "8231"
  - "8265"
  - "8338"
  - "8397"
  - "8601"
  - "9403"
  - "9431"
  - "9444"
  - "9603"
  - "9675"
  - "9706"
  - "9708"
  - "9728"
  - "9731"
  - "9859"
  - "9948"
  - "10040"
  - "10122"
  - "10862"
  - "10907"
  - "11111"
source_ids:
  - "8231"
  - "8265"
  - "8338"
  - "8397"
  - "8601"
  - "9403"
  - "9431"
  - "9444"
  - "9603"
  - "9675"
  - "9706"
  - "9708"
  - "9728"
  - "9731"
  - "9859"
  - "9948"
  - "10040"
  - "10122"
  - "10862"
  - "10907"
  - "11111"
series_goal: 从位置编码的数学约束出发，解释Transformer如何在RoPE、长度外推、线性/混合注意力和MLA之间逐步升级。
entry_roles:
  "8231": 用Sinusoidal推导建立绝对位置编码表达相对距离的起点。
  "8265": 提出RoPE并给出相对位置兼容线性Attention的核心构造。
  "8338": 从Performer切入线性Attention，暴露低秩和稀疏性瓶颈。
  "8397": 将RoPE推广到二维位置，确立矩阵指数作为旋转推广工具。
  "8601": 把标准Attention解释为无限维线性Attention，统一两类注意力视角。
  "9403": 证明分块对角RoPE在Self-Attention中的完备性并指出线性Attention例外。
  "9431": 将长度外推失败拆成未训练位置和注意力熵变化两个不一致。
  "9444": 用位置鲁棒性、随机位置训练和CHE基准细化外推诊断。
  "9603": 提出HWFA，用窗口层和无位置全局层兼顾局部外推与全局依赖。
  "9675": 把RoPE重写为β进制编码，统一NTK-RoPE和位置内插。
  "9706": 修正NTK-RoPE并用混合进制分摊不同维度的外推压力。
  "9708": 提出ReRoPE/Leaky ReRoPE，用保近压远的窗口截断支持免微调外推。
  "9728": 反用Leaky ReRoPE，把训练阶段外推策略换成推理期保持原速。
  "9731": 组合HWFA与ReRoPE，降低ReRoPE外推成本并保留全局层。
  "9859": 用Key归一化约束注意力幅值，迫使模型训练余弦相似度。
  "9948": 复盘长度外推，抽象出保近压远、转圈视角和外推税。
  "10040": 将RoPE坐标推广到文本图像混合输入的多模态位置编码。
  "10122": 从语义聚合条件推导RoPE底数下界并解释Partial RoPE。
  "10862": 提出VO-RoPE，把Value/Output旋转连接到复线性RNN和MLA兼容性。
  "10907": 通过消融实验分析MLA组件，指出head_dims是主要收益来源。
  "11111": 从训练/解码约束推导MLA近似最优性。
key_concepts:
  - "[[Sinusoidal位置编码]]"
  - "[[RoPE]]"
  - "[[线性注意力]]"
  - "[[长度外推]]"
  - "[[ReRoPE (Rectified RoPE)]]"
  - "[[Leaky ReRoPE]]"
  - "[[Key Normalization (KeyNorm)]]"
  - "[[Partial RoPE]]"
  - "[[NoPE]]"
  - "[[MLA]]"
key_methods:
  - "[[NTK-aware Scaled RoPE]]"
  - "[[Positional Interpolation]]"
  - "[[ReRoPE窗口外推方法]]"
  - "[[Leaky ReRoPE分段线性外推方法]]"
  - "[[InvLeaky ReRoPE]]"
  - "[[Hybrid Window-Full Attention]]"
  - "[[HWFA2 (HWFA + ReRoPE)]]"
  - "[[Key归一化长度外推方法 (KeyNorm)]]"
reading_paths:
  - "[[Transformer升级之路阅读路径]]"
status: draft
updated: 2026-06-14
---

# Transformer升级之路

## 搜索入口

- 阅读路径: [[Transformer升级之路阅读路径]]
- RoPE理论: [[Sinusoidal位置编码]] -> [[RoPE]] -> [[NTK-aware Scaled RoPE]] -> [[Partial RoPE]]
- 长度外推: [[长度外推]] -> [[ReRoPE窗口外推方法]] -> [[Leaky ReRoPE分段线性外推方法]] -> [[Key归一化长度外推方法 (KeyNorm)]]
- 架构连接: [[Hybrid Window-Full Attention]] -> [[HWFA2 (HWFA + ReRoPE)]] -> [[NoPE]] -> [[MLA]]
- 跨系列桥: [[NTK-aware Scaled RoPE]] 与 [[信噪比对齐调度迁移]] 都通过不变量对齐求缩放参数，但作用对象分别是RoPE频率和扩散噪声日程。

## 系列核心问题

苏剑林的 Transformer 升级之路系列包含 21 篇文章（2021--2025），核心不是罗列技巧，而是围绕 Transformer 的位置表示、长度外推和注意力结构，反复追问“什么数学约束让模型在训练长度之外仍然可用”。主线分为三条：

1. **Position Encoding Design**: From first-principles derivation of Sinusoidal encoding (8231), through the invention and theoretical deepening of RoPE (8265, 8397, 9403, 9675), to multimodal extensions (10040), base selection theory (10122), and alternative RoPE forms (10862).

2. **Length Extrapolation**: How can a Transformer trained on short sequences generalize to longer ones? Diagnosing root causes (9431, 9444), architectural solutions (9603, 9859), inference-time techniques (9675, 9706, 9708, 9728, 9731), and a comprehensive retrospective (9948).

3. **Attention Mechanism Optimization**: From linear attention analysis (8338, 8601), through hybrid architectures (9603, 9731), to the culminating analysis of Multi-head Latent Attention (10907, 11111).

## 文章顺序

### 基础篇 (Articles 1--5): Foundational Principles

1. **8231 -- Sinusoidal位置编码追根溯源** (2021-03-08)\
   Role: Foundational analysis. Derives Sinusoidal positional encoding from first principles (Taylor expansion, relative position via absolute encoding, remote attenuation via oscillatory integrals). Establishes the "absolute encoding achieving relative position effects" paradigm.

2. **8265 -- 博采众长的旋转式位置编码** (2021-03-23)\
   Role: Core innovation. Introduces Rotary Position Embedding (RoPE) and the RoFormer model. Establishes RoPE as the only relative position encoding compatible with linear attention, and proves remote attenuation via Abel transformation.

3. **8338 -- 从Performer到线性Attention** (2021-04-22)\
   Role: Attention mechanism analysis. Identifies the optimal activation function for linear attention (exponential) and analyzes the two fundamental bottlenecks: low-rank approximation and attention sparsity.

4. **8397 -- 二维位置的旋转式位置编码** (2021-05-10)\
   Role: Dimensional extension. Generalizes RoPE to 2D (for Vision Transformers) using matrix exponentials, demonstrating why the quaternion approach is a dead-end and establishing the correct mathematical tool.

5. **8601 -- 作为无限维的线性Attention** (2021-08-06)\
   Role: Theoretical unification. Shows that standard softmax attention IS infinite-dimensional linear attention, providing three deterministic/random projection frameworks (Performer, Taylor expansion, natural exponential definition) that unify the two paradigms.

### 分析篇 (Articles 6--10): Deepening Analysis

6. **9403 -- 旋转位置编码的完备性分析** (2022-12-28)\
   Role: Completeness proof. Proves that block-diagonal RoPE does not lose generality for self-attention via similarity transforms; identifies the exception for linear attention with nonlinear activation functions, suggesting full-matrix RoPE may be beneficial.

7. **9431 -- 长度外推性与局部注意力** (2023-01-12)\
   Role: Length extrapolation diagnosis. Identifies two fundamental inconsistencies causing length extrapolation failure (untrained positions, attention entropy collapse). Proposes the simple Attention Mask baseline, and classifies ALIBI/KERPLE/Sandwich/XPOS as local attention variants.

8. **9444 -- 长度外推性与位置鲁棒性** (2023-01-31)\
   Role: Positional robustness analysis. Introduces Randomized Positional Training (randomizing position indices during training), the CHE benchmark for controlled evaluation, log n scaling for attention entropy, and the equivalence class insight connecting position encoding design to length generalization.

9. **9603 -- 一种全局长度外推的新思路** (2023-05-12)\
   Role: Hybrid architecture. Proposes Hybrid Window-Full Attention (HWFA): most layers use window attention, one layer uses full attention without position encoding. Achieves length extrapolation while preserving global dependency. The only effective method for Post-Norm GAU.

10. **9675 -- RoPE是一种β进制编码** (2023-07-06)\
    Role: Foundational reframing. Reveals RoPE as a beta-encoding (base representation) where each dimension's angular frequency corresponds to a digit position. Explains Positional Interpolation as decimal point shifting and NTK-aware Scaled RoPE as base conversion. Demonstrates zero-shot extrapolation for GAU+PostNorm.

### 扩展篇 (Articles 11--16): Length Extrapolation Deep Dive

11. **9706 -- 将β进制位置进行到底** (2023-07-31)\
    Role: Beta-encoding generalization. Identifies a flaw in the original NTK-RoPE (base change without period rescaling) and proposes NTK-RoPE-fixed. Introduces mixed-radix NTK-RoPE (uneven extrapolation burden across dimensions, low dimensions bear more), achieving superior extrapolation to uniform base conversion. Also proposes posterior log n scaling for models not pre-trained with the trick.

12. **9708 -- 无限外推的ReRoPE？** (2023-08-07)\
    Role: Breakthrough extrapolation method. Proposes ReRoPE (Rectified RoPE) -- keep standard position spacing within a window, truncate to constant beyond it -- achieving theoretically infinite length extrapolation. Introduces Leaky ReRoPE as the general form (1/k step outside window). Demonstrates "longer context, lower loss" on LLAMA2-13b. Main cost: double attention computation, incompatible with Flash Attention.

13. **9728 -- 逆用Leaky ReRoPE** (2023-08-14)\
    Role: Efficiency-focused variation. Proposes InvLeaky ReRoPE -- use Leaky ReRoPE with step > 1 outside window during training, revert to standard RoPE at inference. Keeps inference speed unchanged while retaining extrapolation capability.

14. **9731 -- 当HWFA遇见ReRoPE** (2023-08-24)\
    Role: Architecture-method synergy. Proposes HWFA2 = HWFA + ReRoPE: replace HWFA's Full NoPE Attention with Full RoPE/ReRoPE Attention. Relaxes window attention receptive field constraints, allows multiple full attention layers. Achieves ReRoPE-level extrapolation with HWFA-level inference cost.

15. **9859 -- Key归一化助力长度外推** (2023-11-20)\
    Role: Attention normalization approach. Proposes KeyNorm (L2 normalize the Key sequence before attention). Key insight: models preferentially increase ||k_j|| rather than adjusting cos(q_i,k_j), leaving cos undertrained -- KeyNorm forces cos training. A "pre-training" fix requiring no inference-time modification.

16. **9948 -- "复盘"长度外推技术** (2024-01-26)\
    Role: Comprehensive retrospective. Reviews one year of length extrapolation development. Core insight: the key to training-free extrapolation is "保近压远" (preserve local, compress distant). Introduces the "rotation perspective" revealing OOD as untrained points on the unit circle. Compares all major methods and identifies the universal "extrapolation tax".

### 前沿篇 (Articles 17--21): Frontiers

17. **10040 -- 多模态位置编码的简单思考** (2024-03-29)\
    Role: Multimodal extension. Addresses position encoding for mixed text-image inputs. Proposes RoPE-Tie: 2D coordinates (n,n) for text (degenerating to RoPE-1D) and RoPE-2D for images, with scaling to maintain text-image symmetry.

18. **10122 -- RoPE的底数选择原则** (2024-05-29)\
    Role: Base selection theory. Derives a principled lower bound for RoPE base b from the "semantic aggregation" requirement (f_b(m) >= 0 for all m in [0, L-1]). Numerical values: 2.7e4 for 4K, 8.4e4 for 8K, 6.5e7 for 1M. Shows Partial RoPE naturally satisfies the inequality.

19. **10862 -- 第二类旋转位置编码** (2025-04-18)\
    Role: Alternative RoPE form. Proposes VO-RoPE: apply RoPE to Value and inverse RoPE to Output, achieving a second type of relative position encoding. Bridges attention and complex linear RNNs (when a_{i,j} = gamma^{i-j}, degenerates to complex-decay linear RNN). Potential application: resolving RoPE incompatibility with KV-shared MLA.

20. **10907 -- MLA好在哪里?（上）** (2025-05-04)\
    Role: MLA analysis (experimental). Ablation studies identifying which components make Multi-head Latent Attention effective. Key finding: increasing head_dims is the most critical factor -- GQA1-256-PR surpasses MLA. Partial RoPE and KV-Shared provide additional but smaller gains.

21. **11111 -- MLA好在哪里?（下）** (2025-07-10)\
    Role: MLA analysis (theoretical). Proves MLA's near-optimality under joint training/decode efficiency constraints. Core insight: decoding bottleneck is KV Cache (optimal: MQA with head_dims=KV Cache), training bottleneck is head_dims (optimal: MHA). MLA's dual projection harmonizes these conflicting requirements -- trains as MHA-128, decodes as MQA-512.

## 概念递进

```
Sinusoidal Position Encoding (8231)
    |
    v
Rotary Position Embedding / RoPE (8265)
    |
    +---> 2D RoPE generalization (8397)
    +---> RoPE Completeness Analysis (9403)
    +---> RoPE as Beta-Encoding (9675)
    |        |
    |        +---> Mixed-Radix NTK-RoPE (9706)
    |        +---> RoPE Base Selection Principle (10122)
    |
    +---> VO-RoPE / Second-type RoPE (10862)
    |
    v
Length Extrapolation Problem (9431)
    |
    +---> Positional Robustness / Randomized Training (9444)
    +---> Hybrid Window-Full Attention (9603)
    |        |
    |        +---> HWFA2 = HWFA + ReRoPE (9731)
    |
    +---> NTK-aware Scaled RoPE (9675) ---> Mixed-Radix NTK-RoPE (9706)
    |
    +---> ReRoPE (9708)
    |        |
    |        +---> InvLeaky ReRoPE (9728)
    |        +---> HWFA + ReRoPE (9731)
    |
    +---> Key Normalization (9859)
    |
    +---> Length Extrapolation Retrospective (9948)

Multimodal RoPE (10040)

Standard Attention <--> Linear Attention (8338, 8601)
    |
    v
MLA / Multi-head Latent Attention (10907, 11111)
    |
    +---> head_dims scaling analysis
    +---> Partial RoPE theory
    +---> KV-Shared / Dual Projection
```

## 命题递进

1. Absolute position encodings CAN express relative position information (8231).
2. RoPE achieves "absolute encoding, relative effect" with mathematical rigor; it is the only relative encoding compatible with linear attention (8265).
3. Exponential is the optimal activation for linear attention; low-rank and sparsity are key bottlenecks (8338).
4. 2D RoPE requires both relativity and invertibility; matrix exponential is the correct tool (8397).
5. Standard attention IS infinite-dimensional linear attention (8601).
6. Block-diagonal RoPE is complete for self-attention; linear attention may benefit from full matrices (9403).
7. Length extrapolation failures stem from TWO inconsistencies, not just position encoding design (9431).
8. Randomizing positions during training teaches the model to learn "order" rather than exact indices; log n scaling resolves entropy inconsistency (9444).
9. Window Attention + Full Attention hybrid can achieve global length extrapolation (9603).
10. RoPE is fundamentally a beta-encoding; NTK-RoPE = base conversion; Positional Interpolation = decimal point shift (9675).
11. NTK-RoPE-old was incomplete (base changed but period not rescaled); mixed-radix NTK-RoPE distributes extrapolation burden unevenly across dimensions for better results (9706).
12. ReRoPE achieves theoretically infinite length extrapolation by "preserving local, compressing distant"; "longer context, lower loss" is possible (9708).
13. InvLeaky ReRoPE decouples training and inference position encoding strategies, trading some extrapolation quality for inference speed (9728).
14. HWFA2 combines ReRoPE-level extrapolation with HWFA-level inference efficiency (9731).
15. Key normalization forces models to sufficiently train cos(q_i, k_j), which is the real hidden cause of attention length extrapolation failure (9859).
16. "保近压远" (preserve local, compress distant) unifies all successful training-free length extrapolation methods; the "rotation perspective" reveals OOD as untrained points on the unit circle (9948).
17. RoPE-Tie provides theoretically unified position encoding for multimodal inputs (10040).
18. RoPE base has a principled lower bound from semantic aggregation; L-long training inherently requires larger base (10122).
19. VO-RoPE (RoPE on Value + inverse RoPE on Output) provides a second type of relative position encoding bridging attention and complex linear RNNs (10862).
20. Increasing head_dims is the single most important factor behind MLA's effectiveness; previous attempts at head_dims=128 started from a deficient baseline (10907).
21. MLA is near-optimal under joint training/decode efficiency constraints; its dual projection harmonizes the conflicting requirements of MHA (training) and MQA (decoding) (11111).

## 反复出现的方法

- **复数/矩阵表示**: Used throughout articles 1, 2, 4, 6, 19 for deriving and proving positional encoding properties; also central to the linear RNN connection in VO-RoPE.
- **泰勒展开/振荡积分**: Article 1 derives Sinusoidal encoding; article 5 uses Taylor expansion for infinite-dimensional linear attention; article 18 uses integral approximation for asymptotic analysis of base lower bound.
- **Abel变换/分部求和**: Article 2 uses it to prove RoPE's remote attenuation; reappears in article 10's beta-encoding analysis.
- **矩阵指数**: Articles 4 and 6 use matrix exponentials to analyze RoPE in 2D and prove completeness; article 19 uses it in the VO-RoPE proof.
- **log n scaling**: Appears in articles 8, 9, 10, 11 as a solution to attention entropy inconsistency during extrapolation; evolves into posterior log n scaling for post-hoc application (9706).
- **β进制类比**: Introduced in article 10, extended in article 11 (mixed-radix), and referenced in article 18 (base selection theory) as a unifying framework for understanding RoPE's dimension-wise frequency design.
- **Partial RoPE / 部分旋转**: Introduced in article 18 as a theoretically optimal variant, becomes central to the MLA analysis in articles 20-21 where it enables the separation of NoPE computation from position encoding.
- **消融实验 / 控制变量**: Used systematically in articles 20-21 to isolate the contribution of each MLA component (head_dims, Partial RoPE, KV-Shared, dual projection).

## 阅读路径

### 位置编码入门 (Position Encoding Fundamentals)
8231 (Sinusoidal derivation) -> 8265 (RoPE) -> 8397 (2D RoPE) -> 9675 (RoPE as beta-encoding)

### 长度外推技术 (Length Extrapolation)
9431 (diagnosis) -> 9444 (robustness) -> 9603 (HWFA) -> 9675 (NTK-RoPE) -> 9706 (mixed-radix NTK) -> 9708 (ReRoPE) -> 9728 (InvLeaky ReRoPE) -> 9731 (HWFA+ReRoPE) -> 9859 (KeyNorm) -> 9948 (retrospective)

### 注意力机制优化 (Attention Mechanism Optimization)
8338 (linear attention) -> 8601 (infinite-dim linear attention) -> 9603 (HWFA) -> 9731 (HWFA2) -> 10907 (MLA part 1) -> 11111 (MLA part 2)

### 位置编码理论深化 (Position Encoding Theory Deepening)
9403 (completeness) -> 9675 (beta-encoding) -> 10122 (base selection) -> 10862 (second-type RoPE / VO-RoPE)

### 完整顺序 Complete Sequential (recommended)
8231 -> 8265 -> 8338 -> 8397 -> 8601 -> 9403 -> 9431 -> 9444 -> 9603 -> 9675 -> 9706 -> 9708 -> 9728 -> 9731 -> 9859 -> 9948 -> 10040 -> 10122 -> 10862 -> 10907 -> 11111

## 与其他系列的连接

- **线性Attention探索**: The linear attention analysis in articles 3 and 5 builds on Su Jianlin's earlier work on linear attention (archives/7546).
- **Performer/随机投影**: Article 3 references and extends the Performer model discussion from article 7921.
- **NTK/神经网络理论**: Articles 10-11 connect to Neural Tangent Kernel literature for the theoretical backing of NTK-aware Scaled RoPE.
- **GAU/模型架构**: Articles 9, 12-14's experiments are built on GAU_alpha, connecting to the GAU architecture discussion (archives/8934, 9052).
- **LLAMA系列**: Articles 12, 18 discuss LLAMA2 and LLAMA3's practical choices (ReRoPE on LLAMA2-13b, b=500000 in LLAMA3 connecting to base selection theory).
- **DeepSeek / MLA**: Articles 19-21 connect directly to DeepSeek's MLA architecture, analyzing its design choices (VO-RoPE for KV compatibility, head_dims scaling, dual projection).
- **复线性RNN**: Article 19 draws connections between VO-RoPE and complex linear RNNs (LRU, RetNet, RWKV), positioning it as a bridge between attention and state-space models.

## 缺口与待验证关系

- **Linear Attention + RoPE completeness**: Article 6 identifies that linear attention with nonlinear activation functions may benefit from full-matrix RoPE (not just block-diagonal). This claim lacks experimental validation.
- **Randomized training on CHE**: Article 8 proposes combining log n scaling with randomized positional training but notes CHE benchmark results are not yet available for this combination.
- **HWFA scaling laws**: Article 9 raises the concern that HWFA's slight training performance degradation may amplify at larger scales (billions of parameters). This has not been empirically tested.
- **NTK-RoPE + CHE**: Article 10 demonstrates NTK-RoPE effectiveness on language modeling but does not evaluate on the CHE benchmark.
- **Single-head vs multi-head extrapolation**: Article 9 notes that many length extrapolation methods (ALIBI, Sandwich, XPOS) fail on GAU (single-head attention), raising questions about the role of multi-head design in extrapolation.
- **VO-RoPE practical application**: Article 19 proposes VO-RoPE as a solution to MLA's RoPE incompatibility, but this application has not been experimentally validated.
- **Partial RoPE vs Full RoPE theoretical comparison**: Article 18 suggests Partial RoPE may be theoretically superior, but article 20 shows only marginal improvement over standard RoPE -- the regime where Partial RoPE decisively outperforms Full RoPE remains unclear.
- **KeyNorm + ReRoPE combination**: Article 15 notes KeyNorm appears to "immunize" against existing RoPE extrapolation tricks. Whether KeyNorm + ReRoPE provides additive gains has not been tested.
- **MLA optimality at scale**: Article 21's theoretical argument for MLA near-optimality assumes Partial RoPE is "not worse than" Full RoPE. Whether this holds at hundreds-of-billions scale or across diverse training distributions is unverified.
- **Extrapolation tax universality**: Article 16 identifies the "extrapolation tax" (performance degradation within training length) as a universal phenomenon. The fundamental cause and whether architectural changes could eliminate it entirely remain open questions.
