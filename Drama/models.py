from django.db import models

# Create your models here.
class Drama(models.Model):
    name = models.CharField('名称', max_length=100, blank=True)
    img = models.CharField('图片链接地址', max_length=200, blank=True)
    url = models.CharField('网址', max_length=200, primary_key=True)
    intro = models.TextField('简介', max_length=2000, default=None)
    LOAD_TIME = models.DateTimeField('入库时间', auto_now=True)

