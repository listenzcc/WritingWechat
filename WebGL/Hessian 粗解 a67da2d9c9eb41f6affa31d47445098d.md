# Hessian 粗解

Newton 法是一种迭代优化算法，用于求解非线性优化问题。它利用目标函数的二阶导数信息（Hessian 矩阵）来进行迭代，以更快地收敛到局部最小值。尽管 Newton 法在很多情况下具有快速收敛的特性，但也存在一些问题，其中之一是它的稳定性可能较差，也更容易陷入鞍点。

本文将其与梯度方法进行平行对比，开源代码可见我的 ObservableHQ 笔记本

[Searching maximum by Hessian](https://observablehq.com/@listenzcc/searching-maximum-by-hessian)

---
- [Hessian 粗解](#hessian-粗解)
  - [二元函数的泰勒分解](#二元函数的泰勒分解)
  - [Hessian 矩阵](#hessian-矩阵)
  - [Newton 法潜在的不稳定性](#newton-法潜在的不稳定性)


## 二元函数的泰勒分解

考虑二元函数，将它的两个自变量写成向量的形式

$$
\begin{cases}
f(z) = f(x, y)\\
z = \begin{bmatrix} x\\y \end{bmatrix}
\end{cases}
$$

当该函数及其高阶导数连续时，可以表示成如下形式

$$
f(z) \approx f(z_0) + (z - z_0)^Tg(z_0) + \frac{1}{2}(z-z_0)^TH(z_0)(x-x_0) + \cdots
$$

其中，$g, H$ 分别代表一、二阶导数对应的向量和矩阵，分别是梯度向量和 Hessian 矩阵

$$
g(z) = i \cdot \frac{\partial f}{\partial x} + j \cdot \frac{\partial f}{\partial y} = \begin{bmatrix} f_x \\ f_y \end{bmatrix}
$$

## Hessian 矩阵

Hessian 矩阵是二阶偏导数组成的 $2 \times 2$ 矩阵

$$
H(z) = \begin{bmatrix}
f_{xx} &f_{xy} \\
f_{yx} &f_{yy}
\end{bmatrix}
$$

[Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix)

因此，原二元函数转换成矩阵方程，对其求导可得 $g(z) = \frac{d}{dz}f(z)$

$$
g(z) \approx g(z_0) + H(z_0)(z-z_0)
$$

令 $g(\hat{z})=\vec 0$，则有

$$
\hat{z} \approx z_0 - H^{-1}(z_0) \cdot g(z_0)
$$

当 Hessian 矩阵为正定矩阵时该处的二阶导数始终为正，由二阶导数的性质可知，此时偏导数为零的点是函数的局部极小值点。具体来说，当 Hessian 矩阵是正定矩阵时，这意味着对于任何非零向量 $v$，都有 $v^T H v > 0$，其中 $H$ 是 Hessian 矩阵。正定矩阵的这个性质确保了函数的二次型在该点是严格的下凹的，因此该点是一个局部极小值点。二阶偏导数的正定性与局部极小值的关系是由二次型的性质决定的。如果一个函数的二次型是正定的，那么函数在该点附近的局部极小值就是由于对应的二阶偏导数都为正。总的来说，Hessian 矩阵为正定矩阵是一个在优化问题中常见的条件，因为它确保了对应的点是一个局部极小值。

因此，这是通过二阶导数寻找极小值点的高效迭代方法，这种方法称为 Newton 法。

[Newton&#039;s method in optimization](https://en.wikipedia.org/wiki/Newton's_method_in_optimization)

## Newton 法潜在的不稳定性

下图中灰色较大的方框代表梯度方法寻找到的极小值点，而白色较小的方框代表 Newton 法寻找到的极小值点。从下图中可见，虽然 Newton 法找到了左下角的极小值点，但该方法却显得更加不稳定。

![Untitled](Hessian%20%E7%B2%97%E8%A7%A3%20a67da2d9c9eb41f6affa31d47445098d/Untitled.png)

![20231112-171228.gif](Hessian%20%E7%B2%97%E8%A7%A3%20a67da2d9c9eb41f6affa31d47445098d/20231112-171228.gif)

Newton 法是一种迭代优化算法，用于求解非线性优化问题。它利用目标函数的二阶导数信息（Hessian 矩阵）来进行迭代，以更快地收敛到局部最小值。尽管 Newton 法在很多情况下具有快速收敛的特性，但也存在一些问题，其中之一是它的稳定性可能较差，特别是在一些特殊情况下。

以下是 Newton 法可能面临的一些稳定性问题：

1. **初始点选择：** Newton 法对初始点的选择敏感。如果选择的初始点距离最优解太远，可能导致迭代过程无法收敛，或者收敛到非理想的局部最小值。
2. **Hessian 矩阵的计算：** 在某些情况下，计算 Hessian 矩阵可能是数值上不稳定的，特别是在函数具有奇异点或者 Hessian 矩阵接近奇异的地方。
3. **二阶导数为零：** 如果在某个迭代步骤中 Hessian 矩阵退化为零矩阵，算法可能无法继续进行。这通常发生在函数的某些方向上的曲率非常小的地方。
4. **高维问题：** 在高维问题中，计算和存储 Hessian 矩阵可能非常昂贵，并且容易导致数值不稳定性。使用近似的 Hessian 矩阵或者其他变种可能是一种解决方法。

为了解决 Newton 法的稳定性问题，人们通常会采用改进的算法，例如拟牛顿法（Quasi-Newton methods）或者共轭梯度法（Conjugate Gradient methods）。这些方法在一些情况下能够继承 Newton 法的快速收敛性，同时减轻了稳定性方面的一些问题。

另外，Newton 法也更容易陷入鞍点，而不是极值点。Newton 法容易受到鞍点的影响。鞍点是目标函数在某些方向上是局部最小值而在其他方向上是局部最大值的点，因此梯度为零但 Hessian 矩阵包含正负特征值的情况。下图中黑色位置就对应鞍点。

![Untitled](Hessian%20%E7%B2%97%E8%A7%A3%20a67da2d9c9eb41f6affa31d47445098d/Untitled%201.png)

![Untitled](Hessian%20%E7%B2%97%E8%A7%A3%20a67da2d9c9eb41f6affa31d47445098d/Untitled%202.png)

在鞍点附近，Newton 法的二次逼近可能会导致算法在沿着负特征值的方向上朝着局部最大值移动，而在正特征值的方向上朝着局部最小值移动，从而导致迭代在鞍点附近徘徊而难以收敛。这是因为在鞍点处，Hessian 矩阵的特征值可能有正有负，使得二次逼近在不同方向上的行为截然不同。

为了克服这个问题，一些改进的优化算法采用了预处理的方法，或者使用了一些正则化手段来调整 Hessian 矩阵，以减轻在鞍点附近的振荡。共轭梯度法和一些拟牛顿法的变种是一些相对较好的选择，因为它们在一定程度上可以绕过鞍点问题。