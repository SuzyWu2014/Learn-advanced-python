# Object Introspection

Introspection 指的是在程序运行时时检查一个 Object 的类型。Python 里所有的东西都是 Object，同时 Python 也内建了一些方法来帮助我们查看这些 Object。

## dir

`dir` 可以返回一个 Object 包含的所有 Attributes 和 Methods。 下面是例子：

```python
my_list = [1, 2, 3]
dir(my_list)
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']
```

## type 和 id

type function 返回这个 Object 的类型：

```python
print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>
```

id 返回一个 Object 在内存中的地址。 这个用不太到。

```python
name = "Yasoob"
print(id(name))
# Output: 139972439030304
```

## inspect module

这个 inspect module 提供一些额外的查看 live object 信息的 function. 比如：

```python
import inspect
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... ...

```
