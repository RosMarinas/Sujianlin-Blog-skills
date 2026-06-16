# Wiki Index

This is the default entry point for LLM queries over the compiled wiki. Start
here before expanding into raw source pages or graph JSONL.

## Query Entry Points

| Query type | Start here | Then inspect |
| --- | --- | --- |
| Repository purpose and scope | [[overview]] | [Purpose](../purpose.md), [Schema](../schema.md) |
| Series-local reading order | `wiki/series/` | `wiki/reading_paths/`, `probes/questions.jsonl` |
| Cross-series method transfer | `wiki/methods/` | `wiki/methods/_candidates.md`, `graph/edges.jsonl` |
| Evidence-backed claim check | `wiki/sources/` | `graph/evidence_spans.jsonl`, `probes/results.jsonl` |
| Failed or deferred answers | `probes/failures.jsonl` | `wiki/log.md` |
| Graph/query health | `graph/nodes.jsonl` | `graph/edges.jsonl`, `skill/tools.py` |

## Series Catalog

| Series | Sources | Summary | Key methods | Probe entry |
| --- | ---: | --- | --- | --- |
| [[基于流式幂迭代的Muon实现]] | 5 | Muon implementation through streaming power iteration and matrix optimizer scaling. | [[将昂贵矩阵运算流式化]], [[用稳定性指标约束优化器缩放]] | `probe::mvp::streaming_muon_path` |
| [[MoE环游记]] | 8 | Expert routing, load balancing, quantile balancing, and sequence-level balance. | [[用对偶偏置改写路由约束]], [[用分布估计近似滑动分位数]] | `probe::moe_tour::reading_path` |
| [[低秩近似之路]] | 5 | From pseudoinverse and SVD to CR, ID, and CUR structural low-rank approximations. | [[将矩阵近似问题化为骨架选择问题]] | `probe::low_rank::series_path` |
| [[让炼丹更科学一些]] | 6 | SGD convergence, endpoint loss, and learning-rate schedule derivations. | [[通过恒等式重写优化轨迹]], [[自上而下构造辅助序列]] | `probe::scientific-alchemy-sgd::reading-path` |
| [[重新思考学习率与Batch Size]] | 4 | Learning-rate and Batch Size scaling for SGD, SignSGD, Muon, and EMA/Adam-style momentum. | [[用平均场近似替代复杂期望计算]], [[用等效Batch Size解释动量降噪]] | `probe::lr_batch::reading_path` |
| [[从动力学角度看优化算法]] | 7 | Optimization algorithms interpreted as ODE/SDE dynamics, stability, and trajectory integral. | [[把优化算法解释为动力系统离散化]] | `probe::dynamics::reading_path` |
| [[流形上的最速下降]] | 5 | Constrained steepest descent on sphere, orthogonal, Stiefel, spectral-sphere, and dual-gradient settings. | [[用切空间投影改写约束最速下降]], [[用对偶目标求解约束更新系数]] | `probe::manifold::reading_path` |
| [[SVD分解]] | 3 | SVD as a representation-learning lens for linear autoencoders, clustering semantics, and Word2Vec structure. | [[用矩阵分解重写表示学习结构]] | `probe::svd::reading_path` |
| [[MuP之上]] | 4 | Stability indicators for good models, linear-layer MuP-Muon, special modules, and parameter stability. | [[用稳定性指标约束优化器缩放]] | `probe::mup_above::reading_path` |
| [[更别致的词向量模型]] | 6 | PMI/simpler-GloVe word-vector construction from mutual information to vector geometry. | [[用互信息内积构造词向量几何]] | `probe::word_vector::reading_path` |
| [[CoSENT]] | 3 | 有监督句向量从分类式训练转向余弦排序损失，并推广到交互式相似度模型。 | [[CoSENT排序损失]], [[CoSENT阅读路径]] | `probe::cosent::reading_path` |
| [[重温SSM]] | 4 | HiPPO, S4, and rational transfer functions for state-space models. | [[生成函数化卷积核计算]], [[对角加低秩与Woodbury加速]] | `probe::revisit_ssm::reading_path_order` |
| [[Transformer升级之路]] | 21 | Positional encoding, length extrapolation, RoPE variants, and MLA analysis. | [[NTK-aware Scaled RoPE]], [[ReRoPE窗口外推方法]], [[HWFA2 (HWFA + ReRoPE)]], [[Transformer升级之路阅读路径]] | `probe::transformer_upgrade::notation_base_beta_mapping` |
| [[生成扩散模型漫谈]] | 31 | DDPM, DDIM, score matching, ODE/SDE views, and consistency-style diffusion variants. | [[ODE直接推导法]], [[恒等式蒸馏法]], [[特征线ODE构造法]] | `probe::forced_connection::muon_vs_mla` |
| [[变分自编码器]] | 14 | VAE derivation, posterior sampling, KL vanishing, geometry, density estimation, CNN poems, VIB, VQ-VAE, NVAE, and UniVAE. | [[VAE联合分布最小化]], [[直通估计方法]], [[重要性加权估计]] | `probe::variational-autoencoders::vib_regularization_benefit` |
| [[细水长flow]] | 4 | Normalizing flows: NICE coupling layers, RealNVP & Glow affine coupling, f-VAEs, and i-ResNet. | [[加性耦合层变换]], [[仿射耦合层变换]], [[可逆残差网络前向与逆迭代]] | `probe::normalizing_flows::series_path` |
| [[从费马大定理谈起]] | 12 | Fermat's Last Theorem from Pythagorean triples through Gaussian integers, Eisenstein integers, unique factorization, infinite descent, and rational points. | [[无穷下降法]], [[扩域求解丢番图方程]], [[切割线法]] | `probe::fermat::reading_path` |
| [[费曼积分法]] | 7 | Differentiation under the integral sign, Euler-style parameter integration, and applications. | [[积分符号内取微分法]] | `probe::feynman::reading_path` |
| [[当概率遇上复变]] | 4 | 利用生成函数和复变函数工具分析离散与连续概率问题，推导随机游走、路径积分和概率分布极限。 | [[通过特征函数将连续概率卷积转化为乘积]], [[用路径积分表示随机过程转移概率]] | — |
| [[新理解矩阵]] | 6 | 建立符合直觉的、数形结合的矩阵、行列式与相似矩阵的几何与代数理解方式。 | [[用相似矩阵表达同一线性变换]], [[用公理化性质定义行列式]] | — |
| [[不可思议的Word2Vec]] | 5 | 从原理、模型、到实际应用全面且深层次地剖析与实现Word2Vec模型. | [[基于Word2Vec的无监督关键词提取]], [[基于Word2Vec计算相关词]] | `probe::word2vec::reading_path` |
| [[通用爬虫探索]] | 3 | 探索一种不依赖特定正则表达式、基于网页交集及DOM树位置信息的无监督通用信息抽取与论坛分块聚类爬虫方案。 | [[网页标准模板比对法]], [[基于差分峰值的楼层切分聚类]] | — |
| [[基于深度学习的阅读理解问答]] | 3 | 探索基于卷积神经网络、自回归Seq2Seq及非自回归MLM模型在阅读理解式问答任务中的结构设计与性能演进。 | [[基于MLM的非自回归阅读理解问答]] | — |
| [[中文分词系列]] | 3 | 通过深度学习与非监督/半监督统计方法解决中文分词、新词发现以及歧义切分问题。 | [[多阶凝固度与回溯过滤新词发现]] | — |
| [[欧拉数学]] | 5 | 通过直观且具有启发性的初等推导，展现欧拉在数论和拓扑学中的创造性直觉与方法。 | [[基于生成函数的欧拉乘积展开]] | — |
| [[理解黎曼几何]] | 6 | 从直观物理与几何图景出发，逐步建立并计算黎曼度量、测地线、联络、协变导数和黎曼曲率等核心内蕴几何实体。 | [[变分求解联络系数法]], [[活动正交标架度规分解法]] | — |
| 摄动与ODE系列 | 12 | Perturbation theory, Gaussian integral perturbation, operator methods for ODEs, Lie symmetry. | — | — |
| [[优化器稳定性与自适应机制]] | 13 | 深度神经网络在缩放（Scaleup）以及极速下降探索中参数和注意力层的稳定性约束与更新调度机制。 | — | `probe::optimizers_vq_embeddings::lion_memory` |
| [[向量量化优化]] | 5 | 探索向量量化（Vector Quantization）在大自编码与注意力机制线性化中的逼近与优化技巧。 | — | `probe::optimizers_vq_embeddings::fsq_superiority` |
| 多模态与文本搜索 | 7 | Multimodal position encoding (RoPE-TV), MCMC text generation, Gibbs/CGMH sampling. | — | — |
| [[GAN目标函数与约束专题]] | 8 | GAN targets, dual divergences, Lipschitz penalties, RSGAN and stop-gradient implementation. | [[用对偶散度构造对抗生成目标]], [[梯度惩罚满足L约束]] | `probe::gan_attention::gan_objective_path` |
| [[Attention归一化与线性化专题]] | 7 | Standard attention, sparse attention, linear attention, Nyströmformer, entropy-invariant scaling and GAU normalization. | [[用结构约束线性化Attention计算]], [[Attention-E熵不变性缩放]] | `probe::gan_attention::attention_efficiency_path` |
| [[LLM架构与上下文扩展]] | 10 | 从注意力机制的本质性质和概率视角出发，探索如何通过架构优化与即插即用算法提高模型的表达容量与上下文处理窗口。 | [[LRU参数化与初始化]], [[LRU并行化递归算法]], [[最小熵Pooling]], [[无交跳转加权]], [[非线性RNN摄动并行化]] | `probe::llm_arch::decoder_only_rank` |
| [[GlobalPointer与联合抽取]] | 5 | 基于GlobalPointer及其变体GPLinker与条件层归一化在信息抽取、命名实体识别与关系抽取中的方法探索与性能演进。 | [[基于条件LayerNorm的实体关系抽取]], [[基于概率分解的关系抽取]] | `probe::ie::efficient_global_pointer` |
| [[Transformer架构与归一化]] | 10 | 探讨Transformer自注意力机制的瓶颈、Talking-Heads、Synthesizer、Gated Attention Unit与层归一化位置的选择。 | [[gated_attention_unit_fusion]], [[roformer_v2_simplification]] | `probe::architecture::gau_head_count` |

