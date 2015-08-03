#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request

# Create your views here.

data = ['重庆','南川','服了']

def index(request):
    return HttpResponse('<h1>app01</h1>')

def List(request,view,id):
    if id:
        result = data[int(id)]
        return HttpResponse('<h1>'+result+'</h1>')
        
    else:
        result = '<br/>'.join(data)    
        return HttpResponse('<h1>'+result+'</h1>')
   
from app01.models import *

def Model(request):
    model = ColorDic.objects.values('ColorName')

    print model

    return HttpResponse(model)

