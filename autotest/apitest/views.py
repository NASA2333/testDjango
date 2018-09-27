from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate

# Create your views here.
def test(request):
    return HttpResponse('hello word')

def do_login(request):
    # return render(request,'login.html')
    if request.POST:
        username = password =''
        username=request.POST.get('username')
        password=request.POST.get('password')
        user =auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user'] =username
            response =HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error': '账号或密码错误'})

    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')