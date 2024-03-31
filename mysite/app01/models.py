from django.db import models

# Create your models here.
class userInfo(models.Model):
    name = models.CharField(max_length=32,primary_key=True)
    password = models.CharField(max_length=64)
    role = models.CharField(max_length=32)

class sc(models.Model):
    stuName = models.CharField(max_length=32)
    cid = models.CharField(max_length=32)

class course(models.Model):
    cname = models.CharField(max_length=64)
    cid = models.CharField(max_length=32)
    teacher = models.CharField(max_length=32)