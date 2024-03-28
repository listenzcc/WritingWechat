# Asyncio，两种异步过程的实现方式

使用Python的Asyncio包可实现两种异步任务管理方式：1. 使用asyncio.gather()同时执行一组已知任务；2. 利用asyncio.Queue()实现生产者-消费者模式，适用于随机出现的任务。在生产者-消费者模式中，queue.join()方法可阻塞主协程直至队列中的任务全部完成。本文记录它们，以备后察。

[https://github.com/listenzcc/async-python](https://github.com/listenzcc/async-python)

---
[toc]

## 我有一堆异步任务，需要执行它们

我们可以使用**asyncio.gather()**来管理这些异步任务的执行。它们的好处是自动管理异步进程，并且能够在进程出错时保留**traceback**信息，下面是核心代码：

![Untitled](Asyncio%EF%BC%8C%E4%B8%A4%E7%A7%8D%E5%BC%82%E6%AD%A5%E8%BF%87%E7%A8%8B%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F%203b13d1f7d7f8410989b231a13e504a64/Untitled.png)

```python
# %% ---- 2024-03-15 ------------------------
# Function and class

def ns2ms(ns: int) -> int:
    return int(ns*1e-6)

async def method(ad: AttrDict, sleep_secs: float = 0.1, copy: bool = False, failure_prob: float = 0.2) -> AttrDict:
    # Do something to ad
    return ad

# %% ---- 2024-03-15 ------------------------
# Play ground
if __name__ == '__main__':
    # ----------------------------------------
    # Run until complete
    # 1. Get or create a new loop
    try:
        loop = asyncio.get_running_loop()
        print(f'Got running loop: {loop}')
    except RuntimeError:
        loop = asyncio.new_event_loop()
        print(f'Created loop: {loop}')
    asyncio.set_event_loop(loop)
    
    # 2. Create the jobs
    ads = [AttrDict(idx=i) for i in range(10)]
    jobs = asyncio.gather(*[method(ad) for ad in ads], return_exceptions=True)
    
    # 3. Run the jobs one-by-one until finished
    print(loop.run_until_complete(jobs))
    print(ads)
```

## 任务随机出现，需要异步执行它们

对于这种情况，我们可以使用**asyncio.Queue()**来实现生产者-消费者模式，其中生产者将任务放入队列，放入队列的时间是随机的，而消费者则从队列中获取并执行任务。下面是对应的代码。需要注意的是，**queue.join()**方法会将进程阻塞起来，释放的条件是**_unfinished_tasks**计数器清零，该计数器随着put()方法而增加，随着task_done()方法而降低。

在本例中，我们加入了**await queue.join()**语句，这会使主协程在队列中的所有任务都被消费完毕之前阻塞。当队列中的任务都被消费完毕后，**queue.join()**返回，解除阻塞状态。这样可以确保在所有任务都被处理完毕之后程序才会退出。

```python
# %% ---- 2024-03-26 ------------------------
# Function and class
async def consumer(queue: asyncio.Queue):
    print(f'---- Consumer starts')
    i = 0
    # Run forever
    while True:
        time.sleep(0.5)
        item = await queue.get()
        queue.task_done()
        # Break if get the None
        if item is None:
            break
        print(f'    {i:4d} | Consumer got: {item} | {queue.qsize()}')
        i += 1
    print(f'---- Consumer finished')

def _producer(queue: asyncio.Queue):
    for _ in range(1000):
        inp = input('>> ')
        if inp == 'q':
            break
        queue.put_nowait(inp)
    queue.put_nowait(None)

async def main():
    queue = asyncio.Queue()  # type: asyncio.Queue
    for j in range(10):
        queue.put_nowait(j)
    # Run the consumer in background
    _ = asyncio.create_task(consumer(queue))
    # Run the producer blocking the system
    Thread(target=_producer, args=(queue, )).start()
    # Wait for the queue._unfinished_tasks back to zero
    await queue.join()

# %% ---- 2024-03-26 ------------------------
# Play ground
if __name__ == '__main__':
    asyncio.run(main())
```
