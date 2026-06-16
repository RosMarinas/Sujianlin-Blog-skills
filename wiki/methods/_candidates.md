--------|---------|
| 让炼丹更科学一些 | [[通过恒等式重写优化轨迹]], [[用期望消去采样依赖]] |
| 生成扩散模型漫谈 | [[估计-校正分解]], [[恒等式蒸馏法]] |
| 变分自编码器 | [[VAE联合分布最小化]], [[球面VAE构造法]] |
| MoE环游记 | [[从计算节省目标重写模型结构]] |
| Transformer升级之路 | ALIBI, KERPLE, Sandwich, Matrix Exponential for RoPE |

**Verified bridge (Bridge Pass D)**: [[通过恒等式重写优化轨迹]] (SGD: rewrites terminal loss through a weighted endpoint-average identity) and [[恒等式蒸馏法]] (diffusion: rewrites generator loss through the score identity) — both use an algebraic/expectation identity to replace a hard optimization target with a tractable equivalent expression. Evidence: `ev::11494::新恒等式`, `ev::10567::恒等变换`. Promoted graph edge status: `candidate/strong`.

**Key bridge**: [[VAE联合分布最小化]] (VAE: rewrites ELBO as KL between joint distributions) and [[从计算节省目标重写模型结构]] (MoE: rewrites compute-saving as Dense-output approximation) — both start from a system design goal, rewrite it as a mathematical optimization, and derive architecture from the rewritten form.

**Tentative**: The Transformer ALIBI/KERPLE/Sandwich family rewrites attention scores with additive biases. The generative move (additive identity transform) matches, but the application domain (position encoding vs. loss design) is different enough that the connection remains tentative.

### 2. Align / calibrate by invariance (10 methods, 3 series)

**Shared generative move**: Identify a quantity that should remain invariant under a transformation, then derive constraints or scaling rules from enforcing this invariance.

| Series | Methods |
|--------|---------|
| Transformer升级之路 | [[ReRoPE窗口外推方法]], [[Leaky ReRoPE分段线性外推方法]], [[NTK-aware Scaled RoPE]], [[Positional Interpolation]], [[Key归一化长度外推方法 (KeyNorm)]], XPOS |
| 生成扩散模型漫谈 | [[一致性蒸馏法]], [[信噪比对齐调度迁移]], [[捷径模型训练法]] |
| 基于流式幂迭代的Muon实现 | [[将昂贵矩阵运算流式化]] |

**Verified bridge (Bridge Pass D)**: [[NTK-aware Scaled RoPE]] and [[信噪比对齐调度迁移]] both choose a scale by enforcing an invariant equation. NTK-RoPE solves $\lambda$ so the lowest-frequency RoPE term matches positional interpolation while high-frequency terms remain near extrapolation; SNR migration solves the high-resolution schedule so downsampled SNR matches the low-resolution schedule under $\bar{\alpha}_t^2+\bar{\beta}_t^2=1$. Evidence: `ev::9675::进制类比`, `ev::10047::向低看齐`. Promoted graph edge status: `candidate/strong`.

**Tentative after Bridge Pass D**: [[Positional Interpolation]] and [[信噪比对齐调度迁移]] share a rescaling intuition, but PI directly maps $n\mapsto n/k$ while SNR migration solves from an explicit invariant equation plus normalization constraint. Keep the PI/SNR bridge as `tentative/weak`.

**Series-internal hierarchy (Compliance Pass)**: Transformer length-extrapolation methods now have explicit layering edges: [[NTK-aware Scaled RoPE]] specializes [[Positional Interpolation]]; [[ReRoPE窗口外推方法]] specializes [[NTK-aware Scaled RoPE]]; [[Leaky ReRoPE分段线性外推方法]] specializes [[ReRoPE窗口外推方法]]. Additive-bias methods are layered as ALIBI → KERPLE → Sandwich. XPOS is linked as a RoPE specialization, while HWFA2 is linked to both HWFA and ReRoPE. KeyNorm remains a weak/tentative relation to ReRoPE because it is a training-time normalization, not an inference-time position transform.

**Key bridge**: [[一致性蒸馏法]] (consistency across adjacent time steps) and [[捷径模型训练法]] (self-consistency across step sizes) — both train by enforcing that model outputs are invariant to the discretization parameter (time step).

**Tentative**: [[将昂贵矩阵运算流式化]] — aligns under "maintaining invariant approximation quality while replacing one-shot computation with streaming updates." The invariance argument is structural rather than formula-level. Confidence: tentative.

### 3. Discrete ↔ continuous bridge (8 methods, 3 series)

**Shared generative move**: Construct a continuous process (ODE, SDE, PDE) whose solution at a specific point recovers the discrete quantity of interest.

