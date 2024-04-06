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
    cid = models.CharField(max_length=32,primary_key=True)
    teacher = models.CharField(max_length=32)
    introduction = models.TextField(default='暂无介绍')
    xueshi = models.CharField(max_length=64,default='无')
    img = models.CharField(max_length=64,default='defaultCourse.png')
    stuNum = models.IntegerField(default=0)
    username = models.CharField(max_length=32,default='')#创建课程的账号
    status = models.CharField(max_length=64,default='进行中')
    # createdate = models.DateField()

class w_c(models.Model):#课程对应的作业
    cid = models.CharField(max_length=32)
    wid = models.CharField(max_length=32)

class s_q(models.Model):#学生对每一道题的解答
    qid = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    ans = models.TextField(default='')

class w_s(models.Model):#作业和学生
    wid = models.CharField(max_length=32)
    name = models.CharField(max_length=32)#学生账户名（唯一)
    t = models.DateTimeField(default=None)#提交时间
    status = models.CharField(max_length=64,default='未提交')#作业状态

class Work(models.Model):#作业
    wid = models.CharField(max_length=32,primary_key=True)
    wname = models.CharField(max_length=64)
    begin = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)


class w_q(models.Model):#作业--题目
    wid = models.CharField(max_length=32)
    qid = models.CharField(max_length=32)

class question(models.Model):
    qid = models.CharField(max_length=32,primary_key=True)
    qname = models.CharField(max_length=64) #例如：第一题
    info = models.TextField(default='')#题目具体内容
    q_ans = models.TextField(default='')#客观题就直接由系统批改

class p_c(models.Model):
    pid = models.CharField(max_length=32)
    cid = models.CharField(max_length=32)

class problem(models.Model):
    pid = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=32)#账号名
    info = models.TextField(default='')
    t = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=64,default='未解决')
    ans = models.TextField(default='')

