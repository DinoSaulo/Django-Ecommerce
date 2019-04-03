# coding=utf-8

from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registro/$', views.register, name='register'),
]