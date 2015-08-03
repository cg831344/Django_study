from django.conf.urls import patterns, include, url
from django.contrib import admin
#from app01 import  views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^userlist/(?P<view>\w*)/(?P<id>\d*)', views.List,{'view':'list','id':1}),
#    url(r'^userlist/(?P<id>\d*)', views.List,{'id':1}),
    url(r'web/',include('app02.url')),
    
                        
                        )


urlpatterns += patterns('app01.views',
    url(r'^view1/$','index'),
    url(r'^model/$','Model'),
                        )

urlpatterns += patterns('app02.views',
    url(r'^view2/$','index'),
                        )
