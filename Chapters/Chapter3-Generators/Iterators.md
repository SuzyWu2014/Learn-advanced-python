# iterator

Iterator 是一个 stateful helper object, 他可以产生通过调用 next() 来产生 iterable 中的下一个元素的 value。也就是说， 任何有一个 `__next__()` method 的 object 都是 iterator, 我们并不关心 next() 是如何产生 value 的。

换一个角度看，可以把 iterator 看作一个 value factory, 他知道如何获取 next value 因为他保存了一个 internal state.

接下来来看几个例子。所有 itertool functions 都是返回 iterators, 有一些还是无限的 sequence.

```python
>>> from itertools import count
>>> counter = count(start=13)
>>> next(counter)
13
>>> next(counter)
14
```

从有限的 sequence 里产生无穷的 sequence:

```python
>>> from itertools import cycle
>>> colors = cycle(['red', 'white', 'blue'])
>>> next(colors)
'red'
>>> next(colors)
'white'
>>> next(colors)
'blue'
>>> next(colors)
'red'
```

从无限序列中产生有限序列：

```python
>>> from itertools import islice
>>> colors = cycle(['red', 'white', 'blue'])  # infinite
>>> limited = islice(colors, 0, 4)            # finite
>>> for x in limited:                         # so safe to use for-loop on
...     print(x)
red
white
blue
red
```

接下来我们来看一下 iterator 的内部是如何实现的。让我们来写一个 interator 来产生斐波那契数列：

```python
>>> class fib:
...     def __init__(self):
...         self.prev = 0
...         self.curr = 1
...
...     def __iter__(self):
...         return self
...
...     def __next__(self):
...         value = self.curr
...         self.curr += self.prev
...         self.prev = value
...         return value
...
>>> f = fib()
>>> list(islice(f, 0, 10))
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

这个 class 既是 iterable (因为有 `__ter__()` method), 也是 iterator (因为有 `__next__()`). 这个 iterator 的状态是通过改变 curr 和 prev 的值来保存的。