| Series | Methods |
|--------|---------|
| 生成扩散模型漫谈 | [[Fokker-Planck方程推导法]], [[ODE直接推导法]], [[特征线ODE构造法]], [[矫流构造法]], [[万有引力类比构造法]] |
| 重温SSM | [[正交基投影推导状态动力学]], [[生成函数化卷积核计算]] |
| 让炼丹更科学一些 | [[用变分法反推学习率]] |

**Key bridge**: [[ODE直接推导法]] (diffusion: derives ODE from continuity equation via Jacobian) and [[正交基投影推导状态动力学]] (SSM: derives state ODE from orthogonal projection via differentiation) — both construct continuous dynamics by writing a conservation/compression condition then differentiating through time.

**Key bridge**: [[用变分法反推学习率]] (SGD: continuous limit of discrete learning rate, solved via Euler-Lagrange) and [[ODE直接推导法]] (diffusion: continuous limit of discrete denoising, solved via continuity equation) — both take the continuous limit of a discrete process and solve the resulting differential equation.

**Key bridge**: [[特征线ODE构造法]] (designs trajectory then solves continuity along it) and [[生成函数化卷积核计算]] (maps convolution to generating function on unit circle) — both convert a discrete sequence operation into evaluation along a continuous curve (characteristic lines ↔ unit circle).

### 4. Decompose / reduce dimension (6 methods, 4 series)

**Shared generative move**: Replace a high-dimensional free object with a low-dimensional structure (skeleton, low-rank, local/global split, decoupled variables).

| Series | Methods |
|--------|---------|
| 低秩近似之路 | [[将矩阵近似问题化为骨架选择问题]], [[用结构分解降低计算复杂度]] |
| 重温SSM | [[对角加低秩与Woodbury加速]], [[用结构分解降低计算复杂度]] |
| 生成扩散模型漫谈 | [[方差消减技术]] |
| Transformer升级之路 | [[Hybrid Window-Full Attention]], [[HWFA2 (HWFA + ReRoPE)]] |

**Stable hub (Bridge Pass D+)**: [[用结构分解降低计算复杂度]] connects 低秩近似之路 and 重温SSM via `generalizes` / `specializes`. Stable evidence is limited to low-rank skeleton selection and SSM/S4 diagonal-plus-low-rank Woodbury acceleration: `ev::10427::问题背景`, `ev::10662::基本定义`, `ev::10162::点睛之笔::dlr`.

**Key bridge**: [[方差消减技术]] (orthogonal linear transform to decouple noise variables) and [[Hybrid Window-Full Attention]] (decompose attention into local window + global full layers) — both separate a coupled system into independent components (noise variables ↔ attention layers), reducing the effective dimension of the problem.

**Tentative**: The connection between matrix skeleton selection and attention decomposition is structural (both decompose a high-dim object into structured sub-components) but lacks formula-level analogy.

### 5. Estimate / sample instead of compute (5 methods, 4 series)

**Shared generative move**: Replace an intractable sum, integral, or expectation with a tractable estimator or sampling scheme, then bound or correct the error.

| Series | Methods |
|--------|---------|
| 生成扩散模型漫谈 | [[最优方差估计]], [[码本选择法]] |
| 变分自编码器 | [[重要性加权估计]] |
| MoE环游记 | [[用分布估计近似滑动分位数]] |
| Transformer升级之路 | Equal Mean Randomized Position Training |

**Key bridge**: [[重要性加权估计]] (VAE: importance sampling for intractable marginal likelihood) and [[用分布估计近似滑动分位数]] (MoE: histogram EMA for non-incremental quantile) — both replace an exact computation with an empirical distribution estimate, then read the target quantity from the estimate.

**Key bridge**: [[最优方差估计]] (marginalizes x0 uncertainty for optimal variance) and [[码本选择法]] (importance sampling correction for codebook encoding) — both use a sampling-based correction to improve an approximate solution.

**Tentative**: Equal Mean Randomized Position Training uses randomized position sampling, which structurally matches the estimation pattern, but the application domain (training data augmentation) differs from the other methods (inference-time estimation).

### 6. Construct auxiliary sequence (4 methods, 4 series)

**Shared generative move**: Build an auxiliary sequence, variable, or function that bounds or interpolates the target, then optimize or analyze the auxiliary object instead.

| Series | Methods |
|--------|---------|
| 让炼丹更科学一些 | [[自上而下构造辅助序列]] |
| 变分自编码器 | [[BN防止KL消失]] |
| 生成扩散模型漫谈 | [[Cauchy-Schwarz不等式放缩]] |
| 矩阵优化 (topic) | [[用稳定性指标约束优化器缩放]] |

