## 创建 models

在 `codingtool/models` 里定义所有的 Models 对象。`Model field` 的官方文档请戳 `=>`
[Model field reference](https://docs.djangoproject.com/en/1.8/ref/models/fields/#module-django.db.models.fields)

这里需要先简要地介绍一下我要写的这个 web app. 我目前是在做关于 Explanation 的 Qualitative Analyze，目前的样本选择的是所有关于 Dijkstra 算法的解释，对于每一篇解释文档，我进行 Tag，Tag 所包括的信息有解释的目标，运用的策略 以及使用的 Notation. 同时，对于每一篇文档，我需要保存所有 Tags 的顺序。这个 app 的第一版所需要有的功能就是可以让我轻松的输入tags，并保存到数据库或者文件中。

所以我的 models 也比较简单，大致长下面这样。想要看源码请戳 `=>` [models.py](https://github.com/SuzyWu2014/qualitative-coding-tool/blob/master/codingtool/models.py)

```python
from django.db import models
import uuid

class Tag(models.Model):
    ...

    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goal = models.CharField(max_length=200, choices=GOAL_CHOICE, default='Problem')
    role = models.CharField(max_length=200, choices=ROLE_CHOICE, default='definition')
    notation = models.CharField(max_length=200, choices=NOTATION_CHOICE, default='English')
    trait = models.CharField(max_length=200, choices=TRAIT_CHOICE, default='None')
    order = models.PositiveIntegerField()


class Explanation(models.Model):
    """Explanation object"""
    explanation_id = models.CharField(max_length=5, primary_key=True)
    source_link = models.URLField()
    evernote_link = models.URLField()
    Tags = models.ManyToManyField(Tag, through='Membership', through_fields=('tag', 'explanation'))


class Membership(models.Model):
    tag = models.ForeignKey(Tag)
    explanation = models.ForeignKey(Explanation)
```
