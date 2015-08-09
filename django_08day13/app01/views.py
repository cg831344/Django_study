#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from app01 import models
from app01 import http_helper
# Create your views here.


from app01 import common
from django.utils.safestring import mark_safe

def index(request,page):
    #操作数据库,进行分页
    '''
    try:     
        page = int(page)
    except BaseException,e:
        page = 1
    '''
    page = common.try_int(page,1) #将char转换为int，如果不能转换就成为默认值
    count = models.Host.objects.all().count()
    
    
    pageObj = http_helper.PageInfo(page,count)
    
    
    result = models.Host.objects.all()[pageObj.start():pageObj.end()]
    page_string = http_helper.Pager(page, pageObj.all_page_count())
    
    ret = {'data':result,'count':count,'page':page_string}
    return render_to_response('index.html',ret)


