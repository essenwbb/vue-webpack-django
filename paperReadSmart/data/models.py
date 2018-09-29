from django.db import models


class Paper(models.Model):
    title = models.CharField('标题', max_length=200)
    summary = models.CharField('摘要', max_length=1000)
    content = models.CharField('正文', max_length=100000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class LifeGdp(models.Model):
    title = models.CharField('标题', max_length=200)
    json_data = models.CharField('json数据', max_length=10000)
    create_time = models.DateTimeField('date create')

    def __str__(self):
        return self.title
