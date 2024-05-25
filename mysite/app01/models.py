from datetime import datetime

from django.db import models

# Create your models here.
# current_date = datetime.now().date()

class CompositeField(models.Field):
    def __init__(self, fields, *args, **kwargs):
        self.fields = fields
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['fields'] = self.fields
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'varchar'

    def get_attname(self):
        return '_'.join([field.get_attname() for field in self.fields])

class userInfo(models.Model):
    name = models.CharField(max_length=32,null=False,primary_key=True)#账号名
    password = models.CharField(max_length=64,null=False)
    role = models.CharField(max_length=32,null=False)
    sex = models.CharField(max_length=32,default='')
    info = models.CharField(max_length=256,default='暂无介绍')
    username = models.CharField(max_length=32,default='')
    img = models.CharField(max_length=64,default='default.jpg')
    #primary_key = CompositeField([name, role])

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
    username = models.CharField(max_length=32,default='')#创建课程的账号
    status = models.CharField(max_length=64,default='进行中')
    zhibo = models.CharField(max_length=64,default='暂无直播')
    # createdate = models.DateField()

# 学生点击作业的时候再存入数据库
class s_q(models.Model):#学生对每一道题的解答
    qid = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    ans = models.TextField(default='')
    score = models.CharField(max_length=32,default='')
    judgement = models.TextField(default='无')

class w_s(models.Model):#作业和学生
    wid = models.CharField(max_length=32)
    name = models.CharField(max_length=32)#学生账户名（唯一)
    t = models.CharField(max_length=64)#提交时间
    status = models.CharField(max_length=64,default='待批改')

class Work(models.Model):#作业
    wid = models.CharField(max_length=32,primary_key=True)
    wname = models.CharField(max_length=64)
    # begin = models.DateTimeField(default=datetime.now)
    # end = models.DateTimeField(default=datetime.now)
    begin = models.CharField(max_length=64)
    end = models.CharField(max_length=64)
    cid = models.CharField(max_length=32,default='')




class question(models.Model):
    qid = models.CharField(max_length=32,primary_key=True)
    qname = models.CharField(max_length=64) #例如：第一题
    info = models.TextField(default='')#题目具体内容
    q_ans = models.TextField(default='')#客观题就直接由系统批改
    wid = models.CharField(max_length=32,default='')
    kind = models.CharField(max_length=32,default='')#题目类型
    a = models.TextField(default='')
    b = models.TextField(default='')
    c = models.TextField(default='')
    d = models.TextField(default='')
    score = models.CharField(max_length=32,default='')


class problem(models.Model):
    pid = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=32)#账号名
    info = models.TextField(default='')
    # t = models.DateTimeField(default=datetime.now)
    t = models.CharField(max_length=64)
    status = models.CharField(max_length=64,default='未解决')
    ans = models.TextField(default='')
    cid = models.CharField(max_length=32,default='')
    jh = models.CharField(max_length=32,default='0')#是不是精华

class Answer(models.Model):
    aid = models.CharField(max_length=32, primary_key=True)
    pid = models.CharField(max_length=32, default='')
    ans = models.TextField(default='')
    name = models.CharField(max_length=32)#回复者账号名
    t = models.CharField(max_length=64)

class records(models.Model):
    cid = models.CharField(max_length=32,default='')#stream的名称
    period = models.CharField(max_length=32,default='')
    path = models.CharField(max_length=128,default='')
    rname = models.CharField(max_length=32,default='')#教师可以自定义视频的名字

class learningMaterials(models.Model):
    cid = models.CharField(max_length=32, default='')
    did = models.CharField(max_length=32, default='')
    label = models.CharField(max_length=64, default='')
    parentdid = models.CharField(max_length=32, default='')
    path =  models.CharField(max_length=128,default='')
