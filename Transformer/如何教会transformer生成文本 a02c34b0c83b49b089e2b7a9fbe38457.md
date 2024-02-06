# 如何教会transformer生成文本

什么是大模型？我想，至少在在2024年初，我可以简单地说：使用transformer的模型就是大模型。

本文尝试开一个新坑，简述我对transformer网络结构的理解，并且尝试说明它是如何进行文本和图像处理的。

[https://github.com/listenzcc/learn-ViT](https://github.com/listenzcc/learn-ViT)

---
[toc]

## 形式化的数据流

首先，我想以纯粹外行的角度理解什么是transformer。有多外行呢？假设我是一名知道什么是机器学习的人，但我既不会线性代数又不知道神经网络为何物。那么，什么是机器学习呢？它是将万事万物都转化成数字，通过数学计算解决实际问题的方法。现在举几个例子，

首先是图像处理的机器学习：将场景框起来，这个框称为ROI，将ROI内图像看作颜色的实数矩阵，通过各种计算方法得到一个实数向量，这个向量代表图像的语义信息，比如图像的内容属于哪个类别，图像如何分割等

$$
\begin{cases}
Scene \rightarrow_{ROI} Image \rightarrow I\in\mathbb{R}^{w \times h \times c} \\
u= \varphi(I), u \in \mathbb{R}^{k\times1}
\end{cases}
$$

接下来是自然语言处理的机器学习：将语言看作文本，文本是符号的有序组合，符号可以量化成实数向量。将一段话分成两段，那么前一段就是一堆向量的组合，通过各种计算方法预测出后续的向量组合，如果算法足够好用的话，那么预测出的向量组合与原始文本的向量组合相似

$$
\begin{cases}
Sentence \rightarrow_{embedding} [
v_1, v_2 \dots v_n
], v_i\in \mathbb{R}^{m\times1} \\
[v_{n/2}, v_{n/2+1} \dots v_n] \approx \Psi([v_1, v_2 \dots v_{n/2}])
\end{cases}
$$

另外，自然语言处理有其特殊之处，特殊的地方在于它处理的内容是符号序列，因此在理解情况下这是一个自回归问题，所谓自回归就是将序列拆开，不断地从已有序列推知序列的“下一个值”的过程。

$$
v_{m+1} = \psi([v_1, v_2 \dots v_m])
$$

如果前四个字是“床前明月”的话，那么下一个字就是“光”。这个过程可以不断迭代下去，一个字一个字地写出“疑是地上霜”。这时自然语言处理和图像分类的机器学习算法在形式上是一致的

$$
\begin{cases}
v = \psi(J)= \psi([v_1, v_2 \dots v_m])\\
u = \varphi(I) = \dots
\end{cases}
$$

顺着这个思路继续下去，只要我们有办法把图像序列化，那么它就可以解决图像处理和自然语言处理的机器学习问题。因此，从纯粹外行的角度理解transformer，它就是序列处理的一把锤子（这个说法并不严谨，但我想把它放在这里是没什么问题的），任何向量序列在它眼中都是钉子。

## 最最基本的文本生成

本着务实的态度，我使用最最基本的transformer网络进行了最最基本的文本生成实验。（当然，这个实验需要事先了解一些神经网络的东西，关于神经网络的细节将在后续慢慢介绍）。

为什么说是最最基本的呢？是因为我在符号方面只考虑了$26$个英文字母和空格，共计$27$个字符。那么所谓序列就是这些字符构成的序列，而transformer网络的任务就是从给定的字符串中“预测”出后续的字符串。这个网络的结构非常简单，构建它的方法如下代码所示

```python
def __init__(self, d_model=128):
    super(TaskModel, self).__init__()
    
    # 定义词向量，词典数为27。
    n = 27
    self.embedding = nn.Embedding(num_embeddings=n, embedding_dim=128)
    # 定义Transformer。超参是我拍脑袋想的
    self.transformer = nn.Transformer(d_model,
                                      nhead=16,
                                      num_encoder_layers=4,
                                      num_decoder_layers=4,
                                      dim_feedforward=512,
                                      norm_first=True,
                                      batch_first=True
                                      )
    
    # 定义位置编码器
    self.positional_encoding = PositionalEncoding(d_model, dropout=0)
    
    # 定义最后的线性层，这里并没有用Softmax，因为没必要。
    # 因为后面的CrossEntropyLoss中自带了
    self.predictor = nn.Linear(128, n)
```

为了让网络进行“学习”，我从wikipedia上拷贝了三段英文词条，分别是Winston Churchill人物、covid-19事件和Structural Similarity方法词条的全部内容。下图表示学习结果，其中箭头左侧部分是输入到transformer中的文本前段，箭头右侧部分是transformer预测的后续文本。

由于我训练网络的方法过于简单粗暴，导致transformer网络虽然学会了几个英文单词，但没有理解它们之间的意思，具体表现为

1. conservative party 和 covid pandemic 是文本中大量出现的、连续出现的词组，导致它们会以较大的概率出现在生成的文本中；
2. 类似的，churchill和covid这些单词也会驴唇不对马嘴地出现在同一个句子中。

但不管怎么说，一个基本的框架是搭起来了，这时的loss大概是0.00079。

![Untitled](%E5%A6%82%E4%BD%95%E6%95%99%E4%BC%9Atransformer%E7%94%9F%E6%88%90%E6%96%87%E6%9C%AC%20a02c34b0c83b49b089e2b7a9fbe38457/Untitled.png)

为什么我满意于以上这个笨笨的生成式transformer呢？这是由于我有理由猜测这种现象的成因包括训练不足和网络结构过于简单。下面分两种情况讨论这个事情。

## 网络训练不足时的样子

首先，在网络训练的初始阶段，它生成的文本是下图这个样子的，只会将“有把握”的助词堆砌在一起。随着训练轮次的继续增加，情况才慢慢好起来了，这里的loss大概在0.0013左右。

![Untitled](%E5%A6%82%E4%BD%95%E6%95%99%E4%BC%9Atransformer%E7%94%9F%E6%88%90%E6%96%87%E6%9C%AC%20a02c34b0c83b49b089e2b7a9fbe38457/Untitled%201.png)

## 网络再多学习一阵的样子

如果我让网络再多学习一会，当它的loss达到0.00038时，其生成文本的多样性会进一步提高。再继续跑下去已经没什么意思了，因为我的transformer网络还太简单，完成不了太复杂的事情。不过它给2024起了个好头。

![Untitled](%E5%A6%82%E4%BD%95%E6%95%99%E4%BC%9Atransformer%E7%94%9F%E6%88%90%E6%96%87%E6%9C%AC%20a02c34b0c83b49b089e2b7a9fbe38457/Untitled%202.png)