## Method Hubs

### Cross-Series Method Hubs

| Method hub | Layer | Connected series | Lower-level implementations | Status |
| --- | --- | --- | --- | --- |
| [[用结构分解降低计算复杂度]] | High-level generative move | [[低秩近似之路]], [[重温SSM]] | [[将矩阵近似问题化为骨架选择问题]], [[对角加低秩与Woodbury加速]] | stable |

### Formula-Verified Bridge Pairs

| Bridge pair | Operation type | Evidence | Status |
| --- | --- | --- | --- |
| [[通过恒等式重写优化轨迹]] ↔ [[恒等式蒸馏法]] | Rewrite / identity transform | `ev::11494::新恒等式`, `ev::10567::恒等变换` | candidate |
| [[NTK-aware Scaled RoPE]] ↔ [[信噪比对齐调度迁移]] | Align / calibrate by invariance | `ev::9675::进制类比`, `ev::10047::向低看齐` | candidate |
| [[Cauchy-Schwarz不等式放缩]] ↔ [[自上而下构造辅助序列]] | Construct auxiliary sequence | `ev::9467::牛刀小试`, `ev::11540::最强结论` | candidate |
| [[用对偶偏置改写路由约束]] ↔ [[高斯噪声正则化]] | Dual / constraint rewrite | `ev::11619::线性规划`, `ev::5253::分布标准化` | candidate |
| [[把优化算法解释为动力系统离散化]] ↔ [[ODE直接推导法]] | Discrete ↔ continuous bridge | `ev::5655::GD与ODE` | candidate |
| [[用对偶目标求解约束更新系数]] ↔ [[用对偶偏置改写路由约束]] | Dual / constraint rewrite | `ev::11388::对偶目标`, `ev::11619::线性规划` | candidate |
| [[用矩阵分解重写表示学习结构]] ↔ [[用结构分解降低计算复杂度]] | Decompose / reduce dimension | `ev::4208::等价性`, `ev::10662::基本定义` | candidate |
| [[用等效前向表达保留SVD梯度]] ↔ [[用对偶目标求解约束更新系数]] | Rewrite / identity transform | `ev::10878::梯度三`, `ev::11388::基本概念` | candidate |
| [[用稳定性指标约束优化器缩放]] ↔ [[用切空间投影改写约束最速下降]] | Dual / constraint rewrite | `ev::11605::最速下降`, `ev::11196::优化原理` | candidate |
| [[用互信息内积构造词向量几何]] ↔ [[用矩阵分解重写表示学习结构]] | Structure-expose by factorization | `ev::4671::模型形式`, `ev::4233::Word2VecSVD` | candidate |
| [[用对偶散度构造对抗生成目标]] ↔ [[VAE联合分布最小化]] | Dual / constraint rewrite | `ev::6163::对偶散度定义`, `ev::5343::直面联合分布` | candidate |
| [[用结构约束线性化Attention计算]] ↔ [[用结构分解降低计算复杂度]] | Decompose / reduce dimension | `ev::8180::三矩阵近似`, `ev::10662::基本定义` | candidate |

