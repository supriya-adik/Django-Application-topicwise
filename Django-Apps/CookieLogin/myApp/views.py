from django.shortcuts import render
from .forms import MyForm
from datetime import datetime

# Create your views here.
def home(request) :
    form=MyForm()
    return render(request,'home.html',{'form':form})

def date_time_view(request) :
    name=request.GET['name']
    email=request.GET['email']
    response=render(request,'datetime.html',{'name':name,'email':email})
    response.set_cookie('name',name)
    response.set_cookie('email',email)
    return response

def result_view(request) :
    name=request.COOKIES['name']
    email=request.COOKIES['email']
    my_dict={'name':name,'email':email,'date_time':datetime.now()}
    return render(request,'result.html',my_dict)