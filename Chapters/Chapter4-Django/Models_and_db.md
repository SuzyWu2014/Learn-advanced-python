## 创建 models

在 `codingtool/models` 里定义所有的 Models 对象。`Model field` 的官方文档请戳 `=>`
[Model field reference](https://docs.djangoproject.com/en/1.8/ref/models/fields/#module-django.db.models.fields)

这里需要先简要地介绍一下我要写的这个 web app. 我目前是在做关于 Explanation 的 Qualitative Analyze，目前的样本选择的是所有关于 Dijkstra 算法的解释，对于每一篇解释文档，我进行 Tag，Tag 所包括的信息有解释的目标，运用的策略 以及使用的 Notation. 同时，对于每一篇文档，我需要保存所有 Tags 的顺序。这个 app 的第一版所需要有的功能就是可以让我轻松的输入tags，并保存到数据库或者文件中。

所以我的 models 也比较简单，大致长下面这样。想要看源码请戳 `=>` [models.py](https://github.com/SuzyWu2014/qualitative-coding-tool/blob/master/codingtool/models.py)

```python
from django.db import models
import uuid

class Explanation(models.Model):
    """Explanation unit"""
    explanation_id = models.AutoField(primary_key=True)
    explanation = models.CharField(max_length=16)
    source_link = models.URLField(max_length=256)
    evernote_link = models.URLField(max_length=256, blank=True)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.explanation
...

class Code(models.Model):
    """Code object for each explanation unit"""
    code_id = models.AutoField(primary_key=True)
    explanation = models.ForeignKey(Explanation)
    position = models.IntegerField()
    goal = models.ForeignKey(Goal)
    role = models.ForeignKey(Role)
    notations = models.ManyToManyField(Notation,
        through="Membership", through_fields=('code', 'notation'))
    is_partial = models.BooleanField(default=False)
    is_emphasized = models.BooleanField(default=False)
    has_many = models.BooleanField(default=False)
    description = models.CharField(max_length=256, blank=True)


class Membership(models.Model):
    code = models.ForeignKey(Code)
    notation = models.ForeignKey(Notation)
```

## 在你的数据库中为模型创建数据表

利用 `manage.py` 在更新或生成数据库中的表结构

```
python manage.py makemigrations codingtool
python manage.py migrate codingtool
```
