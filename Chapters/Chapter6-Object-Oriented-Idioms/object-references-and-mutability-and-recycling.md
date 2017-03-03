# Object references, Mutability, and Recycling

## Variables 不是容器， 而是 lable

```python
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

>>> x = Gizmo()
Gizmo id: 140390185502256
>>> y = Gizmo() * 10
Gizmo id: 140390185502312
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'
>>> z = x
>>> z is x
>>> True
```

等式的右边决定了我们该如何理解 Python 的变量赋值，他可能是新创建的，例如调用构造函数 `Gizmo()`, 也有可能是 retrieved，而在这种情况下就相当于给原来的 Object 加了另一个引用标签， 例如 `z` 和 `x`。

## Identity, Equality, and Aliases

每个 object 都有自己的 identity, type 以及 value. 只有 identity 一旦生成就不再改变。 `is` operator 对比的就是两个 object 的 identity. (使用 id() 函数)

### `==` vs `is`

首先明确：
+ `==` 比较的是 values of objects
+ `is` 比较的是 identity of Objects

`is` 要比 `==` 快，因为 `is` 只是对比了两个 Object 的 id. `a == b` 相当于 `a.__eq__(b)` 的简写。 `__eq__` 方法继承自那些对比 `id` 的 object, 但是大多数的 build-in 数据类型都重写了 `__eq__` 方法，来匹配各自的 equality behavior.

## The Relative Immutability of Tuples

我们通常认为 tuple 是 immutable, 但准确的说，他应该是相对 immutable. 举个例子：

```python
>>> t1 = (1, 2, [30, 40])
>>> t2 = (1, 2, [30, 40])
>>> t1 == t2
True
>>> id(t1[-1])
140390184237384
>>> t1[-1]
[30, 40]
>>> id(t1[-1])
140390184237384
>>> t1[-1].append(99)
>>> t1
(1, 2, [30, 40, 99])
>>> id(t1[-1])
140390184237384 # Tuple 中的 list 的 identity 保持不变
>>> t1 == t2 # 但是 tuple 的值改变了
False

```

也就是说，tuple 的 immutability 指的是其所包含的 references 不可改变，但不包括这些 references 所指向的内容。

## Copies Are Shallow by Default

先来看看 shallow copy 的例子：

```python

>>> l1 = [3, [66, 55, 44], (7, 8, 9)]
>>> l2 = list(l1) # or l2 = l1[:]
>>> l1.append(100)
>>> l1[1].remove(55)
>>> print('l1: ', l1)
l1:  [3, [66, 44], (7, 8, 9), 100]
>>> print('l2: ', l2)
l2:  [3, [66, 44], (7, 8, 9)] # l2 sub-list 的值也发生了改变
>>> l2[1] += [33, 22]
>>> l2[2] += (10, 11)
>>> print('l2: ', l2)
l2:  [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]
>>> print('l1: ', l1)
l1:  [3, [66, 44, 33, 22], (7, 8, 9), 100]

```

如上面的例子，l2 是 l1 的 shallow copy, 也就是说最外层的 list 引用是各自独立的，这也是为什么直接 append 到 l1 的操作并不会影响 l2 的值。可是 l1 的内容并没有被复制，l1 和 l2 都 refer to 相同的 object references. 所以一旦这里面包含了对 mutable object 的引用，如 list, 就会出现对 l1 和 l2 的操作互相影响的状况。

## Deep and Shallow Copies of Arbitrary Objects.

```python
import copy

>>> l1 = [3, [66, 55, 44], (7, 8, 9)]
>>> l2 = copy.copy(l1)
>>> l3 = copy.deepcopy(l1)
>>> l1[1].append(33)
>>> l1
[3, [66, 55, 44, 33], (7, 8, 9)]
>>> l2
[3, [66, 55, 44, 33], (7, 8, 9)] # 改变 l1, 也影响了 l2
>>> l3
[3, [66, 55, 44], (7, 8, 9)] # l1 的改变不影响 l3

```

