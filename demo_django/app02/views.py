from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request
# Create your views here.

def index(request):
    return HttpResponse('<h1>app02</h1>')

def test1(request):
    return HttpResponse('<h1>tes1</h1>')

def test2(request):
    return HttpResponse('<h1>tes2</h1>')