## WebGL绘图（之三）

我在之前的基础上添加了一点点细节。
现在能够呈现一个动态的复数空间。

---

- [WebGL绘图（之三）](#webgl绘图之三)
- [复多项式的零点与极点](#复多项式的零点与极点)


## 复多项式的零点与极点

假如你学过复数，
就应该了解一个复多项式函数，
可以用它的全部零点和极点进行表示。

比如这样一个多项式，

$$  f(z) = (z-p_1)^2 \cdot (z^2 - p_2) \cdot (z^2 - p_4) \cdot (z^2-p_3)^{-1} $$

它包含这些要素

- 一个二阶零点 $p_1$；
- 一对共轭零点 $p_2$；
- 另一对共轭零点 $p_4$；
- 最后一对共轭极点 $p_3$。

当这些点动起来之后，
就能形成一段看上去挺好玩的动态效果。

【这是一段棒到不行的视频】

具体代码可见我的[ObservableHQ](https://observablehq.com/@listenzcc/complex-space "ObservableHQ")工程。

另外，为了补足公众号要求的300字原创要求，我就再啰嗦两句。

1. 图中的不同颜色，代表该位置复数的相角；
2. 图中黑色、白色区域，分别代表复数的模值较小、大的情况；
3. 图中蛛网状的白色曲线，代表复数实部和虚部的等值线，

   > 这里，我们几乎立即遇到了一个巧合式的问题，这就是，
   > 为什么这些曲线之间“总是”保持着相互垂直的关系？

   > 简要简答：这并不是一个巧合。
   > ​事实上，由于复多项式是复数之间的连续映射，
   > ​而连续映射有“保角”特性​。
   > ​因此，就像在笛卡尔坐标系中的x轴和y轴一样，
   > ​这些“等值线”永远保持正交关系。

​水完字数了，收工。