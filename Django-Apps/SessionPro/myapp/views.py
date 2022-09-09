from django.shortcuts import render
from .forms import NameForm,AgeForm,GfForm
from .models import NameModel,GfModel,AgeModel
# Create your views here.

def nameview(request) :
    form=NameForm()
    return render(request,'name.html',{'form':form})

def ageview(request) :
    form=AgeForm()
    fname=request.GET['fname']
    lname=request.GET['lname']
    request.session['fname']=fname
    request.session['lname']=lname
    my_dict={'name':fname,'form':form}
    return render(request,'age.html',context=my_dict)

def gfview(request) :
    form=GfForm()
    age=request.GET['age']
    request.session['age']=age
    return render(request,'gf.html',{'form':form})
def resultview(request) :
    gf=request.GET['gf']
    request.session['gf']=gf
    return render(request,'results.html')

def page_count_view(request):
    count=request.session.get('count',0)
    nc=count+1
    request.session['count']=nc
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'count.html',{'count':nc})
def page_count_using_cookie(request) :
    if 'count' in request.COOKIES :
        nc=int(request.COOKIES['count'])+1
    else:
        nc=1
    response=render(request,'count.html',{'count':nc})
    response.set_cookie('count',nc)
    return response