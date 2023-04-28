from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^basic_info/$', views.basic_info, name='basic info'),
    re_path(r'^avatar/$', views.avatar, name='avatar'),
    re_path(r'^teacherstudents/$', views.teacher_students, name='teacher students'),
    re_path(r'^papers/$', views.papers, name='scholar papers'),
]