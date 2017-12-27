from django.shortcuts import render,HttpResponse,render_to_response,redirect
from django.template.loader import get_template
from django.template import Template,Context
# Create your views here.

'''
render :渲染的意思(把变量嵌套到html里,解析完之后在实例化HttpResponse在发给浏览器)
django:每一次改完一点内容不需要重启
它自己的模板语言:jinja2

HttpResponse:它本身是一个类,后面加的字符串是实例化出来的对象,这个对象是返回给浏览器的对象,所有返回给浏览器的内容都是通过它实现的
HttpResponse,render区别:相比就是多了个渲染功能,底层还是调用的HttpResponse

取数据通过 req取
发数据通过HttpResponse 他来发

总共做了两件事情进行映射关系,视图函数(用到了模板),

python manage.py shell 进入django命令行

>>> from django.template import Context, Template
>>> t = Template("hello{{name}}")
>>> c = Context({"name":"lex"})
>>> t.render(c)
'hellolex'

1个Template对象可以渲染多个context对象,可重复使用
t.render(Context({"name":"lex1"}))
'''

import datetime
from blog import models
def current_time(req):
    times = datetime.datetime.now()
    #第一种:
    t = Template('<html><body>现在时刻是:<h1 style="color:red">{{current_date}}</h1></body></html>')
    c = Context({'current_date':times})
    html = t.render(c)
    return HttpResponse(html)
    #第二种(推荐)
    # return render(req,"current_time.html",{"time":times})#第二个参数是模板,第三个参数是上下文
user_list = []
def userInfo(req):
	#首先知道post还是get
	if req.method == 'POST':
		username = req.POST.get("username",None) #有的话拿出来,没有返回None
		sex = req.POST.get("sex",None) #有的话拿出来,没有返回None
		email = req.POST.get("email",None) #有的话拿出来,没有返回None
		#user = {"username":username,"sex":sex,"email":email}
		#user_list.append(user)
		#创建数据
		models.UserInfo.objects.create(
			username=username,
			sex=sex,
			email=email,
		)
	#获取数据
	user_list = models.UserInfo.objects.all()
	return render(req,"index.html",{"user_list":user_list}) #将user和index.html,通过render根据模板语言的语法规范进行渲染
#后端传给前端,并不意味着前端已经被浏览器渲染了,是后端传给前端之后,前端渲染完了,在发给浏览器,浏览器再去渲染


def special_case_2003(req):
	return HttpResponse("<h1>2003</h1>")

def year_archive(req,year,month): #到视图函数这里接收的都是字符串,如果是无名分组,那么这个有位置关系,位置一一对应,有名分组则没有位置关系
	return HttpResponse("<h1>%s-%s</h1>"%(year,month))

def index(req):
	if req.method == "POST":
		username = req.POST.get('user')
		password = req.POST.get('pwd')
		if username == 'alex' and password == '123':
			return HttpResponse("<h1>登陆成功</h1>")
	#return render(req,'login.html')

	#return render_to_response("new.html",{"name":"你好render_to_response","eric":"big",})  #这个写法不用加req了,其他功能跟render一样

	eric = 'new'
	name = '你好'
	#return render_to_response("new.html",locals())  #locals是本地变量的意思,加了他直接获取所有变量,前端直接用变量名就能拿到数据了
		#但是有一个弊端
	#html里面{% %}里面放的是语句,{{}}里面放的是变量
	#locals()效率不高,他会把其他的变量也放里面了,全给前端
	#redirect 跳转用的比较重要
	return redirect("http://www.baidu.com")

def intro(req):
	return HttpResponse('哈哈')

def login(req):
	if req.method == 'POST':
		if 1:#提交的数据从库取出匹配
			return redirect("/home/") #走url路径,访问home函数
			# return render(req,"home.html") #这个直接返回html页面,

	return render(req,"login.html")


def home(req):
	name = "小胡"
	return render(req,"home.html",{'name':name})

#==============temp练习
def tem_index(req):
	s1 = [11,22,33]
	s2 = {"name":"eric","sex":'男'}
	s3 = datetime.datetime.now()

	class Person:
		def __init__(self,name,age):
			self.name = name
			self.age = age

	s4 = Person('小军',23)
	s5 = "helloH"
	s6 = 50
	s7 = []
	s8 = "<a href='#'>哈哈</a>"
	s9 = 'CPTTTTTTTTTTTT'

	return render(req,'tem_demo/index.html',{'list':s1,"info":s2,'date':s3,'person_obj':s4,'str':s5,'num':s6,'emp':s7,'link':s8,'val':s9})

