from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_08day13.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/(\d*)', views.index),
)

urlpatterns +=  patterns('app02.views',
    url(r'^app02/login','login'),
    url(r'^app02/index','index'),
    url(r'^app02/logout','logout'),
    )