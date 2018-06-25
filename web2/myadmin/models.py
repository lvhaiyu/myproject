from django.db import models

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=80)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=11)
	age = models.IntegerField(null=True)
	sex = models.CharField(max_length=1)
	pic = models.CharField(max_length=100,null=True)
    #
	status = models.IntegerField(default=0)
	addtime = models.DateTimeField(auto_now_add=True)


# 
class Types(models.Model):
    name = models.CharField(max_length=20)
    pid = models.IntegerField()
    path = models.CharField(max_length=50)