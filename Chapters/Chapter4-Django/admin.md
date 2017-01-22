# Django admin 管理后台

## 注册 Models

Django 提供了后台管理页面来增删改 Model 的数据。要使用这个功能，首先要在 `codingtool/admin.py` 文件里注册我们创建的 Models。

```python
from django.contrib import admin
from .models import Goal, Role, Explanation, Notation, Code, Membership

admin.site.register(Goal)
admin.site.register(Role)
admin.site.register(Notation)
admin.site.register(Explanation)
admin.site.register(Code)
admin.site.register(Membership)
```

## 创建 admin super user

```bash
(env)$ python manage.py createsuperuser
```

## 使用 admin 后台管理

+ 1 启动服务器：`python manage.py runserver`
+ 2 Go to: `http://127.0.0.1:8000/admin`

## 自定义后台管理界面

```python
# in admin.py
@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('explanation',
                    'position',
                    'goal',
                    'is_partial',
                    'is_emphasized',
                    'has_many'
                    )
    list_filter = ('roles', 'notations')
    filter_horizontal = ('roles', 'notations') # 为括号中的 fields 添加复选效果
```

为需要自定义功能的 Model 添加 ModelAdmin 类，具体参数可参照 [The Django admin site](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_vertical)
