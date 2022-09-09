from django.shortcuts import render

# Create your views here.
def name_view(request) :
    return render(request,'name.html')

def age_view(request) :
    name=request.GET['name']
    response=render(request,'age.html')
    response.set_cookie('name',name,max_age=60)
    return response

def gf_view(request) :
    age=request.GET['age']
    response=render(request,'gf.html')
    response.set_cookie('age',age)
    return response

def result_view(request) :
    gf=request.GET['gfname']
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    response=render(request,'result.html',{'name':name,'age':age,'gf':gf})
    return response