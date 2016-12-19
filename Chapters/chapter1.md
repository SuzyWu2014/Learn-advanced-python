# Chapter 1: `*args` and `**kwargs`

在定义一个 function 的时候，当我们需要传入的参数个数是不确定的情况下，`*args` 和 `**kwargs`就会派上用场。需要注意的是，args 和 kwargs 只是变量名，如果你愿意的话，你可以用任何你喜欢的 variable name 替换它们, 例如，var 和 vars。这里的区别只是 `*` 的个数。

## 使用 `*args` 来定义function

`*args` 用在传入的参数没有关键字的时候，即仅仅传入参数值。

```python
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test') # 直接传入参数值

# 运行结果：
>>>
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
```

## 使用 `**kwargs`来定义function

`**kwargs` 用于传入参数名+参数值的情况, 其实 kwargs 就是个 dictionary, 例子如下：

```python
def greet_me(**kwargs):
    if "key" in kwargs:
        print("key = ", kwargs["key"])
    else:
        print("Missing key")

    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

>>> greet_me(name="yasoob")
name = yasoob
```

## 调用function时使用 `*args` 和 `**kwargs` 来作为参数

```python
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# 使用 *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# 使用 **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```

如果想要同时使用 `*args`, `**kwargs` 以及普通的 args, 则 function 定义时参数的顺序为：
`some_func(fargs, *args, **kwargs)`

## 何时使用

常用于 decorator,我会在之后的章节会提到。另一个使用场景就是 Monkey patch, 也就是在 runtime 的时候改变一些代码。比如说，
假设你有一个 class，其中有一个 get_info function. 这个 funciton 会调用一个 API function, 然后返回此API的数据。但在测试的时候，你希望返回一些测试数据，而不是用这个真正的 get_info() 的数据，你就可以定义另一个 get_info() 的 function, 将它赋给这个 class.

```python
import someclass

def get_info(self, *args):
    return "Test data"

someclass.get_info = get_info #此时若调用 someclass.get_info(),就会返回 "Test data"
```