**Key bridge**: [[自上而下构造辅助序列]] (SGD: designs auxiliary weight sequence for stronger upper bound) and [[BN防止KL消失]] (VAE: uses BN statistics to construct positive KL lower bound) — both construct an auxiliary quantity (weight sequence ↔ BN statistics) that provides a bound on the target, then optimize through the auxiliary object.

**Verified bridge (Bridge Pass D+)**: [[Cauchy-Schwarz不等式放缩]] (diffusion/Wasserstein: constructs $\tilde{\mathcal{W}}_2$ as an upper bound, derives a differential inequality, then integrates it) and [[自上而下构造辅助序列]] (SGD: constructs $\boldsymbol{\psi}_t$ and weights $w_t$ to bound endpoint loss) — both construct an auxiliary bound object and analyze the target through that object. Evidence: `ev::9467::牛刀小试`, `ev::11540::最强结论`. Promoted graph edge status: `candidate/strong`.

**Key bridge**: [[Cauchy-Schwarz不等式放缩]] (uses inequality to construct Wasserstein upper bound) and [[用稳定性指标约束优化器缩放]] (uses stability indicators to derive norm constraints) — both derive bounds by introducing auxiliary inequality constraints.

### 7. Dual / constraint rewrite (3 methods, 2 series)

**Shared generative move**: Convert a constrained problem into an unconstrained one by introducing dual variables or penalty terms that absorb the constraint into the objective.

| Series | Methods |
|--------|---------|
| MoE环游记 | [[用对偶偏置改写路由约束]], [[用分位数求解负载均衡偏置]] |
| 变分自编码器 | [[高斯噪声正则化]] |

**Verified bridge (Bridge Pass D+)**: [[用对偶偏置改写路由约束]] (MoE: introduces Lagrangian multipliers / routing biases so equality-constrained assignment becomes shifted-score Top-k) and [[高斯噪声正则化]] (VAE: uses KL to penalize deviation from the standard-normal latent prior) — both absorb a constraint or prior requirement into the optimized expression. Evidence: `ev::11619::线性规划`, `ev::5253::分布标准化`. Promoted graph edge status: `candidate/strong`; not stable because the mechanisms are dual variable vs. KL penalty.

## Method-Layering Review Records

The following records track methods whose cross-series bridge evidence is still partial or whose hierarchy remains tentative. After the compliance pass, all 48 method nodes have at least one method-layering edge; records below are retained as caution notes, not as missing-edge records.

| Method | Operation type | Clustered with (cross-series) | Reason null |
|--------|---------------|-------------------------------|-------------|
| [[通过恒等式重写优化轨迹]] | rewrite | 恒等式蒸馏法, VAE联合分布最小化 | Bridge to 恒等式蒸馏法 verified in Pass D as formula-level identity rewriting; VAE connection remains tentative. |
| [[恒等式蒸馏法]] | rewrite | 通过恒等式重写优化轨迹, VAE联合分布最小化 | Bridge to 通过恒等式重写优化轨迹 verified in Pass D; other rewrite-cluster connections remain tentative. |
| [[估计-校正分解]] | rewrite | — | Probability identity decomposition; shares pattern with other identity-rewrite methods but applied specifically to diffusion reverse process. |
| [[ODE直接推导法]] | discrete↔continuous | 正交基投影推导状态动力学, 用变分法反推学习率 | All three derive continuous dynamics from discrete processes, but via different mechanisms (Jacobian+Taylor vs. orthogonal projection vs. Euler-Lagrange). |
| [[正交基投影推导状态动力学]] | discrete↔continuous | ODE直接推导法, 用变分法反推学习率 | See above. |
| [[用变分法反推学习率]] | discrete↔continuous | ODE直接推导法, Fokker-Planck方程推导法 | Continuous limit of discrete updates; structurally matches diffusion ODE derivation but via different mathematical route. |
| [[将矩阵近似问题化为骨架选择问题]] | decompose | 方差消减技术, HWFA | Decomposition type matches (selecting skeleton ≈ selecting window), but applied to matrices vs. attention layers. |
| [[方差消减技术]] | decompose | 将矩阵近似问题化为骨架选择问题 | Orthogonal transform to decouple noise vs. skeleton selection to decouple rows/columns. Structural match but different mathematical tools. |
| [[一致性蒸馏法]] | align | Positional Interpolation, 信噪比对齐调度迁移 | All three rescale by invariant, but different invariants (time consistency ↔ relative position ↔ SNR). |
| [[信噪比对齐调度迁移]] | align | Positional Interpolation, NTK-aware Scaled RoPE | Bridge to NTK-aware Scaled RoPE verified in Pass D as scale-from-invariant equation. PI remains tentative because it is direct compression, not constraint-derived alignment. |
| [[用对偶偏置改写路由约束]] | dual | 高斯噪声正则化 | Bridge to 高斯噪声正则化 verified in Bridge Pass D+ as candidate/strong; not stable because MoE uses Lagrangian dual variables while VAE uses KL penalty. |
| [[重要性加权估计]] | estimate | 用分布估计近似滑动分位数 | Both replace exact with empirical estimate but via different mechanisms (importance sampling ↔ histogram EMA). |
| [[Cauchy-Schwarz不等式放缩]] | auxiliary | BN防止KL消失, 自上而下构造辅助序列 | Bridge to 自上而下构造辅助序列 verified in Bridge Pass D+ as candidate/strong; BN connection remains tentative because the bounding tool differs. |
| (* no unlayered methods remain *) | — | — | Compliance pass added at least one method-layering edge to every method. Weak/tentative edges still require formula-level review before promotion. |

