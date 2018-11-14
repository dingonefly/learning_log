#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 21:24
# @Author  : dingyifei
'''定义learning_logs的URL模式'''

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    #显示所有主题
    url(r'^topics/$', views.topics, name='topics'),
    #特定主体的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新的条目
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #用于编辑新的条目
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]
