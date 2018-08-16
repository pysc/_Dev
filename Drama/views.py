from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.conf import settings
from Common.requests import *

import uuid
import datetime
import pymysql
import xlrd


# 首页
def index(request):
    keyword = get_request_keyword(request, 'GET')
    page = get_request_page(request, 'GET')
    limit = get_request_limit(request, 'GET')

    return render(request, 'SchoolManage/index.html', {'keyword': keyword,
                                                       'page': page,
                                                       'limit': limit})

