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

官方文档请戳 `==>` [The Django admin site](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_vertical)

简单来说主要可配置以下内容：

+ `ModelAdmin`: 配置针对 Registered Models 的增删改界面的功能

```python
# in admin.py
@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    # Model list 页面
    empty_value_display = '-- empty --'
    list_display = ('explanation',
                    'position',
                    'goal',
                    'role',
                    'is_partial',
                    'is_emphasized',
                    'has_many'
                    )
    list_filter = ['notations', 'explanation', 'role', 'goal']
    show_full_result_count = True
    ordering = ['explanation', 'position']
    list_per_page = 50
    filter_horizontal = ['notations']

    # 添加修改 Model 页面
    radio_fields = {"goal": admin.HORIZONTAL}
    save_on_top = True
```

+ `InlineModelAdmin`: 配置在 List 页面添加 `add model` 功能，但是不针对当前 model

```python
# in admin.py

class CodeInline(admin.TabularInline):
    model = Code


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('goal', 'description')
    inlines = [CodeInline, ]
```
