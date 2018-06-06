#!/usr/local/python3/bin/python3
from django.conf.urls import url
from blog import views
from .feeds import PostRssFeed


urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'detail/', views.detail, name='detail'),
    url(r'p_time/(?P<year>[0-9]{4})/(?P<month>[1-9]|1[0-2])/(?P<day>[0-9]|1[0-9]|2[0-9]|3[0-1])/$', views.p_time, name='p_time'),
    url(r'p_category/', views.p_category, name='p_category'),
    url(r'p_tags/', views.p_tags, name='p_tags'),
    url(r'rss/', PostRssFeed(), name='rss'),
    url(r'search/', views.search, name='search'),
    url(r'relation/', views.relation, name='relation'),
]
