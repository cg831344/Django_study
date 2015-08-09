#coding=utf-8
from django.shortcuts import render,render_to_response,redirect
from django.template.context import RequestContext
from django.http import HttpResponse
from django.core.context_processors import request

# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        if user == 'alex' and pwd == '123':
           request.session['is_login'] = {'user':user}
           return redirect('/app02/index')
        
        else:
            return render_to_response('/app02/login.html',{'msg':pwd},context_instance=RequestContext(request))
        
    return render_to_response('app02/login.html',context_instance=RequestContext(request))

def index(request):
    user_dict = request.session.get('is_login',None)
    if not user_dict:
        return redirect('/app02/login/')
    else:
        return render_to_response('app02/index.html',{'user':user_dict})
    
def logout(request):
    #销毁session
    del request.session['is_login']
    return redirect('/app02/login/')
