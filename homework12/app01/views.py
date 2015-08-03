from django.shortcuts import render,render_to_response
from django.core.context_processors import request
from django.http.response import HttpResponse
import json

# Createb
data = {
        'shandong':{
                    'jinan':['a','b','c'],
                    'dezhou':['hh','dd','ii']
                    },
        'hebei':{
                 'shijian':['aa','bb','vv'],
                 'baoding':['cc','dd','ee'],
                 },
        'chonqing':{
                    'naanqu':['gg','fwef','ewf'],
                    'shapingban':['fwef','ee','ee'],
                    'ahuo':['dd']
                    },
        }

def Index(request):
    return render_to_response('index.html')

def GetProvice(request):
    result = data.keys()
    return HttpResponse(json.dumps(result))

def GetCity(request):
    getDate = request.GET
    provinceID = getDate.get('Id')
    result = data.values()[int(provinceID)].keys()
    result.sort()
    return HttpResponse(json.dumps(result))

def GetCounty(request):
    getDate = request.GET
    provinceID = getDate.get('proId')
    cityID = getDate.get('Id')
    result = data.values()[int(provinceID)].values()[int(cityID)]
   # result = data.values()[int(cityID)]
    print result
    result.sort()
    return HttpResponse(json.dumps(result))

    