from django.db import models


# Create your models here.
class Drama(models.Model):
    name = models.CharField('名称', max_length=100, null=True, blank=True)
    img = models.CharField('图片链接地址', max_length=200, null=True, blank=True)
    url = models.CharField('网址', max_length=200, primary_key=True)
    intro = models.TextField('简介', max_length=2000, null=True, blank=True)
    type = models.CharField('分类', max_length=10,null=True, blank=True)
    LOAD_TIME = models.DateTimeField('入库时间', blank=True, null=True, auto_now=True)
