#coding=utf-8
from django.db import models
from django.template.defaultfilters import default

# Create your models here.

class FirstModel(models.Model):
    Username = models.CharField(max_length=20)


class SecondModel(models.Model):
    Nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,default='hanxin')
    Address = models.CharField(max_length=10,default='alex')
    Gender = models.NullBooleanField()
    Age = models.IntegerField(default=1,help_text='不要超过10岁')
    Date = models.DateField()

class ThirdModel(models.Model):
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    IP = models.IPAddressField()
    IP2 = models.GenericIPAddressField(null=True)
class ColorDic(models.Model):
    ColorName = models.CharField(max_length=20)
    def __unicode__(self):
        return self.ColorName

class Person(models.Model):
    Name = models.CharField(max_length=20)
    Gender = models.BooleanField(default=False)
    Color = models.ForeignKey(ColorDic)
    def __unicode__(self):
        return u"%s %s %s" % (self.Name,self.Gender,self.Color)

class AuthList(models.Model):
    Name = models.CharField(max_length=10)
  
class Book(models.Model):
    BookName = models.CharField(max_length=10)
    Author = models.ManyToManyField(AuthList)
    


    