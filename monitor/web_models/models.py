#coding=utf-8
from django.db import models

# Create your models here.

#监控的具体项目如idle ,user , iowait, Buffers
class Items(models.Model):
    name = models.CharField(max_length=50,unique=True)
    key = models.CharField(max_length=100,)
    data_type_option = (('float','Float'),('string','String'),('integer','Integer'))
    data_type = models.CharField(max_length=50,choices=data_type_option)
    unit = models.CharField(max_length=50,default='%')
    enabled = models.BooleanField(default=True)
    service = models.ForeignKey('Services')
    
    def __unicode__(self):
        return self.name

#监控的服务如CPU,memory,load    
class Services(models.Model):
    monitor_type_list = (('agent','Agent'),('snmp','Snmp'),('wget','Wget'))
    monitor_type = models.CharField(max_length=50,choices=monitor_type_list)
    name = models.CharField(max_length=50,unique=True)
    plugin = models.CharField(max_length=100)
    
    
    def __unicode__(self):
        return self.name

#服务模板，如监控服务的检查间隔时间
class ServiceTemplate(models.Model):
    name = models.CharField(max_length=50,unique=True)
    key = models.CharField(max_length=50)
    check_interval = models.IntegerField(default=300)
    service = models.ForeignKey('Services')
    conditions = models.ManyToManyField('Conditions',verbose_name=u'阀值列表')
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

#运算函数 如 sum,max,min
class Formulas(models.Model):
    name = models.CharField(max_length=32,unique=True)
    key = models.CharField(max_length=32)
    memo = models.TextField()
    
    def __unicode__(self):
        return self.name

#运算符 如gt,lt
class Operators(models.Model):
    name = models.CharField(max_length=32,unique=True)
    key = models.CharField(max_length=32)
    memo = models.TextField()
    
    def __unicode__(self):
        return self.name


#监控的阀值    
class Conditions(models.Model): 
    name = models.CharField(max_length=100,unique=True)
    item = models.ForeignKey('Items',verbose_name=u'监控值')
    formula = models.ForeignKey('Formulas',verbose_name=u'运算函数')
    operator = models.ForeignKey('Operators',verbose_name=u'运算符',null=True,blank=True) #
    data_type = models.CharField(default='char',max_length=32,verbose_name=u'数据类型')
    threshold = models.CharField(max_length=64,verbose_name=u'阀值')
    
    def __unicode__(self):
        return self.name

class Idc(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name


#主机组  由主机组来控制调用监控模板
class HostGroup(models.Model):
    name = models.CharField(max_length=50,unique=True)
    service_template = models.ManyToManyField('ServiceTemplate') #多对多，如主机组需要cpu1,memory1,load1
    
    def __unicode__(self):
        return self.name
    


class Host(models.Model):
    hostname = models.CharField(max_length=50,unique=True)
    ip = models.GenericIPAddressField()
    idc = models.ForeignKey('Idc')
    group = models.ForeignKey('HostGroup')
    
    def __unicode__(self):
        return "%s %s" % (self.hostname,self.ip)


class UserGroup(models.Model):
    name = models.CharField(max_length=50,unique=True)
    host_group = models.ManyToManyField('HostGroup')
    user_info = models.ManyToManyField('UserInfo')
    
    def __unicode__(self):
        return self.name
    
class UserInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    tel = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
    
     
class Cpu(models.Model):
    host = models.ForeignKey('Host')
    
    user = models.CharField(max_length=64)
    nice = models.CharField(max_length=64)
    system = models.CharField(max_length=64)
    iowait = models.CharField(max_length=64)
    steal = models.CharField(max_length=64)
    idle = models.CharField(max_length=64)
    
class Memory(models.Model):
    MemTotal = models.CharField(max_length=64)
    MemUsage = models.CharField(max_length=64)
    Cached = models.CharField(max_length=64)
    MemFree = models.CharField(max_length=64)
    Buffers = models.CharField(max_length=64)
    SwapFree = models.CharField(max_length=64)
    SwapTotal = models.CharField(max_length=64)
    


    