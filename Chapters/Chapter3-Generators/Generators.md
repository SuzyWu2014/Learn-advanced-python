# Generators

Generators 简单来说就是优雅的 iterator, 他提供了一种简洁的语法来定义 iterators。首先，我们先明确两点：

+ 任何 generator 同时也是一个 iterator, 反之则不一定成立。
+ 任何 generator 都可以认为是一个以 lazy 的方式产生 value 的 factory.

下面是之前斐波那契数列写成 generator 的版本：

```python
>>> def fib():
...     prev, curr = 0, 1
...     while True:
...         yield curr
...         prev, curr = curr, prev + curr
...
>>> f = fib()
>>> list(islice(f, 0, 10)) # islice 本身也是一个 iterator.
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

另一个例子：

```python
def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
print(next(gen))
# Output: Traceback (most recent call last):
#            File "<stdin>", line 1, in <module>
#         StopIteration
```

从上面的例子可以看出，当我们 yield 出了所有的 value, next() function 就会抛出一个 StopIteration 的异常。我们在用 for 来遍历 generator 的时候看不到这个异常是因为 for  自动获取了这个异常并以此结束调用 next().

Python 中有一些 build-in 的数据类型也是支持 iteration 的：

```python
my_string = "Yasoob"
next(my_string)
# Output: Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: str object is not an iterator
```

上面的 Error message 说 str object 不是 iterator. 其实这就验证了我们在前面说到的，str 是 iterable, 他支持 iteration, 但是因为他不是 iterator, 所以我们不能直接遍历。 这时候就需要用到 iter() function 了。

```python
int_var = 1779
iter(int_var)
# Output: Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
# This is because int is not iterable

my_string = "Yasoob"
my_iter = iter(my_string)
next(my_iter)
# Output: 'Y'
```
