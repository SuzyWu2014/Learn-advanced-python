# 创建第一个视图

View 是存放应用逻辑的地方，他可以从我们创建的 Model 中获取数据，并将它传递给 template 以显示在页面上。View 简单来说就是一个 Python function.

## 添加 View

打开 `codingtool/views.py`, 添加以下内容：

```python

from django.shortcuts import render


def add_code(request):
    return render(request, "codingtool/add_code.html", {})
```

## 添加模版

在 application 文件夹下添加模版文件夹以及模版 `add_code`, 文件目录长这样：

```
codingtool
├── templates
│   └── codingtool
│       └── add_code.html
```

