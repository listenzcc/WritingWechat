## Tensor flow 踩坑记

Tensor flow 删除了 contrib 模块，这是万恶之源。

---

- [Tensor flow 踩坑记](#tensor-flow-踩坑记)
- [万恶之源](#万恶之源)
  - [API的改动](#api的改动)
  - [Contrib的删除](#contrib的删除)
- [有一说一](#有一说一)
  - [arg_scope](#arg_scope)
  - [load_variable](#load_variable)

## 万恶之源

Tensorflow 是著名的深度学习计算软件，先不说它与 CUDA 和 GPU 驱动之间超强的、说不清道不明的依赖关系，单说它在诞生不久就进行的重大改版

$$
Tensorflow 1.x \rightarrow Tensorflow 2.x
$$

它改了什么呢？

- 改了很多 API，也就说同一件事情、或者同一个计算逻辑，使用的语句是不一样的；
- 删除了 contrib 模块，将该模块的功能转移到了其他模块中，这个就很欠打。

### API的改动

总的来说，API的改动是使软件更加适于使用而自然发生的。

```python
# TF1.x
outputs = session.run(f(placeholder), feed_dict={placeholder: input})
# TF2
outputs = f(input)
```

虽然我更喜欢1版本的语句，因为它的含义更加明确。这句话的意思是，f代表某个网络的前向计算，网络本身是结构和参数的集合，它本身不能计算，是程序创建的session通过它完成了计算工作。但是为了语句更加简洁，改到2版本也无可厚非。

然而，这种改动吧，不是说不让你改。而是说这种改动没有什么必要，更加没必要的是这些改动会“摒弃”掉之前的写法。

也就是说，如果你用 TF1 撰写了程序，迁移到 TF2 时就需要对这些东西进行无意义的改写。这种改动有点像 Python 2 到 Python 3 中 print 语句的改动

```python
# Python 2
print 'abc'

# Python 3
print('abc')
```

有意义吗？不能说没有；有必要吗？不好说。

不过，好在有 2to3 这样的专门处理升级程序的小工具，虽然可能导致一堆新的 BUG ，但聊胜于无。

后来TF 官方还专门推出了如下这样欲盖弥彰的方法，来“兼容”之前版本的程序。

```python
# Compat TF v1
import tensorflow.compat.v1 as tf  # pylint: disable=import-error
tf.disable_v2_behavior()
```

### Contrib的删除

如果说API的改版还有办法自动化兼容的话。contrib的删除就让人啼笑皆非。

先说说contrib是个啥，它其实相当于是 TF 官方提供的插件接口。成千上万的程序开发者能够通过这个接口，给TF添加各种各样的个性化功能。或者这样说，这个接口就是随软件附带的TF社区。

久而久之，这个接口开始大放异彩，上面的功能极大的推动了TF的发展，甚至开始覆盖TF本身的，使用起来不那么方便的特性。

然而，在TF改版的过程中，它被砍掉了。这就很恶心人。因为在新版本的TF中，所有

```python
tensorflow.contrib
```

的功能都没有了，这个模块也没有了。之前contrib社区有多繁荣，改版之后的TF就有多难用。而想要用新版的TF运行之前版本的程序时，软件版本迁移需要做的工作就有多繁琐。

虽然，TF官方承诺将contrib中的功能都迁移到软件的其他模块中，但是这样做只是减轻了这些模块的开发成本，并没有丝毫减轻迁移时面临的困难。

雪上加霜的是，官方的迁移说明是动态的线上内容，出于某个众所周知的原因，这个文档不怎么容易刷出来。所以本文将对 TF 使用过程中，涉及版本转换的内容进行长期的、简要的记录。既有助于自己，也希望能帮到大家。

## 有一说一

### arg_scope

![Untitled](Tensor%20flow%20%E8%B8%A9%E5%9D%91%E8%AE%B0%208164d61b7bad4ab887c63d937df3a2fc/Untitled.png)

[TF2.0中从tensorflow.contrib.framework.python.ops导入arg_scope的等价物？ - 问答 - 腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/ask/sof/1147742)

### load_variable

![Untitled](Tensor%20flow%20%E8%B8%A9%E5%9D%91%E8%AE%B0%208164d61b7bad4ab887c63d937df3a2fc/Untitled%201.png)

[tf.train.load_variable  |  TensorFlow Core v2.9.1 (google.cn)](https://tensorflow.google.cn/api_docs/python/tf/train/load_variable)