def tem_login(req):
	if req.method == "POST":
		return HttpResponse("<h1>登录成功</h1>")
	#return render(req,'tem_demo/login.html')
	return render_to_response('tem_demo/login.html')


def ordered(req):

	return render(req,"tem_demo/ordered.html")


def shopping_car(req):
	return render(req,"tem_demo/shopping_car.html" )




from blog.models import Book
from blog.models import Author




'''
# 查询相关API：

#  <1>filter(**kwargs):      它包含了与所给筛选条件相匹配的对象

#  <2>all():                 查询所有结果

#  <3>get(**kwargs):         返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。

#-----------下面的方法都是对查询的结果再进行处理:比如 objects.filter.values()--------

#  <4>values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列 model的实例化对象，而是一个可迭代的字典序列
                                     
#  <5>exclude(**kwargs):     它包含了与所给筛选条件不匹配的对象

#  <6>order_by(*field):      对查询结果排序

#  <7>reverse():             对查询结果反向排序

#  <8>distinct():            从返回结果中剔除重复纪录

#  <9>values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列

#  <10>count():              返回数据库中匹配查询(QuerySet)的对象数量。

# <11>first():               返回第一条记录

# <12>last():                返回最后一条记录

#  <13>exists():             如果QuerySet包含数据，就返回True，否则返回False。

'''
def create_info(req):
	#一对多:一个出版社可以出版多本书,一个书只能被一个出版社出版
	#多对多:一个作者可以有多本书,一本书可以有多个作者
	#添加对象----------------------------------
	#
	# authors = models.Author.objects.filter(id__gt=1)

	#create方式一:
	#一对多两种插入形式一个是 publisher_id,publisher=pub[0]
	# Book.objects.create(
	# 	title="漂流",
	# 	price= 1,
	# 	color="red",
	# 	publisher_id=4,
	# 	#因为外键关系是一对多,publisher只能对应一个对象,
	# )

	# pub = models.Publish.objects.filter(id=4)
	#如果用publisher,要跟一个pub对象,(因为publisher是为这本书绑定一个出版射,一本书只能有一个出版社)
	# Book.objects.create(
	# 	title="漂流22222",
	# 	price= 1,
	# 	color="red",
	# 	publisher=pub[0],
	# 	#因为外键关系是一对多,publisher只能对应一个对象,
	# )

	#方式二:字典创建方式:(推荐)
	# Book.objects.create(**{
	# 	'title':"瓶子",
	# 	'price':10,
	# 	'color':"red",
	# 	'publisher_id':4,
	# 	#因为外键关系是一对多,publisher只能对应一个对象,
	# })

	#get是一个对象,filter是一个对象集合
	#用代码证明多对多的关系,一个作者可以有多本书,一本书可以有多个作者

	#----django自动创建第三张表的情况
	#正向
	# author1 = models.Author.objects.get(id=3)
	# print(type(author1)) #<class 'blog.models.Author'>
	# author2 = models.Author.objects.get(id=4)
	# book = models.Book.objects.filter(id=3)
	# book = models.Book.objects.get(id=3)
	# print(type(book)) #<class 'blog.models.Book'>

	# book.author.add(author1,author2)    #这里author是一个属性  ,book绑定的作者对象集合--->book.author

	# book.author.add(*[author1,author2])    #

	# book.author.add(author1)
	# book.author.add(author2)
	#以上三种add方式都可以

	#反向
	# book1 = models.Book.objects.get(id=3)
	# book2 = models.Book.objects.get(id=4)
	# author = models.Author.objects.get(id=3)
	# author.book_set.add(book1,book2)

	#删除: 多对多
	# book.author.remove(*[author1,author2])    #
	# author.book_set.remove(book1,book2)

	#删除对象-----------------------------------
	#Book.objects.filter(id=2).delete()
	#修改对象
	#方式1:
	#author = Book.objects.get(id=3) #get是一个model对象
	#print(type(author))  #<class 'blog.models.Book'>
	# author.title = "alex"
	# author.save()
	#方式2:
	# q = Book.objects.filter( id = 3 ) #<QuerySet [<Book: jom>]>
	# Book.objects.filter(id=3).update(title="jom") #一定要是一个querySet 对象
	#save没有update效率高,因为save会把一行的数据都更新一遍,而update只更新你有变化的那个字段

	#手动创建第三张表



	#查询---------------------------------------
	#filter 满足条件的筛选
	# book = models.Book.objects.filter(id=3).values() #不指定字段取一条数据
	# print(book)#<QuerySet [{'publisher_id': 4, 'id': 3, 'color': 'red', 'page_num': None, 'title': 'jom', 'price': 10}]>
	# book = models.Book.objects.filter(id=3).values("price") #指定字段取一条数据
	# print(book) #<QuerySet [{'price': 10}]>

	#exclude 与filter相反,不满足的都筛选出来
	# book = models.Book.objects.exclude( id = 3 ).values()
	# print( book )

	#orderby
	#book = models.Book.objects.order_by("id").values() #asc排序
	# book = models.Book.objects.order_by("-id").values() #desc排序
	# print(book)
	#reverse

	#first(?)
	#last(?)
	#exists
	#flag = models.Book.objects.filter(id=10).exists() #是否存在 返回true or flase
	#print(flag)
	#all
	# list = models.Book.objects.all().values()
	# print(list)

	#get
	# book_obj = models.Book.objects.get(id=6)  #一个对象
	# 如何拿到与它绑定的Book对象呢?
	# book_obj = models.Book.objects.first()
	#book_obj = models.Book.objects.last()
	# print(book_obj.price)

	## 正向查找
	# ret1 = models.Book.objects.first()
	# print( ret1.title )
	# print( ret1.price )
	# print( ret1.publisher )
	# print( ret1.publisher.name )  # 因为一对多的关系所以ret1.publisher是一个对象,而不是一个queryset集合[一本书被属于一个出版社]

	# 反向查找
	# ret2 = models.Publish.objects.last()  #通过出本社,找他出版过的书
	# print( ret2.name )
	# print( ret2.city )
	# # 如何拿到与它绑定的Book对象呢?
	# print( ret2.book_set.all() )  # ret2.book_set是一个queryset集合

	# ---------------了不起的双下划线(__)之单表条件查询----------------
	# obj_dic = models.Book.objects.filter(id__lt = 4).values() #id` < 4
	#obj_dic = models.Book.objects.filter(id__gt = 4).values() #`id` > 4
	#obj_dic = models.Book.objects.filter(id__gt = 4,id__lt = 10).values() #(`blog_book`.`id` > 4 AND `blog_book`.`id` < 10)
	# obj_dic = models.Book.objects.filter(id__gte = 3).values() #`blog_book`.`id` >= 3
	# obj_dic = models.Book.objects.filter(id__in = [3,4,5]).values() #`id` IN (3, 4, 5)
	#obj_dic = models.Book.objects.exclude(id__in = [3,4,5]).values() # not in
	#obj_dic = models.Book.objects.filter(title__contains="m").values() # WHERE `blog_book`.`title` LIKE BINARY %m%
	#obj_dic = models.Book.objects.filter(id__range = [3,5]).values() # between
	#obj_dic = models.Book.objects.filter(title__startswith = "j").values() # 以..开头
	#istartswith,endswith,iendswith

	#print(obj_dic)

	# ----------------了不起的双下划线(__)之多表条件关联查询---------------
	#######正向查找条件之一对多
	# obj_dict = models.Book.objects.filter(title='jom').values('publisher__city') #<QuerySet [{'publisher__city': '鹤岗'}]>
	# print(obj_dict) #
	#######正向查找之多对多
	# ret5 = models.Book.objects.filter( title = 'jom' ).values( 'author__name' ) #<QuerySet [{'author__name': '老舍'}, {'author__name': '严父'}]>
	# ret6 = models.Book.objects.filter( author__name = "严父" ).values( 'title' ) #<QuerySet [{'title': 'jom'}, {'title': 'kill'}]>
	# print( ret6 )
	# 注意
	# 正向查找的publisher__city或者author__name中的publisher,author是book表中绑定的字段
	# 一对多和多对多在这里用法没区别


	################反向查找
	# ret8 = models.Publish.objects.filter(book__title = "jom").values("name")
	# print(ret8)
	# 一对多和多对多在这里用法没区别



	##################惰性机制
	list = models.Book.objects.filter(id__gt = 1) #当执行这段代码,并没有查询数据库,类似于生成器,不用不取
	# print(list.query) #显示sql语句
	# print(list.count()) #显示数据数量
	# for obj in list: #当执行for循环,他走了一遍数据库,把数据放到django的cache里面,会针对queryset提供一个缓存,取出的数据放缓存里面,在执行一次for循环,他就不去数据库拿了,去缓存拿数据
	# 	if obj:
	# 		print(obj.title) #只有执行for循环才真正执行这个sql
	# # list.update(title='777')
	# # list = models.Book.objects.filter( id = 1 )
	# for obj in list: #这一遍就去缓存拿了,因为sql只打印了一遍,
	# 	if obj:
	# 		print(obj.title) #只有执行for循环才真正执行这个sql
	#缓存机制弊端:
	# 1:我并不想要这些数据,只想判断他有没有,他还是会走一遍数据库,把数据丢缓存,所以用list.exists,这样就不会把数据缓存了,
	#2:假如10条数据,他会把所有数据都放到缓存池,这个时候也是1种压力,用迭代器解决所以用list.iterator()
	# if list.exists():
	# 	i_list = list.iterator()  #<generator object QuerySet._iterator at 0x102357db0>
	# 	print(next(i_list))
	# 	print(next(i_list))

	#对象形式的查找
	#正向查找:
	# obj = models.Book.objects.filter(id=1)[0]
	# print(obj.publisher.city)
	#反向查找
	# obj = models.Publish.objects.filter(id = 2)[0]
	# titles = obj.book_set.values('title').distinct() #根据title去重
	# print(titles)

	#关联表查询(重要) 双下划线可以进行关联查询
	# dic = models.Publish.objects.filter(book__title = '777').values('name')
	# dic = models.Book.objects.filter(publisher__name = "北京大学出版社").values('title').distinct()
	# dic = models.Book.objects.filter(title = "如何").values("publisher__city")
	# dic = models.Book.objects.filter(publisher__city = "深圳").values("publisher__name")
	# print(dic)









	return HttpResponse("<h1>创建成功</h1>")



