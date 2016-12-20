# Containers

Containers 是一种非常常见的数据结构，他们自身以及他们所承载的值都存在 memory 中。Python 中常见的 containers 有：

+ `list, deque,...`
+ `set, frozonsets,...`
+ `dict, defaultdict, OrderedDict, Counter,...`
+ `tuple, namedtuple,...`
+ `str`

我们也可以认为 container 是那些可以被问是否包含某个成员的数据结构。

例如在 lists, sets 和 tuple 中查看元素是否存在：

```python
>>> assert 1 in [1, 2, 3]      # lists
>>> assert 4 not in [1, 2, 3]
>>> assert 1 in {1, 2, 3}      # sets
>>> assert 4 not in {1, 2, 3}
>>> assert 1 in (1, 2, 3)      # tuples
>>> assert 4 not in (1, 2, 3)
```

在 dict 中查看 key 是否存在：

```python
>>> d = {1: 'foo', 2: 'bar', 3: 'qux'}
>>> assert 1 in d
>>> assert 4 not in d
>>> assert 'foo' not in d  # 'foo' is not a _key_ in the dict
```

在 string 中查看 substring 是否存在：

```python
>>> s = 'foobar'
>>> assert 'b' in s
>>> assert 'x' not in s
>>> assert 'foo' in s  # a string "contains" all its substrings， 但是string 并没有在 memory 里存储所有 substring 的 copy。
```

需要注意的是，containers  虽然提供了一个方式是生成他们所包含的每一个元素，但是他们并不都是 iterables. 例如对于有些数据结构 ([Bloom filter](https://www.wikiwand.com/en/Bloom_filter)
)，你只能询问某个成员函数是否存在，却无法返回每个成员本身。
