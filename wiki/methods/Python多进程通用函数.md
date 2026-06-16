---
type: method
title: "Python多进程通用函数（parallel_apply）"
aliases:
  - parallel_apply
  - "Python Pool+Queue"
  - "多进程封装"
tags: [python, multiprocessing, parallel-computing]
operation_types:
  primary: "Estimate / sample instead of compute"
  secondary:
    - "Decompose / reduce dimension"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-02-19-Python的多进程编程技巧.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-10-27-什么时候多进程的加速比可以大于1.md
source_ids:
  - "4231"
  - "7031"
status: draft
updated: 2026-06-14
method_summary: "封装multiprocessing.Pool+Queue模式的多进程通用函数，支持对象方法中的并行计算和超线性加速。"
typical_structure: "建立in_queue和out_queue；定义worker_step循环处理；Pool(workers, worker_step, queues)启动；主进程放/取数据。"
applicability: "大规模数据处理中的并行加速场景，特别是dict操作密集型任务。"
tools:
  - multiprocessing.Pool
  - multiprocessing.Queue
related_concepts:
  - [[Python多进程编程模式]]
related_methods: []
examples:
  - [[article::4231]]
  - [[article::7031]]
---

## 适用问题

Python的 `multiprocessing.Pool.map` 无法在类的成员方法中直接使用——多进程pickle时会报 `Can't pickle <function>` 错误。此外，标准 `Pool.map` 要求所有数据预先加载到内存中，无法处理流式数据或带状态累积的回调。

问题场景：在类的 `__init__` 中初始化数据，在 `run` 方法中启动多进程处理，每个工作进程需要共享主进程的上下文，并且处理结果需要逐条回调汇总。

## 核心变换

利用 `multiprocessing.Pool` 的初始化参数特性——`Pool(processes, initializer, initargs)` 接受初始化函数和参数，让每个工作进程启动时运行一个从Queue读取任务、写入Queue结果的循环函数。

封装为通用函数 `parallel_apply`：

```python
def parallel_apply(func, iterable, workers, max_queue_size,
                   callback=None, dummy=False):
    """多进程地将func应用到iterable的每个元素。
    dummy=False为多进程，True为多线程。
    """
    from multiprocessing import Pool, Queue
    in_queue, out_queue = Queue(max_queue_size), Queue()

    def worker_step(in_queue, out_queue):
        while True:
            d = in_queue.get()
            r = func(d)
            out_queue.put(r)

    pool = Pool(workers, worker_step, (in_queue, out_queue))

    results = [] if callback is None else None
    # 主进程放数据、取结果的循环...
    for d in iterable:
        in_queue.put(d)
        # 从out_queue取结果
        while not out_queue.empty():
            r = out_queue.get()
            if callback is None:
                results.append(r)
            else:
                callback(r)

    pool.terminate()
    return results
```

**关键技巧**：`Pool(workers, worker_step, (in_queue, out_queue))` — `Pool` 的第二个参数是在每个进程中运行的初始化函数，第三个参数是传给它的参数。利用这一点，让每个工作进程启动后进入 `worker_step` 循环，不断从 `in_queue` 取数据、处理、放入 `out_queue`。

**线程模式**：将 `multiprocessing` 替换为 `multiprocessing.dummy`，即可将多进程切换为多线程，代码无需其他修改。

## 典型步骤

1. 定义处理函数 `func`（接受单个输入，返回处理结果）
2. 准备可迭代的输入数据 `iterable`
3. 定义可选的 `callback` 用于逐条处理输出（如累积统计）
4. 调用 `parallel_apply(func, iterable, workers=N, callback=callback)`
5. 如需多线程模式，设置 `dummy=True`

## 直觉

标准 `Pool.map` 是"全进全出"模式：所有数据进入、所有结果返回。但在流式数据处理或类方法中，需要"边进边出"的异步模式。通过Queue解耦了任务发放和结果收集——主进程可以持续放入新任务并取回结果，工作进程独立运行互不阻塞。

用 `Pool(workers, worker_step, args)` 而非 `Process` 手动管理的好处是：Pool自动处理进程的生命周期管理和异常传播。

## 边界

- Queue大小限制：`max_queue_size` 控制in_queue的缓冲区大小，防止内存爆炸
- 结果无序：工作进程处理速度不同，输出顺序与输入顺序无关
- 跨平台注意事项：macOS上默认使用fork启动方式，某些场景可能需要设置 `spawn`
- 超线性加速仅出现在特定场景：如dict操作随数据量增大变慢，分批处理可绕过此瓶颈
- 不适合IO密集型任务：IO等待时多进程加速比有限，此时多线程可能更合适

## 例子

- THUCNews词频统计：10进程处理55秒完成（单进程20分钟），加速比达2.0（超线性）
- 对象方法中多进程：类的 `run` 方法内启动 Pool+Queue，替代不可用的 Pool.map
- 文本批处理：将1000条文本分为一批，多进程并行分词+词频统计

## 证据

- ev::4231::多进程核心技巧：Pool(workers, worker_step, (in_queue, out_queue)) 启动工作进程
- ev::4231::Queue+Pool模式替换不可用的Pool.map，支持类方法内多进程
- ev::4231::multiprocessing → multiprocessing.dummy 一键切换多线程
- ev::7031::THUCNews词频统计：10进程55秒完成，单进程20分钟，超线性加速（加速比2.0）
- ev::7031::超线性加速原理：分批处理规避了dict随数据量增大变慢的问题
- ev::7031::单进程分批优化也可提速（20分钟→8分钟），但parallel_apply更方便