### Series-Local Methods Needing Later Bridge Review

- [[通过恒等式重写优化轨迹]]: currently centered on SGD convergence and learning-rate schedules.
- [[特征线ODE构造法]]: currently centered on diffusion/ODE construction.
- [[BN防止KL消失]]: currently centered on VAE KL-vanishing repair.
- [[用分布估计近似滑动分位数]]: currently centered on MoE sequence-level balancing.

## Bridge Candidates

- [[通过恒等式重写优化轨迹]] and diffusion [[恒等式蒸馏法]] passed Bridge Pass D formula-level verification as an identity-rewrite bridge.
- [[NTK-aware Scaled RoPE]] and [[信噪比对齐调度迁移]] passed Bridge Pass D formula-level verification as a scale-from-invariant bridge.
- [[Cauchy-Schwarz不等式放缩]] and [[自上而下构造辅助序列]] passed formula-level verification as an auxiliary-bound construction bridge.
- [[用对偶偏置改写路由约束]] and [[高斯噪声正则化]] passed formula-level verification as a constraint-absorption bridge, but remain below stable because dual variables and KL penalties are not identical mechanisms.
- [[用平均场近似替代复杂期望计算]] and [[用期望消去采样依赖]] are a new tentative expectation-reasoning bridge: both manipulate expectations to reduce sampling complexity, but the new method is an approximation while the older SGD proof is an exact expectation rewrite inside a bound.
- [[用等效Batch Size解释动量降噪]] and [[用稳定性指标约束优化器缩放]] are a new tentative optimizer-scaling bridge pending formula-level verification against the Muon/MuP sources.
- [[把优化算法解释为动力系统离散化]] and [[ODE直接推导法]] are a candidate discrete-continuous bridge: both construct continuous dynamics before returning to a discrete process, but optimizer gradient flow and diffusion probability-flow ODE act on different state objects.
- [[用对偶目标求解约束更新系数]] and [[用对偶偏置改写路由约束]] are a candidate dual-variable bridge: both absorb constraints into auxiliary variables, while manifold coefficients and MoE routing biases remain mathematically distinct mechanisms.
- [[用矩阵分解重写表示学习结构]] and [[用结构分解降低计算复杂度]] are a candidate factorization bridge: both replace a large object with structured low-dimensional factors, with different goals.
- [[用等效前向表达保留SVD梯度]] and [[用对偶目标求解约束更新系数]] are a candidate SVD-calculus bridge through msign/nuclear-norm reasoning.
- [[用稳定性指标约束优化器缩放]] and [[用切空间投影改写约束最速下降]] are a candidate constrained-update bridge: both derive a fastest update from norm/stability constraints.
- [[用互信息内积构造词向量几何]] and [[用矩阵分解重写表示学习结构]] are a candidate representation-matrix bridge: PMI embeddings fit a Gram matrix while SVD rewrites representation learning as matrix factorization.
- Keep [[Positional Interpolation]] ↔ [[信噪比对齐调度迁移]] tentative: PI directly compresses positions, while SNR migration solves a constrained alignment equation.
- Test whether [[用对偶偏置改写路由约束]] and optimizer constraint methods share a real dual-variable pattern.
- [[用对偶散度构造对抗生成目标]] and [[VAE联合分布最小化]] are a candidate generative-distribution bridge: both define generation as distribution discrepancy minimization, but GAN uses a dual adversarial objective while VAE uses direct joint KL.
- [[用结构约束线性化Attention计算]] and [[用结构分解降低计算复杂度]] are a candidate structure-decomposition bridge through Nyströmformer three-matrix attention approximation.
- Keep new high-level method names in `wiki/methods/_candidates.md` until at least two source-backed implementations support them.