## Draft Evidence Triage (2026-06-10 Compliance Pass)

Draft cognitive pages that still lack direct evidence spans now carry `null_evidence_reason` in frontmatter. This records that the page is retained for navigation or later compilation, but must not be promoted until source-level `evidence_spans` are attached. This is intentionally weaker than upgrading status and avoids treating worker residue as stable knowledge.

## Pruned Method Nodes (2026-06-10 Bridge Pass D)

Coordinator review deleted the following duplicate or wrong-level graph method nodes after redirecting useful incident edges:

| Deleted node | Canonical target | Decision |
| --- | --- | --- |
| `method::Hybrid Window-Full Attention (HWFA)` | `method::Hybrid Window-Full Attention` | Duplicate abbreviation with no wiki page; canonical page already carries the method. |
| `method::Key归一化长度外推方法` | `method::Key归一化长度外推方法 (KeyNorm)` | Duplicate non-wiki node; canonical node matches the existing `wiki/methods/key-normalization.md` page title. |
| `method::Positional Interpolation (PI)` | `method::Positional Interpolation` | Duplicate abbreviation with no wiki page; canonical page already carries PI. |
| `method::InvLeaky ReRoPE逆用方法` | `method::Leaky ReRoPE分段线性外推方法` | Wrong-level node; current Leaky ReRoPE method page treats InvLeaky ReRoPE as a variant, not a standalone transferable method. |

No `Data/Spaces_ac_cn/` files or article summary pages were modified by this pruning pass.


## 2026-06-10 Learning-Rate Batch Size Bridge Notes

- New method `[[用平均场近似替代复杂期望计算]]` is classified as `estimate / sample instead of compute`; it has tentative bridge edges to `[[用期望消去采样依赖]]` because both reason through expectations, but one is approximate while the other is an exact expectation rewrite inside a convergence bound.
- New method `[[用等效Batch Size解释动量降噪]]` is classified as `align / calibrate by invariance`; it has a tentative bridge to `[[用稳定性指标约束优化器缩放]]` pending formula-level verification against the Muon/MuP scaling sources.
- No new high-level hub is promoted in this cycle; the new methods are source-backed but cross-series links remain tentative until Bridge Pass D.

## Bridge Candidate Clusters (2026-06-10 Dynamics + Manifold Batch)

### Discrete ↔ continuous bridge additions

- [[把优化算法解释为动力系统离散化]] joins the existing discrete-continuous cluster with [[ODE直接推导法]] and [[用变分法反推学习率]]. Formula-level evidence exists for optimizer-side GD→ODE (`ev::5655::GD与ODE`), but diffusion-side matching is only structural in this batch, so the new bridge is `candidate/strong` rather than stable.

### Dual / constraint rewrite additions

- [[用切空间投影改写约束最速下降]] adds a manifold-constraint branch to the dual/constraint cluster.
- [[用对偶目标求解约束更新系数]] shares a dual-variable move with [[用对偶偏置改写路由约束]]: constraints are moved into auxiliary variables that are updated by a derived objective or shifted score rule. Evidence: `ev::11388::对偶目标`, `ev::11619::线性规划`. Keep as `candidate/strong` because the mathematical mechanisms differ.

### Deferred method candidates

- 用不动点迭代求约束最速方向：supported by `11221` and `11241`, but retained as an implementation tactic under [[用切空间投影改写约束最速下降]] until more non-Muon examples appear.

## Bridge Candidate Clusters (2026-06-10 SVD Residual Batch)

- [[用矩阵分解重写表示学习结构]] joins the decompose/rewrite boundary: it factorizes representation structures for interpretation, while [[用结构分解降低计算复杂度]] factorizes structures for computation. Bridge is `candidate/strong`.
- [[用等效前向表达保留SVD梯度]] connects to [[用对偶目标求解约束更新系数]] through SVD/msign calculus. Bridge is `candidate/strong`, because one is an autograd rewrite and the other is a constrained optimizer update.

## Bridge Candidate Clusters (2026-06-10 MuP + Word Vector Batch)

