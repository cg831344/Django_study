from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homework12.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',views.Index),
    url(r'^getprovince/',views.GetProvice),
    url(r'^getcity/',views.GetCity),
    url(r'^getcounty/',views.GetCounty),
)

