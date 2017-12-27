"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include



from django.conf.urls import url
from blog import views



'''
通过for循环,挨个匹配,匹配到break返回
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current_time/', views.current_time),





    #映射userInfo
    #path('userInfo/', views.userInfo),
    #url配置就是一个映射表:即url与视图函数之间的映射
    #url(r'^userInfo',views.userInfo),

    #url(r'^articles/2003/$', views.special_case_2003),#以..开头..结尾
    ########下面叫无名分组
    #url(r'^articles/[0-9]{4}/$', views.year_archive),
    #url(r'^articles/([0-9]{4})/$', views.year_archive),#()代表分组,我们可以通过一个变量接收了,如果有三个(),就用三个变量接收;   在url上面可以通过这种格式,给视图函数传递参数,参数就是url的路径,url可以作为路径参数传递到视图函数里面
    #url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.year_archive),  #no_named group

    #########有名分组
    #year_archive() got an unexpected keyword argument 'month'如果进行了分组,起了名字,那么views里面的形参必须按照我起的名字来,不能随便定义了

    # url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.year_archive),


    # url(r'^index', views.index,{"name":'alex'}),#他会去index函数里面找对应的形参,没有就报错
    #参数三:
    #url(r'^index/(?P<name>[0-9]{4})/', views.index,{"name":'alex'}),#后面的name会覆盖前面的
    #参数四
    #url(r'^pay/index', views.index,name='alex'),#name是一个别名就是第一个参数的别名,无论你第一个参数怎么变,只要用了别名我前端都不用改


    #这个文件是一个全局的文件,如果url都写在这一个文件里面,它太大了,会造成干扰,没有解耦
    #全局的只做一个指派,开头是blog,就去blog里面找url
    #url(r'login', views.login),
    # url(r'home', views.home),
    # url(r'cur_time',views.current_time),
    path('blog/', include('blog.urls')),


    #===================template 练习
    url(r'tem_index/',views.tem_index),
    url(r'tem_login/',views.tem_login),
    #==================订单系列
    url(r'ordered',views.ordered),
    url(r'shopping_car/',views.shopping_car),



]
#year_archive# () takes 1 positional argument but 2 were given 这个函数接收了一个参数,但是应该有两个参数被给












