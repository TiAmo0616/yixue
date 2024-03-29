from django.db import models

# Create your models here.
class userInfo(models.Model):
    name = models.CharField(max_length=32,primary_key=True)
    password = models.CharField(max_length=64)
    role = models.IntegerField()