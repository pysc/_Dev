import pymysql
from django.shortcuts import render
from django.http import JsonResponse
from Drama.models import *
import pymysql, time, datetime


class Teleplay(object):
    def __init__(self, name='teleplay'):
        self._registry = {}
        self.name = name

    def get_urls(self):
        from django.conf.urls import url, include

        urlpatterns = [
            url(r'^$', self.index, name='index'),
            # url(r'^unhandle_alarm_show/$', self.unhandle_alarm_show, name='unhandle_alarm_show'),

        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'teleplay', self.name

    def index(self, request):
        result = {}
        total = Drama.objects.filter().all().count()
        rows = Drama.objects.all().order_by('-LOAD_TIME')[1:10]
        for rows in rows:
            result['total'] = total
            result['rows'].append({
                'name': rows.name,
                'img': rows.img,
            })
        return render(request, 'index.html', result)

    # 未处理报警
    def unhandle_alarm_show(self, request):
        result = {
            'total': None,
            'rows': []
        }

        page_no = int(request.POST.get('page', 1))  # 第几页
        page_size = int(request.POST.get('rows', 10))  # 每页显示几条数据
        sort = request.POST.get('sort', '')  # 按照哪个字段进行排序
        order = request.POST.get('order')  # 是升序还是降序排序
        if order == 'desc':
            sort = '-' + sort

        BJSJ = request.POST.get('BJSJ', '')  #
        SSPC = request.POST.get('SSPC', '')  #
        BJJB = request.POST.get('BJJB', '')  #
        BJLX = request.POST.get('BJLX', '')  #

        if BJSJ:
            year = BJSJ[0:4]
            month = BJSJ[5:7]
            day = BJSJ[8:10]

        start = (page_no - 1) * page_size
        end = page_no * page_size
        print(start, end)
        total = Teleplay.objects.filter(SFYCL=0).all().count()

        searchCondition = {'BJSJ__date': BJSJ, 'SSPC': SSPC, 'BJJB': BJJB, 'BJLX': BJLX, }
        kwargs = self.getKwargs(searchCondition)

        if sort == '':
            print('默认排序规则')
            alarms = Teleplay.objects.filter(SFYCL=0).filter(**kwargs).order_by('-BJSJ')[start:end]
        else:
            print('用户自定义的排序规则', sort)
            alarms = Teleplay.objects.filter(SFYCL=0).filter(**kwargs).order_by(sort)[start:end]

        for teleplay in alarms:
            result['total'] = total
            result['rows'].append({
                'BJSJ': teleplay.BJSJ.strftime('%Y-%m-%d %H:%M:%S'),
                'SSPC': teleplay.SSPC,
                'BJJB': teleplay.BJJB,
                'BJLX': teleplay.BJLX,
                'BJSM': teleplay.BJSM,
            })
        return JsonResponse(result, )


teleplay = Teleplay()