- [[用稳定性指标约束优化器缩放]] ↔ [[用切空间投影改写约束最速下降]]: candidate/strong. Shared move: formulate the fastest useful update under a norm/stability constraint. Evidence: `ev::11605::最速下降`, `ev::11196::优化原理`.
- [[用互信息内积构造词向量几何]] ↔ [[用矩阵分解重写表示学习结构]]: candidate/strong. Shared move: rewrite representation learning as fitting or factorizing a matrix/Gram structure. Evidence: `ev::4671::模型形式`, `ev::4233::Word2VecSVD`.

Null records:

- No new high-level method hub was promoted for `用稳定性指标约束优化器缩放`; the existing method already covers the MuP continuation at the right abstraction level.

## Null layering-edge records (2026-06-10 Fermat + Feynman + Perturbation + Optimizer + Multimodal batches)

Methods without any generalizes/specializes/shares_pattern_with/is_example_of edge — none have a cross-series method at the same operation type with supporting formula-level evidence.

- **无穷下降法** (fermat, decompose): Pure number-theoretic descent technique with no ML analog. Cross-series match: null.
- **扩域求解丢番图方程** (fermat, structure-expose): Ring extension is algebraic number theory; no operation-type match in ML compiled methods. Cross-series match: null.
- **积分符号内取微分法** (feynman, rewrite): Feynman integration is calculus-specific; no ML method shares this generative move. Cross-series match: null.
- **用互信息发现句模版** (min-entropy): Series-local to minimum entropy principle. Cross-series match: null.
- **用层次编码最小化实现聚类** (min-entropy, decompose): Hierarchical encoding clustering is series-local. Cross-series match: null.
- **用局部归一化加速序列模型训练** (optimizer): Series-local to the optimizer deep-dive. Cross-series match: null.
- **Patchify** (multimodal, decompose): Image patching is domain-specific to multimodal vision. Cross-series match: null.
- **AR+Diffusion混合生成方法** (multimodal): Hybrid autoregressive diffusion generation is multimodal-specific. Cross-series match: null.
- **重要性采样** (text-search, estimate/sample): Belongs to the estimate/sample operation-type cluster internal to the sampling method hierarchy. Cross-series match: null.
- **拒绝采样** (text-search, estimate/sample): Same cluster as above. Cross-series match: null.


## Proposed Candidates from Batch: new-matrix-understanding

### 1. 用矩阵幂级数展开做近似求逆
- **Operation Type**: Rewrite / identity transform
- **Source ID**: `1765`
- **Evidence Span**: `ev::1765::代数方面的理解`
- **Description**: 将矩阵逆 $(I-A)^{-1}$ 展开为形式级数 $I+A+A^2+\dots$ 并做近似截断。
- **Cross-series match**: null

### 2. 用矩阵表示仿射坐标变换
- **Operation Type**: Rewrite / identity transform
- **Source ID**: `1768`
- **Evidence Span**: `ev::1768::几何理解`
- **Description**: 矩阵的列向量视为基向量，用 $y = Ax$ 描述点在不同坐标系下的度量。
- **Cross-series match**: null

### 3. 用公理化性质定义行列式
- **Operation Type**: Rewrite / identity transform
- **Source IDs**: `1770`, `2208`
- **Evidence Spans**: `ev::1770::公理化性质`, `ev::2208::严谨的公理化对应`
- **Description**: 通过列线性、交错重合两列为0和单位归一化性质，公理化唯一确立行列式映射及其有向体积本质。
- **Cross-series match**: null

### 4. 用相似矩阵表达同一线性变换
- **Operation Type**: Rewrite / identity transform
- **Source ID**: `1777`
- **Evidence Span**: `ev::1777::物理理解`
- **Description**: 相似矩阵 $B = P^{-1}AP$ 描述相同几何变换在不同仿射坐标系下的坐标测量值。
- **Cross-series match**: null

### 5. 通过概率生成函数求解离散概率矩
- **Operation Type**: Discrete ↔ continuous bridge
- **Source ID**: `2550`
- **Evidence Span**: `ev::2550::离散概率与母函数`
- **Description**: 离散变量分布写为幂级数，通过对数导数在 $z=1$ 处求值直接求解期望与方差。
- **Cross-series match**: null

### 6. 通过特征函数将连续概率卷积转化为乘积
- **Operation Type**: Discrete ↔ continuous bridge
- **Source IDs**: `2550`, `2573`
- **Evidence Span**: `ev::2550::连续概率与傅里叶变换`
- **Description**: 将概率密度进行傅里叶变换，把实域卷积转换为频域乘积。
- **Cross-series match**: null