值得注意的，object 有时候会有 cyclic 引用，此时如果使用 deepcopy 就会进入死循环。而且，deepcopy 有时候也有可能 too deep. Object 有时候会使用 external resource 或者 singleton， 而我们并不想要复制他们。

## Function Parameters as References

### Call by Sharing

对于每一个传入 python function 的参数，函数内部使用的都是这个参数的　shallow copy. 也就是说，如果传入的参数是　mutable 类型，那么原参数的值也有可能被改变。例如：

```python
>>> def f(a, b):
...     a += b
...     return a
>>> x = 1
>>> y = 2
>>> f(x, y)
3
>>> x, y
(1, 2)
>>> a = [1, 2]
>>> b = [3, 4]
>>> f(a, b)
[1, 2, 3, 4]
>>> a, b
([1, 2, 3, 4], [3, 4])  # a 的值也发生了变化
>>> t = (10, 20)
>>> u = (30, 40)
>>> f(t, u)
(10, 20, 30, 40)
>>> t, u
((10, 20), (30, 40))
```

###  不要用　mutable type 作为　Parameter Defaults

```python
class HauntedBus:
    """A bus model haunted by ghost passengers"""
    def __init__(self, passengers=[]):
        self.passengers = passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

>>> bus1 = HauntedBus(['Alice', 'Bill'])
>>> bus1.passengers
['Alice', 'Bill']
>>> bus1.pick('Charlie')
>>> bus1.drop('Alice')
>>> bus1.passengers
['Bill', 'Charlie']
>>> bus2 = HauntedBus()
>>> bus2.pick('Carrie')
>>> bus2.passengers
['Carrie']
>>> bus3 = HauntedBus()
>>> bus3.passengers　# bus3 的 default 不再是　[]
['Carrie']
>>> bus3.pick('Dave')
>>> bus2.passengers
['Carrie', 'Dave']
>>> bus2.passengers is bus3.passengers
True
>>> bus1.passengers
['Bill', 'Charlie']

```

因此，如果 parameters 有可能收到　mutable values, 我们通常将 default value 设为　None.

### Defensive programming with mutable parameters

还有另一种情况是，我们可能并不想要传入的参数本身发生变化，如下：

```python
class TwilightBus:
    """A bus model that makes passengers vanish"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

>>> basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
>>> bus = TwilightBus(basketball_team)
>>> bus.drop('Tina')
>>> bus.drop('Pat')
>>> basketball_team
['Sue', 'Maya', 'Diana']　# 经过　TwilightBus 的操作之后，basketball_team 本身的值不应该发生变化
```

除非你的意图就是要改变传入的参数，否则就使用参数的拷贝。例子如下：

```python
def __init__(self, passengers=None):
    if passengers is None:
        self.passengers = []
    else:
        self.passengers = list(passengers)
```

## del and garbage collection

`del` 删除的是　names 不是　objects，　当一个 object 的 reference count 为　０，他就会被 GC 处理掉。

## Weak reference (待续)

一个 object　的 weak reference 并不会增加他的　reference count.

```python
>>> import weakref
>>> a_set = {0, 1}
>>> wref = weakref.ref(a_set)
>>> wref
<weakref at 0x100637598; to 'set' at 0x100636748>
>>> wref()
{0, 1}
>>> a_set = {2, 3, 4}
>>> wref()
{0, 1}
>>> wref() is None
False
>>> wref() is None
True
```

weak reference 可以应用于 application caching, 但是比起直接使用　weakref.ref, 我们更推荐使用　weakref collections.

### The weakValueDictionary skit

```python
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

>>> import weakref
>>> stock = weakref.WeakValueDictionary()
>>> catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
...                     Cheese('Brie'), Cheese('Parmesan')]
...
>>> for cheese in catalog:
...     stock[cheese.kind] = cheese
...
>>> sorted(stock.keys())
['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
>>> del catalog
>>> sorted(stock.keys())
['Parmesan'] # as catalod is deleted, most of the values are gone
>>> del cheese
>>> sorted(stock.keys())
[]
```

