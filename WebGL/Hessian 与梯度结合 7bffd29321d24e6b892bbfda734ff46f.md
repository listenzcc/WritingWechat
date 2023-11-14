# Hessian 与梯度结合

本文讲述了利用 Hessian 提供的二阶信息确定梯度下降最优步长的方法，这种梯度下降法只进行了 10 次迭代即可找到极小值，这说明该方法大大提高了寻优效率，并且有机会跳出局部最优值，受起始点影响更小。

本文代码还是在我的 ObservableHQ 笔记本上。

[Searching maximum by Hessian (Improve)](https://observablehq.com/@listenzcc/searching-maximum-by-hessian-improve)

---
- [Hessian 与梯度结合](#hessian-与梯度结合)
  - [起点](#起点)
  - [最高效的梯度下降](#最高效的梯度下降)
  - [寻优实例](#寻优实例)
  - [附录：优化问题的问题小结](#附录优化问题的问题小结)


## 起点

前文已经将标量场表示成二元函数，并且这个二元函数可以表示成向量的形式

$$
\begin{cases}
f(z) = f(x, y)\\
z = \begin{bmatrix} x\\y \end{bmatrix}
\end{cases}
$$

它在某个点 $z_0$ 的一阶偏导数和二阶偏导数矩阵分别为梯度向量

$$
g(z) = \begin{bmatrix} f_x \\ f_y \end{bmatrix}
$$

和 Hessian 矩阵

$$
H(z) = \begin{bmatrix}
f_{xx} &f_{xy} \\
f_{yx} &f_{yy}
\end{bmatrix}
$$

因此，它的泰勒展开如下式

$$
f(z) \approx f(z_0) + (z - z_0)^Tg(z_0) + \frac{1}{2}(z-z_0)^TH(z_0)(z-z_0) + \cdots
$$

这是寻优方法推导的起点。

## 最高效的梯度下降

从这个起点开始，我已经分别涉及了梯度下降和 Newton 法，它们都可以用于找到连续保守场的极值小点。其中，梯度下降法可以表示为迭代过程

$$
z_{k+1} = z_k - \alpha \cdot g(z_k)
$$

其中，$k \in [1, 2, \dots]$$k$$\alpha \in \mathbb{R}^+$ 代表梯度下降的学习率，而 Newton 法的迭代过程不需要学习率的参与

$$
z_{k+1} \approx z_k - H^{-1}(z_k) \cdot g(z_k)
$$

稍加分析并结合之前的可视化结果可以看到，梯度下降法的学习率具有任意性，并且效率不高；而 Newton 法却面临不稳定的问题，造成这种问题的原因是实验场景中的标量场并不服从简单的二次型分布，这导致泰勒分解的二次函数与真实值差异过大，导致结果难以收敛。

[Searching maximum by gradient ascending](https://observablehq.com/@listenzcc/searching-maximum-by-gradient-ascending)

[Searching maximum by Hessian](https://observablehq.com/@listenzcc/searching-maximum-by-hessian)

为了解决以上问题，一个可行的思路是从二阶偏导数中找到一些信息，用于指导学习率的选择，目标是沿着梯度方向进行更新时，更新的步长达到最优。

![Untitled](Hessian%20%E4%B8%8E%E6%A2%AF%E5%BA%A6%E7%BB%93%E5%90%88%207bffd29321d24e6b892bbfda734ff46f/Untitled.png)

最优的标准是解决如下最小化问题

$$
f(z) \approx \alpha g^T(z_k)g(z_k) + \frac{\alpha^2}{2}g^T(z_k) H(z_k)g(z_k) + \mathcal{C}
$$

易见，当 $\alpha$ 为变量时，上式的最小值对应的取值为

$$
\hat{\alpha} = \frac{g^Tg}{g^THg}
$$

易见，在二项假设下，上式决定了梯度下降的最优步长。

## 寻优实例

下图中较小的亮白色框代表最优步长的梯度下降法寻优结果；较大的暗灰色框代表固定学习率的梯度下降寻优结果。值得一提的是，最优步长的梯度下降法只进行了 10 次迭代即可找到极小值（小梯度下降法迭代了 100 次），这说明该方法大大提高了寻优效率，并且有机会跳出局部最优值，受起始点影响更小。

![Untitled](Hessian%20%E4%B8%8E%E6%A2%AF%E5%BA%A6%E7%BB%93%E5%90%88%207bffd29321d24e6b892bbfda734ff46f/Untitled%201.png)

![Untitled](Hessian%20%E4%B8%8E%E6%A2%AF%E5%BA%A6%E7%BB%93%E5%90%88%207bffd29321d24e6b892bbfda734ff46f/Untitled%202.png)

![Untitled](Hessian%20%E4%B8%8E%E6%A2%AF%E5%BA%A6%E7%BB%93%E5%90%88%207bffd29321d24e6b892bbfda734ff46f/Untitled%203.png)

![Untitled](Hessian%20%E4%B8%8E%E6%A2%AF%E5%BA%A6%E7%BB%93%E5%90%88%207bffd29321d24e6b892bbfda734ff46f/Untitled%204.png)

## 附录：优化问题的问题小结

1. **梯度下降法的学习率问题：**
    - 学习率确实是梯度下降法中一个关键的超参数。如果学习率设置得太小，收敛速度会很慢；如果设置得太大，可能会错过最优点。这种任意性可能需要通过调整学习率、使用自适应学习率算法（如Adagrad、Adam等）来解决。
2. **Newton 法的不稳定性问题：**
    - Newton 法通常在局部极小值附近更快地收敛，但也容易受到初始点的选择影响。如果初始点选择不当，可能会导致不稳定性。此外，Newton 法的计算开销较大，特别是在高维问题中。
3. **标量场不服从简单的二次型分布：**
    - 这是一个重要的观点。如果优化问题的梯度和Hessian矩阵的性质不适合Newton法的假设，那么Newton法可能表现不佳。在实际问题中，确保选择合适的优化算法以适应问题的性质至关重要。
4. **泰勒分解的二次函数与真实值差异过大：**
    - 这可能与问题的非线性性质有关。Newton法在处理非凸问题时可能受到限制。在这种情况下，可能需要考虑使用更为鲁棒的优化算法，例如随机梯度下降的变种，或者考虑预处理技术来改进收敛性。

总体而言，优化算法的选择通常取决于问题的性质和要解决的具体挑战。在实践中，很多问题可能需要尝试不同的优化算法，超参数调整和正则化方法，以找到最佳的收敛策略。