### 7. 通过连续极限推导离散过程的极限分布
- **Operation Type**: Discrete ↔ continuous bridge
- **Source ID**: `2573`
- **Evidence Span**: `ev::2573::连续极限与正态分布`
- **Description**: 引入 $\Delta t$ 与 $\Delta s$ 极限，在 $\Delta s^2 = \alpha \Delta t$ 标度下逼近特征函数极限得到连续分布 PDF。
- **Cross-series match**: null

### 8. 用路径积分表示随机过程转移概率
- **Operation Type**: Discrete ↔ continuous bridge
- **Source ID**: `2609`
- **Evidence Span**: `ev::2609::随机游走路径积分`
- **Description**: 时空网格细分，将高斯步转移乘积在连续极限下写为路径指数积分形式。
- **Cross-series match**: null

### 9. 通过母函数做分布极限近似
- **Operation Type**: Discrete ↔ continuous bridge
- **Source ID**: `3188`
- **Evidence Span**: `ev::3188::泊松分布推导`
- **Description**: 在期望恒定条件下，将二项母函数在 $n \to \infty$ 下极限逼近为泊松指数母函数，极大地简化了概率分布极限的证明。
- **Cross-series match**: null


## Bridge Candidate Clusters (2026-06-11 GAN + Attention Topic Batch)

| Cluster | Operation type | Evidence | Decision |
| --- | --- | --- | --- |
| [[用对偶散度构造对抗生成目标]] ↔ [[VAE联合分布最小化]] | Dual / constraint rewrite / distribution discrepancy | `ev::6163::对偶散度定义`, `ev::5343::直面联合分布` | candidate: shared distribution-discrepancy construction, but adversarial min-max and direct joint KL remain different mechanisms. |
| [[用结构约束线性化Attention计算]] ↔ [[用结构分解降低计算复杂度]] | Decompose / reduce dimension | `ev::8180::三矩阵近似`, `ev::10662::基本定义` | candidate: Nyströmformer is a source-backed Attention specialization of structural computation reduction. |
| [[Attention-E熵不变性缩放]] ↔ [[NTK-aware Scaled RoPE]] | Align / calibrate by invariance | `ev::8823::熵不变性缩放`, `ev::9675::进制类比` | candidate: both solve scale from length/extrapolation invariance; keep below stable pending a dedicated formula-level review tying the exact invariants. |
| [[用对偶散度构造对抗生成目标]] ↔ diffusion GAN/WGAN-GP sources | Discrete-continuous / distribution flow | `ev::6139::WGAN-div训练`, `ev::9668::WGAN-GP` | tentative: related through WGAN-GP and generative distribution transport, but source-level operation differs. |

## Method Layer Defer Records (2026-06-11 Quality Repair)

These records close the 2026-06-11 method-layer repair pass without inventing unsupported edges or pages. A method listed here is allowed to remain draft/candidate only because the missing contract is explicit.

