# Chapter 5: Decorators

Decorators 是 Python 中很重要的一部分。简单的说，他们是用来改变其他 function 的功能的 function. 同时 decorators 也使我们的代码更简短更  pythonic。

首先，我们需要了解怎样写我们自己的 decorator。

## Python 里的一切都是 Object.

让我们先来看看 Python 里的 function：

```python
def hi(name="yasoob"):
    return "hi " + name

print(hi())
# output: 'hi yasoob'

# We can even assign a function to a variable like
greet = hi
# We are not using parentheses here because we are not calling the function hi
# instead we are just putting it into the greet variable. Let's try to run this

print(greet())
# output: 'hi yasoob'

# 假如我们删掉这个旧的 hi function!
del hi
print(hi())
#outputs: NameError

print(greet())
#outputs: 'hi yasoob'
```

## 在 function 内部声明 function

```python
def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
#output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function

# This shows that whenever you call hi(), greet() and welcome()
# are also called. However the greet() and welcome() functions
# are not available outside the hi() function e.g:
# 定义在方法内部的方法，不能在外部直接被访问

greet()
#outputs: NameError: name 'greet' is not defined
```

## function 作为返回值

```python
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a)
#outputs: <function greet at 0x7f2143c01500>

#This clearly shows that `a` now points to the greet() function in hi()
#Now try this

print(a())
#outputs: now you are in the greet() function

print(hi()())
#outputs: now you are in the greet() function
```

## 将 function 作为其他 function 的参数

```python
def hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)
#outputs:I am doing some boring work before executing hi()
#        hi yasoob!
```

## 第一个 decorator

```python
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()
```

如上文中的代码所示，decorator 可以把一个方法包裹起来然后添加一些 behavior，另一种更简单的写法是用 `@`。

```python
@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a_function_requiring_decoration()
#outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

#the @a_new_decorator is just a short way of saying:
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
```

但是这里有一个问题，如果我们执行一下代码：

```python
print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction
```

这明显不是我们想要的，“a_function_requiring_decoration” 才是我们想要返回的。Python 提供了一个简单的方法来解决这个问题： `functools.wraps`.

```python
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration
```

让我们来看一个 decorator 的模版：

```python
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run
```

我们将要被 decorated 的 function 传入 `@wraps`，相应的函数名，docstring, 参数列表等将会被复制进来。

### Use-cases

#### Authorization

Decorators 可以拿来验证是否一个用户被授权使用某个网页。这个在 Flask 跟 Django 中经常被使用。下面是一个例子：

```python
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated

```

#### Logging

日志是另一个常见的例子：

```python
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
# Output: addition_func was called
```

## 带参数的 decorator

```python
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# A file called out.log now exists, with the above string

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# A file called func2.log now exists, with the above string
```

上面的代码中，我们可以把日志写入一个文件。但有时候，我们还想要这个 decorator 有其他的辅助功能，比如当系统发生错误时，你需要发邮件给管理员。幸运的是，Decorator 也可以是一个类。
```python
class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log_string = func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self.logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

    def notify(self):
        # logit only logs, no more
        pass

@logit()
def myfunc1():
    pass
```

现在我们可以写一些子类来添加 email 的功能.

```python
class email_logit(logit):
    '''
    A logit implementation for sending emails to admins
    when the function is called.
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # Send an email to self.email
        # Will not be implemented here
        pass
```

