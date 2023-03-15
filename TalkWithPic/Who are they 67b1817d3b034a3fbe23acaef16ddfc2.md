# Who are they

为纪念两会胜利召开，本文提供一个前端工具，分析代表们的性别、年龄、民族和地域分布。当然，这些都是 baidu 上搜来的公开信息。

[Who are they](https://observablehq.com/@listenzcc/who-are-they)

---
- [Who are they](#who-are-they)
  - [整体分布](#整体分布)
  - [民族分布](#民族分布)
  - [年龄分布](#年龄分布)
  - [姓氏分布](#姓氏分布)
  - [信息获取方式](#信息获取方式)


## 整体分布

这是全国各省级行政单位的代表数量图，它几乎可以当作目前的省级行政单位人口、经济和发展分布的有力参考。性别和民族统计分析表明，全国男性代表数量多于女性代表，其中男性以汉、回、蒙、满、壮和藏族居多；女性以汉、回、满、壮和苗族居多。

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled.png)

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%201.png)

## 民族分布

下图左图为各省代表的民族数量图，右图为各省代表的女性比例图。图中结果表明我国女性代表所占的比例均值集中在 0.2 到 0.3 之间，回归线的斜率为 0.26，极值出现在广西和云南达到了 0.33。另外，我还发现如下两图有一定的相似性。于是开始好奇一个问题，那就是西南地区女性代表的比例高是由于特定民族中女性参政比例高？还是由于民族杂居现象导致女性参政比例高？

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%202.png)

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%203.png)

为了对上述假设进行取舍，我进行了回归分析。下图左侧图代表不同民族的女性代表数量关系，回族、壮族等出现在回归线左上侧，这代表该族女性参政比例更高。而下图右侧图是将各省进行比较，其横坐标代表该省代表的民族数量，纵坐标为女性代表的比例。除了回归线有从左下到右上的趋势微弱之外（p值也并不显著），看不到两者之间的联系。因此“西南地区女性代表的比例高是由于特定民族中女性参政比例高”这一说话的合理性更高。

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%204.png)

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%205.png)

## 年龄分布

通过我提供的前端工具，可以快速获取他们之间的年龄比较结果，其中男性代表的年龄普遍大于女性代表，不管从地域上看，还是从民族上看都是如此。但这个结果什么都说明不了，因为中国现行的退休政策是女性退休年龄比男性少 5 岁，因此约 5 年的年龄差距大概率是由这个因素引起的。

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%206.png)

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%207.png)

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%208.png)

## 姓氏分布

姓氏分布与中国人口的姓氏分布基本一致，其中李、王、张、刘、陈为人口较多的姓氏。

![Untitled](Who%20are%20they%2067b1817d3b034a3fbe23acaef16ddfc2/Untitled%209.png)

## 信息获取方式

1. 姓名的获取，采用查官方网站的方式，将他们的姓名、民族和省份存储起来；
2. 年龄的获取，由于官方网站除了提供姓名、性别、民族信息之外没有提供任何其他信息，因此我通过 baidu 搜索引擎获取此人的信息，搜索的格式为“<省份>+代表+<姓名>”，在搜索结果页面中，会有一定的概率出现其出生年月；
3. 使用正则表达式对网页进行分析便可以得到其年龄信息。

```python
'''
Require the baidu page of the person
'''
url = f'http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&'
params = {
    'wd': f'{province} 代表 {name}'
}

resp = requests.get(url, headers=headers, params=params)
content = resp.content

def find_birth_year(text):
    '''
    Find the birth year from the give text,
    since the text is the got by the BeautifulSoup.get_text(),
    the '\n's should be removed from the article.
    
    Then the patters are tried one-by-one until the birth year is found.
    '''
    text = text.replace('\n', '')
    for pattern in [
        '.+生日：(\d\d\d\d)年.+',
        '.+(\d\d\d\d)年(\d\d)月生.+',
        '.+(\d\d\d\d)年生.+',
    ]:
        obj = re.match(pattern, text)
        if obj:
            return obj.groups()[0]

    return None
```