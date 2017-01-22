# 配置 URL 的路由

在 Django 中，我们使用 URLconf 机制，将 URL 匹配成相对应的 View。

## 配置整个 site 的路由机制

打开 `qualitative_coding/urls.py`, 添加导向 Application codingtool的路由：

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('codingtool.urls')),
]
```

如果有多个 Application，也将在这里配置在各个应用的路由。

## 配置 Application 的路由

在 Application 的文件夹下添加 `urls.py`， 并编辑如下：

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^codes/add$', views.add_code, name='add_code'),
]

```

`add_code` 是 `views.py` 中的一个 function, 以上的代码表示 所有来自 `codes/add` 的 请求将由 `add_code` 这个方法来处理。