#!/bin/env python
#coding=utf-8

from django.conf.urls import *
from app02 import views
urlpatterns = patterns('',
    url(r'1/$',views.test1),
    url(r'2/$',views.test2),                   
                       )
