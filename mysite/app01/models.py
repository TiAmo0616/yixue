from datetime import datetime

from django.db import models

# Create your models here.
# current_date = datetime.now().date()
class userInfo(models.Model):
    name = models.CharField(max_length=32,primary_key=True)#账号名
    password = models.CharField(max_length=64)
    role = models.CharField(max_length=32)
    sex = models.CharField(max_length=32,default='')
    info = models.CharField(max_length=256,default='暂无介绍')
    username = models.CharField(max_length=32,default='')
    img = models.CharField(max_length=64,default='default.jpg')

class sc(models.Model):
    stuName = models.CharField(max_length=32)
    cid = models.CharField(max_length=32)

class Course(models.Model):
    cname = models.CharField(max_length=64)
    cid = models.CharField(max_length=32)
    teacher = models.CharField(max_length=32)
    introduction = models.TextField(default='暂无介绍')
    xueshi = models.CharField(max_length=64,default='无')
    img = models.CharField(max_length=64,default='defaultCourse.png')
    stuNum = models.IntegerField(default=0)
    username = models.CharField(max_length=32,default='')#创建课程的账号
    status = models.CharField(max_length=64,default='进行中')
    # createdate = models.DateField()

class w_c(models.Model):
    cid = models.CharField(max_length=32)
    wid = models.CharField(max_length=32)

class w_s(models.Model):
    wid = models.CharField(max_length=32)
    name = models.CharField(max_length=3)

class Work(models.Model):
    wid = models.CharField(max_length=32)
    wname = models.CharField(max_length=64)
    begin = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)
    info = models.TextField(default='')
