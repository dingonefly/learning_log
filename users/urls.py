#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 21:24
# @Author  : dingyifei
'''定义users的URL模式'''

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登录页
    url(r'^login/$', login,{'template_name':'users/login.html'},
        name='login'),
    url(r'^logout/$', views.logout_view,name='logout'),
    url(r'^register/$', views.register,name='register'),


]
