from django.db import models

# Create your models here.
class userInfo(models.Model):
    name = models.CharField(max_length=32,primary_key=True)#账号名
    password = models.CharField(max_length=64)
    role = models.CharField(max_length=32)
    sex = models.CharField(max_length=32,default='')
    info = models.CharField(max_length=256,default='')
    username = models.CharField(max_length=32,default='')
    img = models.CharField(max_length=64,default='default.jpg')

class sc(models.Model):
    stuName = models.CharField(max_length=32)
    cid = models.CharField(max_length=32)

class course(models.Model):
    cname = models.CharField(max_length=64)
    cid = models.CharField(max_length=32)
    teacher = models.CharField(max_length=32)

