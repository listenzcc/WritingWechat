## Movie in Machine Learning

如果你实在是没有时间看电影，不妨让算法把相似的信息提取出来。

当然，目前的算法很粗糙，提取的信息也很朴实。

----
- [Movie in Machine Learning](#movie-in-machine-learning)
- [分析方法](#分析方法)
  - [谱聚类](#谱聚类)
- [Ekaterina S01E01](#ekaterina-s01e01)
- [Homeland S01E01](#homeland-s01e01)

## 分析方法

把电影视频当作是图像序列，图像序列在一个一个的小段具有连续性，称为片断。

导演通过片断之间的顺序关系，讲述一个故事，就称为剪辑。

那么我就用工程师的无聊方法把这个过程反过来。

把图像当作是矩阵，黑白图像是二维矩阵，彩色图像是具有通道的RGB三维矩阵。

这样，电影的图像序列就变成了矩阵的连续流形

$$
X \in R^{n \times w \times h \times c}
$$

其中，$n代表图像数量，w和h代表画幅宽度和高度，c代表通道数（黑白为1，彩色为3）$。

### 谱聚类

接下来，对$n$这个维度进行谱聚类。就是把单时间点的图像作为样本点，进行谱聚类。取得它们的类别标签。将类别标签绘制在原始时间轴上，如下图所示

![类别标签示意图](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled.png)

类别标签示意图

根据类别标签，就可以实现相似图像的归类。

我选择了两部美剧的第一集作为例子，看看分析效果如何。

- 第一部是 Ekaterina
- 第二部是 Homeland

从结果上看，

- 这种土办法对人物特写比较有效，但它分不出来特定的角色；
- 对远景的效果也还行，但容易和人群混淆；
- 另外，看来好看的电影需要有合适比例的特写和远景，所以难拍。

所以进一步工作（如果有的话）的思路异常简单，就是找一个神经网络，它应该有区分图像内容的能力。之后用它提取的图像特征重复上面的聚类工作，希望新结果能够更加有效地提取场景并对它们进行归类。

## Ekaterina S01E01

![Untitled](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled%201.png)

![Untitled](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled%202.png)

![Untitled](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled%203.png)

![Untitled](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled%204.png)

## Homeland S01E01

![Untitled](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled%205.png)

![Untitled](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled%206.png)

![Untitled](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled%207.png)

![Untitled](Movie%20in%20Machine%20Learning%2090e69f092ccb4359b20caf97439cf41b/Untitled%208.png)