# Chapter 2: Python Debugger (pdb)

本章来介绍Python debugger: pdb

## 基本用法

使用如下 command 来以 debugging 模式运行 Python script。此命令会停留在 script 的第一行，输入 `n` 逐行往下执行。

```bash
python -m pdb my_script.py
```

## 设置断点：`pdb.set_trace()`

```python
import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())
```

## Commands:

+ `c`: 继续执行
+ `w`：显示当前行的上下文
+ `a`: 打印当前funciton的参数
+ `s`：执行当前行，停在最早可以停的地方
+ `n`：持续执行至下一行结束