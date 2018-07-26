from django.db import models

# Create your models here.

class Person(models.Model):
    MAN = 9
    WOMAN = 0

    FIRSTGRADE = 1
    SECONDGRADE = 2
    THIRDGRADE = 3
    FOURTHGRADE = 4
    FIFTHGRADE =5

    #名前
    name = models.CharField(max_length=128)
    #性別
    sex = models.IntegerField(editable=False)
    #sex = models.CharField(max_length=16)
    #学年
    grade = models.IntegerField(editable=False)
    #grade = models.CharField(max_length=16)
    #楽器
    instrument= models.CharField(max_length=64)

from django.contrib.auth.models import AbstractBaseUser
from manager.managers import PersonManager

class Loguser(AbstractBaseUser):  #1
    objects = PersonManager()  # 2

    identifier = models.CharField(max_length=64, unique=True, blank=False)  # 3
    name = models.CharField(max_length=128)
    email = models.EmailField()

    is_active = models.BooleanField(default=True)  # 必要です！

    USERNAME_FIELD = 'identifier'  # 4
