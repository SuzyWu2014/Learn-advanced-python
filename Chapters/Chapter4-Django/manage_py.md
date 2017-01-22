# Django 命令行工具

## 使用

```bash
$ django-admin <command> [options]
$ python manage.py <command> [options]
$ python -m django <command> [options]

```

django-admin 和 manage.py 其实提供了一样的功能，但是 `manage.py` 帮你做了以下设定：

+ 将 project 的 package 放在 `sys.path`
+ 设置了 DJANGO_SETTINGS_MODULE 环境变量，即指向了 `setting.py`

## 常用操作

```bash
# 导出数据
python manage.py dumpdata codingtool --exclude=auth --exclude=contenttypes > data.json

```