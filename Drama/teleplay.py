import pymysql
from django.shortcuts import render
from django.http import JsonResponse
from Drama.models import *
import pymysql, time, datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


class Teleplay(object):
    def __init__(self, name='teleplay'):
        self._registry = {}
        self.name = name

    def get_urls(self):
        from django.conf.urls import url, include

        urlpatterns = [
            url(r'^$', self.index, name='index'),
            # url(r'^details/$', self.details, name='details'),
        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'teleplay', self.name

    def index(self, request):

        drama_list = Drama.objects.filter(type='电视剧').all()  # 获取所有contacts,假设在models.py中已定义了Contacts模型
        paginator = Paginator(drama_list, 12)  # 每页12条
        page = request.GET.get('page')
        try:
            rows = paginator.page(page)  # contacts为Page对象！
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            rows = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            rows = paginator.page(paginator.num_pages)

        return render(request, 'index.html', {'rows': rows})


teleplay = Teleplay()
