# Websocket 的极简后端

在对连接不敏感的情况下，Websocket 能够给 Web 后端开发带来极其轻便的开发体验。

---

-   [Websocket 的极简后端](#websocket-的极简后端)
    -   [Websocket](#websocket)
    -   [异步执行机制](#异步执行机制)
    -   [应用实例：NLP 词语关系视图](#应用实例nlp-词语关系视图)

## Websocket

Websocket 简称 WS 是一种面向连接的网络传输协议，在 python 中有它的实现库。

[WebSocket - Web APIs | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket "WebSocket - Web APIs | MDN (mozilla.org)")

与同行 httpsocket 相比，我觉得 ws 的实现更加简便。因为它可以简单地实现短连接通信，从而以“异步”的机制进行网络服务。

## 异步执行机制

所谓异步执行机制是相对于“同步”来讲的。假设我们有任务序列 abcdefg，那么同步机制是顺序地执行它们，并且每一项任务都在之前的任务执行完毕后才开始。这样做的好处是任务之间的顺序一定，由于时序有保证，它们能简单地、顺序地工作在同一块内存区域中，不用担心彼此冲突。

$$
a\rightarrow b \rightarrow \dots \rightarrow g
$$

而异步执行是指 abcdefg 任务能够在同时，或者恰当的时候开始执行，而不考虑彼此之间的执行顺序。

$$
\begin{cases}
a\\
b\\
\dots\\
g
\end{cases}
$$

与同步机制相比，这就导致了两个问题

1. 任务顺序被打乱
2. 可能产生难以预测的资源冲突

因此，一个解决办法是通过多线程或进程的方式，在不同的内存区域中开始各自的工作，这时，异步机制与 Javascript 的 promise 机制相似。另一个解决办法是通过防冲突设计来避免程序异常，这个工作极其复杂，一般没有人这么干。

那么从 Javascript 的角度出发，它的 Promise 可以是如下形式。它在某个用户输入的地方读取必要信息，之后建立 WS 连接，然后注册一堆程序，包括 onopen, onmessage, onclose，分别代表建立连接时执行、收到消息时执行和关闭时执行。注册完成后，这部分代码工作随即完成，后续代码立即进行。有种下达指令后不再管的感觉，这就是异步请求。

```jsx
{
    const content = document.getElementById("textarea-1").value;
    console.log(content);

    const ws = new WebSocket("ws://localhost:9386/?accessToken=123456");

    ws.onopen = function (evt) {
        console.log("Connection open ...");
        ws.send(content);
    };

    ws.onmessage = function (evt) {
        const { data } = evt;
        console.log("Received Message: " + data);

        if (data.startsWith("<Ent>:")) {
            document.getElementById("div-1-ent").innerHTML = data.slice(
                "<Ent>:".length
            );
        }

        if (data.startsWith("<Dep>:")) {
            document.getElementById("div-1-dep").innerHTML = data.slice(
                "<Dep>:".length
            );
        }

        if (data.startsWith("<Final>:")) {
            ws.close();
        }
    };

    ws.onclose = function (evt) {
        console.log("Connection closed.");
    };
}
```

而在后端，假如我们用 Python 搭建一个 WS 后端的话，它也会以异步的方式处理这些请求。其中，关键词 async 就代表异步函数，它与 Promise 相似，在注册后立即执行。执行到什么时候呢？执行到函数内部全部 await 关键字指定的函数完成之后。

```python
'''
Websocket server example for short connections
'''

import spacy
from spacy import displacy

import asyncio
import websockets

nlp = spacy.load("en_core_web_sm")

async def handle(websocket, path):
    '''
    Handle message from the client

    Args:
        :param:websocket: The websocket connection
        :param:path: The path of the client connection
    '''
    def send(response):
        print(f"> {response[:20]}, {len(response)}")
        return websocket.send(response)

    print('Client connects', websocket, path)

    msg = await websocket.recv()
    print(f"< {msg}")

    # ------------------------------------------------
    text = msg
    doc = nlp(' '.join([e for e in text.split() if e]))
    sentence_spans = list(doc.sents)

    # ------------------------------------------------
    html = displacy.render(sentence_spans, style="ent")
    response = '<Ent>:' + html
    # await websocket.send(response)
    # print(f"> {response[:20]}, {len(response)}")
    await send(response)

    # ------------------------------------------------
    html = displacy.render(sentence_spans, style="dep")
    response = '<Dep>:' + html
    # await websocket.send(response)
    # print(f"> {response[:20]}, {len(response)}")
    await send(response)

    response = '<Final>:'
    await send(response)
    # await websocket.send('<Final>:')
    # print(f'Terminate.')
    return

params = dict(
    host='localhost',
    port=9386
)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", help="host of the websocket connection", default=params['host'])
    parser.add_argument(
        "--port", help="port of the websocket connection", default=params['port'])
    args = parser.parse_args()

    host = args.host
    port = args.port

    start_server = websockets.serve(handle, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
```

## 应用实例：NLP 词语关系视图

上述实例完成了这样一个功能，用户在前端网页上的指定位置输入一段文档，而 Python 的 spacy 模块则负责对这段文档进行分析，并给出可视化结果。最近 ChatGPT 比较火，所以突然对词向量比较感兴趣，希望它流入中国之前，我能把它的原理弄明白。

[https://spacy.io/](https://spacy.io/ "https://spacy.io/")

![NLP Analysis](Websocket%E7%9A%84%E6%9E%81%E7%AE%80%E5%90%8E%E7%AB%AF%20f62e3d7eedc941f6a07f537a36acfaa0/Untitled.png)

NLP Analysis
