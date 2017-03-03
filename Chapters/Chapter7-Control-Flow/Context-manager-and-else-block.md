# Context Managers and else Blocks

## else Blocks

+ `for/else`: The else block will run only if and when the for loop runs to completion; i.e. not if the for is aborted with a break.
+ `while/else`: The else block will run only if and when the while loop exits because the condition became falsy; i.e. not when the while is aborted with a break
+ `try/else`: The else block will only run if no exception is raised in the try block.

下面是例子：
```python
for item in my_list:
    if item.flavor == 'banana':
        break
else:
    raise ValueError('No banana flavor found!')

try:
    dangerous_call()
except OSError:
    log('OSError...')
else:
    after_call() # 当　dangerous_call() 成功执行后，执行 after_all()
```

## Context managers and with blocks

Context manager objects 的存在是用来控制　with statement, 就像　iterators 的存在是用来控制　for statement.

with statement　是用来简化　try/finally pattern 的，他保证了在某段代码之后一些操作可以总是被执行，　即使这段代码的执行过程中出现了　exception。

Context manager protocol 包括　`__enter__` 和　`__exit__`　方法。在　with statement　开始的时候，`__enter__`  被调用，结束时则调用　`__exit__`. `__exit__` 最普遍的作用是用来确保　file object 被关闭。

```python
>>> with open('mirror.py') as fp: #
...     src = fp.read(60) #
...
>>> len(src)
60
>>> fp #
<_io.TextIOWrapper name='mirror.py' mode='r' encoding='UTF-8'>
>>> fp.closed, fp.encoding #
(True, 'UTF-8')
>>> fp.read(60) #
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### The contextlib utilities
See also the documentation: [contextlib — Utilities for with-statement contexts](https://docs.python.org/3/library/contextlib.html)

#### Using @contextmanager

这个　`@contextmanager` decorator　简化了创建　context manager 的流程，我们不再需要实现 `__enter__/__exit__` 方法，只需要　implement 一个带有　yield 的 generator。

```python
@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
```

`yield` 将程序分成两个部分，yield 之前的部分会在　interpter 调用 `__enter__` 的时候执行， yield 之后的部分会在调用 `__exit__` 的时候执行。在 yield 周围包裹上 `同意/catch` 基本上是使用 `@contextmanager` decorator 的代价，毕竟我们不知道用户们会在 with block 里做些什么。