from django.db.models import Avg,Max,Min,Sum
from django.db.models import F,Q
#聚合查询与分组查询 一个处理一个对象,一个处理多个对象
def aggregation(req):
	#聚合查询
	#price = models.Book.objects.all().aggregate(Avg('price'))
	# price = models.Book.objects.all().aggregate(Sum('price'))
	# print(price) #{'price__avg': 12.0}
	#分组查询
	# res = models.Book.objects.values("publisher__name").annotate(Sum('price')) #分组

	#<QuerySet [{'publisher__name': '清华大学出版社', 'price__sum': 10}, {'publisher__name': '北京大学出版社', 'price__sum': 38}]>
	# print(res.query)
	#SELECT `blog_publish`.`name`, SUM(`blog_book`.`price`) AS `price__sum` FROM `blog_book` INNER JOIN `blog_publish` ON (`blog_book`.`publisher_id` = `blog_publish`.`id`) GROUP BY `blog_publish`.`name` ORDER BY NULL


	#F查询与Q查询
	#F查询
	#给所有书的价格+20
	# models.Book.objects.all().update(price = F('price')+20) #对一列数值进行操作
	#Q查询
	# dic = models.Book.objects.filter(Q(id=3)|Q(title=777)).values() #| 或
	# dic = models.Book.objects.filter(Q(price=210)&(Q(title="如何")|Q(title="777")),color = "red",) #| 或  & 且   ,如果有类似于title = 123,这种的关键字要放在Q查询后面
	# print(dic)
	#SELECT `blog_book`.`id`, `blog_book`.`title`, `blog_book`.`price`, `blog_book`.`color`, `blog_book`.`page_num`, `blog_book`.`publisher_id` FROM `blog_book` WHERE (`blog_book`.`price` = 30 AND (`blog_book`.`id` = 3 OR `blog_book`.`title` = 777))




	return HttpResponse( "<h1>success</h1>" )

















