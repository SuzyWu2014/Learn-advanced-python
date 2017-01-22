# 环境搭建 VS 项目初始化

## Python Version

Django 是支持 python2 和 python3 的，尤其是 Django 1.6 之后，官方宣称 Django 对 Python3 有了稳定的支持。我也算借机正式从 python2 转换到 Python3， 也就是说下面的操作全部基于 Python3.

## 虚拟环境

Virtualenv 是一个极好用的工具，我在[这篇 Post](http://suzywu2014.github.io/python/2016/06/15/virtualenv-wiki) 里简单介绍了 Virtualenv 的基本使用命令。这里介绍另一种虚拟环境的使用方法：

```python
python -m venv myvenv # 创建虚拟环境
source myvenv/bin/activate # 激活虚拟环境
# 我使用的是 fish, 所以用到的是 activate.fish. 不过这个 activate.fish 有 bug, 大家根据错误提示删掉两个 $ 就好。
deactive
```

## 安装 Django

```
(myenv) pip install django
```

## 初始化项目

### 创建 project

```bash
(myenv) django-admin startproject qualitative_coding .
```

不要忘记末尾的 `.`!

`django-admin.py` 是一个脚本，将自动帮你创建目录和文件。现在我的目录结构就是下面这样：

```
├── manage.py
└── qualitative_coding
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

下面来看这些文件都是做什么的：

+ `manage.py` 是一个帮助管理站点的脚本。他的主要作用就是在不需要安装任何东西的情况下，在本机上启动一个 web 服务器。
+ `setting.py` 文件包含的是网站的配置数据。
+ `urls.py` 文件包含 urlsolver 所需的模型的列表。换句话说，就是负责 url routing, 将 request 根据 url 的路径转到相应的位置来处理。

### 更改设置

#### 修改时区

在 `setting.py` 文件中，找到 `TIME_ZONE` 并将其设置为你所在的时区， 时区列表可查看 [wikipedia timezones list](https://www.wikiwand.com/en/List_of_tz_database_time_zones). 例如：

```python
TIME_ZONE = 'US/Pacific'
```

#### 添加静态文件路径

下拉到 `setting.py` 的最底部， 在 `STATIC_URL` 添加 `STATIC_ROOT`：

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

### 设置数据库

Django 默认使用 `sqlite3`, 你可以在 `setting.py` 中看到：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

如果你需要创建一个数据库，则运行以下命令：

```bash
python manage.py migrate
```

#### 设置 Mysql 数据库

##### 安装 modules

+ 安装 mysql

```bash
# MacOS
brew mysql

alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin
```

+ 安装 python module

```bash
# 仅支持 python2
pip install MySQLdb

# Python 3.3 以上版本
pip3 install mysqlclient

# 假如以上都无法成功安装
pip3 install PYMySQL

# 并在 setting.py 上加入一下代码
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
```


```python
# in setting.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/mysql.cnf', # 绝对路径
        },
    }
}

#mysql.cnf
[client]
database = NAME
host = HOST NAME or IP
user = USER
password = PASSWORD
default-character-set = utf8
```



## 启动服务器

```
(myenv) python manage.py runserver

### output ####

Performing system checks...

System check identified no issues (0 silenced).
December 20, 2016 - 17:55:11
Django version 1.10.4, using settings 'qualitative_coding.settings'
Starting development server at http://127.0.0.1:8000/
```

## Note

如果使用 mysql, 要先在数据库了创建数据库：

```sql
CREATE DATABASE DB_NAME;
```
