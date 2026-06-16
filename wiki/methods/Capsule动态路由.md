---
type: method
title: "Capsule动态路由"
aliases:
  - "Dynamic Routing"
operation_types:
  primary: "Structure-expose by factorization"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-01-23-揭开迷雾-来一顿美味的Capsule盛宴.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-02-12-再来一顿贺岁宴-从K-Means到Capsule.md
source_ids:
  - "4819"
  - "5112"
method_summary: "Hinton提出的迭代式路由算法：底层胶囊通过内积计算与高层胶囊的相似度，加权传递信息。"
typical_structure: |
  1. 底层胶囊u_i通过内积计算与v_j的相似度
  2. softmax得到耦合系数c_ij
  3. 加权求和后用squash激活
  4. 迭代更新v_j
applicability: "图像识别中的姿态建模，NLP中的层次特征组合"
tools:
  - Squash函数
  - 内积相似度
  - 迭代路由
related_methods: []
examples:
  - [[article::4819]]
  - [[article::5112]]
status: draft
updated: 2026-06-13
---

## 适用问题

需要层次化特征表示的视觉或NLP任务，特别是特征间存在明确组合关系（如"部件→物体"、"字→词→句"）的场景。Capsule网络通过动态路由实现特征间的聚类组合。

## 核心变换

**输入**：底层胶囊向量集合 $\{\boldsymbol{u}_i\}_{i=1}^n$（每个$\boldsymbol{u}_i$表示一个底层特征）
**输出**：高层胶囊向量集合 $\{\boldsymbol{v}_j\}_{j=1}^k$（每个$\boldsymbol{v}_j$表示一个组合后的高层特征）

动态路由迭代更新耦合系数和胶囊输出：
$$
c_{ij} = \text{softmax}_j(\langle \boldsymbol{u}_i, \boldsymbol{v}_j \rangle), \quad
\boldsymbol{s}_j = \sum_i c_{ij} \boldsymbol{u}_i, \quad
\boldsymbol{v}_j = \text{squash}(\boldsymbol{s}_j) = \frac{\|\boldsymbol{s}_j\|^2}{1+\|\boldsymbol{s}_j\|^2} \frac{\boldsymbol{s}_j}{\|\boldsymbol{s}_j\|}
$$

## 典型步骤

1. **初始化**：底层胶囊$\boldsymbol{u}_i$通过变换矩阵$W_{ij}$映射到高层胶囊的"预测向量"$\hat{\boldsymbol{u}}_{j|i}=W_{ij}\boldsymbol{u}_i$
2. **计算相似度**：底层胶囊$\hat{\boldsymbol{u}}_{j|i}$与各高层胶囊$\boldsymbol{v}_j$做内积$e^{\langle \hat{\boldsymbol{u}}_{j|i}, \boldsymbol{v}_j \rangle}$
3. **Softmax归一化**：得到耦合系数$c_{ij} = \text{softmax}_j(\langle \hat{\boldsymbol{u}}_{j|i}, \boldsymbol{v}_j \rangle)$
4. **加权求和**：$\boldsymbol{s}_j = \sum_i c_{ij} \hat{\boldsymbol{u}}_{j|i}$
5. **Squash激活**：$\boldsymbol{v}_j = \text{squash}(\boldsymbol{s}_j)$，将模长压缩到$(0,1)$
6. **迭代**：重复步骤2-5共3次（实验表明3次即可收敛）

## 直觉

**从K-Means视角**：高层胶囊$\boldsymbol{v}_j$本质上是底层胶囊$\boldsymbol{u}_i$的聚类中心。耦合系数$c_{ij}$相当于"软分配"——每个底层胶囊以不同权重分配到各高层胶囊。动态路由就是迭代求解这一软聚类分配的过程。

**从特征组合视角**：底层特征（如"羽毛"）通过内积判断自己属于哪个上层特征（如"鸡"、"鸭"、"鱼"、"狗"），然后将自身按比例传递给各上层特征。上层特征聚合所有底层输入，形成更抽象的特征表示。

Squash函数将模长压缩到$(0,1)$，使胶囊的模长代表该特征出现的"显著程度"（概率的替代度量）。

## 边界

- 动态路由迭代不依赖梯度下降（仅使用前向迭代），但整体网络仍需反向传播训练其他参数
- 迭代次数为3时性能最佳，更多迭代可能过拟合
- Squash函数的形式不是唯一的，实验中将分母1改为0.5有时效果更好
- Capsule的计算效率低于标准CNN/RNN，限制了大规模应用
- 需要精心设计网络结构以发挥胶囊的优势，简单替换标准层不一定有效

## 例子

- MNIST数字识别：CapsuleNet在重叠数字识别上优于CNN，能利用"部件间姿态关系"区分重叠数字
- 从K-Means到Capsule的理论对应：软化的K-Means loss $L \approx -\frac{1}{K}\sum_i \ln(\sum_j e^{-K\cdot d(\boldsymbol{u}_i, \boldsymbol{v}_j)})$ 的梯度形式正好导出动态路由更新公式

## 证据

- ev::4819::动态路由算法：内积相似度→softmax耦合系数→加权求和→squash激活的完整迭代过程
- ev::4819::Squash函数：$\text{squash}(\boldsymbol{x}) = \frac{\|\boldsymbol{x}\|^2}{1+\|\boldsymbol{x}\|^2} \frac{\boldsymbol{x}}{\|\boldsymbol{x}\|}$ 将模长压缩到(0,1)
- ev::5112::K-Means视角：胶囊输出是输入的聚类结果，动态路由是迭代求解聚类中心
- ev::5112::特征间聚类：Capsule对输入特征向量做聚类（而非样本间聚类），层层递进完成抽象
