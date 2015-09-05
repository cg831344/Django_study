#coding=utf-8
from django.shortcuts import render,HttpResponse
from web_models import models
import json


# Create your views here.
def get_config(request):
    ret =  {'status':0,'data':'','message':''}
    try:
        data = {}
        hostname = request.GET.get('hostname',None)
        if not hostname:
            ret['message'] = '请输入主机名'
            return HttpResponse(json.dumps(ret))
        
        hostObj = models.Host.objects.get(hostname=hostname)
        hostname = hostObj.hostname
        host_group = hostObj.group
        
        service_templates = host_group.service_template.all()
        
        #item为service_templates中的每个对象
        for item in service_templates:
            temp = {}
            temp['last_time'] = 0
            temp['interval'] = item.check_interval
            temp['plugin_name'] = item.service.plugin #通过item的外键service的字段plugin
            temp['element'] = {}
            
            #service_templates中conditions是多对多关系，可能有多个
            for cond in item.conditions.all():
                
                item_key = cond.item.key
                #如果第一次循环后有了item_key
                #监控的具体项目如idle ,user , iowait, Buffers
                if temp['element'].has_key(item_key):
                    temp['element'][item_key].append({'formula':cond.formula.key,'operator':cond.operator.key,'threshold':cond.threshold})
                else:
                    temp['element'][item_key] = [{'formula':cond.formula.key,'operator':cond.operator.key,'threshold':cond.threshold}]
            data[item.key] = temp
        ret['data'] = data
        ret['status'] = 1
    
    except Exception,e:
        ret['message'] = e
        
    return HttpResponse(json.dumps(ret))
        
        