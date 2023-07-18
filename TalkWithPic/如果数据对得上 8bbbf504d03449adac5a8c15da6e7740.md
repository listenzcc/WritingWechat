# 如果数据对得上

这是一件值得高兴的事情，因为这个数据它吻合得很好。

说是英国 2022 的新生儿名字排名第一名是 Muhammad，即伊斯兰教的教名“穆罕默德”。经过数据分析可知，这主要是因为穆斯林的命名习惯，而不是因为他们人多或者生育意愿更高。

本工程的开源代码可见我的github仓库

[https://github.com/listenzcc/baby-names-in-england](https://github.com/listenzcc/baby-names-in-england)

---
- [如果数据对得上](#如果数据对得上)
  - [Muhammad成为近年来英国的“热门名”](#muhammad成为近年来英国的热门名)
  - [英国有多少穆斯林](#英国有多少穆斯林)
  - [数据分析](#数据分析)
  - [附录：为么穆斯林中 Muhammad 名较多](#附录为么穆斯林中-muhammad-名较多)
  - [附录：总和生育率](#附录总和生育率)


## Muhammad成为近年来英国的“热门名”

事情的起因是这样的，就是我看到一则新闻，说是英国 2022 的新生儿名字排名第一名是 Muhammad，即伊斯兰教的教名“穆罕默德”。我的好奇心一下就起来了，于是从英国政府网站下载到 2021 年的出生姓名数据，（他们的权威数据只支持到这一年）。数据显示虽然 Muhammad 名没有那么排名第一这么危言耸听，但也基本上支持这种观点。

下图中的趋势图呈现了 muhammad 新生儿数量不断增加的趋势。与之相对的，Thomas 和 Charlie 等传统大名则逐渐式微。

既然有了数据，于是我开始分析，看看英国在 2021 年的出生人口数据中，究竟有多少 Muhammad。这个工作不难做，因为数据是现成的。但有个小问题需要注意，那就是 Muhammad 作为教名有几个变形，在统计时需要将这些变形全部统计进来。

统计结果表明，2021 年全年英国新生儿男婴共 295,057 名，其中 Muhammad 名的共 6,685 名。

[UK's most popular baby names for 2022 revealed, as Sophia and Muhammad top the list](https://www.lbc.co.uk/news/uks-most-popular-baby-names-for-2022-revealed-as-sophia-and-muhammad-top-the-lis/)

[Baby names in England and Wales Statistical bulletins - Office for National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/bulletins/babynamesenglandandwales/previousReleases)

![Untitled](%E5%A6%82%E6%9E%9C%E6%95%B0%E6%8D%AE%E5%AF%B9%E5%BE%97%E4%B8%8A%208bbbf504d03449adac5a8c15da6e7740/Untitled.png)

![Untitled](%E5%A6%82%E6%9E%9C%E6%95%B0%E6%8D%AE%E5%AF%B9%E5%BE%97%E4%B8%8A%208bbbf504d03449adac5a8c15da6e7740/Untitled%201.png)

![Untitled](%E5%A6%82%E6%9E%9C%E6%95%B0%E6%8D%AE%E5%AF%B9%E5%BE%97%E4%B8%8A%208bbbf504d03449adac5a8c15da6e7740/Untitled%202.png)

> **Muhammad** ([Arabic](https://en.wikipedia.org/wiki/Arabic_language): مُحَمَّد, [romanized](https://en.wikipedia.org/wiki/Romanization_of_Arabic): *Muḥammad*), also spelled **Muhammed**, **Muhamad**, **Mohammad**, **Mohammed**, **Mohamad**, **Mohamed** or in a variety of other ways, is an Arabic given male name literally meaning 'Praiseworthy'.
> 
> 
> [Muhammad (name)](https://en.wikipedia.org/wiki/Muhammad_(name))
> 

## 英国有多少穆斯林

这些数据代表什么呢？代表叫 Muhammad 的英国新生儿男婴更多，而这是由于穆斯林习惯将他们的第一个男孩命名为 Muhammad。

还有呢？还有两个可能性

- 首先，它可能代表英国的穆斯林的绝对数量更多；
- 其次，它可能代表英国的穆斯林生育数量比其他英国人更多。

遗憾的是，经过数据分析，我发现这两个假说都不成立。

## 数据分析

首先，英国的穆斯林并不多。援引wikipedia的数据，英国在 2021 年的穆斯林人口占总人口的 6.7%，并不占大多数。

> According to the latest [2021 United Kingdom census](https://en.wikipedia.org/wiki/2021_United_Kingdom_census), 3,801,186 Muslims live in England, or 6.7% of the population. The Muslim population again grew by over a million compared to the previous census.
> 

其次，数量为 6,685 的 Muhammad 新生儿看似在全部 295,057 名新生儿男婴中占比很多，但是该数字只需要英国穆斯林家庭的总和生育率达到 3 即可。分析如下，

- 首先，英国人口的 6.5% 对应新生儿数量的 6.5%；
- 其次，全部新生儿数量的 6.5% 为 19,768.82 人；
- 最后，6,685 的三倍等于 20,055，基本等于 19,768.82 人。

这里暗含一个假设，那就是只考虑男婴的情况下，英国穆斯林家庭平均生育 3 个孩子，这 3 个孩子中有 1 个是老大，以 Muhammad 为名。所以 Muhammad 男婴们的数量乘以 3 即可得到全体穆斯林的新生儿男婴数量。

## 附录：为么穆斯林中 Muhammad 名较多

在一些穆斯林家庭中，的确存在这样的传统，他们会把第一个儿子命名为穆罕默德。这是因为穆罕默德（Muhammad）是伊斯兰教的创始人，被穆斯林视为先知和榜样。他的名字在伊斯兰世界中非常普遍，成为许多男性的名字。

然而，这并不是所有穆斯林家庭的必然选择。命名是一个个人和家庭的决定，根据文化、传统和个人信仰可以有所不同。有些家庭可能会根据其他重要人物、先知或家族成员来取名，也有些家庭可能会选择不同的名字，以示个性或个人喜好。因此，穆罕默德并不是每个穆斯林家庭的第一个儿子的固定名字。

## 附录：总和生育率

总和生育率（Total Fertility Rate，TFR）是衡量一个特定人口群体在特定时期内，平均每名女性预计生育的孩子数量的指标。它是人口学中一个重要的指标，用于描述特定地区或国家的生育水平。

总和生育率通常以每位女性的平均生育子女数来计算，假设她在生育年龄期间（通常在15至49岁之间）的生育模式在整个生育期内保持不变。因此，总和生育率不考虑特定年龄组的生育分布，而是对整个生育年龄范围的生育行为进行综合评估。

总和生育率的值通常是一个正数，但如果总和生育率低于2.1，那么就表示一个地区或国家的生育水平处于低于替代水平。替代水平是指在没有考虑迁移的情况下，让每代人口维持在相对稳定水平所需的生育水平。如果总和生育率高于2.1，则表示该地区或国家的人口在增长。

总和生育率的变化对于了解人口结构、劳动力市场、社会保障和人口迁移等方面的趋势和挑战非常重要，因此它是人口学和社会学领域中一个关键的指标。