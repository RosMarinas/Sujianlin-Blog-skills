---
type: formula
title: ReLU-GeLU-Swish恒等式
aliases:
- Activation Function Identity
latex: x = f(x) - f(-x)
symbol_meanings:
  \phi(x): 奇函数
standard_notation: x = f(x) - f(-x) \quad \text{where} \quad f(x) = \frac{1}{2}(\phi(x)
  + 1)x, \ \phi(-x) = -\phi(x)
conditions: 激活函数 $f(x)$ 满足对应的特征方程，且 $\phi(x)$ 是严格的奇函数。例如对于 ReLU、GeLU 和 Swish 激活函数该等式恒成立。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-08-16-ReLU-GeLU-Swish的一个恒等式.md
source_ids:
- '11233'
appears_in:
- '[[spaces-11233-ReLU-GeLU-Swish的一个恒等式]]'
status: draft
null_evidence_reason: Initial compilation draft
updated: "2026-06-14"
---

## 概述

该公式指出了 ReLU、GeLU、Swish 等主流神经网络激活函数的一个普适恒等关系。

对于这些函数，均可找到一个奇函数 $\phi(x)$，使得激活函数写成 $f(x) = \frac{1}{2}(\phi(x) + 1)x$：
- **ReLU**：$\phi(x) = \text{sign}(x)$
- **Swish**：$\phi(x) = \tanh(x/2)$
- **GeLU**：$\phi(x) = \text{erf}(x/\sqrt{2})$

由于 $\phi(x)$ 是奇函数，代入展开即可轻松证明：

$$f(x) - f(-x) = \frac{1}{2}(\phi(x) + 1)x - \frac{1}{2}(\phi(-x) + 1)(-x) = \frac{1}{2}(\phi(x) + 1)x + \frac{1}{2}(-\phi(x) + 1)x = x$$

该恒等式意味着，两层神经网络可通过权重对齐直接实现恒等映射：

$$x = f(x) - f(-x) = f\left(\begin{bmatrix}x & -x\end{bmatrix}\right)\begin{bmatrix}1 \\ -1\end{bmatrix}$$

这使得网络具备自适应调节深度的潜能。