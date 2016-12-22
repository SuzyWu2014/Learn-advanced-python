# 三元运算符

# 常用的形式

```python
is_fat = True
state = "fat" if is_fat else "not fat"
```

# 不常用的形式

```python
fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)
# Output: Ali is fat
```

上式成立的原因是 `True = 1`,`False = 0`。尽量避免这种写法。

# 一个奇怪的异常

```python
condition = True
print(2 if condition else 1/0)
#Output is 2

print((1/0, 2)[condition]) #这是由于使用 tupled 三元运算符， tuple 会先编译
#ZeroDivisionError is raised
```

