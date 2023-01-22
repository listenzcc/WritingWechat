# Bunny Render

本文尝试通过 WebGL 渲染 Bunny 兔子模型，它的颜色受到一个简单的神经网络的控制。

从结果上来看，虽然实验用的神经网络极其简单，但它可以用来高亮模型表面的任何区域。

本文代码可见我的前端笔记本

[Demo of Neural Network](https://observablehq.com/@listenzcc/demo-of-neural-network "Demo of Neural Network")

---
- [Bunny Render](#bunny-render)
  - [渲染规则](#渲染规则)


## 渲染规则

通过使用具有随机参数的简单2层神经网络，我们可以突出显示兔子表面的每一个组件，神经网络的设置方式如下，首先，网络的输入特征是节点的模型顶点的$(x, y, z)$坐标，激活函数为 Sigmoid 函数，我们使用更多的通道数来扩展网络的表达能力，本实验中使用 10 个通道。

$$
y = \frac{e^x}{1 + e^x}
$$

由于没有任何“目的”，即我没有任何主观的意愿使 Bunny 兔子具有某种纹理。因此，我简单地采用随机数来设置神经网络的参数。而由于参数是随机的，因此最终呈现的纹理也是随机的。但是，这种随机性并没有破坏纹理的完整性和连续性，这得益于神经网络的特性或者说表达能力。

![Untitled](Bunny%20Render%207f51a37f94614b6fba27f52f0a2e17b1/Untitled.png)