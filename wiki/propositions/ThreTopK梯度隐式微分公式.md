---
type: proposition
title: ThreTopK梯度隐式微分公式
statement: "对于ThreTopK的待定阈值lambda(x)，有偏导数梯度为 rac{\partial\lambda(oldsymbol{x})}{\partial x_j} = rac{\sigma'(x_j - \lambda(oldsymbol{x}))}{\sum\limits_{i=1}^n \sigma'(x_i - \lambda(oldsymbol{x}))}"
assumptions:
  - sigmoid(x)光滑且导数非负
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md
source_ids:
  - 10373
proof_route: 对约束和式两边求xj偏导，利用链式法则解出偏导数项。
status: draft
updated: 2026-06-11
---

# ThreTopK梯度隐式微分公式

解决了无法直接求导出的反向传播梯度流问题，使ThreTopK可以自定义前向与后向图实现端到端训练。
