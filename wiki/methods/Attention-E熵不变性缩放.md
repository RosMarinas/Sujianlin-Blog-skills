---
type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: Attention-E熵不变性缩放方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-12-21-从熵不变性看Attention的Scale操作.md
source_ids:
  - 8823
method_summary: "用随序列长度增长的对数缩放因子替换标准 Attention scale，使注意力分布熵对长度变化更不敏感并改善长度外推。"
typical_structure: |
  1. 获取输入序列长度 n。
  2. 计算调整后的缩放因子：\kappa * log(n) / d 或 log_{512}(n) / \sqrt{d}。
  3. 将注意力得分矩阵 QK^T 乘以该缩放因子。
  4. 应用 Softmax 操作得到注意力分布。
applicability: "在基于 Attention 机制的模型中，需要使注意力分布具有长度外推泛化能力（能在超出训练长度的序列上表现良好）时。"
examples:
  - "[[article::8823]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8823::为了使得模型结果能够更好地泛化到未知长度，Attention机制的设计应该使得 a_{i,j} 尽量具备熵不变性。... 从而得出 \\lambda = \\log n / (0.24 d)，引入超参数 \\kappa 后得到 \\frac{\\kappa\\log n}{d}。"
---

# Attention-E熵不变性缩放方法

## 适用问题
如何调整注意力机制的 Scale 操作，以缓解当输入序列长度变长时，注意力过度分散（熵增大）的问题，从而提升模型的长度外推性能？

## 核心变换
将标准的缩放因子 $1/\sqrt{d}$ 替换为与输入序列长度 $n$ 相关的缩放因子：
$$ softmax\left(\frac{\kappa \log n}{d}QK^{\top}\right)V $$
或等价的简化版本：
$$ softmax\left(\frac{\log_{512} n}{\sqrt{d}}QK^{\top}\right)V $$
从而使得注意力的熵对序列长度不敏感。

## 典型步骤
1. 获取输入序列长度 n。
2. 计算调整后的缩放因子：\kappa * log(n) / d 或 log_{512}(n) / \sqrt{d}。
3. 将注意力得分矩阵 QK^T 乘以该缩放因子。
4. 应用 Softmax 操作得到注意力分布。

## 直觉
当序列长度变长时，由于要分配给更多 token 注意力，注意力分布的熵会天然增加，这意味着模型会难以“聚焦”到少数重要的 token 上。引入 $\log n$ 的缩放能够恰好抵消增加的 token 数量带来的熵增，使注意力的聚焦程度对序列长度保持一种“不变性”。

## 边界
这种熵不变性推导基于一系列近似假设（比如 $K$ 向量均匀分布在超球面上），并非严格的等式。此外，虽然理论上 $\log n$ 可以避免由于长度剧增造成的注意力分散，但如果 $n$ 过大，缩放因子也可能导致梯度消失问题。

## 例子
训练时模型固定长度为 512，我们将缩放因子设为 $\frac{\log_{512} n}{\sqrt{d}}$，当测试长度为 64 时，缩放因子变小，测试长度外推到 1024 时，缩放因子变大，实验表明在 RoFormer small 等模型中 MLM 的外推准确率得到显著提升。

## 证据
- 8823 提到，根据熵不变性可以得出 $\lambda = \frac{\kappa\log n}{d}$，并推导出 $Attention(Q,K,V) = softmax\left(\frac{\log_{512} n}{\sqrt{d}}QK^{\top}\right)V$，实验验证外推效果好。