| method_id | missing_contract | reason | next_action |
| --- | --- | --- | --- |
| `method::AR+Diffusion混合生成方法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::BERT-of-Theseus` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::BIO Copy机制` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::BytePiece` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::CAN后处理` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::DiVeQ无辅助损失量化训练法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::DropToken` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::Dropout` | belongs_to | no article series/topic provenance resolved | bind to source-backed series/topic or keep deferred |
| `method::EAE` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::EMO损失函数` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::GatedDeltaNet` | operation_types, belongs_to, wiki_path | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved; shadow method node without canonical page | classify from source before promotion; bind to source-backed series/topic or keep deferred; create minimal source-backed page only if reused |
| `method::GlobalPointer` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::IGN` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::IMLE` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::JensenExponential极值估计` | wiki_path | shadow method node without canonical page | create minimal source-backed page only if reused |
| `method::Jensen不等式放缩` | operation_types, belongs_to, wiki_path | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved; shadow method node without canonical page | classify from source before promotion; bind to source-backed series/topic or keep deferred; create minimal source-backed page only if reused |
| `method::Keras侵入式优化器注入法` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::Keras分层学习率包装法` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::Keras权重滑动平均注入法` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::Keras梯度累积优化器` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::MesaNet解析解序列建模` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::MuonClip优化方法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::O-GAN` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::Patchify` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Perturbed Masking` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::QK-Clip权重裁剪法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Residual Connection` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::RoPE-Tie` | operation_types, wiki_path | no matched method page operation_types or source-backed classification; shadow method node without canonical page | classify from source before promotion; create minimal source-backed page only if reused |
| `method::SPACES摘要模型` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Short-Conv键值异源化` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Sparse Softmax` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::TTT框架构建RNN` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Token Healing` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Update RMS 对齐法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::VQ旋转技巧` | wiki_path | shadow method node without canonical page | create minimal source-backed page only if reused |
| `method::Viterbi Sampling` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Viterbi完美采样` | wiki_path | shadow method node without canonical page | create minimal source-backed page only if reused |
| `method::WGAN` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::WMD文本相似度计算` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::WRD文本相似度计算` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::cascading-rejection` | operation_types, belongs_to, layering, wiki_path | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; bind to source-backed series/topic or keep deferred; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::denoising-score-matching` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::designing-gans` | operation_types, belongs_to, layering, wiki_path | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; bind to source-backed series/topic or keep deferred; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::f-GAN` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::gradient-normalization` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::以复指数为纽带将泰勒级数转化为傅里叶级数` | operation_types, belongs_to, layering | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | classify from source before promotion; bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::参数变换微扰法` | operation_types | no matched method page operation_types or source-backed classification | classify from source before promotion |
| `method::噪声对比估计` | wiki_path | shadow method node without canonical page | create minimal source-backed page only if reused |
| `method::基于MLM的非自回归阅读理解问答` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::基于差分峰值的楼层切分聚类` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::外微分计算黎曼曲率` | operation_types, layering | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass | classify from source before promotion; review within operation-type cluster |
| `method::多Gram哈希路由法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::多篇章投票Beam Search解码算法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::奇异矩阵的对角微扰化简法` | operation_types, belongs_to | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved | classify from source before promotion; bind to source-backed series/topic or keep deferred |
| `method::容斥原理求概率` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::局部全局混合拟合法` | operation_types, belongs_to, layering | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | classify from source before promotion; bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::局部拟合` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::平均场优化器动力学分析法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::平面二次曲线的复数坐标代换化简法` | operation_types, belongs_to | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved | classify from source before promotion; bind to source-backed series/topic or keep deferred |
| `method::扩域求解丢番图方程` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::拉普拉斯近似` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::拒绝采样` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::指数系数变易摄动法` | operation_types, belongs_to, wiki_path | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved; shadow method node without canonical page | classify from source before promotion; bind to source-backed series/topic or keep deferred; create minimal source-backed page only if reused |
| `method::摄动级数展开法` | operation_types | no matched method page operation_types or source-backed classification | classify from source before promotion |
| `method::方差无偏估计校正` | wiki_path | shadow method node without canonical page | create minimal source-backed page only if reused |
| `method::旋转技巧STE` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::无穷下降法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::无穷范数求导` | operation_types, belongs_to, wiki_path | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved; shadow method node without canonical page | classify from source before promotion; bind to source-backed series/topic or keep deferred; create minimal source-backed page only if reused |
| `method::条件LayerNorm多任务学习` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::活动正交标架度规分解法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::测试函数法` | operation_types | no matched method page operation_types or source-backed classification | classify from source before promotion |
| `method::特征线法` | operation_types, layering | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass | classify from source before promotion; review within operation-type cluster |
| `method::狄拉克函数光滑近似法` | operation_types, layering | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass | classify from source before promotion; review within operation-type cluster |
| `method::用AI Agent翻译编译LaTeX论文` | layering, wiki_path | no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用AM-Softmax做句子相似度` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用Householder变换构造向量变换的正交矩阵` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用Metadata嵌入和Translator适配Zotero` | layering, wiki_path | no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用Monarch分解实现结构化矩阵近似` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用Seq2Seq+Attention生成标题` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用TF-IDF关键词检索相关论文` | layering, wiki_path | no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用mcsgn分块恒等计算矩阵平方根` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用mcsgn解代数Riccati方程` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用tantivy搭建轻量级全文检索系统` | layering, wiki_path | no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用上下文管理器和迭代器优化重试模式` | layering, wiki_path | no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用互信息发现句模版` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用互信息发现词语边界` | operation_types, wiki_path | no matched method page operation_types or source-backed classification; shadow method node without canonical page | classify from source before promotion; create minimal source-backed page only if reused |
| `method::用伪逆投影优化LoRA更新` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用伴随矩阵计算逆矩阵元素` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用修正交叉熵聚焦难分样本` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用公理化性质定义行列式` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::用分块矩阵变换推导矩阵恒等式` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用分块递归加速结构化矩阵求逆` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用变分推断统一生成模型` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用多优先级队列管理爬取和对话任务` | layering, wiki_path | no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用奇异值分布度量矩阵本质维度` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用奇异值裁剪近似谱归一化` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用局部归一化加速序列模型训练` | belongs_to, layering | no article series/topic provenance resolved; no evidence-backed same-operation neighbor selected in this pass | bind to source-backed series/topic or keep deferred; review within operation-type cluster |
| `method::用层次编码最小化实现聚类` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用幂迭代估计谱范数梯度` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用平均场近似替代复杂期望计算` | operation_types | no matched method page operation_types or source-backed classification | classify from source before promotion |
| `method::用数值稳定性分析推导非对称学习率` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用数学归纳法证明矩阵性质` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用条件Normalization融合外部条件` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用标量迭代优化确定迭代系数` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用梯度SVD初始化LoRA` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用测试函数定义与运算广义函数` | operation_types, belongs_to | no matched method page operation_types or source-backed classification; no article series/topic provenance resolved | classify from source before promotion; bind to source-backed series/topic or keep deferred |
| `method::用矩阵幂级数展开做近似求逆` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::用矩阵恒等式重写奇异值操作` | operation_types | no matched method page operation_types or source-backed classification | classify from source before promotion |
| `method::用秩1近似构造谱权重衰减` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用等效Batch Size解释动量降噪` | operation_types | no matched method page operation_types or source-backed classification | classify from source before promotion |
| `method::用线性递归技巧计算G·P^{-1/2}` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用缓存变量实现三角低秩矩阵的线性递归求逆` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用语言模型预训练做半监督学习` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用谱条件推导模型缩放规律` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用路径积分表示随机过程转移概率` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::用迭代格式推广矩阵方根计算` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用迭代逼近替代矩阵分解` | operation_types | no matched method page operation_types or source-backed classification | classify from source before promotion |
| `method::用重定向扩展实现曲线救国搜索` | layering, wiki_path | no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用预训练补充Transformer归纳偏置` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::用高维数组变换推导矩阵恒等式` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::矩阵分块递归求逆` | operation_types, layering, wiki_path | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass; shadow method node without canonical page | classify from source before promotion; review within operation-type cluster; create minimal source-backed page only if reused |
| `method::积分估计极值原理` | wiki_path | shadow method node without canonical page | create minimal source-backed page only if reused |
| `method::积分符号内取微分法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::算子分解法` | operation_types, layering | no matched method page operation_types or source-backed classification; no evidence-backed same-operation neighbor selected in this pass | classify from source before promotion; review within operation-type cluster |
| `method::素数积加一构造法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::线性Attention中的遗忘门` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::网页标准模板比对法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::贪心负载均衡表生成法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::通过连续极限推导离散过程的极限分布` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::采样优化统一视角` | wiki_path | shadow method node without canonical page | create minimal source-backed page only if reused |
| `method::采样定理重建` | wiki_path | shadow method node without canonical page | create minimal source-backed page only if reused |
| `method::随机Softmax损失函数优化` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::R-Drop` | examples | resolved unmatched status, examples deferred | review within operation-type cluster |
| `method::Integrated Gradients` | examples, layering | resolved unmatched status, examples and layering deferred | review within operation-type cluster |


### Deferred Method Shadows

| Method ID | Target | Status | Reason | Date |
| --- | --- | --- | --- | --- |
| method::VQ旋转技巧 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::Viterbi完美采样 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::采样定理重建 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::JensenExponential极值估计 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::方差无偏估计校正 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::积分估计极值原理 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::采样优化统一视角 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::RoPE-Tie | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::cascading-rejection | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::designing-gans | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::GatedDeltaNet | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::Jensen不等式放缩 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::指数系数变易摄动法 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::无穷范数求导 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::BERT-of-Theseus | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::BytePiece | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::DropToken | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::Dropout | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::EAE | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::IGN | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::IMLE | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::Keras侵入式优化器注入法 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::Keras分层学习率包装法 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::Keras权重滑动平均注入法 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::Keras梯度累积优化器 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::O-GAN | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::Residual Connection | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::WGAN | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::denoising-score-matching | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::f-GAN | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::gradient-normalization | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::以复指数为纽带将泰勒级数转化为傅里叶级数 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::奇异矩阵的对角微扰化简法 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::局部全局混合拟合法 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::平面二次曲线的复数坐标代换化简法 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::用局部归一化加速序列模型训练 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |
| method::用测试函数定义与运算广义函数 | belongs_to | deferred | No series/topic membership found for source articles. Pending source review. | 2026-06-12 |


| `method::EM路由算法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::用RNN解ODE并估计参数法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::基于热传导方程的特征预测法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::显式可逆矩阵构造法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::带参求导构造ODE证明法` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Center Loss` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Deep INFOMAX无监督学习` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Flooding训练策略` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::GLU激活函数` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::GPT背棋谱下棋` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Keras多GPU训练` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Keras层重用` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Keras自定义Loss模式` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Keras重计算` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Label Smoothing` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Logit Adjustment Loss` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Numpy Apriori` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::ON-LSTM有序神经元` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::Python多进程` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::RNN输入重要性评估` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::T5.1.1 GEGLU FFN` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::TeaForN训练策略` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::WoBERT词级预训练` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::ZLPR多标签损失函数` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::synthesizer_static_attention` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::交叉熵准确率分析` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::传递聚类` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::判别器采样` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::大文件打乱` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::门控残差CNN` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
| `method::矩阵Capsule` | layering | no evidence-backed same-operation neighbor selected in this pass | review within operation-type cluster |
