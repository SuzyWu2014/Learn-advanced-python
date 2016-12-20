# Iterables

大多数的 containers 都是 iterables, 但 iterables 不局限于 containers, 例如 open files, open sockets 都是 iterables. Containers 通常都是有限的元素集，而 iterables 可以表示无限的数据集。

iterable 是任何可以返回 iterator 的 object, 这个 iterable object 并不一定是某种数据结构，他只要定义了 `__iter__()` method 或者是 `__getitem__()` method 就可以称为iterable, 而 iterator 的功能是可以返回 iterable object 里的所有元素。 下面来看个例子：

```python
>>> x = [1, 2, 3]
>>> y = iter(x)
>>> z = iter(x)
>>> next(y)
1
>>> next(y)
2
>>> next(z)
1
>>> type(x)
<class 'list'>
>>> type(y)
<class 'list_iterator'>
```

例子中，x 是 interable, y 和 z 是两个各自独立的 iterator. y 和 z 会保存当前遍历的状态，一旦往前遍历，就无法获取之前的元素。

需要注意的是，出于实用主义的原因，iterable class 会在 class 中实现 `__iter__()` 和 `__next__()`，并且 `__iter()__` function 会返回 self. 这种做法使得这个 class 既是 iterable 也是自己的 iterator.当然我们也可以返回一个不同的 object 作为 iterator.

通常我们会遍历 list 如下：

```python
x = [1, 2, 3]
for elem in x:
    ...
```

![](pic/iterable-vs-iterator.png)

这个过程中，python 先是调用了 GET_ITER, 也就是等同于执行了 `iter(x)`。 这个 FOR_ITER 等同于重复调用了 `next()`。这个过程是出于速度的考量，被 interpreter 优化出来的，所以在 byte code 中并不能看见。

```python
>>> import dis
>>> x = [1, 2, 3]
>>> dis.dis('for _ in x: pass')
  1           0 SETUP_LOOP              14 (to 17)
              3 LOAD_NAME                0 (x)
              6 GET_ITER
        >>    7 FOR_ITER                 6 (to 16)
             10 STORE_NAME               1 (_)
             13 JUMP_ABSOLUTE            7
        >>   16 POP_BLOCK
        >>   17 LOAD_CONST               0 (None)
             20 RETURN_VALUE
```


