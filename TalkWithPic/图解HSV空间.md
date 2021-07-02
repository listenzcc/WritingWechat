## 图解HSV空间

以颜色空间的“舌形图”为蓝本，我们可以在RGB空间之外，得到更加符合人眼观感的HSV空间。
本文对其进行图解。

---
- [图解HSV空间](#图解hsv空间)
- [HSV空间图解](#hsv空间图解)
  - [色相 Hue](#色相-hue)
  - [饱和度 Saturation](#饱和度-saturation)
  - [明度 Value](#明度-value)
  - [实现代码](#实现代码)

## HSV空间图解

将颜色空间中的“舌形图”的最外包络进行提取，我们可以得到一个圆环。
这个圆环就代表HSV空间的H维度。

![hsv-pic.png](hsv-pic.png)

其中，左上角的圆环图，代表最饱和且最亮时的色相值。另外三张图，分别代表在$3$种色相中，不同饱和度和明度的颜色分布。

### 色相 Hue

色相，也称为色调。
色相代表颜色的相位，私以为比色调更加贴切。

结合颜色空间的“舌形图”，可以看到它即是舌形图的最外层包络。

### 饱和度 Saturation

饱和度代表颜色的饱和程度。
另外三张子图的横轴即是饱和度值。
越饱和，则代表颜色越“纯”和“充足”。
饱和度最低时，通常代表无颜色相位的“白色”。

### 明度 Value

明度代表颜色的亮度。
子图的纵轴即是明度值。
明度最低时，为最不明亮的“黑色”。

当然，我们可以将其表示为三维空间中的椎形图形。

![hsv-color-space-5.jpg](hsv-color-space-5.jpg)

### 实现代码

计算过程使用`python`代码，可以参考我的[GITHUB仓库](https://github.com/listenzcc/JupyterScripts.git "GITHUB仓库")。

由于本计算过程较为简单，我们直接列出如下。

- 引用的包

```python
import cv2
import numpy as np
import pandas as pd
from PIL import Image

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
```

- 自定义工具

```python
def rgb2str(rgb):
    return '#' + ''.join([hex(e).replace('x', '')[-2:] for e in rgb])

class MyImage(object):
    ''' Class of the Images with its Matrix in HSV ColorSpace '''

    def __init__(self, resolve=100):
        ''' Initialization with Resolve [resolve] '''
        # Init Resolve
        self.resolve = resolve
        pass

    def mk_h_circle(self):
        ''' Make Circle for H Dim'''
        hc = np.zeros((180, 3)).astype(np.uint8)
        hc[:, 0] = range(180)
        hc[:, 1:] = 255

        self.hc = hc

        # Make Image
        rgb = cv2.cvtColor(hc[:, np.newaxis, :], cv2.COLOR_HSV2BGR)
        rgb = rgb.squeeze()

        df = pd.DataFrame()
        df['rgb'] = [e for e in rgb]
        df['color'] = df['rgb'].map(rgb2str)
        df['idx'] = range(180)

        def ang2pos(a):
            t = a / 180 * np.pi * 2
            return (np.cos(t), np.sin(t))

        df['pos'] = df['idx'].map(ang2pos)

        df['x'] = df['pos'].map(lambda x: x[0])
        df['y'] = df['pos'].map(lambda x: x[1])

        fig = go.Figure(data=[go.Scatter(x=df['x'],
                                         y=df['y'],
                                         marker={'color': df['color']},
                                         mode='markers')])
        fig.update_layout(dict(title='Hue Ring'))

        return fig


    def mk_hsv(self, h=0):
        ''' Make HSV Matrix based on H Dim [h] '''
        # Get Resolve
        r = self.resolve

        # Init HSV Matrix
        hsv = np.zeros((r, r, 3)).astype(np.uint8)

        # Set H Dim
        hsv[:, :, 0] = h % 180

        # Set SV Dim
        hsv[:, :, 1:] = np.array(np.meshgrid(np.linspace(0, 255, resolve), np.linspace(0, 255, resolve))).transpose((1, 2, 0))

        self.hsv = hsv
        return hsv

    def plot_hsv(self, hsv=None):
        ''' Plot HSV Matrix '''
        if hsv is None:
            if hasattr(self, 'hsv'):
                hsv = self.hsv
            else:
                hsv = self.mk_hsv()

        # Make Image
        im = Image.fromarray(cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))

        # Plot SV Matrix
        fig = px.imshow(im)
        fig.update_xaxes(title_text='S')
        fig.update_yaxes(title_text='V')
        return fig
```

- 画图

```python
mi = MyImage()

fig = make_subplots(rows=2, cols=2, subplot_titles=['Hue Ring', 'SV Matrix H 30', 'SV Matrix H 90', 'SV Matrix H 150'])

fig1 = mi.mk_h_circle()

fig.add_trace(
    fig1.data[0],
    row=1,
    col=1,
)

hsv = mi.mk_hsv(30)
fig2 = mi.plot_hsv(hsv)
fig.add_trace(
    fig2.data[0],
    row=1,
    col=2,
)

hsv = mi.mk_hsv(90)
fig3 = mi.plot_hsv(hsv)
fig.add_trace(
    fig3.data[0],
    row=2,
    col=1,
)

hsv = mi.mk_hsv(150)
fig4 = mi.plot_hsv(hsv)
fig.add_trace(
    fig4.data[0],
    row=2,
    col=2,
)

fig.update_layout(dict(
        height=800,
        width=800,
    ))

fig
```