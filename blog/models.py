from django.db import models

#Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length = 64)
    sex = models.CharField(max_length = 64)
    email = models.CharField(max_length = 64)

class Book(models.Model):
    title = models.CharField(max_length = 64)
    price = models.IntegerField()
    color = models.CharField(max_length = 64)
    page_num = models.IntegerField(null=True)

    publisher = models.ForeignKey("Publish",on_delete=models.CASCADE,)

    #接收对象
    # author = models.ManyToManyField("Author") #写上它自动为你创建第三张表

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Publish(models.Model):
    #my_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=64) #相当于database里面的varchar
    city = models.CharField(max_length=64)
    def __str__(self):
        return self.city

#手动创建第三张关联表
class Book2Author(models.Model):
        author = models.ForeignKey('Author',on_delete = models.CASCADE,)
        book = models.ForeignKey('Book',on_delete = models.CASCADE,)
        #绑定联合唯一索引
        class Meta: #不一定非要有,根据需求来
            unique_together = ['author','book']


# manytomany 实质是在这个表通过2个外键建立多对多的关系
# onetoone   在多的那个表建立外键+unique=true
#onetomany   在多的那个表建立外键
























