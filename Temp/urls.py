'''
Created on Mar 6, 2015

@author: kartiksahnbhag
'''

from django.conf.urls import patterns, url
from Temp import views

urlpatterns = patterns('',
    url(r'^$', views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^schedule/$',views.schedule,name='schedule'),
    url(r'^error/$',views.error,name='error'),
    url(r'^addtask/$',views.addtask,name='addtask'),
    url(r'^gettask/$',views.gettask,name='gettask'),
    url(r'^getLastCount/$',views.getLastCount,name='getLastCount'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^deletetask/$',views.deletetask,name='deletetask'),
)

