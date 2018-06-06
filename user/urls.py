from django.conf.urls import url, static
# from django.conf import settings
# from myblog import settings

from user import views

urlpatterns = [
    url(r'register/$', views.register, name='register'),
    url(r'personInfo/$', views.personInfo, name='personInfo'),
]