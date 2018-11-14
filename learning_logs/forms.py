#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 14:20
# @Author  : dingyifei
# 新建表单
from django import forms
from .models import Topic,Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}