#!/bin/env python
#coding=utf-8
from django.conf.urls import patterns, include, url
from web_api import views

urlpatterns = patterns('',
   url(r'^get_config/',views.get_config),
)                    