## Collections

- `sources/`: article summaries tied to immutable source markdown.
- `series/`: ordered article groups and local method summaries.
- `topics/`: cross-series topical aggregation.
- `concepts/`: definitions and reusable notation.
- `formulas/`: reusable formulas and standard notation.
- `propositions/`: evidence-backed claims.
- `methods/`: high-level and low-level method pages.
- `problem_patterns/`: recurring problem forms.
- `examples/`: derivation blocks and worked source-local examples.
- `reading_paths/`: ordered study routes.

## Health Snapshot

Latest cycle: `2026-06-12` Cycle 5 VAE/Flow batches (9 articles: Normalizing Flows & Variational Autoencoders).

Current stage progress: `9/9` new articles compiled this cycle.

- Source coverage: `476/674` converted source IDs compiled; `198` remaining.
- Graph nodes: `3284` (including `1442` evidence spans as nodes).
- Graph edges: `4262`.
- Evidence spans: `1442`.
- Active probes: `323` questions, `246` results.
- Duplicate probe result IDs: `0`.
- Active probes without result or unresolved failure: `0`.
- Cross-series method hubs: `1 stable` ([[用结构分解降低计算复杂度]]), connecting low-rank approximation and SSM series.
- Formula-verified or formula-anchored bridge pairs: `12`.
- Method nodes: `316`.
- Formula notation coverage: all formula pages pass current frontmatter lint.
- Example notation coverage: all example pages pass current frontmatter lint.
- Default hard health gate: `0` issues after schema-path/status repair.
- Strict quality review backlog: `1102` historical required-field issues remain; see `docs/superpowers/reports/2026-06-11-wiki-quality-review-and-merge-gate.md`.

### New this session (9 articles)

- **Batches**:
  - `normalizing-flows` (4 articles)
  - `variational-autoencoders` (5 articles)
- **Series**:
  - [[细水长flow]] (created)
  - [[变分自编码器]] (updated)
- **Topics**:
  - [[生成模型]] (updated)
  - [[向量量化优化]] (updated)
  - [[Lipschitz约束与泛化]] (updated)
- Frontmatter type normalization: `0` quoted `type` fields remain.
- Official health validation: `0` issues after this batch.
- Quality merge policy updated: future staged batches require strict quality review before merge.
