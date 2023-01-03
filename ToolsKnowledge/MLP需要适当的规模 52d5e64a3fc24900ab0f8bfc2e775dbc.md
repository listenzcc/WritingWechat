# MLP需要适当的规模

由于上次 MLP 回归失败，因此我决定对它进行改进。在增加了网络层数之后，我发现回归精度和收敛速度均有所提高。

[https://github.com/listenzcc/MLP-notebook](https://github.com/listenzcc/MLP-notebook "https://github.com/listenzcc/MLP-notebook")

---
- [MLP需要适当的规模](#mlp需要适当的规模)
  - [问题简化](#问题简化)
  - [网络优化](#网络优化)
  - [回归效果](#回归效果)


## 问题简化

首先将等式两侧的函数进行重新设计，在不改变方程形式的情况下给它提供一个可以解释的意义，即试图用频率较低的函数（蓝）去预测频率较高的函数（红），生成这些数据的关键代码如下所示

$$
\begin{cases}
f(t) &= r(t) \cdot e^{-j (\omega t + \phi)} \\
r(t) &= k \cdot t + b
\end{cases}
$$

![Untitled](MLP%E9%9C%80%E8%A6%81%E9%80%82%E5%BD%93%E7%9A%84%E8%A7%84%E6%A8%A1%2052d5e64a3fc24900ab0f8bfc2e775dbc/Untitled.png)

![Untitled](MLP%E9%9C%80%E8%A6%81%E9%80%82%E5%BD%93%E7%9A%84%E8%A7%84%E6%A8%A1%2052d5e64a3fc24900ab0f8bfc2e775dbc/Untitled%201.png)

```python
# src
theta = np.linspace(0, np.pi * 2, n)
r = np.linspace(0.2, 0.8, n)

# target
theta = np.linspace(0, np.pi * 6, n)
r = np.linspace(0.1, 0.9, n)
```

## 网络优化

由于之前的网络不能很好地完成回归任务，因此我对它进行改进，但改进的方法非常简单粗暴，就是简单的加一个宽度为 8 个通道的隐藏层，现在它更像是一个细头细脚和大肚子的形状。

```python
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.mlp = torchvision.ops.MLP(
            2, [4, 8, 4, 2], activation_layer=nn.LeakyReLU)
        self.sig = nn.Tanh()

    def forward(self, x):
        return self.sig(self.mlp(x))
```

经过 3000 次训练后，损失函数的变化情况如下，可以看到它在 1000 次迭代之前就已经收敛，下图左侧代表增加中间层的 MLP 损失函数变化情况，右侧代表原始 MLP 损失函数变化情况。可见，虽然增加了 MLP 的网络规模，但收敛速度却变快了，损失函数也更低。

![New (large) MLP](MLP%E9%9C%80%E8%A6%81%E9%80%82%E5%BD%93%E7%9A%84%E8%A7%84%E6%A8%A1%2052d5e64a3fc24900ab0f8bfc2e775dbc/Untitled%202.png)

New (large) MLP

![Raw (small) MLP](MLP%E9%9C%80%E8%A6%81%E9%80%82%E5%BD%93%E7%9A%84%E8%A7%84%E6%A8%A1%2052d5e64a3fc24900ab0f8bfc2e775dbc/Untitled%203.png)

Raw (small) MLP

## 回归效果

简单的改动带来了良好的效果，回归结果如下，可以看到回归误差已经被压缩到较小的区间，这说明增加 MLP 的规模有助于提高它的准确性和收敛速度。

![Untitled](MLP%E9%9C%80%E8%A6%81%E9%80%82%E5%BD%93%E7%9A%84%E8%A7%84%E6%A8%A1%2052d5e64a3fc24900ab0f8bfc2e775dbc/Untitled%204.png)

![Untitled](MLP%E9%9C%80%E8%A6%81%E9%80%82%E5%BD%93%E7%9A%84%E8%A7%84%E6%A8%A1%2052d5e64a3fc24900ab0f8bfc2e775dbc/Untitled%205.png)

![Untitled](MLP%E9%9C%80%E8%A6%81%E9%80%82%E5%BD%93%E7%9A%84%E8%A7%84%E6%A8%A1%2052d5e64a3fc24900ab0f8bfc2e775dbc/Untitled%206.png)