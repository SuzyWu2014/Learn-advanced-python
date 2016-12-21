# 创建应用程序

我们使用 `manage.py` 来创建 app 目录：

```
(myenv) python manage.py startapp codingtool
```

此时的文件目录应该长这样：

```
├── codingtool
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── qualitative_coding
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

创建应用程序后，我们还需要告诉 Django 如何使用它。 在 `setting.py` 中设置 app 如下：

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'codingtool',
]
```
