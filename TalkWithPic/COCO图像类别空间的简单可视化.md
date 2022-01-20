## COCO图像类别空间的简单可视化

本文将分别使用`PCA`、`TSNE`和`SOM`三种方法对`COCO`数据图像的类别信息进行映射。
从而以较低的维度对数据进行呈现。

---

- [COCO图像类别空间的简单可视化](#coco图像类别空间的简单可视化)
- [方法简介](#方法简介)
- [可视化结果](#可视化结果)
  - [`PCA`可视化结果](#pca可视化结果)
  - [`TSNE`可视化结果](#tsne可视化结果)
  - [`SOM`可视化结果](#som可视化结果)

## 方法简介

之前，我们已经对`COCO`数据集中图像的类别向量进行了量化，
并形成了矩阵

$$M \in R^{80 \times m}$$

其中，$m$代表图像数量。

本文将分别对$M$矩阵进行`PCA`分解，
`TSNE`和`SOM`映射，
从而以较低的维度对数据进行呈现，
试图对类别信息进行展示，
实现对该图像数据的进一步理解。

其中，

- `PCA`方法是常用的数据降维方法。

- `TSNE`方法是 [t-distributed Stochastic Neighbor Embedding （t-SNE）](https://lvdmaaten.github.io/tsne/#:~:text=t-Distributed%20Stochastic%20Neighbor%20Embedding%20%28t-SNE%29%20is%20a%20technique,it%20to%20be%20applied%20on%20large%20real-world%20datasets. "t-distributed Stochastic Neighbor Embedding （t-SNE）")方法，

   > t-SNE is a technique for dimensionality reduction that is particularly well suited for the visualization of high-dimensional datasets.

  它是在保持样本之间“距离”关系不变的条件下，
  将样本进行低维映射的方法。

- `SOM`方法是[自组织映射（Self-Organizing Map）](https://www.sciencedirect.com/topics/engineering/self-organizing-map "自组织映射（Self-Organizing Map）")方法，
  借助大牛在书本中对它的描述

  > The advantage of a SOM is that it can be used to partition the data with easy two-dimensional visualization of expression patterns.
  >
  > From: Handbook of Stem Cells (Second Edition), 2013

  它是`2`维空间的可视化映射方法，主要用于进行“数据分割”。

## 可视化结果

### `PCA`可视化结果

在`PCA`空间中，全部`3`万多张图像映射如下，
图中的每个点代表一张图像，

![PCA-1](./coco-3-pca-1.png)

上图的颜色为图像的样本类别，
由于图像中有多个样本，
因此将图像中“面积”最大的样本类别作为图像的样本类别。

从另一个视角来看，

![PCA-2](./coco-3-pca-2.png)

上图的颜色代表图像中的类别数量。

可以看到，`PCA`给出了一个不太令人满意的结果，

- 它将样本分成了两个大类；
- 两个大类都呈现`L`形的分布；
- 首先，两个大类大致对类别进行了区分，
  它对“天蓝色”样本和“粉色”样本进行了区分，
  但没有对“蓝色”和“红色”样本进行区分；
- 其次，它对样本类别数量的图像也没有区分；
- 总结来说，从`PCA`映射的结果来说，
  它并没有提供对区分能力。

也就是说，`PCA`方法对理解数据并没有什么帮助。

### `TSNE`可视化结果

在`TSNE`空间中的映射结果分别如下图所示

![TSNE-1](./coco-3-tsne-1.png)

其中，点的颜色代表图像物体类别。

![TSNE-3](./coco-3-tsne-3.png)

其中，点的颜色代表图像物体类别，点的大小代表物体数量

![TSNE-2](./coco-3-tsne-2.png)

其中，点的颜色代表图像中物体数量。

可以看到，`TSNE`给出了一个较为清晰的结果，

- 不同的类别具有清晰的聚类趋势；
- 不同的样本数量也出现在空间中不同的区域。

也就是说，`TSNE`方法对理解数据有较大的帮助。

### `SOM`可视化结果

在`SOM`空间中的映射结果分别如下图所示

![SOM-1](./coco-3-som-1.png)

和

![SOM-2](./coco-3-som-2.png)

其中，图中样本点颜色的意义与之前相同。
值得说明的是，
`SOM`方法是二维可视化方法，
因此，图中`X-Y`平面的位置代表样本点真实的位置，
而`Z`轴的位置代表该图中样本的数量。

可以看到，虽然`SOM`方法能够对样本进行较好的“聚类”，
但聚类的意义并不明确，
与`TSNE`方法相比，
它既没有区分样本类别，也没有区分样本数量，
因此这是十分令人疑惑的结果。

本文的分析代码可见[我的GITHUB仓库](https://github.com/listenzcc/cocoLearning "我的GITHUB仓库")。