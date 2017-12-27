#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: mytag.py 
@time: 2017/12/25 
"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()   #register的名字是固定的,不可改变




#参数不能超过2个
@register.filter
def filter_multi(v1,v2):
    return  v1 * v2

#不能用于if语句
@register.simple_tag
def simple_tag_multi(v1,v2):
    return  v1 * v2


@register.simple_tag
def my_input(id,arg):
    result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
    return mark_safe(result)

@register.simple_tag
def my_add100(v1):
	return  v1+100

@register.simple_tag
def my_add1000(v1,v2,v3):
	return  v1+v2+v3