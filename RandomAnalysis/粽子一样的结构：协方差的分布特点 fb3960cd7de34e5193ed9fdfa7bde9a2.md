# 粽子一样的结构：协方差的分布特点

前文说明了协方差矩阵是对称矩阵的子集，本文通过蒙特卡洛模拟的方法进一步绘制了协方差矩阵非对角线上的值的联合分布特性，实验表明，低维特征协方差的联合分布不仅不会占满整个空间，甚至呈现出一种粽子皮一样的四棱椎形结构。

---
[toc]

## 协方差矩阵不必然是对称矩阵

在下图中，我建立了笛卡尔坐标系，它的原点是半球的球心。白色指向左边的线段代表某个单位向量 

$$
v_1=[0, 0, 1]^T
$$

那么这个坐标系下的其他两个单位向量，$v_2$和$v_3$，我指定它们之间满足内积关系

$$
\begin{cases}
v_1 \cdot v_2 = a\\
v_1 \cdot v_3 = b， b < a\\
v_2 \cdot v_3 = c
\end{cases}
$$

那么，这两个向量必然出现在$v_2$红色和$v_3$黄色圆环上。不失一般性，我指定红色向量$v_2$如图所示。那么由它和$v_3$之间的内积关系可知，$v_3$必然出现在绿色圆环上。因此，我肯定$v_3$必然出现在黄色和绿色圆环的交点上，这对应二次方程有两个实数解的情况。

![Untitled](%E7%B2%BD%E5%AD%90%E4%B8%80%E6%A0%B7%E7%9A%84%E7%BB%93%E6%9E%84%EF%BC%9A%E5%8D%8F%E6%96%B9%E5%B7%AE%E7%9A%84%E5%88%86%E5%B8%83%E7%89%B9%E7%82%B9%20fb3960cd7de34e5193ed9fdfa7bde9a2/Untitled.png)

接下来，假设$v_2$和$v_3$之间的内积逐渐增大，这导致绿色圆环不断缩小。那么必然有一个临界值，导致绿色和黄色圆环彼此不再相交。这对应二次方程没有实数解的情况，也就是协方差矩阵不可达到的情况。

![Untitled](%E7%B2%BD%E5%AD%90%E4%B8%80%E6%A0%B7%E7%9A%84%E7%BB%93%E6%9E%84%EF%BC%9A%E5%8D%8F%E6%96%B9%E5%B7%AE%E7%9A%84%E5%88%86%E5%B8%83%E7%89%B9%E7%82%B9%20fb3960cd7de34e5193ed9fdfa7bde9a2/Untitled%201.png)

从以上分析中不难发现，对称矩阵不一定是协方差矩阵，其中包含有后者无法达到的情况。绘图代码可见我的开源代码本

[Why covariance matrix equals not to syn. matrix](https://observablehq.com/@listenzcc/why-covariance-matrix-equals-not-to-syn-matrix)

## 协方差的蒙特卡洛模拟

接下来，我开始好奇“究竟有多少不可达到的情况？”于是开始了蒙特卡洛模拟，模拟过程将在下文详述，本文只给出初步结果。简单来说，我随机构造了$1000$个$3$阶协方差矩阵。

$$
\Sigma^{3\times3} = \begin{bmatrix}1&a&b\\a&1&c\\b& c&1\end{bmatrix}
$$

对矩阵上三角的三个值，$a, b, c$，进行记录，将三个值分别作为$xyz$坐标绘制在三维图中，因此图中每一个点代表一个协方差矩阵。为了增加可区分度，我将点的颜色按三个值给$RGB$通道赋值。

在随机数较为简单的情况下，这些点的分布非常有趣。它们不仅不会占满整个空间，甚至呈现出一种粽子皮一样的四棱椎形结构。

![20231210-183745.gif](%E7%B2%BD%E5%AD%90%E4%B8%80%E6%A0%B7%E7%9A%84%E7%BB%93%E6%9E%84%EF%BC%9A%E5%8D%8F%E6%96%B9%E5%B7%AE%E7%9A%84%E5%88%86%E5%B8%83%E7%89%B9%E7%82%B9%20fb3960cd7de34e5193ed9fdfa7bde9a2/20231210-183745.gif)

![Untitled](%E7%B2%BD%E5%AD%90%E4%B8%80%E6%A0%B7%E7%9A%84%E7%BB%93%E6%9E%84%EF%BC%9A%E5%8D%8F%E6%96%B9%E5%B7%AE%E7%9A%84%E5%88%86%E5%B8%83%E7%89%B9%E7%82%B9%20fb3960cd7de34e5193ed9fdfa7bde9a2/Untitled%202.png)

![Untitled](%E7%B2%BD%E5%AD%90%E4%B8%80%E6%A0%B7%E7%9A%84%E7%BB%93%E6%9E%84%EF%BC%9A%E5%8D%8F%E6%96%B9%E5%B7%AE%E7%9A%84%E5%88%86%E5%B8%83%E7%89%B9%E7%82%B9%20fb3960cd7de34e5193ed9fdfa7bde9a2/Untitled%203.png)

绘图代码可见我的开源代码本

[Covariance matrix's semi definite](https://observablehq.com/@listenzcc/covariance-matrixs-semi-definite)