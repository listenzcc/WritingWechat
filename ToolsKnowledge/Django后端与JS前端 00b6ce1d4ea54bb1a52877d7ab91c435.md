# Django后端与JS前端

本文将以一个图像工程为线索，记录Django后端与JS前端的合作过程。虽然这些工作必将被 AI 取代，但现在还得有人干不是？这可能是一个较长期的记录，所以下次还会看到我，但是肯定会有些不一样。

---
- [Django后端与JS前端](#django后端与js前端)
  - [后端部署](#后端部署)
    - [模版页面](#模版页面)
    - [静态库](#静态库)
    - [图像和特征计算服务](#图像和特征计算服务)
  - [前端设计](#前端设计)
    - [请求规划](#请求规划)
    - [快速表格](#快速表格)
    - [快速绘图](#快速绘图)
  - [代码附录](#代码附录)
    - [Django 设置和服务](#django-设置和服务)
    - [HTML节点](#html节点)
    - [JS请求和计算](#js请求和计算)


## 后端部署

### 模版页面

模版页面用于返回主页，它的占位符可以用于显示未来可能会有的用户登陆信息。

### 静态库

静态文件用于存储复用的 JS 和 CSS 文件，目前静态文件和使用的库包括

```
# The files in static

static:
img  library  loadResources.js  refreshHistogram.js  style.css  toolbox.js

static/img:
favicon.ico

static/library:
chart.js@4.2.1  d3.v7.min.js  datatables.1.13.2  jquery-3.5.1.js

static/library/chart.js@4.2.1:
chart.umd.min.js

static/library/datatables.1.13.2:
jquery.dataTables.min.css  jquery.dataTables.min.js

```

### 图像和特征计算服务

静态文件的另一个功能是提供图像服务，将图像所在目录设置为静态目标可以使前端能够直接通过 static 路径得到目标图像。在上述设置完成后，通过 [urls.py](http://urls.py) 实现路由功能。其中，view.image_features 提供对应图像的特征提取和计算服务，其中被分析的图像由 request 的内容解析得到，而所有可选图像的信息通过 view.resources 获取。

## 前端设计

### 请求规划

前端通过 request 请求实现后端资源获取，因此为了简化通信内容，前端首先通过请求获取全部可用资源，之后再按需请求获取这些资源对应的特征。

### 快速表格

表格使用datatable和jquery的结合版本，它的优点是提供完全“无痛”的交互式表格开发体验。在定义表格之后，仅需要设置其类别就可以实现表格互动。

### 快速绘图

为什么不用plotly.js？首先明确一点，那就是plotly.js能够提供非常优秀的交互操作体验。但因为它强制安装自己的d3.js，而且它强制使用的版本与d3的新版本冲突，因此不选择使用它。

本工程选择的方案是目前流行的 chart.js。它的优点是绘图过程较为独立，通过在恰当的地方修改其绘图数据就可以实现新数据的绘制，还能稍微自带一些刷新动效，算是意外惊喜。

![Untitled](Django%E5%90%8E%E7%AB%AF%E4%B8%8EJS%E5%89%8D%E7%AB%AF%2000b6ce1d4ea54bb1a52877d7ab91c435/Untitled.png)

![Untitled](Django%E5%90%8E%E7%AB%AF%E4%B8%8EJS%E5%89%8D%E7%AB%AF%2000b6ce1d4ea54bb1a52877d7ab91c435/Untitled%201.png)

## 代码附录

### Django 设置和服务

```python
# -------------------------------------------------
# Django settings.py
template_dirs = [
    BASE_DIR.joinpath('template'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': template_dirs,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

'''
// template/index.html
<footer id="footer">{{ date }}</footer>
'''

# -------------------------------------------------
# Django settings.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR.joinpath("static"),
    RDM_ROOT_DIR.joinpath('input_data')
]

'''
## The files in static/
static:
img  library  loadResources.js  refreshHistogram.js  style.css  toolbox.js

static/img:
favicon.ico

static/library:
chart.js@4.2.1  d3.v7.min.js  datatables.1.13.2  jquery-3.5.1.js

static/library/chart.js@4.2.1:
chart.umd.min.js

static/library/datatables.1.13.2:
jquery.dataTables.min.css  jquery.dataTables.min.js
'''

# -------------------------------------------------
# File: urls.py

from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=r'static/img/favicon.ico')),
    path('index', view.index),
    path('index.html', view.index),
    path('resources', view.resources),
    path('imagefeatures', view.image_features),
]

# -------------------------------------------------
# File: view.py
'''
Require resources json,
the available images are returned.
'''

def resources(request):
    df = resource_table_input_data[public_columns]

    parse = parse_request(request)

    if parse.query:
        df = df.query(parse.query)

    df.index = range(len(df))
    print(request, len(df))

    data = df.to_json()

    return HttpResponse(data, content_type='application/json')

'''
Compute the image feature,
the image is specified by the request
'''

def image_features(request):
    df = resource_table_input_data

    parse = parse_request(request)

    dct = split_parse(parse)

    select = df.query(
        'module=="{module}" & set=="{set}" & name=="{name}"'.format(**dct))

    img = Image.open(select.iloc[0]['fullPath'])
    rgb = np.array(img)
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    hls = cv2.cvtColor(rgb, cv2.COLOR_RGB2HLS)
    dct['shape'] = rgb.shape

    for name, channel, data in zip(['red', 'green', 'blue', 'hue', 'saturation', 'value', 'brightness'],
                                   [0, 1, 2, 0, 1, 2, 1],
                                   [rgb, rgb, rgb, hsv, hsv, hsv, hls]):
        d = data[:, :, channel]

        hist = np.histogram(d, bins=255, range=(0, 255))
        dct['channel_' + name] = tuple([int(e) for e in hist[0]])
        print(name, np.sum(hist[0]), np.min(d), np.max(d))
    dct['bins'] = tuple([int(e) for e in hist[1]])
    dct['dim'] = 255
    dct['dim_hue'] = 180

    return HttpResponse(json.dumps(dct), content_type='application/json')
```

### HTML节点

```html
// Require stimuli_data/..../image_02.jpg from the input-data folder.
<img id="singleImageImg" src="static/stimuli_data/78images/image_02.jpg" alt="Image"></img>
```

### JS请求和计算

```jsx
// All-in-one request at startup

const AllImageOptions = [];
const VariableContainer = {};

/**
 * Require and deal with the resources
 */
function loadResources() {
    Object.assign(VariableContainer, {
        singleImageImgNode: document.getElementById("singleImageImg"),
        singleImageHistogramChartJS: "singleImageHistogramChartJS",
        resourceTableD3Select: d3.select("#table-container-1"),
        moduleSelector: d3.select("#selectModule"),
        setSelector: d3.select("#selectSet"),
        nameSelector: d3.select("#selectName"),
    });

    d3.json("resources").then((json) => {
        log("Load sources", json);
        fillResourceTable(json);
        // Fill the AllImageOptions
        initImageOptions(json);
    });
}
```