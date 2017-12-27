#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: urls.py 
@time: 2017/12/24
关于微博的映射写到这里
"""
from django.conf.urls import url
from blog import views

urlpatterns = [
	url(r'new/story',views.intro),
	url(r'pay/index', views.index,name='alex'),


	#---------------创建表
	url(r'book/create_info',views.create_info),
	url(r'aggregation',views.aggregation),



]



from django.conf.urls import url
from blog import views